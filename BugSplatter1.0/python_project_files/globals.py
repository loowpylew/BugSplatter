import f_driver_init as fdi 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from openpyxl import load_workbook
import openpyxl
from openpyxl.styles import PatternFill, Font
import xlsxwriter
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os 
import time 
import json
import admin as a
import menu_items as mi

# Initialize colorama
init()

# To note* - Always create a 'nested' version of the function you make for modulation purposes. 
# i.e. You as the user could've already called to log into a system when creating your own batch processes. 
#      Therefore, re-logging in within another process for instance: 'check the user role is root upon entering the homepage
#      would call the login function again if we didnt have a the nested version of 'checkInitialUserRole' to select from. 
# Params to look out for: 
# driver_response=None, optional_error_catch=None
# driver_response=None: You would define this in the instance you're not passing the function over to another function as it will intialize its own driver repsonse that will be passed to it. 
# optional_error_catch=None: You would define to activate 'Test Status' results, when you don't pass a parameter in main, it will not return any 'Test Status'result and just perform the action of
# the contents within the nested function, otherwise, will return the test status.  


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Check Login 
def loginToUserAccount(target_sys, headless_mode, username, password, driver_response=None, optional_error_catch=None): 
    

    def loginToUserAccount(driver_response, target_sys, username, password): 

         # Read the JSON file
        with open('..\\json_config\\system_urls.json', 'r') as file:
            json_data = json.load(file)
        
        if target_sys in json_data["urls"]: 
            url = json_data["urls"][target_sys] # urls now given unique binding thus will fetch from json config. Relates to the system you input during startup
            #print(url)
        else: 
            print("Error: Target System does not have an associated URL.")
        
        #url = f'https://dev.nextracloud.com/{target_sys}/login' - old method
        driver_response.get(url)    

        # Wait for the username input field to be visible and clickable    

        wait = WebDriverWait(driver_response, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "username")))    

        username_element = driver_response.find_element(By.ID, "username")
        username_element.click()
        username_element.clear()  # Clear any existing text
        username_element.send_keys(username)
        password_element = driver_response.find_element(By.ID, "password")
        password_element.send_keys(password)
        login_button = driver_response.find_element(By.ID, "loginScreen-button")
        login_button.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass
 
    if optional_error_catch is not None:
        loginToUserAccount(driver_response, target_sys, username, password)
    else: 
        try: 
            loginToUserAccount(driver_response, target_sys, username, password)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Login and Load Homepage 
def loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response=None, optional_error_catch=None): 


    def loginAndLoadHomePage(driver_response): 
        wait = WebDriverWait(driver_response, 10)
        # Home section class name for Hompage 
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "home-section")))


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        loginToUserAccount(target_sys, headless_mode, username, password, driver_response, True) # Always specify true when using an external function to avoid locla host timeouts.
        loginAndLoadHomePage(driver_response)
    else: 
        try: 
            loginToUserAccount(target_sys, headless_mode, username, password, driver_response, True) # Always specify true when using an external function to avoid local host timeouts.
            loginAndLoadHomePage(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
    

# Check User Role
def checkInitialUserRole(target_sys, headless_mode, username, password, driver_response=None, optional_error_catch=None):

    errors_responses = []


    def checkInitialUserRole(driver_response): 
        # Based on the target system. This will determine the expected role.
        if target_sys == 'NextraTest_NHSBT_Upgrade': 
            expected_role = 'Administrator (NHSBT) - NHSBT Root | Corporate'
        elif target_sys == 'NextraDev': 
            expected_role = 'System Administrator - Corporate'
        else: 
            pass
        
        # Wait for the page to load (you may need to adjust the wait time)
        WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))

        # Find the <select> element with class "switchroleDropList"
        select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

        # Get the text of the selected option
        selected_option = select_element.find_element(By.CSS_SELECTOR, 'option:checked')
        user_role = selected_option.text.strip()

        # Check if the user role matches the expected role
        if user_role != expected_role: # and for more conditions that need to be met within the homepage
            errors_responses.append("User role does not match the expected user role for the current system.")


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        checkInitialUserRole(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)
            checkInitialUserRole(driver_response)
            if len(errors_responses) == 0: 
                driver_response.quit()
                print(f"{Fore.GREEN}Test Passed{Fore.WHITE}")
            else: 
                driver_response.quit()
                print(f"{Fore.RED}Test Failed{Fore.WHITE}")
                for error in errors_responses:
                    print(f"{Fore.RED}Error:{Fore.WHITE}", error)
        except Exception as e: 
            driver_response.quit()
            # In the instance the webdriver couldn't find the specified elements
            print(f"{Fore.RED}Test Failed{Fore.WHITE}\n")
            print(f"{Fore.RED}Error: {Fore.WHITE}Webdriver could not find a specific web object specified within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}Webdriver response: {Fore.WHITE} \n{e}")


# Check Homepage has expected Characteristics
def checkHomePageloaded(target_sys, headless_mode, username, password, driver_response=None, optional_error_catch=None): 
    # Example:
    # Check another aspect of the page
    # if some_condition:
    #     errors_responses.append("Error message for the condition")    
    errors_responses = []

    def checkHomePageLoaded(driver_response, headless_mode, target_sys, username, password): 

        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)
        
        # Wait for the page to load (you may need to adjust the wait time)
        WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))    

        ########################################Validating Page Structure######################################    

        # Home Page expected partial Greeting
        expected_greeting_parts = ["Good morning", "Good afternoon", "Good evening", "Hello"]    

        # Find the element with the class "welcome-text" and get its text content
        # Wait for the element with the class "welcome-text" to be visible
        wait = WebDriverWait(driver_response, 10)
        welcome_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "welcome-text")))    

        actual_greeting = welcome_element.text    

        # Check if any of the expected greeting parts is present in the actual greeting
        if not any(part in actual_greeting for part in expected_greeting_parts):
            errors_responses.append(f"Greeting does not contain any of the expected parts: {expected_greeting_parts}")    

        # Continue to check other aspects of the page and append errors to the errors_responses list if any    

        expected_tile_titles = ["Absence Summary", "Next Absence", "Next Shift"]
           
        # Wait for the parent elements to be present with unique IDs
        parent_element_1 = WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HOMEPAGE_203_header_content_scroll")))
        parent_element_2 = WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HOMEPAGE_204_header_content_scroll")))
        parent_element_3 = WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HOMEPAGE_34_header_content_scroll")))

        # Wait for the <h1> element to be present within the parent element
        h1_element_1 = WebDriverWait(parent_element_1, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element_2 = WebDriverWait(parent_element_2, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element_3 = WebDriverWait(parent_element_3, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Get the text from the <h1> elements
        text_1 = h1_element_1.text  # "Absence Summary"
        text_2 = h1_element_2.text  # "Next Absence"
        text_3 = h1_element_3.text  # "Next Shift"

        if text_1 == expected_tile_titles[0]:
           pass 
        else: 
           errors_responses.append(f"Tile does not contain the correct title: {expected_tile_titles[0]}")   
         
        if text_2 == expected_tile_titles[1]:
           pass 
        else: 
           errors_responses.append(f"Tile does not contain the correct title: {expected_tile_titles[1]}")   

        if text_3 == expected_tile_titles[2]:
           pass 
        else: 
           errors_responses.append(f"Tile does not contain the correct title: {expected_tile_titles[2]}")     

        
    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        checkHomePageLoaded(driver_response, target_sys, username, password)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            checkHomePageLoaded(driver_response, target_sys, username, password)
            if len(errors_responses) == 0: 
                driver_response.quit()
                print(f"{Fore.GREEN}Test Passed{Fore.WHITE}")
            else: 
                driver_response.quit()
                print(f"{Fore.RED}Test Failed{Fore.WHITE}")
                for error in errors_responses:
                    print(f"{Fore.RED}Error: {Fore.WHITE}", error)
        except Exception as e: 
            driver_response.quit()
            # In the instance the webdriver couldn't find the specified elements
            print(f"{Fore.RED}Test Failed{Fore.WHITE}\n")
            print(f"{Fore.RED}Error:{Fore.WHITE}Webdriver could not find a specific web object specified within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}Webdriver response: {Fore.WHITE}\n{e}")


def web_element_exists(selector_function):
    try:
        selector_function # Just runs function you pass, if any errors occur, will fail and will be caught.
        return True
    except NoSuchElementException:
        return False

# This function differs from the usertype checker used for batch processes.
# The batch processes version will define the column name used within the excel spreadsheets. 
# Whereas this function strictly uses the entire name of the usertype/location to produce the XPATH to click on. 
# SELECT DISTINCT 
#     u.username + ' - ' + 
#     l.LocationName + 
#     ISNULL(' | ' + pl.LocationName, '') AS FullLocationName
# FROM
#     rf_Contacts_Roles cr
# INNER JOIN 
#     rf_usertypes u ON cr.RoleID = u.UsertypeID 
# INNER JOIN
#     rf_location l ON cr.LocationID = l.LocationID 
# LEFT JOIN
#     rf_location pl ON l.ParentLocationID = pl.LocationID;
# ^ Useful query to discover every usertype/location/parentlocation permutation.
def checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    # IMPORTANT - WILL NEED TO ADD MORE USERTYPES 
    def checkAndSwitch(driver_response, target_sys, user_type):
        drop_list_xpath = '/html/body/section/div[2]/div/div[1]/select' # Indexing remains consistant across systems for class="switchroleDropList" <select> element.
   
        desired_user_type = {
            "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {}
            , "": {
                    '{Place Usertype name as shown on front end} : f"{drop_list_xpath}/option[text()='{Place Usertype Name as shown on front end}']"
            }
                
        }   
          
        # Wait for the page to load (you may need to adjust the wait time)
        WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))

        # Find the <select> element with class "switchroleDropList"
        select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

        # Get the text of the selected option
        selected_option = select_element.find_element(By.CSS_SELECTOR, 'option:checked')
        
        user_role = selected_option.text.strip()
        
        # will need to change so that shortened usertype in excel sheet is equal to the text in user role i.e. 
        # create a list of usertypes as shown in the bnbrwoser thhat match with the shortend versions i.e. 
        #usertype_list_excel_accom = { 
        #    Administrator (NHSBT): System Administrator - Corporate
        #}

        # if user_role == usertype_list_excel_accom[usertype]
        # pass

        if user_role == user_type:
           #print("Should return 'True' as they're the same")
           return True
        elif target_sys in desired_user_type: 
            #print("This should only trigger if they're the same")
            #select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

            #print(desired_user_type[target_sys][user_type])

            select_user_role = select_element.find_element(By.XPATH, desired_user_type[target_sys][user_type])

            # Scroll the element into view if needed
            driver_response.execute_script("arguments[0].scrollIntoView();", select_user_role)

            # Click the element using execute_script directly
            driver_response.execute_script("arguments[0].click();", select_user_role)

            # Select the desired option by its value
            select_user_role.click()

            return True
        else: 
            #print("This should trigger if the usertype doesn't exist")
            return False

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        checkAndSwitch(driver_response, target_sys, user_type)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            checkAndSwitch(driver_response, target_sys, user_type)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"User type doesn't exist for current system: {target_sys}")
            print("Value inputted: ", e)
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            


#def checkUserRoleAndSwitch(driver_response, target_sys, user_type):
#    
#    drop_list_xpath = '/html/body/section/div[2]/div/div[1]/select' # Indexing remains consistant across systems for class="switchroleDropList" <select> element.
#   
#    desired_user_type = {
#        "DemandEngine_Dev": {}
#        , "DemandEngine_NextraDev": {}
#        , "DemandEngine_NextraTest": {}
#        , "NextraDemo_Hutchison": {}
#        , "NextraDemo_Lite_v4_2": {}
#        , "NextraDemo_Lite2_v4_2": {}
#        , "NextraDemo_v4_2": {}
#        , "NextraDev_1": {}
#        , "NextraDev_2": {}
#        , "NextraDev_3": {}
#        , "NextraDev": {}
#        , "NextraPreRelease": {}
#        , "NextraRefSQL": {}
#        , "NextraRelease_4_0": {}
#        , "NextraRelease_4_1_1": {}
#        , "NextraRelease_4_1": {}
#        , "NextraRelease_4_2_0": {}
#        , "NextraRelease_4_2_1": {}
#        , "NextraRelease_4_2_2": {}
#        , "NextraRelease_4_2_3": {}
#        , "NextraRelease_Candidate": {}
#        , "NextrasoftLiveSQL_CloudHR": {}
#        , "NextraTest_ANRG": {}
#        , "NextraTest_BritishHome": {}
#        , "NextraTest_NHSBT": {}
#        , "NextraTest_NHSBT_Upgrade": {
#            'System Administrator': f"{drop_list_xpath}/option[text()='System Administrator - Corporate']"
#            ,'Employee': f"{drop_list_xpath}/option[text()='Employee - NHSBT Root | Corporate']"
#            ,'Administrator (NHSBT)': f"{drop_list_xpath}/option[text()='Administrator (NHSBT) - NHSBT Root | Corporate']"
#            ,'Pay Support': f"{drop_list_xpath}/option[text()='Pay Support - NHSBT Root | Corporate']"
#            ,'Manager': f"{drop_list_xpath}/option[text()='Manager - NHSBT Root | Corporate']"
#            ,'Model Adjustments': f"{drop_list_xpath}/option[text()='Model Adjustments - NHSBT Root | Corporate']"
#            ,'National Managers': f"{drop_list_xpath}/option[text()='National Managers - NHSBT Root | Corporate']"
#            ,'Regional Manager': f"{drop_list_xpath}/option[text()='Regional Manager - NHSBT Root | Corporate']"
#            ,'Area Manager': f"{drop_list_xpath}/option[text()='Area Manager - NHSBT Root | Corporate']"
#            ,'Data upload': f"{drop_list_xpath}/option[text()='Data upload - NHSBT Root | Corporate']"
#            ,'PerfTest': f"{drop_list_xpath}/option[text()='PerfTest - NHSBT Root | Corporate']"
#            ,'Reporting': f"{drop_list_xpath}/option[text()='Reporting - NHSBT Root | Corporate']"
#            ,'Test': f"{drop_list_xpath}/option[text()='Test - NHSBT Root | Corporate']"
#        }
#        , "NextraTest_v4_2": {}
#        , "NextraTimesheet_NextraDev": {}
#    }    
#      
#    # Wait for the page to load (you may need to adjust the wait time)
#    WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))#

#    # Find the <select> element with class "switchroleDropList"
#    select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')#

#    # Get the text of the selected option
#    selected_option = select_element.find_element(By.CSS_SELECTOR, 'option:checked')
#    
#    user_role = selected_option.text.strip()
#    
#    try: 
#        # will need to change so that shortened usertype in excel sheet is equal to the text in user role i.e. 
#        # create a list of usertypes as shown in the bnbrwoser thhat match with the shortend versions i.e. 
#        #usertype_list_excel_accom = { 
#        #    Administrator (NHSBT): System Administrator - Corporate
#        #}#

#        # if user_role == usertype_list_excel_accom[usertype]
#        # pass#

#        if user_role == user_type:
#           pass
#        else: 
#            if target_sys in desired_user_type: 
#                #select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')#

#                #print(desired_user_type[target_sys][user_type])#

#                select_user_role = select_element.find_element(By.XPATH, desired_user_type[target_sys][user_type])#

#                # Scroll the element into view if needed
#                driver_response.execute_script("arguments[0].scrollIntoView();", select_user_role)#

#                # Click the element using execute_script directly
#                driver_response.execute_script("arguments[0].click();", select_user_role)#

#                # Select the desired option by its value
#                select_user_role.click()#

#                return True
#    except: 
#        print(f"User type doesn't exist for current system: {target_sys}")
#        return False
            

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
        with open('..\\json_config\\dns_server_list.json', 'r') as file:
            json_data = json.load(file)

        # Print server options
        for key, value in json_data["DNS_server_list"].items():
            print(f"{key}: {value['name']} ({value['host']}:{value['port']})")

        print("Please enter the server option (1-7): ")
        option = input()

        # Check if the entered option is valid
        if option in json_data["DNS_server_list"]:
            selected_server = json_data["DNS_server_list"][option]
            print(f"You selected: {selected_server['name']} ({selected_server['host']}:{selected_server['port']})")

            print(selected_server['host'] + "," + selected_server['port'])
            return selected_server['host'] + "," + selected_server['port']# Return the selected server
        else:
            print("Invalid option. Please enter a valid option.")


def get_nextra_contact_ids(username): 
    # Read the JSON file
    with open('..\\json_config\\contact_ids.json', 'r') as file:
        json_data = json.load(file)

    user_id = None  # Initialize with a default value
    
    if username in json_data["contact_id's"]: 
        user_id = json_data["contact_id's"][username]
    
    return user_id


########################################################## WRAPPER FUNCTIONS FOR TARGET WEB OBJECTS ################################################################

def web_element_exists(selector_function):
    try:
        selector_function() # Just runs function you pass, if any errors occur, will fail and will be caught.
        return True
    except TimeoutException:
        return False 
    except NoSuchElementException:
        return False
    except: 
        False

# Function Meta data - required to specify what item the function derives from:

# Tags for Admin: Main Menu Items 
a.adminLoadMenuTabs.tag = ["ADMIN", "Main Menu Option - "] 
# Tags for Admin: Sub Menu Item 
a.adminLoadSubMenuTabs.tag = ["ADMIN", "Sub Menu Option - "]
# Tag for Admin: Sub Sub Menu Items 
a.adminLoadSubSubMenuTabs.tag = ["ADMIN", "Sub Sub Menu Option - "]

# Logs into system, updates the user role and checks to see if the homepage tile exists. 
# This has been replicated from user_tiles.py and can be further condensed to reduce repeated code. 

def target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response):
    # Call the login function to log in and open the Homepage
    loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

    # Check user role, switch if not the desired target
    if lambda: checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True):
        user_role_perm_check = True
    else: 
        print("Result: ", checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True))
        user_role_perm_check = False

    #print(target_func.tag[0])

    # Conditional logic to open menu item based on function meta data associated with it.  
    if hasattr(target_func, 'tag') and target_func.tag[0] == "HOME":
        pass 
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "ADMIN":
        mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "MANAGEMENT":
        mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "BANK":
        mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "DATA PROCESSING":
        mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "SELF SERVICE":
        mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "REPORTS":
        mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "DASHBOARD REPORTS":
        mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "ABOUT":
        mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
    
    return user_role_perm_check


# This Function will do the following: 
# Check if all web_objects exist or not
# If an 'X' is present within a cell, will colour GREEN to signify it exists for that usertype 
# If an 'X' is present within a cell, will colour RED to signify it does not exist for that usertype
# If a cell is empty, will check if the web object exists or not. 
# If it does exist for that usertype, will highlight red to signify it should not exist for that usertype, otherwise, will leave as is. 
# Perfecto!
####################################################################END OF WRAPPER FUNCTION######################################################################

def global_web_object_processor_main_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    cell = row[object] # object3 being one of the following: 
                        #'SubSubMenuContactTab'
                        #, 'SubSubMenuTabLocTab'c
                        #, 'SubSubMenuTabAbsenceType'
                        #, 'SubSubMenuTabShiftMask'

    print("Cell Value:", cell)
    if cell == 'X':
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)
                               
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object, 'X', False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object) + f"' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
                return worksheet, object, 'X', True
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object) + f"' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', red_format)
                return worksheet, object, 'X', False
        else: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object, 'X', False

    elif pd.isna(cell): #  the NaN values are of type float, not a string
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)

        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the {target_func.tag[1]}" + str(object) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, driver_response, True)
            if web_element_exists(web_object):                                              #{target_func.tag[1]} replace when all fucntions have been implemented
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object) + f"' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                #worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
                return worksheet, object, '', True
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object) + f"' does not exist{Fore.WHITE}")
        else:
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")


def global_web_object_processor_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, object2, worksheet, df, green_format, red_format): 
    cell = row[object2] # object3 being one of the following: 
                        #'SubSubMenuContactTab'
                        #, 'SubSubMenuTabLocTab'c
                        #, 'SubSubMenuTabAbsenceType'
                        #, 'SubSubMenuTabShiftMask'

    print("Cell Value:", cell)
    if cell == 'X':
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)
                               
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object2) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object2, 'X', False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object2, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object2) + f"' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object2), 'X', green_format)
                return worksheet, object2, 'X', True
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object2) + f"' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object2), 'X', red_format)
                return worksheet, object2, 'X', False
        else: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object2) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object2, 'X', False

    elif pd.isna(cell): #  the NaN values are of type float, not a string
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)

        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the {target_func.tag[1]}" + str(object2) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object2, driver_response, True)
            if web_element_exists(web_object):                                              #{target_func.tag[1]} replace when all fucntions have been implemented
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object2) + f"' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                #worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
                return worksheet, object2, '', True
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object2) + f"' does not exist{Fore.WHITE}")
        else:
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object2) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")


def global_web_object_processor_sub_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, object2, object3, worksheet, df, green_format, red_format): 
    cell = row[object3] # object3 being one of the following: 
                        #'SubSubMenuContactTab'
                        #, 'SubSubMenuTabLocTab'c
                        #, 'SubSubMenuTabAbsenceType'
                        #, 'SubSubMenuTabShiftMask'

    print("Cell Value:", cell)
    if cell == 'X':
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)
                               
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object3, 'X', False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object3, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object3) + f"' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object3), 'X', green_format)
                return worksheet, object3, 'X', True
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object3) + f"' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
                return worksheet, object3, 'X', False
        else: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            #worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            return worksheet, object3, 'X', False

    elif pd.isna(cell): #  the NaN values are of type float, not a string
        web_obj_sch = False
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)

        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the {target_func.tag[1]}" + str(object3) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object3, driver_response, True)
            if web_element_exists(web_object):                                              #{target_func.tag[1]} replace when all fucntions have been implemented
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object3) + f"' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                #worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
                return worksheet, object3, '', True
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object3) + f"' does not exist{Fore.WHITE}")
        else:
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")
        

# Old Version
#def global_web_object_processor_sub_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, object2, object3, worksheet, df, green_format, red_format): 
    cell = row[object3] # object3 being one of the following: 
                        #'SubSubMenuContactTab'
                        #, 'SubSubMenuTabLocTab'c
                        #, 'SubSubMenuTabAbsenceType'
                        #, 'SubSubMenuTabShiftMask'

    print("Cell Value:", cell)
    if cell == 'X':
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)
                               
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object3, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object3) + f"' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object3), 'X', green_format)
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object3) + f"' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)
        else: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            worksheet.write(index + 1, df.columns.get_loc(object3), 'X', red_format)

    elif pd.isna(cell): #  the NaN values are of type float, not a string
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)

        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the {target_func.tag[1]}" + str(object3) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, object, object2, object3, driver_response, True)
            if web_element_exists(web_object):                                              #{target_func.tag[1]} replace when all fucntions have been implemented
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}" + str(object3) + f"' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}" + str(object3) + f"' does not exist{Fore.WHITE}")
        else:
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}" + str(object3) + f"' tile does not exist or has issues as stated above{Fore.WHITE}")