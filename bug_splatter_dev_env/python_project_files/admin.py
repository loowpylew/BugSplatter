import f_driver_init as fdi 
import globals as gs
import menu_items as mi
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
import main as m 
########################################## STANDARD ADMIN FUNCTIONS ##############################################


def staffAdminLoadMenuOptions(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    
    
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
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass
    
    if optional_error_catch is not None:
       clickStaffAdminButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)
            
            clickStaffAdminButton(driver_response)
        
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def locationAdminLoadMenuOptions(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    def clickLocationAdminButton(driver_response):
        # Wait for the "Staff Admin" link to become available
        wait = WebDriverWait(driver_response, 10)
        # Locate the "Staff Admin" link
        staff_admin_link = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="icon-link"]//span[text()=""]'))
        )     

        actions = ActionChains(driver_response)
        
        actions.move_to_element(staff_admin_link).click().perform() 


    if driver_response is None:  
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass
    
    if optional_error_catch is not None:
       clickLocationAdminButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)
            
            clickLocationAdminButton(driver_response)
        
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)




def staffAdminLoadEmployees(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    def clickEmployeesButton(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate and click the "Employees" link

        try: 
            employees_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//li[@class="sub-menu-item"]//a[text()="Employees"]'))
            )
        except: 
            employees_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//li[@class="sub-menu-item"]//a[text()="List of Employees"]'))
            )
        

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", employees_link)

        # Click the element using execute_script directly
        
        driver_response.execute_script("arguments[0].click();", employees_link)

        #employees_link.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickEmployeesButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)

            staffAdminLoadMenuOptions(target_sys, headless_mode, username, password, driver_response, True)

            clickEmployeesButton(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def systemAdminLoadSubMenuItems(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSystemAdminMenuItem(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate and click the "Employees" link

        wait = WebDriverWait(driver_response, 10)
        admin_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="icon-link"]//span[text()="System Admin"]')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", admin_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", admin_menu_button)
        
    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickSystemAdminMenuItem(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)

            staffAdminLoadMenuOptions(target_sys, headless_mode, username, password, driver_response, True)

            clickSystemAdminMenuItem(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def systemAdminLoadManifests(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickManifestSubMenuItem(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate and click the "Employees" link

        wait = WebDriverWait(driver_response, 10)
        admin_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="sub-menu-item"]//a[text()="Manifest Admin"]')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", admin_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", admin_menu_button)
        
    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickManifestSubMenuItem(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)

            systemAdminLoadSubMenuItems(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickManifestSubMenuItem(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

########################################### END OF STANDARD ADMIN FUNCTIONS ##############################################


########################################## MODULAR ADMIN FUNCTIONS FOR BATCH PROCESSING ##############################################

# Generified function where we can plug in the name of the main menu tab
def adminLoadMenuTabs(target_sys, headless_mode, user_type, username, password, menu_item_tab, driver_response=None, optional_error_catch=None): 
    def clickMainMenuButton(driver_response):
        # Wait for the "Staff Admin" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate the "Staff Admin" link
        staff_admin_link = wait.until(
            #EC.presence_of_element_located((By.XPATH, f'//div[@class="icon-link"]//span[text()="{menu_item_tab}"]'))
            EC.element_to_be_clickable((By.XPATH, f'//div[@class="icon-link"]//span[text()="{menu_item_tab}"]'))
        )     

        #actions = ActionChains(driver_response)
        
        #actions.move_to_element(staff_admin_link).click().perform() 

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_admin_link)

        # Click the element using execute_script directly
        
        driver_response.execute_script("arguments[0].click();", staff_admin_link)


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass
    
    if optional_error_catch is not None:
       clickMainMenuButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
            
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickMainMenuButton(driver_response)
        
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Generified function where we can plug in the name of the sub menu tab with it's assocatiated main menu tab
def adminLoadSubMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, sub_menu_tab, driver_response=None, optional_error_catch=None): 
    def clickSubMenuButton(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate and click the "Employees" link

        
        sub_menu_item_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//li[@class="sub-menu-item"]//a[text()="{sub_menu_tab}"]'))
        )
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sub_menu_item_link)

        # Click the element using execute_script directly
        
        driver_response.execute_script("arguments[0].click();", sub_menu_item_link)

        #employees_link.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        adminLoadMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, driver_response, True)
        clickSubMenuButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
                                         
            adminLoadMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, driver_response, True)

            clickSubMenuButton(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Generified function where we can plug in the name of the sub sub menu tab, the associated sub menu tab and it's assocatiated main menu tab
def adminLoadSubSubMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, sub_menu_tab, sub_sub_menu_tab, driver_response=None, optional_error_catch=None):
    def clickSubSubMenuButton(driver_response): 
        # Wait for the "" link to become available
        wait = WebDriverWait(driver_response, 20)
        # Locate and click the "Employees" link

        # Locate the <div> container for widget used to open upn cards 
        div_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="grid_areaFooter"]'))
        )
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", div_container)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", div_container)

        # Wait for the tab label to become clickable
        tab_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//label[@class="toptab tabshow" and text()="{sub_sub_menu_tab}"]'))
        )

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", tab_label)

        # Click the element using execute_script directly
        
        driver_response.execute_script("arguments[0].click();", tab_label)

        #employees_link.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        adminLoadSubMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, sub_menu_tab, driver_response, True)
        clickSubSubMenuButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)
                                   
            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)

            #adminLoadMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, driver_response, True)
            
            adminLoadSubMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, sub_menu_tab, driver_response, True)
            
            clickSubSubMenuButton(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

########################################## END OF MODULAR ADMIN FUNCTIONS FOR BATCH PROCESSING ##############################################

if __name__ == '__main__': 
    username = ""
    password = "!"

    target_sys = ""
    headless_mode = m.setHeadlessMode(target_sys)
    user_type = ''
    main_menu_tab = 'Staff Admin'
    sub_menu_tab = 'Staff'
    sub_sub_menu_tab = 'Details'
                                                                                                                            
    adminLoadSubSubMenuTabs(target_sys, headless_mode, user_type, username, password, main_menu_tab, sub_menu_tab, sub_sub_menu_tab)

    