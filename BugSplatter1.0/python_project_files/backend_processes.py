import os
import pyodbc
import pandas as pd
import json
import pypyodbc as odbc
from colorama import Fore, Style, init
from datetime import datetime
import pyodbc
import xlsxwriter
import pandas as pd
from openpyxl import load_workbook


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_date_format(input_date):
    expected_format = '%Y-%m-%d'
    try:

        # Try to parse the input date using the expected format
        datetime.strptime(input_date, expected_format)
        return True  # Format is correct
    except ValueError:
        return False  # Format is incorrect
    

def get_server(): 
    while True:
        print("\nDNS's SERVER LIST")
        print("-----------------")

        # Read the JSON file
        with open('..\\json_config\\dns_DB_server_list.json', 'r') as file:
            json_data = json.load(file)

        # Print server options
        for key, value in json_data["DNS_DB_server_list"].items():
            print(f"{key}: {value['name']} ({value['host']}:{value['port']})")

        print("Please enter the server option (1-7): ")
        option = input()

        # Check if the entered option is valid
        if option in json_data["DNS_DB_server_list"]:
            selected_server = json_data["DNS_DB_server_list"][option]
            print(f"You selected: {selected_server['name']} ({selected_server['host']}:{selected_server['port']})")

            #print(selected_server['host'] + "," + selected_server['port'])
            return selected_server['host'] + "," + selected_server['port']# Return the selected server
        else:
            print("Invalid option. Please enter a valid option.")


#def get_server_auto(target_sys): 
#    with open('..\\json_config\\dns_db_server_list_auto.json', 'r') as file:
#        json_data = json.load(file)#

#    # Get the associated dns/port for system we're logged in as i.e. NextraDev
#    selected_server = json_data["dns_server_list"][target_sys]
#    
#    return selected_server

def get_server_auto(target_sys): 
    with open('..\\json_config\\dns_db_server_list_auto.json', 'r') as file:
        json_data = json.load(file)

    # Iterate over the DNS server list and find the target system
    for dns_server, systems in json_data["dns_server_list"].items():
        if target_sys in systems:
            return dns_server


def get_nextra_contact_ids(username): 
    # Read the JSON file
    with open('..\\json_config\\contact_ids.json', 'r') as file:
        json_data = json.load(file)

    user_id = None  # Initialize with a default value
    
    if username in json_data["contact_id's"]: 
        user_id = json_data["contact_id's"][username]
    
    return user_id


def checkTimesheetRuns(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    print("\033[1;31m| Timesheet Runs |\033[0m")

    # Input the hostname of the server instance you want to connect to 
    server = get_server()

    # Input the date the timesheets you want to run
    print("Please enter a date the timesheet was run - [Example: 2023-04-24 ('YYYY-MM-DD')]: ")
    while(1): 
        # Define the specific criteria for CreateDate
        target_date_criteria = input()

        if check_date_format(target_date_criteria):
            print("Date accepted")
            break
        else: 
            print("Please enter a date within the specified format - [Example: 2022-01-25 ('YYYY-MM-DD')]: ")
            clear_console()
    

    # Define the parameters for the stored procedure
    compare_calc_run_id = -1 #-1
    user_id = get_nextra_contact_ids(username)

    db = target_sys
    
    #Create a connection to the database
    conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'
    print(conn_string)
    conn = pyodbc.connect(conn_string)    
    # Create a cursor from the connection
    cursor = conn.cursor()   

    # Query to get calcRunId values based on the specific date criteria
    sql_query = f'''
        SELECT 
            CalcRunID
        FROM 
            rf_Scheduled_Calculation_Run
        WHERE 
            CONVERT(DATE, CreateDate) = '{target_date_criteria}';
    '''

    # Execute the query to get calcRunId values
    cursor.execute(sql_query)        

    # Fetch all rows from the result set
    calc_run_ids = [row.CalcRunID for row in cursor.fetchall()]        
    
    differences_found = False # Prevents alert from being printed recursivley. 

    # Loop through each calcRunId and execute the stored procedure
    # Loop through calc_run_ids
    for calc_run_id in calc_run_ids:

        # print(calc_run_id)    
        # Execute the stored procedure
        #[dbo].[rf_Report_Timesheet_Balances_Testing]
        stored_proc_query = "EXEC [dbo].[rf_Report_Timesheet_Balances_Testing] ?, ?, ?"
        params = (int(calc_run_id), int(compare_calc_run_id), int(user_id))
        #print(params)
        output_param = conn.cursor()
        output_param.execute(stored_proc_query, params)   

        # Fetch the result set or process the results as needed
        #rows = output_param.fetchall()
        #for row in rows:
        #    #Process each row of the result set
        #    print(row)     
        result_set = output_param.fetchall()
        #print(result_set)  
        for row in result_set:
            contact_id = row[1]
            expected_balance = row[4] # Display Value
            actual_balance = row[5] # Value
            difference = row[7]

            #print(f"Contact ID: {contact_id} | Expected Balance: {expected_balance} | Actual Balance: {actual_balance} | Difference: {difference}")

            if difference != 0:
                differences_found = True
                # Now you can use these values as needed
                print(f"\nContact ID: {contact_id} | Expected Balance: {expected_balance} | Actual Balance: {actual_balance} | Difference: {difference}")
            else: 
                # No difference was found, so we don't print anything here
                pass

    cursor.close()
    conn.close()
    
    # Check if any differences were found
    if not differences_found:
        print("\nNo difference were found between base set values and timesheet runs")
    else: 
        print("Differences have been found")

    print("\n[End of Execution]")


def check_stored_proc_exists(server, username, password, proc_name):

    # Establish connection to the server using SQL Server authentication
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';UID=' + username + ';PWD=' + password + ';')

    # Get a cursor
    cursor = conn.cursor()

    # Query to check if the stored procedure exists in each database
    query = """
    SELECT name
    FROM sys.databases
    WHERE state_desc = 'ONLINE' AND database_id > 4
    """
    
    # Execute the databases query
    cursor.execute(query)
    rows = cursor.fetchall()

    # Iterate through databases
    for row in rows:
        no_found = False

        database_name = row[0]
        print("Checking database:", database_name)

        # Query to check if the stored procedure exists in the current database
        query = f"""
        USE [{database_name}];
        IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = ?)
        BEGIN
            PRINT 'Found in database: {database_name}';
        END
        """
        
        # Execute the query for the current database
        cursor.execute(query, proc_name)
        
        # Check if any results were returned
        if cursor.rowcount > 0:
            print(f"Stored procedure '{proc_name}' found in database '{database_name}'")
            no_found = True
        
        
    
    if no_found == False:
        print(f"\nDB Server: {server}")
        print(f"Stored procedure '{proc_name}' not found in any database instance")

    # Close the conn
    conn.close()


# If it's 'X', but the usertype doesnt exist, it ignores. If it is 'X' and the usertype exists and the menu item exists, then its green
# If its 'X' and the usertype exists and the menu item doenst exist, then it's red. 
# Psudo
# Get all tabnames and set them as columns in the excel file
# Get all the usertypes/locations appended to them that we know exist and set them as the rows
# Where they exist, assign an X to them.

# Will mark an 'X' with the corresponding 'full location name' and 'main menu item' under Admin Homepage Menu Item
def populateExcelSheetWithExpecrfNavTypesTabs(connection_string, filename, client):
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabName FROM rf_nav_types_tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TypeTabID FROM rf_nav_types_tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%{client}%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        ntt.TabName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types_tabs ntt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + ntt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE ntt.TypeTabID = {index_value} AND lang.LanguageName LIKE '%{client}%'
        #    AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #                    )
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                ntt.TabName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID 
            INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types_tabs ntt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + ntt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE ntt.TypeTabID = {index_value} AND lang.LanguageName LIKE '%{client}%'
            AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
                            )
            AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        # Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)
            
            workbook = writer.book
            worksheet = writer.sheets[client]

            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)

            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)

    #print(full_location_names)
    #print(tab_names)
    
    #print(full_location_names)

    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)

    return filename


# Will mark an 'X' with the corresponding 'full location name' and 'sub menu item' under Admin Homepage Menu Item
def populateExcelSheetWithExpecrfNavTypes(connection_string, filename, client):
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TypeDescription FROM rf_nav_types")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TypeTabID FROM rf_nav_types")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""
        
        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%{client}%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        nt.TypeDescription
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE nt.TypeTabID = {index_value} AND lang.LanguageName LIKE '%{client}%'
        #    AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #                    )
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                nt.TypeDescription
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID 
            INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE nt.TypeTabID = {index_value} AND lang.LanguageName LIKE '%{client}%'
            AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
                            )
            AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'

        """
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        # Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)

            workbook = writer.book
            worksheet = writer.sheets[client]

            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)

            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)

    #print(full_location_names)
    #print(tab_names)
    
    #print(full_location_names)

    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)

    return filename


# Will mark an 'X' with the corresponding 'full location name' and tab associated with 'sub sub menu item' of type 'CONTACT' under Admin Homepage Menu Item
def populateExcelSheetWithExpecrfContactsTabs(connection_string, filename, client):
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabDisplayName FROM rf_Contacts_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabID FROM rf_Contacts_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%British%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        c.TabDisplayName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
	    #	 LEFT JOIN rf_Contacts_Tabs c ON c.LabelSetID = nt.TypeLabelSetID 
	    #	 WHERE nt.TypeTabID = {index_value} 
	    #	 AND lang.LanguageName LIKE '%{client}%'
	    #	 AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #                    )
        #"""
        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                c.TabDisplayName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID 
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
			LEFT JOIN rf_Contacts_Tabs c ON c.LabelSetID = nt.TypeLabelSetID 
			WHERE nt.TypeTabID = {index_value}
			AND lang.LanguageName LIKE '%{client}%'
			AND EXISTS (SELECT 3 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
                            )
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        # Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)
            workbook = writer.book
            worksheet = writer.sheets[client]

            # Add custom metadata to workbook - tab type
            # workbook.set_custom_property('TabType', 'CONTACT')
            #props = CustomPropertyList()
            #props.append(StringProperty(name="tabtype", value="CONTACT"))
            #workbook.custom_doc_props = props
            
            #for prop in worksheet.custom_doc_props.props:
            #    print(f"{prop.name}: {prop.value}")
            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)


            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)  

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)

    #print(full_location_names)
    #print(tab_names)
    
    #print(full_location_names)

    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)    

    return filename


# Will mark an 'X' with the corresponding 'full location name' and tab associated with 'sub sub menu item' of type 'LOCATION' under Admin Homepage Menu Item
def populateExcelSheetWithExpecLocTabs(connection_string, filename, client):
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabDisplayName FROM rf_Location_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabID FROM rf_Location_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%{client}%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        lt.TabDisplayName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
	    #	 LEFT JOIN rf_Location_Tabs lt ON nt.TypeLabelSetID = lt.LabelSetID
	    #	 WHERE nt.TypeTabID = {index_value}
	    #	 AND lang.LanguageName LIKE '%{client}%'
	    #	 AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #                    )
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                lt.TabDisplayName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID 
            INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
			LEFT JOIN rf_Location_Tabs lt ON nt.TypeLabelSetID = lt.LabelSetID
			WHERE nt.TypeTabID = {index_value}
			AND lang.LanguageName LIKE '%{client}%'
			AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
                            )
            AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        # Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass 

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)
            workbook = writer.book
            worksheet = writer.sheets[client]

            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)


            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)
    
    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)    

    return filename
    

# Will mark an 'X' with the corresponding 'full location name' and tab associated with 'sub sub menu item' of type 'ABSENCE' under Admin Homepage Menu Item
def populateExcelSheetWithExpecAbsenceTypeTabs(connection_string, filename, client): 
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabDisplayName FROM rf_Absence_Types_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    
    # In this case, we dont use indexes to specify the 'TypeTabID' as they dont relate to rf_nav_types in a generic sense
    # We only use this function to loop through each existing record inside 'rf_Absence_Types_Tabs'
    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabID FROM rf_Absence_Types_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%{client}%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    
    # May be changed in the future so have left the parameter inputs as per how they have been defined in other populate excel sheet functions. 
    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        att.TabDisplayName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
		#    LEFT JOIN rf_Absence_Types_Tabs att ON nt.Typecode = 'ABSENCETYPE'
		#    WHERE att.TabDisplayName IS NOT NULL
		#    AND lang.LanguageName LIKE '%{client}%'
		#    AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #    )
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                att.TabDisplayName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID 
            INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
			LEFT JOIN rf_Absence_Types_Tabs att ON nt.Typecode = 'ABSENCETYPE'
			WHERE att.TabDisplayName IS NOT NULL
			AND lang.LanguageName LIKE '%{client}%'
			AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
            )
            AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        # Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)
            workbook = writer.book
            worksheet = writer.sheets[client]

            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)


            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)
    
    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)    

    return filename


# Will mark an 'X' with the corresponding 'full location name' and tab associated with 'sub sub menu item' of type 'SHIFT MASK' under Admin Homepage Menu Item
def populateExcelSheetWithExpecShiftMaskTabs(connection_string, filename, client): 
    def get_tab_names(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Description FROM rf_Shift_Mask_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_tab_indexes(connection_string):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT TabID FROM rf_Shift_Mask_Tabs")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_full_location_names(connection_string, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
        #    WHERE lang.LanguageName LIKE '%{client}%'
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
			INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
            WHERE lang.LanguageName LIKE '%{client}%'
			AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def fetch_data(connection_string, index_value, client):
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        #query = f"""
        #    SELECT DISTINCT 
        #        u.username + ' - ' + 
        #        l.LocationName + 
        #        ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
        #        u.UsertypeID AS UsertypeID,
        #        smt.Description
        #    FROM
        #        rf_Contacts_Roles cr
        #    INNER JOIN 
        #        rf_usertypes u ON cr.RoleID = u.UsertypeID 
        #    INNER JOIN
        #        rf_location l ON cr.LocationID = l.LocationID 
        #    LEFT JOIN
        #        rf_location pl ON l.ParentLocationID = pl.LocationID
        #    LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
        #    LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
		#    LEFT JOIN rf_Shift_Mask_Tabs smt ON nt.Typecode = 'Shift' AND nt.TypeLabelSetid = 1
		#    WHERE nt.TypeTabID = {index_value}
		#    AND lang.LanguageName LIKE '%{client}%'
		#    AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
        #                    WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
        #                    AND nhi.ItemName = 'Admin'
        #                    )
        #"""

        query = f"""
            SELECT DISTINCT 
                u.username + ' - ' + 
                l.LocationName + 
                ISNULL(' | ' + pl.LocationName, '') AS FullLocationName,
                u.UsertypeID AS UsertypeID,
                smt.Description
            FROM
                rf_Contacts_Roles cr
            INNER JOIN 
                rf_usertypes u ON cr.RoleID = u.UsertypeID
            INNER JOIN 
				rf_Location_Labels ll ON u.LanguageID = ll.LanguageID 
            INNER JOIN
                rf_location l ON cr.LocationID = l.LocationID 
            LEFT JOIN
                rf_location pl ON l.ParentLocationID = pl.LocationID
            LEFT JOIN rf_nav_types nt ON  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nt.Usertypes + ',') > 0
            LEFT JOIN rf_language lang ON lang.LanguageId = u.LanguageID
			LEFT JOIN rf_Shift_Mask_Tabs smt ON nt.Typecode = 'Shift' AND nt.TypeLabelSetid = 1
			WHERE nt.TypeTabID = {index_value}
			AND lang.LanguageName LIKE '%{client}%'
			AND EXISTS (SELECT 1 FROM rf_Nav_Homepage_Items nhi
                            WHERE  CHARINDEX(',' + CAST(u.UserTypeID AS NVARCHAR(MAX)) + ',', ',' + nhi.Usertypes + ',') > 0
                            AND nhi.ItemName = 'Admin'
                            )
            AND Username LIKE '%Administrator (%'
			AND UserName NOT LIKE '%Unsused%'
			AND ll.ParentLabelSetID = -1
			AND ll.LabelSetClass NOT LIKE '%Archive%'
			AND ll.LabelSetClass NOT LIKE '%Scenarios%'
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        #print(rows)
        return rows

    def create_excel(tab_names, full_location_names, data, filename, client):
        result_df = pd.DataFrame(index=full_location_names, columns=tab_names)
        result_df = result_df.fillna('')

        #Print DataFrame's index and columns for debugging
        #print("DataFrame Index:", result_df.index)
        #print("DataFrame Columns:", result_df.columns)

        for full_location_name, _, tab_name in data:
            if full_location_name is not None: 
                full_location_name = full_location_name.strip()
            else: 
                # Handles the case when tab_name is null
                full_location_name = "" 
            if tab_name is not None:
                tab_name = tab_name.strip()
            else:
                # Handles the case when tab_name is null
                tab_name = "" 
            #print(f"Processing: {full_location_name}, {tab_name}")
            if full_location_name in result_df.index and tab_name in result_df.columns:
                result_df.at[full_location_name, tab_name] = 'X'
                #print({full_location_name}, {tab_name}, 'X', ':)')
                #print("Index:", result_df.index)
                #print("Columns:", result_df.columns)
            else:
                #print(f"Full location name '{full_location_name}' or tab name '{tab_name}' not found.")
                #print("Formats dont match:")
                #print(f"Skipping - {full_location_name}, {tab_name}")
                pass

        #Print updated DataFrame for debugging
        #print("Updated DataFrame:")
        #print(result_df)

        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, sheet_name=client, index=True)
            workbook = writer.book
            worksheet = writer.sheets[client]

            # Label "FullLocationNames" above the column of location names
            #worksheet.write(0, 0, "FullLocationNames", bold=True, align='center')

            # Add a format for the header
            header_format = workbook.add_format({'bold': True, 'align': 'center'})

            # Write the label "FullLocationNames" above the column of location names with formatting
            worksheet.write(0, 0, "FullLocationNames", header_format)


            max_length_A = max(result_df.index.map(len).max(), len('FullLocationName'))
            column_width_A = max_length_A + 2
            worksheet.set_column(0, 0, column_width_A)

            for i, col in enumerate(result_df.columns):
                max_length_col = max(result_df[col].astype(str).map(len).max(), len(col))
                column_width_col = max_length_col + 2
                worksheet.set_column(i + 1, i + 1, column_width_col)

                
    full_location_names = get_full_location_names(connection_string, client)
    tab_names = get_tab_names(connection_string)
    tab_indexes = get_tab_indexes(connection_string)
    
    data = []
    for index_value in tab_indexes:
        data.extend(fetch_data(connection_string, index_value, client))

    #print(data)

    create_excel(tab_names, full_location_names, data, filename, client)

    print("Excel File created: ", filename)

    return filename


# Will process all 'sub sub menu items' - CONTACT, LOCATION, ABSENCE, SHIFT MASK
def populateExcelSheetsWithAllExpecSubSubsTabs(connection_string, client):
    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_contact_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    contact_path = populateExcelSheetWithExpecrfContactsTabs(connection_string, fullpath, client)
    
    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_location_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    loc_path = populateExcelSheetWithExpecLocTabs(connection_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_absence_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    absence_path = populateExcelSheetWithExpecAbsenceTypeTabs(connection_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_shiftmask_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    shiftmask_path = populateExcelSheetWithExpecShiftMaskTabs(connection_string, fullpath, client)

    return contact_path, loc_path, absence_path, shiftmask_path


# Will process all tab types i.e. Main, Sub, Sub-Sub 
def populateExcelSheetsWithAllTabTypes(connection_string, client):
    folder_path = "..\\excel_sheets\\admin_nav\\main_menu_tabs\\"
    filename = f"main_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    main_menu_path = populateExcelSheetWithExpecrfNavTypesTabs(connection_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_menu_tabs\\"
    filename = f"sub_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    sub_menu_path = populateExcelSheetWithExpecrfNavTypes(connection_string, fullpath, client)

    contact_path, loc_path, absence_path, shiftmask_path = populateExcelSheetsWithAllExpecSubSubsTabs(connection_string, client)

    return main_menu_path, sub_menu_path, contact_path, loc_path, absence_path, shiftmask_path

# Will generate an array of all key value pairs of main menu tabs with their associated sub menu tabs
def getCorrespondingMainMenuAndSubMenuTabsForAGivenSystem(connection_string): 
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""
        SELECT 
        	DISTINCT(nts.TabName) AS MainMenuTabs, ntt.TypeDescription AS SubMenuTabs
        FROM 
        	rf_nav_types_tabs nts 
        INNER JOIN 
        	rf_nav_types ntt
        ON	nts.TypeTabID = ntt.TypeTabID 
        ORDER BY 
        	MainMenuTabs, SubMenuTabs
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    #print(rows)

    result = []
    for row in rows:
        main_menu_tab, sub_menu_tab = row
        result.append({'MainMenuTab': main_menu_tab, 'SubMenuTab': sub_menu_tab})

    return result


# Will generate an array of all key value pairs of main menu tabs with their associated sub menu tabs with their assocaited sub sub menu tabs.
def getCorrespondingMainMenuAndSubMenuTabsForAGivenSystemAndSubSubMenuTabs(connection_string): 
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""
        SELECT 
        	nts.TabName AS MainMenuTabs, ntt.TypeDescription AS SubMenuTabs, ct.TabDisplayName AS SubSubMenuTabsContacts, lt.TabDisplayName AS SubSubMenuTabsLoc, att.TabDisplayName AS SubSubMenuTabsAbsenceTypes , smt.Description AS SubSubMenuTabsShiftMask
        FROM 
        	rf_nav_types_tabs nts 
		INNER JOIN 
        	rf_nav_types ntt
        ON	nts.TypeTabID = ntt.TypeTabID 
		LEFT JOIN 
			rf_Contacts_Tabs ct 
		ON ntt.TypeLabelSetID = ct.LabelSetID
		LEFT JOIN 
			rf_Location_Tabs lt
		ON ntt.TypeLabelSetID = lt.LabelSetID
		left join 
			rf_Absence_Types_Tabs att
		ON ntt.Typecode = 'ABSENCETYPE'
		left join 
			rf_Shift_Mask_Tabs smt
		ON ntt.Typecode = 'Shift' AND ntt.TypeLabelSetid = 1
        ORDER BY 
        	MainMenuTabs, SubMenuTabs, SubSubMenuTabsContacts, SubSubMenuTabsLoc, SubSubMenuTabsAbsenceTypes, SubSubMenuTabsShiftMask
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    #print(rows)

    result = []
    for row in rows:
        main_menu_tab, sub_menu_tab, sub_sub_menu_tab_contact, sub_sub_menu_tab_loc, sub_sub_menu_tab_abs, sub_sub_menu_tab_shift_mask = row
        result.append({'MainMenuTab': main_menu_tab
                       , 'SubMenuTab': sub_menu_tab
                       , 'SubSubMenuContactTab': sub_sub_menu_tab_contact
                       , 'SubSubMenuTabLocTab': sub_sub_menu_tab_loc
                       , 'SubSubMenuTabAbsenceType': sub_sub_menu_tab_abs
                       , 'SubSubMenuTabShiftMask': sub_sub_menu_tab_shift_mask
        })

    return result


if __name__ == "__main__":
    #username = '' # 'your_username'
    #password = '' # 'your_password'

    username = ""
    password = "!"
    
    #target_sys = 'NextraTest_v4_2_SQL'
    #checkTimesheetRuns(target_sys, None, None, username, password) 
    # 2022-01-25

    #target_sys_db = 'BritishHome_Live' + '_SQL'
    #target_system_generic = "British Home"

    ## redfining for readability within the connection string
    #db = target_sys_db
    ## Will fetch dns/port based on default target system given to bugSplatter on inital startup
    #server = get_server_auto(db)
    #print(server)

    #target_sys_db = 'BritishHome_Live' + '_SQL'
    #client = "British" # Based of langauage name 


    # redfining for readability within the connection string
    #db = target_sys_db
    # Will fetch dns/port based on default target system given to bugSplatter on inital startup
    #server = get_server_auto(db)

    # Example usage:
    #conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'
    #folder_path = "..\\excel_sheets\\admin_nav\\"
    #filename = "main_menu_options.xlsx"
    #fullpath = os.path.join(folder_path, filename)
    #client = "British"

    #conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'
    ##folder_path = "..\\excel_sheets\\admin_nav\\"
    #folder_path = "..\\excel_sheets\\admin_nav\\sub_menu_tabs\\"
    ##filename = f"main_menu_options_{client.lower}.xlsx"
    #filename = f"sub_menu_options_{client.lower()}.xlsx"
    #fullpath = os.path.join(folder_path, filename)

    #populateExcelSheetWithExpecrfNavTypesTabs(conn_string, fullpath, client)

    #populateExcelSheetWithExpecrfNavTypes(conn_string, fullpath, client)

    target_sys_db = 'BritishHome_Live' + '_SQL'
    client = "British" # Based of langauage name 


    # redfining for readability within the connection string
    db = target_sys_db
    # Will fetch dns/port based on default target system given to bugSplatter on inital startup
    server = get_server_auto(db)

    conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'

    folder_path = "..\\excel_sheets\\admin_nav\\main_menu_tabs\\"
    filename = f"main_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecrfNavTypesTabs(conn_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_menu_tabs\\"
    filename = f"sub_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecrfNavTypes(conn_string, fullpath, client)
    

    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_contact_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecrfContactsTabs(conn_string, fullpath, client)
    
    
    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_location_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecLocTabs(conn_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_absence_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecAbsenceTypeTabs(conn_string, fullpath, client)

    folder_path = "..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\"
    filename = f"sub_sub_shiftmask_menu_tabs_{client.lower()}.xlsx"
    fullpath = os.path.join(folder_path, filename)
    populateExcelSheetWithExpecShiftMaskTabs(conn_string, fullpath, client)