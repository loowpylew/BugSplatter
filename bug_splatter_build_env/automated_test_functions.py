import f_driver_init as fdi 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.common.exceptions import NoSuchElementException
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


# Login function
def loginToUserAccount(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    

    def loginToUserAccount(driver_response, target_sys, username, password): 
        url = f'https://dev.nextracloud.com/{target_sys}/login'
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
        driver_response = fdi.initialize_driver()
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


# Used to reduce code duplication in 'loginAndLoadHomePage()' 
def loginAndLoadHomePage(target_sys, username, password, driver_response=None, optional_error_catch=None): 


    def loginAndLoadHomePage(driver_response): 
        wait = WebDriverWait(driver_response, 10)
        # Home section class name for Hompage 
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "home-section")))


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
        loginToUserAccount(target_sys, username, password, driver_response, True) # Always specify true when using an external function to avoid locla host timeouts.
        loginAndLoadHomePage(driver_response)
    else: 
        try: 
            loginToUserAccount(target_sys, username, password, driver_response, True) # Always specify true when using an external function to avoid local host timeouts.
            loginAndLoadHomePage(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
    

def checkInitialUserRole(target_sys, username, password, driver_response=None, optional_error_catch=None):

    errors_responses = []


    def checkInitialUserRole(driver_response): 
        # Based on the target system. This will determine the expected role.
        if target_sys == 'NextraTest_NHSBT_Upgrade': 
            expected_role = 'Administrator (NHSBT) - NHSBT Root | Corporate'
        elif target_sys == 'NextraDev': 
            expected_role = 'NEXTRA Development - NEXTRA | Corporate'
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
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
        checkInitialUserRole(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
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


def checkHomePageloaded(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    # Example:
    # Check another aspect of the page
    # if some_condition:
    #     errors_responses.append("Error message for the condition")    
    errors_responses = []

    def checkHomePageLoaded(driver_response, target_sys, username, password): 

        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)
        
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
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
        checkHomePageLoaded(driver_response, target_sys, username, password)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

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



def homePageLoadAdminScreen(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    
    
    def clickAdminMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        admin_menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.nav-item[onclick*="homepageLoadAdminScreen()"]')))
        admin_menu_button.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickAdminMenuButton(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickAdminMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def staffAdminLoadMenuOptions(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    
    
    def clickStaffAdminButton(driver_response):
        # Wait for the "Staff Admin" link to become available
        wait = WebDriverWait(driver_response, 10)
        # Locate the "Staff Admin" link
        staff_admin_link = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="icon-link"]//span[text()="Staff Admin"]'))
        )     

        actions = ActionChains(driver_response)
        actions.move_to_element(staff_admin_link).click().perform() 


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass
    
    if optional_error_catch is not None:
       clickStaffAdminButton(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
           
            homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
            
            clickStaffAdminButton(driver_response)
        
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def staffAdminLoadEmployees(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    def clickEmployeesButton(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 10)
        # Locate and click the "Employees" link
        employees_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//li[@class="sub-menu-item"]//a[text()="Employees"]'))
        )
        employees_link.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
        clickEmployeesButton(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
           
            homePageLoadAdminScreen(target_sys, username, password, driver_response, True)

            staffAdminLoadMenuOptions(target_sys, username, password, driver_response, True)

            clickEmployeesButton(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


##########################################Batch Processes##########################################

def batchProcessEmployees(target_sys, username, password, paths): 
    try: 
        # Initialize the WebDriver (use the appropriate driver for your browser)
        driver_response = fdi.initialize_driver()    

        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)
        
        # Load up 'Admin Screen' 
        homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
         
        # Load up 'Staff Admin' Menu Options
        staffAdminLoadMenuOptions(target_sys, username, password, driver_response, True)
       
        # Locate and click the "Employees" button
        staffAdminLoadEmployees(target_sys, username, password, driver_response, True)

        # Used for all waits within this function after this line of code
        wait = WebDriverWait(driver_response, 10)

        if len(paths) >= 1: 
            for path in paths: 
                employee_data = pd.read_excel(path, sheet_name="Employees")

                # Find all elements with class "inputLabel"

                for index, row in employee_data.iterrows():
                    # Now, locate and click the "plus" button to load up the "Create" button
                    plus_button = wait.until(EC.element_to_be_clickable((By.ID, "actionToggleIcon")))
                    plus_button.click()
                    
                    # Click the "Create" button to add a new employee
                    # Because there is no exact id/class match, the function fails
                    try: 
                        create_button = wait.until(EC.element_to_be_clickable((By.ID, "rfdrop_action_addnewdata")))
                        create_button.click()
                    except: 
                        pass
    
                    # Add a wait to switch to the "contactframe" iframe
                    wait.until(frame_to_be_available_and_switch_to_it((By.ID, "contactframe")))
                                 
                    # Add a wait to locate the `select` element inside the `dcTable`
                    select_element = wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//table[@class='dcTable']//select[contains(@class, 'inputLabel')]")))             

                    # Create a Select object for the dropdown
                    select = Select(select_element)            

                    # Input the Principle Site from the Excel sheet
                    principle_site = row['Principle Site']            
                 
                    # Use the Select object to select the option by visible text
                    select.select_by_visible_text(principle_site)

                    first_name = row['First Name']

                    first_name_input = driver_response.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")       

                    first_name_input.send_keys(first_name)

                    # Input Last Name
                    last_name = row['Last Name']
                   
                    last_name_input = driver_response.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input") 
                   
                    last_name_input.send_keys(last_name)

                    # Input Assignment Number
                    assignment_number = row['Assignment Number']

                    print(row.keys())
                   
                    assignment_input = driver_response.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/input") 
                   
                    assignment_input.send_keys(assignment_number)
                 
                    # Input Start Date
                    formatted_start_date = datetime.strptime(row['Start Date'], "%d-%m-%Y").strftime("%Y-%m-%d")
                    start_date_input = driver_response.find_element(By.XPATH, "/html/body/form/table/tbody/tr[5]/td[2]/input")
                    start_date_input.send_keys(formatted_start_date)

                    # Submit employee creation form
                    #ok_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="RF_SUBMIT"][value="OK"]')))
                    #ok_button.click()

                    # Cancel employee creation for testing purposes
                    cancel_button =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="RF_CANCEL"][value="Cancel"]')))
                    cancel_button.click()

                    # To switch back to the main content after interacting with elements in the iframe
                    driver_response.switch_to.default_content()

        print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        # Close the WebDriver after processing all employees
        driver_response.quit()
    except Exception as e: 
        driver_response.quit()
        print(f"{Fore.RED}Test Failed{Fore.WHITE}")
        print(e)


def checkUserRoleAndSwitch(driver_response, user_type):

    desired_option_values = {
        'Administrator': '/html/body/section/div[2]/div/div[1]/select/option[3]'
        , 'Employee': '/html/body/section/div[2]/div/div[1]/select/option[13]'
        , 'Manager': '/html/body/section/div[2]/div/div[1]/select/option[14]'
        , 'Pay Support': '/html/body/section/div[2]/div/div[1]/select/option[15]'
    }

    #'/html/body/section/div[2]/div/div[1]/select/option[1]'    # System Administrator - ABP | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[2]'  # System Administrator - Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[3]'  # System Administrator - NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[4]'  # Administrator (NHSBT) - Cumbria Team | NE & Cumbria | North | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[5]'  # Administrator (NHSBT) - Hertfordshire Team | Central South | East | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[6]'  # Administrator (NHSBT) - Luton DC | Central South | East | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[7]'  # Administrator (NHSBT) - MAIDSTONE TEAM | Kent & East Sussex | London and South East | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[8]'  # Administrator (NHSBT) - Newcastle Team | NE & Cumbria | North | Blood Donation | NHSBT Root | Corporate
    #, 'Administartor': '/html/body/section/div[2]/div/div[1]/select/option[9]'  # Administrator (NHSBT) - NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[10]' # Administrator (NHSBT) - Sheffield North Team | East Midlands | Central | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[11]' # Administrator (NHSBT) - SWINDON TEAM | South Midlands | West | Blood Donation | NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[12]' # Administrator (NHSBT) - WORCESTER TEAM | Central West | West | Blood Donation | NHSBT Root | Corporate
    #, 'Employee': '/html/body/section/div[2]/div/div[1]/select/option[13]' # Employee - NHSBT Root | Corporate
    #, 'Manager': '/html/body/section/div[2]/div/div[1]/select/option[14]' # Manager - NHSBT Root | Corporate
    #, 'Pay Support': '/html/body/section/div[2]/div/div[1]/select/option[15]' # Pay Support - NHSBT Root | Corporate
    #, '/html/body/section/div[2]/div/div[1]/select/option[16]' # PerfTest - NHSBT Root | Corporate
      
    # Wait for the page to load (you may need to adjust the wait time)
    WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))

    # Find the <select> element with class "switchroleDropList"
    select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

    # Get the text of the selected option
    selected_option = select_element.find_element(By.CSS_SELECTOR, 'option:checked')
    
    user_role = selected_option.text.strip()

    try: 
        if user_role == user_type:
           pass
        else: 
            #select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

            select_user_role = select_element.find_element(By.XPATH, desired_option_values[user_type])

            # Select the desired option by its value
            select_user_role.click()
    except: 
        print("User type doesn't exist for current system") 


def web_element_exists(selector_function):
    try:
        selector_function # Just runs function you pass, if any errors occur, will fail.
        return True
    except NoSuchElementException:
        return False


#########################################################User Type function calls################################################################
def process_admin_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format):
    # switch to user role i.e. user_role_list[0] 
    admin_cell = row[object]
    if admin_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)

        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Admin' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Admin' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Admin' doesn't need to be checked for User type '{user_type}'")
        pass


def process_rota_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    rota_cell = row[object]
    if rota_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Rota' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Rota' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Rota' doesn't need to be checked for User type '{user_type}'")
        pass


def process_quick_entry_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    quick_entry_cell = row[object]
    if quick_entry_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Quick Entry Screen' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Quick Entry Screen' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Scheduled Rotas' doesn't need to be checked for User type '{user_type}'")
        pass


def process_scheduled_rota_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    sch_rota_cell = row[object]
    if sch_rota_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Scheduled Rotas' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Scheduled Rotas' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Scheduled Rotas' doesn't need to be checked for User type '{user_type}'")
        pass


def process_scheduled_job_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    sch_jb_cell = row[object]
    if sch_jb_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Scheduled Jobs' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Scheduled Jobs' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Scheduled Jobs' doesn't need to be checked for User type '{user_type}'")
        pass

def process_download_esr_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    rota_cell = row[object]
    if rota_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object ''Download ESR Files' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Download ESR Files' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Download ESR Files' doesn't need to be checked for User type '{user_type}'")
        pass


def process_skills_expiry_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    skills_exp_cell = row[object]
    if skills_exp_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Skills Expiry' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Skills Expiry' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Skills Expiry' doesn't need to be checked for User type '{user_type}'")
        pass


def process_rosta_changes_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    rosta_chg_cell = row[object]
    if rosta_chg_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Roster Changes' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Roster Changes' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Roster Changes' doesn't need to be checked for User type '{user_type}'")
        pass

def process_year_annual_leave_adjust_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    yr_ann_cell = row[object]
    if yr_ann_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Year Annual Leave Adj.' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Year Annual Leave Adj.' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Year Annual Leave Adj.' doesn't need to be checked for User type '{user_type}'")
        pass

def process_esr_bulk_timesheets_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
     esr_blk_cell = row[object]
     if esr_blk_cell == 'X':
         # Call the login function to log in and open the Homepage
         loginAndLoadHomePage(target_sys, username, password, driver_response, True)

         checkUserRoleAndSwitch(driver_response, user_type)

         # Replace 'web_object' with the actual method you use to find the web element
         web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
         if web_element_exists(web_object):
             print(f"User type '{user_type}': Web object 'Run ESR Calcs/ Bulk Schedule Timesheets' exists")
             # Update the Excel sheet with 'X' and apply the green format.
             worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
         else:
             print(f"User type '{user_type}': Web object 'Run ESR Calcs/ Bulk Schedule Timesheets' does not exist")
             # Update the Excel sheet with ' ' (empty space) and apply the red format.
             worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
     else: 
        print(f"Web Object 'Run ESR Calcs/ Bulk Schedule Timesheets' doesn't need to be checked for User type '{user_type}'")
        pass

def process_team_calc_sch_timesheets(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    team_clc_cell = row[object]
    if team_clc_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Single Team Calc/ Schedule Timesheets' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Single Team Calc/ Schedule Timesheets' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Single Team Calc/ Schedule Timesheets' doesn't need to be checked for User type '{user_type}'")
        pass

def process_timesheet_runs_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    tsheet_runs_cell = row[object]
    if tsheet_runs_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Timehseet Runs' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Timehseet Runs' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Timehseet Runs' doesn't need to be checked for User type '{user_type}'")
        pass

def process_absence_req_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    absence_req_cell = row[object]
    if absence_req_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Absence Requests' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Absence Requests' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Absence Requests' doesn't need to be checked for User type '{user_type}'")
        pass

def process_cf_req_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    cf_req_cell = row[object]
    if cf_req_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'C/F Requests' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'C/F Requests' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'C/F Requests' doesn't need to be checked for User type '{user_type}'")
        pass

def process_admin_msg_board_object(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    ad_msg_brd_cell = row[object]
    if ad_msg_brd_cell == 'X':
        # Call the login function to log in and open the Homepage
        loginAndLoadHomePage(target_sys, username, password, driver_response, True)

        checkUserRoleAndSwitch(driver_response, user_type)

        # Replace 'web_object' with the actual method you use to find the web element
        web_object = homePageLoadAdminScreen(target_sys, username, password, driver_response, True)
        if web_element_exists(web_object):
            print(f"User type '{user_type}': Web object 'Admin Msg Board' exists")
            # Update the Excel sheet with 'X' and apply the green format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
        else:
            print(f"User type '{user_type}': Web object 'Admin Msg Board' does not exist")
            # Update the Excel sheet with ' ' (empty space) and apply the red format.
            worksheet.write(index, df.columns.get_loc(object), ' ', red_format)
    else: 
        print(f"Web Object 'Admin Msg Board' doesn't need to be checked for User type '{user_type}'")
        pass


def batchProcessUserTypeTiles(target_sys, username, password, paths):

    # Define a mapping from object names to their corresponding processing functions
    object_processors = {
        "Admin": [process_admin_object]
        , "Rota": [process_rota_object]
        , "Quick Entry Screen": [process_quick_entry_object] 
        , "Scheduled Rotas": [process_scheduled_rota_object] 
        , "Scheduled Jobs": [process_scheduled_job_object]
        , "Download ESR Files": [process_download_esr_object]
        , "Skills Expiry": [process_skills_expiry_object]
        , "Roster Changes": [process_rosta_changes_object]
        , "Year Annual Leave Adj.": [process_year_annual_leave_adjust_object]
        , "Run ESR Calcs/ Bulk Schedule Timesheets": [process_esr_bulk_timesheets_object] 
        , "Single Team Calc/ Schedule Timesheets": [process_team_calc_sch_timesheets]
        , "Timehseet Runs": [process_timesheet_runs_object]
        , "Absence Requests": [process_absence_req_object]
        , "C/F Requests": [process_cf_req_object]
        , "Admin Msg Board": [process_admin_msg_board_object]
        # Add more objects and corresponding functions here
    }

    web_objects = ["Admin", "Rota", "Quick Entry Screen", "Scheduled Rotas", "Scheduled Jobs",
                   "Download ESR Files", "Skills Expiry", "Roster Changes", "Year Annual Leave Adj.",
                   "Run ESR Calcs/ Bulk Schedule Timesheets", "Single Team Calc/ Schedule Timesheets",
                   "Timehseet Runs", "Absence Requests", "C/F Requests", "Admin Msg Board"]

    #user_role_list = ['Administrator (NHSBT) - NHSBT Root | Corporate']

    for path in paths:
        df = pd.read_excel(path, sheet_name="Admin_Tiles", engine='openpyxl')
        output_path = path  # Create a new output file

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name="Admin_Tiles", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets["Admin_Tiles"]

        # Create XlsxWriter formats for the green and red colors.
        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})

        for index, row in df.iterrows():
            user_types = row['UserTypes'].split(', ')

            for user_type in user_types:
                #if user_type == 'Adminstrator': 

                for object in web_objects:
                    driver_response = fdi.initialize_driver()

                    # Check if the object has processing functions and call each one if it does
                    if object in object_processors:
                        for processing_functions in object_processors[object]:
                            try: 
                                processing_functions(target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                            except Exception as e:
                                print("Error finding Web_Object: ")
                                print(e)
                    driver_response.quit()  # Ensure that the WebDriver is always closed after checking a web object

        excel_writer.close()

        print("[Batch Process Complete]")