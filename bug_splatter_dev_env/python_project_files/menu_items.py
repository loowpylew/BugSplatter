import f_driver_init as fdi 
import globals as gs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
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

################################################ MENU ITEM ACCESS FUCNTIONS ##################################################
# Admin
def homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    def clickAdminMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Admin']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Admin']]"        

        try:
            admin_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            admin_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", admin_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", admin_menu_button)
        
        #admin_menu_button.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickAdminMenuButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickAdminMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Management
def homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 

    
    def clickManagmentMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Management']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Management']]"       

        try:
            management_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            management_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", management_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", management_menu_button)
        
        #managment_menu_button.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickManagmentMenuButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickManagmentMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Data Processing
def homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickManagerTasksMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Data Processing']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Data Processing']]"      

        try:
            data_processing_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            data_processing_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", data_processing_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", data_processing_button)

        #manager_tasks_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickManagerTasksMenuButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickManagerTasksMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank
def homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickBankMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Bank']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Bank']]"     

        try:
            bank_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            bank_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bank_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bank_menu_button)
        
        #manager_tasks_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickBankMenuButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickBankMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
            

# Self Service 
def homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadSelfServiceButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Self-Service']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Self-Service']]"

        try:
            self_service_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            self_service_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", self_service_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", self_service_button)

        #manager_tasks_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadSelfServiceButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickLoadSelfServiceButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Reports
def homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadReportsButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Reports']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Reports']]"      

        try:
            reports_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            reports_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", reports_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", reports_menu_button)

        #report_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadReportsButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickLoadReportsButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Reports Dashboard
def homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadReportsDashboardButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='Reports Dashboard']]"
        # In the case the item has already been clicked on within the same session
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='Reports Dashboard']]"

        try:
            reports_dashboard_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            reports_dashboard_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", reports_dashboard_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", reports_dashboard_button)

        #reports_dashboard_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadReportsDashboardButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickLoadReportsDashboardButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# About
def homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadAboutButton(driver_response):
        wait = WebDriverWait(driver_response, 10)

        primary_xpath = "//li[contains(@class, 'nav-item') and .//span[text()='About']]"
        fallback_xpath = "//li[@class='nav-item highlight' and .//span[text()='About']]"        

        try:
            about_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, primary_xpath)))
        except TimeoutException:
            print("Primary XPath not found. Trying fallback XPath...")
            about_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, fallback_xpath)))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", about_menu_button)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", about_menu_button)

        #about_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadAboutButton(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickLoadAboutButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


###############################################END OF MENU ITEMS###################################################