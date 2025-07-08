import globals as gs
import batch_processes as bp
import admin as a 
import user_tiles as ut
import menu_items as mi 
import admin as a
import threading
import f_driver_init as fdi
import os
import sys
import json
import pandas as pd
import time
import option_menus as om
from colorama import Fore, Style, init
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_alert(driver):
    while True:
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present()) # set for 10 seconds. After this time, this implies the test failed for 
                                                                           # for the timeout exception clause.
            if alert.text == "sessionTimeoutTest":
                print(f"Alert text: {alert.text}")
                return False
            if alert.text == "Error Building File!": 
                print(f"Alert text: {alert.text}")
                print("WARNING: Test was unsuccessful")
                print("Likey issue: relating to structure of function i.e. missing paraenthesis")
                return False
            elif alert.text == "Test Success":
                print(f"Alert text: {alert.text}")
                alert.accept()  # Click "OK" on the alert
                print("Alert accepted")
                return True
            elif alert.text == "View Build Log?":
                print(f"Alert text: {alert.text}")
                alert.accept()  # Click "OK" on the alert
                print("Alert accepted")
                return True
            else:
                print(f"Alert text: {alert.text}")
                alert.accept()  # Click "OK" on the alert
                print("Alert accepted")   
        except TimeoutException:
            print("No alert present within 10 seconds.")
            print("WARNING: Test was unsuccessful")
            print("Likey issue:  redeclaration of value passed to function - cannot redefine a variable that has already been declared within the same scope.")
            return False
        except NoAlertPresentException:
            print("No alert present.")
            print(f"WARNING: Test was unsuccessful")
            return False
        except Exception as e:
            #print(f"Failed to handle the alert: {e}")
            break  # Break out of the loop if there are no more alerts

#target_system, headless_mode, user_type, username, password

def buildAndReleaseManifests(target_sys, headless_mode, user_type, username, password, index, driver_response=None, optional_error_catch=None): 
    def navigateToBuildManifest(driver_response):
        wait = WebDriverWait(driver_response, 30)

        ## Load JSON configuration from file
        #with open('..\\json_config\\system_admin.json', 'r') as file:
        #    manifests_config = json.load(file)

        ## Will fetch the value correpsonding to the index that has been passed
        #
        #casted_index = str(index)

        #if casted_index in manifests_config["sys_admin"]: 
        #    manifest_name = manifests_config["sys_admin"][casted_index]

        manifest_name = index # logic to find value in key value pair found within main.py
            
        # Given there are multiple references to 'homepagesearch', we have had to specify the css selector in order to grab the required homepagesearch item.
        search_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#searchbar_rfautodrag_type_MANIFEST_1 .homepagesearch'))
        )
        
        # Wait for the search input element to be present and clickable
        #search_input = wait.until(EC.presence_of_element_located((By.ID, "homepagesearch")))

        # Scroll the element into view if needed 
        driver_response.execute_script("arguments[0].scrollIntoView();", search_input)        

        # Click the element using execute_script directly (you can omit this step if not needed) - execute script more headless friendly 
        driver_response.execute_script("arguments[0].click();", search_input)

        # Clear any existing text
        search_input.clear()

        # Insert a value into the search input
        search_input.send_keys(manifest_name)

        # Find the search button by its class name (assuming the class is unique)
        search_button_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "admin_reload")))
        
        
        # Find the <i> element within the container
        search_button = search_button_container.find_element(By.TAG_NAME, "i")

        # Scroll the element into view if needed 
        driver_response.execute_script("arguments[0].scrollIntoView();",  search_button)        

        # Click the element using execute_script directly - search button
        driver_response.execute_script("arguments[0].click();",  search_button)
        
        # 'id' will be the same as the Manifest name inputted
        manifest_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div[title*="{manifest_name}"]')))

        # Scroll the element into view if needed 
        driver_response.execute_script("arguments[0].scrollIntoView();",  manifest_container)        

        # Click the element using execute_script directly - search button
        driver_response.execute_script("arguments[0].click();",  manifest_container)
        
        # Click on the spanner icon within the found container
        spanner_icon = manifest_container.find_element(By.CSS_SELECTOR, 'i.fa-light.fa-wrench')
        
        spanner_icon.click()

        print("\nBuild - Processing...")

        # Switch to the new iframe
        new_iframe_name = "manifestcontent"

        # Switching to bnew frame after clicking on the manifest tile 
        #driver_response.switch_to.frame(new_iframe_name)  # This initally worked, but for some reason, this iframe
                                                           # takes longer to load into the DOM. Maybe temporary issue
                                                           # but will leave commented as has always worked before in the past


        try:
            # Wait until the iframe is available
            WebDriverWait(driver_response, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "manifestcontent"))
            )
            print("Switched to iframe successfully.")
        except Exception as e:
            print(f"Error switching to iframe: {e}")


        # Find and click on the "Build JavaScript" element - only identifyable using XPATH
        build_javascript_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Build Javascript"]')))

        driver_response.execute_script("arguments[0].scrollIntoView();",  build_javascript_button)        

        # Click the element using execute_script directly - search button
        driver_response.execute_script("arguments[0].click();",  build_javascript_button)

        # Locate the dropdown element and select "Build"
        build_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'buildtype')))

        driver_response.execute_script("arguments[0].scrollIntoView();",  build_type_dropdown)        

        # Click the element using execute_script directly - Dropdown Menu
        driver_response.execute_script("arguments[0].click();",  build_type_dropdown)

        build_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="buildtype"]/option[text()="Build"]')))

        driver_response.execute_script("arguments[0].scrollIntoView();",  build_option)        

        # Click the element using execute_script directly - build option in dropdown menu
        driver_response.execute_script("arguments[0].click();",  build_option)

        # Locate the "Build" button and click it
        build_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Build"]')))

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].scrollIntoView();",  build_button)        

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].click();",  build_button) 

        # Override the alert handling to automatically accept (press "OK")
        test_result = handle_alert(driver_response)

        if test_result == False: 
            raise ValueError()
        else: 
            pass

        # Locate the "TestOutput" button and click it
        #test_output_button = driver_response.find_element_by_xpath("//button[text()='TestOutput']")

        test_output_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='TestOutput']")))

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].scrollIntoView();",  test_output_button)        

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].click();",  test_output_button)

        # Assuming driver_response is your WebDriver instance
        element_id = "jstest"

        button_text = "TEST"         

        # Get the handles of all open tabs
        all_tabs = driver_response.window_handles        

        # Switch to the newly opened tab
        new_tab_handle = all_tabs[-1]
        driver_response.switch_to.window(new_tab_handle)
            
        # Find the button by text inside the specified div
        test_button = driver_response.find_element(By.XPATH, f"//div[@id='{element_id}']//button[text()='{button_text}']")

        # Click the element using execute_script directly - 'TEST' button
        driver_response.execute_script("arguments[0].scrollIntoView();",  test_button)        

        # Click the element using execute_script directly - 'TEST' button
        driver_response.execute_script("arguments[0].click();",  test_button)

        # Override the alert handling to automatically accept (press "OK")
        #handle_alert(driver_response)

        # In the instance the test is unsuccessful, a session timeout log message will be generated which will result in the function returning 'False'.
        # The compiler doesn't recognise the log message as a failer so we have to explicitly bomb out the function in which this code resides in order 
        # to be caught by the try catch in the instance the log message returned is not 'Test Successful'.
        test_result = handle_alert(driver_response)

        if test_result == False: 
            raise ValueError()
        else: 
            pass

        # Switch back to the original tab (assuming you have stored the original window handle)
        original_window_handle = driver_response.window_handles[0]
        driver_response.switch_to.window(original_window_handle)

        print("\nBuild & Release - Processing...")

        # Closes the 'TEST' tab
        #driver_response.close()
        
        # Re-switch to the new iframe
        new_iframe_name = "manifestcontent"
        driver_response.switch_to.frame(new_iframe_name) 

        back_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='back']")))

        # Locate and click the "back" button
        #back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='back']"), timeout=30))

        # Click the element using execute_script directly - back button 
        driver_response.execute_script("arguments[0].scrollIntoView();",  back_button)        

        # Click the element using execute_script directly - 'back button
        driver_response.execute_script("arguments[0].click();",  back_button) 

        
        # Locate the drop-down menu and select "Build & Release"
        build_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'buildtype')))

        driver_response.execute_script("arguments[0].scrollIntoView();",  build_type_dropdown)        

        # Click the element using execute_script directly - Dropdown Menu
        driver_response.execute_script("arguments[0].click();",  build_type_dropdown)
        
        build_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="buildtype"]/option[text()="Build & Release"]')))

        #driver_response.execute_script("arguments[0].scrollIntoView();",  build_option)   

        # Click the element using execute_script directly - build option in dropdown menu
        # driver_response.execute_script("arguments[0].click();",  build_option)

        # Create a Select object for the dropdown - Have to explicitly select as opposed to scrolling into view
        select = Select(build_type_dropdown)         

        # Select the option by its visible text
        select.select_by_visible_text("Build & Release")

        # Locate the "Build" button and click it
        build_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Build"]')))

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].scrollIntoView();",  build_button)        

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].click();",  build_button) 

        # Override the alert handling to automatically accept (press "OK")
        test_result = handle_alert(driver_response)

        if test_result == False: 
            raise ValueError()
        else: 
            pass

        # Locate the "TestOutput" button and click it
        test_output_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='TestOutput']")))

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].scrollIntoView();", test_output_button)        

        # Click the element using execute_script directly - build button
        driver_response.execute_script("arguments[0].click();", test_output_button)

        # Get the handles of all open tabs
        all_tabs = driver_response.window_handles        

        # Switch to the newly opened tab
        new_tab_handle = all_tabs[-1]
        driver_response.switch_to.window(new_tab_handle)
            
        # Find the button by text inside the specified div
        test_button = driver_response.find_element(By.XPATH, f"//div[@id='{element_id}']//button[text()='{button_text}']")

        # Click the element using execute_script directly - 'TEST' button
        driver_response.execute_script("arguments[0].scrollIntoView();",  test_button)        

        # Click the element using execute_script directly - 'TEST' button
        driver_response.execute_script("arguments[0].click();",  test_button)

        # Override the alert handling to automatically accept (press "OK")
        #handle_alert(driver_response)

        # In the instance the test is unsuccessful, a session timeout log message will be generated which will result in the function returning 'False'.
        # The compiler doesn't recognise the log message as a failer so we have to explicitly bomb out the function in which this code resides in order 
        # to be caught by the try catch in the instance the log message returned is not 'Test Successful'.
        #test_result = handle_alert(driver_response)

        #print("Testing second possible error")
        #if test_result == False: 
        #    raise ValueError()
        #else: 
        #    pass

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        navigateToBuildManifest(driver_response)
    else: 
        #try: 
            # Login and load Webpage
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            # Check user role and switch
            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
        
            # Load up 'Admin Screen' 
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)

            # Click and load up 'System Configuration' sub menu items 
            a.systemAdminLoadSubMenuItems(target_sys, headless_mode, user_type, username, password, driver_response, True)

            # Click and load Manifest Sub Menu Item - will load all manifests to the page
            a.systemAdminLoadManifests(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            navigateToBuildManifest(driver_response)
            
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")

        #except ValueError as ve:
        #    print(f"{Fore.RED}Test Failed{Fore.WHITE}")
        #except Exception as e: 
        #    driver_response.quit()
        #    print(f"{Fore.RED}Test Failed{Fore.WHITE}")
        #    print(e)


#if __name__ == "__main__":#

#    headless_mode = False
#    driver_response = fdi.initialize_driver(headless_mode)
#    optional_error_catch = None
#    target_sys = ""
#    user_type = '' 
#    username = ''
#    password = ''
#    index = 1

#    buildAndReleaseManifests(target_sys, headless_mode, user_type, username, password, index, driver_response, optional_error_catch)


def get_db_server_list(): 
    # Read the JSON file
    with open('..\\json_config\\dns_DB_server_list.json', 'r') as file:
        json_data = json.load(file)

    # Print server options
    for key, value in json_data["DNS_DB_server_list"].items():
        print(f"{key}: {value['name']} ({value['host']}:{value['port']})")

def get_web_server_list(): 
    # json config not created as won't be attempting to connect to webserver 
    # as we do with db servers i.e. querying db schema for information. 
    print('Web01: ?')
    print('Web02: ?')
    print('Web03: ?')