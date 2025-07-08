import f_driver_init as fdi 
import user_tiles as ut
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
from selenium.common.exceptions import TimeoutException
import openpyxl
from openpyxl.styles import PatternFill, Font
import xlsxwriter
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os 
import time


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


################################################ MENU ITEM ACCESS FUCNTIONS ##################################################

# Admin
def homePageLoadAdminMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None): 
    
    
    def clickAdminMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        admin_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Admin']]"))) #By.CSS_SELECTOR, 'li.nav-item[onclick*="homepageLoadAdminScreen()"]')))
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


# Management
def homePageLoadManagmentMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    
    def clickManagmentMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        managment_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Management']]")))
        managment_menu_button.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickManagmentMenuButton(driver_response)
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickManagmentMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Data Processing
def homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None):

    def clickManagerTasksMenuButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        manager_tasks_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Data Processing']]")))
        manager_tasks_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickManagerTasksMenuButton(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickManagerTasksMenuButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Self Service 
def homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadSelfServiceButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        manager_tasks_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Self-Service']]")))
        manager_tasks_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadSelfServiceButton(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickLoadSelfServiceButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Reports
def homePageLoadReportsMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadReportsButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        about_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Reports']]")))
        about_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadReportsButton(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickLoadReportsButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Reports Dashboard
def homePageLoadReportsDashboardMenuItem(target_sys, username, password, driver_response=None, optional_error_catch=None):

    def clickLoadReportsDashboardButton(driver_response):
        wait = WebDriverWait(driver_response, 10)
        about_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'nav-item') and .//span[text()='Reports Dashboard']]")))
        about_menu_button.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickLoadReportsDashboardButton(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickLoadReportsDashboardButton(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

###############################################END OF MENU ITEMS###################################################

####################################### TARGET FUNCTIONS - SPECIFIC USER TILE #####################################

##################################################### HOME ######################################################## 
# Dashboard Absence Summary - target function
def homePageLoadAbsenceSummaryTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    def clickAbsenceSummaryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_summary_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_203')))
        
        absence_summary_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickAbsenceSummaryTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickAbsenceSummaryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Next Absence - target function
def homePageLoadNextAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    def clickNextAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        next_absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_204')))
        
        next_absence_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickNextAbsenceTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickNextAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Next Shift - target function
def homePageLoadNextShiftTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    def clickNextShiftTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        next_shift_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_34')))
        
        next_shift_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickNextShiftTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)
            
            clickNextShiftTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

##############################################END OF HOME TILES #################################################


############################################## MANAGMENT TILES ##################################################
# Rota - target function 
def managmentPageLoadRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    def clickRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_145')))
        
        rota_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickRotaTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Quick Entry Screen - target function
def managmentPageLoadQuickEntryTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    
    def clickQuickEntryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        quick_entry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_151')))
        
        quick_entry_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickQuickEntryTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickQuickEntryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Scheduled Rota's - target function
def managmentPageLoadScheduledRotasTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    
    def clickScheduledRotasTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        scheduled_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_79')))
        
        scheduled_rota_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickScheduledRotasTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickScheduledRotasTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Scheduled Jobs - target function 
def managmentPageLoadScheduledJobsTile(target_sys, username, password, driver_response=None, optional_error_catch=None): 

    
    def clickScheduledJobsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        scheduled_jobs_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_82')))
        
        scheduled_jobs_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickScheduledJobsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickScheduledJobsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Skills Expiry - target function 
def managmentPageLoadSkillsExpiryTile(target_sys, username, password, driver_response=None, optional_error_catch=None):
    
    def clickSkillsExpiryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        skills_expiry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_5')))
        
        skills_expiry_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickSkillsExpiryTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickSkillsExpiryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence Adjustments - target function
def managmentPageLoadAbsenceAdjustmentsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):
    
    def clickAbsenceAdjustmentsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_adjustments_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_181')))
        
        absence_adjustments_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickAbsenceAdjustmentsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickAbsenceAdjustmentsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Payroll - target function
def managmentPagePayrollTile(target_sys, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPayrollTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        payroll_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_210')))
        
        payroll_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPayrollTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickPayrollTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Absence Requests - target function 
def managmentAbsenceRequestsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickAbsenceRequestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_19')))
        
        absence_requests_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickAbsenceRequestTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickAbsenceRequestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# C/F Requests - target function 
def managmentPageLoadCarryForwardRequestsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        carry_forward_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_176')))
        
        carry_forward_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickCarryForwardRequestsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Move/Terminate Staff - target function  
def managmentPageLoadMoveOrTeminateStaffTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMoveOrTeminateStaffTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        move_or_term_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_208')))
        
        move_or_term_staff_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMoveOrTeminateStaffTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMoveOrTeminateStaffTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bulk Pattern Renewal - target function 
def managmentPageLoadBulkPatternRenewalTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadBulkPatternRenewalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        move_or_term_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_109')))
        
        move_or_term_staff_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadBulkPatternRenewalTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadBulkPatternRenewalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


##########################################FOR NOW, NOT TO BE INCLUDED IN NHSBT TEST##########################################
def managmentPageBulkScheduledTimesheetsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickBulkScheduledTimesheets(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        scheduled_bulk_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_185')))
        
        scheduled_bulk_timesheets_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickBulkScheduledTimesheets(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickBulkScheduledTimesheets(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def managmentPageScheduledTimesheetsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickScheduleTimesheets(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        scheduled_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_146')))
        
        scheduled_timesheets_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickScheduleTimesheets(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
            
            clickScheduleTimesheets(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
############################################## END OF MANAGMENT TILES ###############################################

################################################# DATA PROCESSING ######################################################

# ESR GO Import - target function 
def dataProcessingPageLoadESRGoImportTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoaddESRGoImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_162')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoaddESRGoImportTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoaddESRGoImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# ESR Export - target function 
def dataProcessingPageLoadESRExportTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoaddESRExportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_166')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoaddESRExportTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoaddESRExportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# NHSBT Session Data Import - target function
def dataProcessingPageLoadNHSBTSessionDataImportTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadNHSBTSessionDataTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_144')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadNHSBTSessionDataTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadNHSBTSessionDataTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Driver Allowance Upload - target function
def dataProcessingPageLoadDriverAllowanceUploadTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadDriverAllowanceUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_155')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadDriverAllowanceUploadTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadDriverAllowanceUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
 

 # Annual Leave Plans - target function
def dataProcessingPageLoadAnnualLeavePlansTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAnnualLeavePlansTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_160')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAnnualLeavePlansTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAnnualLeavePlansTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

################################################## END OF DATA PROCESSING TILES ######################################################

################################################# SELF SERVICE TILES ######################################################## 


# My Rota - target function
def selfServicePageLoadMyRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_202')))
        
        my_rota_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyRotaTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Location - target function
def selfServicePageLoadMyLocationTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyLocationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_location_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_14')))
        
        my_location_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyLocationTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyLocationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Team Rota - target function
def selfServicePageLoadMyTeamRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyTeamRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_team_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_179')))
        
        my_team_rota_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyTeamRotaTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyTeamRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Availabilities - target function
def selfServicePageLoadMyAvailabilitiesTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyAvailabilitiesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_availability_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_13')))
        
        my_availability_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyAvailabilitiesTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyAvailabilitiesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Absences - target function
def selfServicePageLoadMyAbsencesTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyAbsencesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_89')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyAbsencesTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyAbsencesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Carry Forward Requests - target function
def selfServicePageLoadCarryForwardRequestsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_176')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadCarryForwardRequestsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Change Password - target function
def selfServicePageLoadChangePasswordTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadChangePasswordTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_59')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadChangePasswordTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadChangePasswordTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My GDPR - target function
def selfServicePageLoadMyGDPRTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyGDPRTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_123')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyGDPRTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyGDPRTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Email Opt Out - target function
def selfServicePageLoadEmailOptOutTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadEmailOptOutTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_97')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadEmailOptOutTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadEmailOptOutTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

########################################## END OF SELF SERVICE TILES ###########################################

############################################# REPORTS TILES ####################################################

# Multi - post - target function
def reportsPageLoadMultiPostTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMultiPostTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1107')))
        
        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMultiPostTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMultiPostTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank Staff Usage - target function
def reportsPageLoadBankStaffUsageTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadBankStaffUsageTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        bank_staff_usage_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1078')))
        
        bank_staff_usage_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadBankStaffUsageTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadBankStaffUsageTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Skills - target function
def reportsPageLoadSkillsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSkillsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        load_skills_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_12')))
        
        load_skills_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSkillsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSkillsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Unsubmitted Sessions - target function
def reportsPageLoadUnsubmittedSessionsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadUnsubmittedSessionsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        unsubmitted_sessions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1101')))
        
        unsubmitted_sessions_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadUnsubmittedSessionsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadUnsubmittedSessionsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# New Starters - target function
def reportsPageLoadNewStartersTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadNewStartersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        new_starters_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1075')))
        
        new_starters_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadNewStartersTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadNewStartersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence - target function
def reportsPageLoadAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        load_absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1102')))
        
        load_absence_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAbsenceTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Away From Home Team - target function
def reportsPageLoadAwayFromHomeTeamTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAwayFromHomeTeamTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        away_from_home_team_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1100')))
        
        away_from_home_team_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAwayFromHomeTeamTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAwayFromHomeTeamTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Calculations - target functions
def reportsPageLoadMyCalculationsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyCalculationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_calculations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1074')))
        
        my_calculations_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyCalculationsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadMyCalculationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Hours Report - target functions
def reportsPageLoadHoursReportTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadHoursReporTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        load_absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_8')))
        
        load_absence_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadHoursReporTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadHoursReporTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Previous Sessions Report for Adjustments - target functions
def reportsPageLoadPreviousSessionReportTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadHoursReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        previous_sessions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1093')))
        
        previous_sessions_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadHoursReportTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadHoursReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Double Sessions - target functions
def reportsPageLoadDoubleSessionsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadDoubleSessionsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        double_sessions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1072')))
        
        double_sessions_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadDoubleSessionsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadDoubleSessionsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Employee Calculations - target function 
def reportsPageLoadEmployeeCalculationsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadEmployeeCalculationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        employee_calc_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1068')))
        
        employee_calc_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadEmployeeCalculationsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadEmployeeCalculationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank Staff Utilisation - target function 
def reportsPageLoadBankStaffUtilTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadBankStaffUtilTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        bank_staff_util_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1079')))
        
        bank_staff_util_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadBankStaffUtilTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadBankStaffUtilTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Extra Duties - target function
def reportsExtraDutiesPageTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadExtraDutiesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        extra_duties_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1071')))
        
        extra_duties_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadExtraDutiesTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadExtraDutiesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

################################################# END OF REPORTS TILES ######################################################

############################################## DASHBOARD REPORTS TILES ######################################################

# Session Working Unavailability Breakdown - target fucntion
def dashboardReportsSessionUnavailablityTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSessionUnavailablityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_unavailablity_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_9')))
        
        session_unavailablity_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionUnavailablityTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSessionUnavailablityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank Hours Paid - Target function 
def dashboardReportsBankHoursPaidTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadBankHoursPaidTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        bank_hours_paid_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_3')))
        
        bank_hours_paid_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadBankHoursPaidTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadBankHoursPaidTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Session Staffing Planned Above and Below BD Staffing Model (Non-Nurses) - Target function 
def dashboardReportsStaffingModelTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadStaffingModelTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        staffing_model_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_8')))
        
        staffing_model_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadStaffingModelTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadStaffingModelTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sessions Operated with Shortfall or Surplus - Target function 
def dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        operated_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_7')))
        
        operated_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sessions Planned with Shortfall or Surplus - Target function 
def dashboardReportsSeshPlannedWithShortfallorSurplusTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSeshPlannedWithShortfallorSurplusTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        planned_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_38')))
        
        planned_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSeshPlannedWithShortfallorSurplusTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSeshPlannedWithShortfallorSurplusTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sessions Expected Vs Sessions Planned - Target function 
def dashboardReportsSeshExpectedVSSeshPlannedTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        expected_vs_planned_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_6')))
        
        expected_vs_planned_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Skills - Target function 
def dashboardReportsSkillsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSkillsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        skills_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_1')))
        
        skills_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSkillsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSkillsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sickness Paid - target function 
def dashboardReportSicknessPaidTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadtSicknessPaidTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        sickness_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_5')))
        
        sickness_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadtSicknessPaidTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadtSicknessPaidTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Absence Reason Breakdown - target function 
def dashboardReportAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_reason_brkdown_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_4')))
        
        absence_reason_brkdown_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAbsenceTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave booked by Day  - target function 
def dashboardReportAnnualLeaveBookByDayTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAnnualLeaveBookByDayTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_book_by_day_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_39')))
        
        annual_leave_book_by_day_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAnnualLeaveBookByDayTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAnnualLeaveBookByDayTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave Booked vs. Allowance - target function 
def dashboardReportAnnualLeaveBookVsAllowanceTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_book_vs_allow_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_40')))
        
        annual_leave_book_vs_allow_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Employee Annual Leave Allowance vs. Booked - target function 
def dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_allow_vs_booked_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_41')))
        
        annual_leave_allow_vs_booked_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Session Overrun Reasons - target function 
def dashboardReportSessionOverrunReasonsTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSessionOverrunReasonsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_overrun_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_43')))
        
        session_overrun_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionOverrunReasonsTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadSessionOverrunReasonsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# To Note* - One off case where a usertile i.e. 'HOMPAGE_?' Tag is used within Dashboards report 
# Dashboard Export Multi to PDF - target function 
def dashboardReportExportMultiToPDFTile(target_sys, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadExportMultiToPDFTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_overrun_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_183')))
        
        session_overrun_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadExportMultiToPDFTile(driver_response)    
    else: 
        try: 
            loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
            
            clickPageLoadExportMultiToPDFTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

############################################## END OF DASHBOARD REPORTS TILES ################################################


def checkUserRoleAndSwitch(driver_response, target_sys, user_type):
    
    drop_list_xpath = '/html/body/section/div[2]/div/div[1]/select' # Indexing remains consistant across systems for class="switchroleDropList" <select> element.
   

    desired_user_type = {
        "DemandEngine_Dev": {}
        , "DemandEngine_NextraDev": {}
        , "DemandEngine_NextraTest": {}
        , "NextraDemo_Hutchison": {}
        , "NextraDemo_Lite_v4_2": {}
        , "NextraDemo_Lite2_v4_2": {}
        , "NextraDemo_v4_2": {}
        , "NextraDev_1": {}
        , "NextraDev_2": {}
        , "NextraDev_3": {}
        , "NextraDev": {}
        , "NextraPreRelease": {}
        , "NextraRefSQL": {}
        , "NextraRelease_4_0": {}
        , "NextraRelease_4_1_1": {}
        , "NextraRelease_4_1": {}
        , "NextraRelease_4_2_0": {}
        , "NextraRelease_4_2_1": {}
        , "NextraRelease_4_2_2": {}
        , "NextraRelease_4_2_3": {}
        , "NextraRelease_Candidate": {}
        , "NextrasoftLiveSQL_CloudHR": {}
        , "NextraTest_ANRG": {}
        , "NextraTest_BritishHome": {}
        , "NextraTest_NHSBT": {}
        , "NextraTest_NHSBT_Upgrade": {
            #f"{drop_list_xpath}/option[@value='59584850']"
            'System Administrator': f"{drop_list_xpath}/option[text()='System Administrator - Corporate']"
            ,'Employee': f"{drop_list_xpath}/option[text()='Employee - NHSBT Root | Corporate']"
            ,'Administrator (NHSBT)': f"{drop_list_xpath}/option[text()='Administrator (NHSBT) - NHSBT Root | Corporate']"
            ,'Pay Support': f"{drop_list_xpath}/option[text()='Pay Support - NHSBT Root | Corporate']"
            ,'Manager': f"{drop_list_xpath}/option[text()='Manager - NHSBT Root | Corporate']"
            ,'Model Adjustments': "{drop_list_xpath}/option[text()='Model Adjustments - NHSBT Root | Corporate']"
            ,'National Managers': f"{drop_list_xpath}/option[text()='National Managers - NHSBT Root | Corporate']"
            ,'Regional Manager': f"{drop_list_xpath}/option[text()='Regional Manager - NHSBT Root | Corporate']"
            ,'Area Manager': f"{drop_list_xpath}/option[text()='Area Manager - NHSBT Root | Corporate']"
            ,'Data upload': f"{drop_list_xpath}/option[text()='Data upload - NHSBT Root | Corporate']"
            ,'PerfTest': f"{drop_list_xpath}/option[text()='PerfTest - NHSBT Root | Corporate']"
            ,'Reporting': f"{drop_list_xpath}/option[text()='Reporting - NHSBT Root | Corporate']"
            ,'Test': f"{drop_list_xpath}/option[text()='Test - NHSBT Root | Corporate']"
        }
        , "NextraTest_v4_2": {}
        , "NextraTimesheet_NextraDev": {}
    }    
      
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
            if target_sys in desired_user_type: 
                #select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

                print(desired_user_type[target_sys][user_type])

                select_user_role = select_element.find_element(By.XPATH, desired_user_type[target_sys][user_type])

                # Select the desired option by its value
                select_user_role.click()

                return True
    except: 
        print(f"User type doesn't exist for current system: {target_sys}")
        return False
    

########################################################## WRAPPER FUNCTION FOR TARGET WEB OBJECTS ################################################################

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

# Function Meta data - required to specify what menu item the function derives from:

# Tags for functions in the HOME section
homePageLoadAbsenceSummaryTile.tag = ["HOME", "HOME Tile - Absence Summary"]
homePageLoadNextAbsenceTile.tag = ["HOME", "HOME Tile - Next Absence"] 
homePageLoadNextShiftTile.tag = ["HOME", "HOME Tile - Next Shift"] 

# Tags for functions in the MANAGEMENT section

managmentPageLoadRotaTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Rota"] 
managmentPageLoadQuickEntryTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Quick Entry Screen"]
managmentPageLoadScheduledRotasTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Scheduled Rotas"]
managmentPageLoadScheduledJobsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Scheduled Jobs"]
managmentPageLoadSkillsExpiryTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Skills Expiry"]
managmentPagePayrollTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Payroll"]
managmentPageLoadCarryForwardRequestsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - C/F Requests"]
managmentPageLoadMoveOrTeminateStaffTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Move Or Terminate Staff"]
managmentPageLoadBulkPatternRenewalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Bulk Pattern Renewal"]

# Tags for functions in the DATA PROCESSING section
dataProcessingPageLoadESRGoImportTile.tag = ["DATA PROCESSING", "DATA PROCESSING - ESR Go Import"]
dataProcessingPageLoadESRExportTile.tag = ["DATA PROCESSING", "DATA PROCESSING - ESR Export Tile"]
dataProcessingPageLoadNHSBTSessionDataImportTile.tag = ["DATA PROCESSING", "DATA PROCESSING - NHSBT Session Data Import"]
dataProcessingPageLoadDriverAllowanceUploadTile.tag = ["DATA PROCESSING", "DATA PROCESSING - Driver Allowance Upload"]
dataProcessingPageLoadAnnualLeavePlansTile.tag = ["DATA PROCESSING", "DATA PROCESSING - Annual Leave Plans"]

# Tags for functions in the SELF SERVICE section
selfServicePageLoadMyRotaTile.tag = ["SELF SERVICE", "SELF SERVICE - My Rota"]
selfServicePageLoadMyLocationTile.tag = ["SELF SERVICE", "SELF SERVICE - My Location"]
selfServicePageLoadMyTeamRotaTile.tag = ["SELF SERVICE", "SELF SERVICE - My Team Rota"]
selfServicePageLoadMyAvailabilitiesTile.tag = ["SELF SERVICE", "SELF SERVICE - My Availabilities"]
selfServicePageLoadMyAbsencesTile.tag = ["SELF SERVICE", "SELF SERVICE - My Absences"]
selfServicePageLoadCarryForwardRequestsTile.tag = ["SELF SERVICE", "SELF SERVICE - C/F Requests"]
selfServicePageLoadChangePasswordTile.tag = ["SELF SERVICE", "SELF SERVICE - Change Password"]
selfServicePageLoadMyGDPRTile.tag = ["SELF SERVICE", "SELF SERVICE - My GDPR"]
selfServicePageLoadEmailOptOutTile.tag = ["SELF SERVICE", "SELF SERVICE - Email Opt"]

# Tags for functions in the REPORTS section
reportsPageLoadMultiPostTile.tag = ["REPORTS", "REPORTS Tile - Multi Post"]
reportsPageLoadBankStaffUsageTile.tag = ["REPORTS", "REPORTS Tile - Staff Usage"]
reportsPageLoadSkillsTile.tag = ["REPORTS", "REPORTS Tile - Skills"]
reportsPageLoadUnsubmittedSessionsTile.tag = ["REPORTS", "REPORTS Tile - Unsubmitted Sessions"]
reportsPageLoadNewStartersTile.tag = ["REPORTS", "REPORTS Tile - New Starters"]
reportsPageLoadAbsenceTile.tag = ["REPORTS", "REPORTS Tile - Absence"]
reportsPageLoadAwayFromHomeTeamTile.tag = ["REPORTS", "REPORTS Tile - Home Team"]
reportsPageLoadMyCalculationsTile.tag = ["REPORTS", "REPORTS Tile - My Calculations"]
reportsPageLoadHoursReportTile.tag = ["REPORTS", "REPORTS Tile - Hours Report"]
reportsPageLoadPreviousSessionReportTile.tag = ["REPORTS", "REPORTS Tile - Previous Session Report"]
reportsPageLoadDoubleSessionsTile.tag = ["REPORTS", "REPORTS Tile - Double Sessions"]
reportsPageLoadEmployeeCalculationsTile.tag = ["REPORTS", "REPORTS Tile - Employee Calculations"]
reportsPageLoadBankStaffUtilTile.tag = ["REPORTS", "REPORTS Tile - Bank Staff Util"]
reportsExtraDutiesPageTile.tag = ["REPORTS", "REPORTS Tile - Extra Duites"]

# Tags for functions in the DASHBOARD REPORTS section
dashboardReportsSessionUnavailablityTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Session Unavailability"]
dashboardReportsBankHoursPaidTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Bank Hours Paid"]
dashboardReportsStaffingModelTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Staff Model"]
dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Operated With Sesssion Shortfall Or Surplus"]
dashboardReportsSeshPlannedWithShortfallorSurplusTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Session Planned With Short fall Or Surplus"]
dashboardReportsSeshExpectedVSSeshPlannedTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - "] 
dashboardReportsSkillsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Session Expected VS Sesh Planned"] 
dashboardReportSicknessPaidTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Sickness Paid"]
dashboardReportAbsenceTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Absence"]
dashboardReportAnnualLeaveBookByDayTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Annual Leave Book By Day"]
dashboardReportAnnualLeaveBookVsAllowanceTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Annual LeaveBook Vs Allowance"] 
dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Annual Leave Allowance Vs Booked"]
dashboardReportSessionOverrunReasonsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Session Overrun Reasons"] 
dashboardReportExportMultiToPDFTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS - Export Multi To PDF"] 


# Logs into system, updates the user role and checks function meta data. 
def target_object_initial_checks(target_func, user_type, driver_response):
    # Call the login function to log in and open the Homepage
    loginAndLoadHomePage(target_sys, username, password, driver_response, True)

    # Check user role, switch if not the desired target
    if checkUserRoleAndSwitch(driver_response, target_sys, user_type) == True: 
        user_role_perm_check = True
    else: 
        user_role_perm_check = False

    # Conditional logic to open menu item based on function meta data associated with it.  
    if hasattr(target_func, 'tag') and target_func.tag[0] == "HOME":
        pass 
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "ADMIN":
        pass
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "MANAGEMENT":
        homePageLoadManagmentMenuItem(target_sys, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "DATA PROCESSING":
        homePageLoadDataProcessingMenuItem(target_sys, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "SELF SERVICE":
        homePageLoadSelfServiceMenuItem(target_sys, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "REPORTS":
        homePageLoadReportsMenuItem(target_sys, username, password, driver_response, True)
    elif hasattr(target_func, 'tag') and target_func.tag[0] == "DASHBOARD REPORTS":
        homePageLoadReportsDashboardMenuItem(target_sys, username, password, driver_response, True)
    
    return user_role_perm_check


# Function will check if web object exists, whether it doesnt exist and if 
def global_web_object_processor(target_func, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
        
    cell = row[object]
    if cell == 'X':
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, user_type, driver_response)
            
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}' tile do not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', red_format)
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, username, password, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', red_format)

    elif cell == '': 
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            target_object_initial_checks(target_func, user_type, driver_response)
            
        except: 
            print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}' does not exist{Fore.WHITE}")
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, username, password, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}' does not exist{Fore.WHITE}")

####################################################################END OF WRAPPER FUNCTION######################################################################


def batchProcessReports(target_sys, username, password, paths): 
    pass 
def batchProcessDashBoardReports(target_sys, username, password, paths): 
    pass


def batchProcessUserTypeTiles(target_sys, username, password, paths):

    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        #"Homepage_1": []
        #,"Homepage_2": []
        #,"Homepage_3": []
        #,"Homepage_4": []
        "Homepage_5": [managmentPageLoadSkillsExpiryTile] # Skills Expiry Tile
        #,"Homepage_6": []
        #,"Homepage_7": []
        #,"Homepage_8": []
        #,"Homepage_10": []
        #,"Homepage_11": []
        #,"Homepage_12": []
        #,"Homepage_13": []
        ,"Homepage_14": [selfServicePageLoadMyLocationTile]
        #,"Homepage_15": []
        #,"Homepage_16": []
        #,"Homepage_17": []
        #,"Homepage_18": []
        ,"Homepage_19": [managmentAbsenceRequestsTile] # Absence Requests Tile
        #,"Homepage_20": []
        #,"Homepage_21": []
        #,"Homepage_22": []
        #,"Homepage_23": []
        #,"Homepage_24": []
        #,"Homepage_25": []
        #,"Homepage_26": []
        #,"Homepage_27": []
        #,"Homepage_28": []
        #,"Homepage_29": []
        #,"Homepage_30": []
        #,"Homepage_31": []
        #,"Homepage_32": []
        #,"Homepage_33": []
        ,"Homepage_34": [homePageLoadNextShiftTile]
        #,"Homepage_35": []
        #,"Homepage_36": []
        #,"Homepage_37": []
        #,"Homepage_38": []
        #,"Homepage_39": []
        #,"Homepage_40": []
        #,"Homepage_41": []
        #,"Homepage_42": []
        #,"Homepage_43": []
        #,"Homepage_44": []
        #,"Homepage_45": []
        #,"Homepage_46": []
        #,"Homepage_47": []
        #,"Homepage_48": []
        #,"Homepage_49": []
        #,"Homepage_50": []
        #,"Homepage_51": []
        #,"Homepage_52": []
        #,"Homepage_53": []
        #,"Homepage_54": []
        #,"Homepage_55": []
        #,"Homepage_56": []
        #,"Homepage_57": []
        #,"Homepage_58": []
        ,"Homepage_59": [selfServicePageLoadChangePasswordTile]
        #,"Homepage_60": []
        #,"Homepage_61": []
        #,"Homepage_62": []
        #,"Homepage_63": []
        #,"Homepage_64": []
        #,"Homepage_65": []
        #,"Homepage_68": []
        #,"Homepage_69": []
        #,"Homepage_70": []
        #,"Homepage_71": []
        #,"Homepage_72": []
        #,"Homepage_73": []
        #,"Homepage_74": []
        #,"Homepage_75": []
        #,"Homepage_76": []
        #,"Homepage_77": []
        #,"Homepage_78": []
        ,"Homepage_79": [managmentPageLoadScheduledRotasTile] # Scheduled Rotas Tile
        #,"Homepage_80": []
        #,"Homepage_81": []
        ,"Homepage_82": [managmentPageLoadScheduledJobsTile] # Scheduled Job Tile 
        #,"Homepage_83": []
        #,"Homepage_84": []
        #,"Homepage_86": []
        #,"Homepage_87": []
        #,"Homepage_88": []
        #,"Homepage_89": []
        #,"Homepage_90": []
        #,"Homepage_91": []
        #,"Homepage_92": []
        #,"Homepage_93": []
        #,"Homepage_94": []
        #,"Homepage_95": []
        #,"Homepage_96": []
        ,"Homepage_97": [selfServicePageLoadEmailOptOutTile]
        #,"Homepage_98": []
        #,"Homepage_99": []
        #,"Homepage_100": []
        #,"Homepage_102": []
        #,"Homepage_103": []
        #,"Homepage_104": []
        #,"Homepage_105": []
        #,"Homepage_106": []
        #,"Homepage_107": []
        ,"Homepage_109": [managmentPageLoadBulkPatternRenewalTile]
        #,"Homepage_110": []
        #,"Homepage_111": []
        #,"Homepage_112": []
        #,"Homepage_113": []
        #,"Homepage_114": []
        #,"Homepage_115": []
        #,"Homepage_116": []
        #,"Homepage_117": []
        #,"Homepage_118": []
        #,"Homepage_119": []
        #,"Homepage_120": []
        #,"Homepage_121": []
        #,"Homepage_122": []
        ,"Homepage_123": [selfServicePageLoadMyGDPRTile]
        #,"Homepage_124": []
        #,"Homepage_125": []
        #,"Homepage_126": []
        #,"Homepage_127": []
        #,"Homepage_128": []
        #,"Homepage_129": []
        #,"Homepage_130": []
        #,"Homepage_131": []
        #,"Homepage_132": []
        #,"Homepage_133": []
        #,"Homepage_134": []
        #,"Homepage_135": []
        #,"Homepage_136": []
        #,"Homepage_137": []
        #,"Homepage_138": []
        #,"Homepage_139": []
        #,"Homepage_140": []
        #,"Homepage_141": []
        #,"Homepage_142": []
        #,"Homepage_143": []
        ,"Homepage_144": [dataProcessingPageLoadNHSBTSessionDataImportTile]
        ,"Homepage_145": [managmentPageLoadRotaTile] # Rota Tile
        ,"Homepage_146": [managmentPageScheduledTimesheetsTile] # Scheduled timesheets Tile
        #,"Homepage_147": []
        #,"Homepage_149": []
        #,"Homepage_150": []
        ,"Homepage_151": [managmentPageLoadQuickEntryTile] # Quick Entry Tile 
        #,"Homepage_153": []
        ,"Homepage_155": [dataProcessingPageLoadDriverAllowanceUploadTile]
        ,"Homepage_160": [dataProcessingPageLoadAnnualLeavePlansTile]
        #,"Homepage_161": []
        ,"Homepage_162": [dataProcessingPageLoadESRGoImportTile]
        #,"Homepage_163": []
        #,"Homepage_164": []
        #,"Homepage_165": []
        ,"Homepage_166": [dataProcessingPageLoadESRExportTile]
        #,"Homepage_167": []
        #,"Homepage_168": []
        #,"Homepage_169": []
        #,"Homepage_171": []
        #,"Homepage_172": []
        #,"Homepage_173": []
        #,"Homepage_174": []
        #,"Homepage_175": []
        #,"Homepage_176": [managmentPageLoadCarryForwardRequestsTile]
        #,"Homepage_177": []
        #,"Homepage_178": []
        ,"Homepage_179": [selfServicePageLoadCarryForwardRequestsTile]
        #,"Homepage_180": []
        ,"Homepage_181": [managmentPageLoadAbsenceAdjustmentsTile]
        #,"Homepage_182": []
        ,"Homepage_183": [dashboardReportExportMultiToPDFTile]
        #,"Homepage_184": []
        ,"Homepage_185": [managmentPageBulkScheduledTimesheetsTile]
        #,"Homepage_190": []
        #,"Homepage_187": []
        #,"Homepage_188": []
        #,"Homepage_189": []
        #,"Homepage_194": []
        #,"Homepage_195": []
        #,"Homepage_196": []
        #,"Homepage_197": []
        #,"Homepage_198": []
        #,"Homepage_199": []
        ,"Admin": [homePageLoadAdminMenuItem] # Admin Tile - actually a button and is part of the menu options so differs in respects to not having a 'HOMEPAGE' tile id name.
        #,"Homepage_201": [] 
        ,"Homepage_202": [selfServicePageLoadMyRotaTile]
        , "Homepage_203": [homePageLoadAbsenceSummaryTile]
        , "Homepage_204": [homePageLoadNextAbsenceTile] 
        #,"Homepage_205": []
        #,"Homepage_206": []
        #,"Homepage_207": []
        ,"Homepage_208": [managmentPageLoadMoveOrTeminateStaffTile]
        #,"Homepage_209": []
        ,"Homepage_210": [managmentPagePayrollTile]
        #,"Homepage_211": []
    }
        

    web_objects = [
        "Homepage_1", "Homepage_2", "Homepage_3", "Homepage_4", "Homepage_5",
        "Homepage_6", "Homepage_7", "Homepage_8", "Homepage_10", "Homepage_11",
        "Homepage_12", "Homepage_13", "Homepage_14", "Homepage_15", "Homepage_16",
        "Homepage_17", "Homepage_18", "Homepage_19", "Homepage_20", "Homepage_21",
        "Homepage_22", "Homepage_23", "Homepage_24", "Homepage_25", "Homepage_26",
        "Homepage_27", "Homepage_28", "Homepage_29", "Homepage_30", "Homepage_31",
        "Homepage_32", "Homepage_33", "Homepage_34", "Homepage_35", "Homepage_36",
        "Homepage_37", "Homepage_38", "Homepage_39", "Homepage_40", "Homepage_41",
        "Homepage_42", "Homepage_43", "Homepage_44", "Homepage_45", "Homepage_46",
        "Homepage_47", "Homepage_48", "Homepage_49", "Homepage_50", "Homepage_51",
        "Homepage_52", "Homepage_53", "Homepage_54", "Homepage_55", "Homepage_56",
        "Homepage_57", "Homepage_58", "Homepage_59", "Homepage_60", "Homepage_61",
        "Homepage_62", "Homepage_63", "Homepage_64", "Homepage_65", "Homepage_68",
        "Homepage_69", "Homepage_70", "Homepage_71", "Homepage_72", "Homepage_73",
        "Homepage_74", "Homepage_75", "Homepage_76", "Homepage_77", "Homepage_78",
        "Homepage_79", "Homepage_80", "Homepage_81", "Homepage_82", "Homepage_83",
        "Homepage_84", "Homepage_86", "Homepage_87", "Homepage_88", "Homepage_89",
        "Homepage_90", "Homepage_91", "Homepage_92", "Homepage_93", "Homepage_94",
        "Homepage_95", "Homepage_96", "Homepage_97", "Homepage_98", "Homepage_99",
        "Homepage_100", "Homepage_102", "Homepage_103", "Homepage_104", "Homepage_105",
        "Homepage_106", "Homepage_107", "Homepage_109", "Homepage_110", "Homepage_111",
        "Homepage_112", "Homepage_113", "Homepage_114", "Homepage_115", "Homepage_116",
        "Homepage_117", "Homepage_118", "Homepage_119", "Homepage_120", "Homepage_121",
        "Homepage_122", "Homepage_123", "Homepage_124", "Homepage_125", "Homepage_126",
        "Homepage_127", "Homepage_128", "Homepage_129", "Homepage_130", "Homepage_131",
        "Homepage_132", "Homepage_133", "Homepage_134", "Homepage_135", "Homepage_136",
        "Homepage_137", "Homepage_138", "Homepage_139", "Homepage_140", "Homepage_141",
        "Homepage_142", "Homepage_143", "Homepage_144", "Homepage_145", "Homepage_146",
        "Homepage_147", "Homepage_149", "Homepage_150", "Homepage_151", "Homepage_153",
        "Homepage_155", "Homepage_160", "Homepage_161", "Homepage_162", "Homepage_163",
        "Homepage_164", "Homepage_165", "Homepage_166", "Homepage_167", "Homepage_168",
        "Homepage_169", "Homepage_171", "Homepage_172", "Homepage_173", "Homepage_174",
        "Homepage_175", "Homepage_176", "Homepage_177", "Homepage_178", "Homepage_179",
        "Homepage_180", "Homepage_181", "Homepage_182", "Homepage_183", "Homepage_184",
        "Homepage_185", "Homepage_190", "Homepage_187", "Homepage_188", "Homepage_189",
        "Homepage_194", "Homepage_195", "Homepage_196", "Homepage_197", "Homepage_198",
        "Homepage_199", "Homepage_200", "Homepage_201", "Homepage_202", "Homepage_203",
        "Homepage_204", "Homepage_205", "Homepage_206", "Homepage_207", "Homepage_208",
        "Homepage_209", "Homepage_210", "Homepage_211"
    ]
    
    for path in paths:
        df = pd.read_excel(path, sheet_name="tiles", engine='openpyxl', header=1)
        
        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\user_tiles\\output_files\\{target_sys}_user_tiles.xlsx'
          

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name="tiles", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets["tiles"]    

        # Auto-adjust columns' width
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_width)
       

        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})    

        for index, row in df.iterrows():
            user_types = row['UserTypes'].split(', ')
            print(user_types)    

            for user_type in user_types:
                for object in web_objects:   
                    if object in object_processors:
                        driver_response = fdi.initialize_driver()    

                        # Retrieve the function from object_processors
                        #target_func = object_processors[object]

                        for target_func in object_processors[object]:
                            try:
                                # Call the retrieved function
                                global_web_object_processor(target_func, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                                #processing_functions(target_func, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                            except Exception as e:
                                print("Error finding Web_Object: ")
                                print(e)
                        driver_response.quit()    

        excel_writer.close()    

        print("[Batch Process Complete]")



def buildAndReleaseManifests(target_sys, username, password, driver_response, user_type, manifest): 
    def searchForManifest(driver_response):
        wait = WebDriverWait(driver_response, 10)

        manifests = {
            1: "rfAdmin"
            , 2: "rfCommon"
            , 3: "rfEditors"
            , 4: "rfGlobals"
            , 5: "rfHomepage"
            , 6: "rfJavScript"
            , 7: "rfLogin"
            , 8: "rfLoginAAD"
            , 9: "rfNavigationMe"
            , 10: "rfQuickEntry"
            , 11: "rfRoster"
            , 12: "rfTableFunctions"
        }

        # Will fetch the value correpsonding to the index that has been passed
        if manifest in manifests: 
            manifest_name = manifests[manifest]

        # Find the search input element by its ID
        search_input = wait.find_element(By.ID, "homepagesearch")        

        # Click on the element to focus on it (optional, if needed)
        search_input.click()        

        # Insert a value into the search input
        search_input.send_keys(manifest_name)        

        # Find the search button by its class name (assuming the class is unique)
        search_button = wait.find_element(By.CLASS_NAME, "admin_reload")        

        # Click on the search button
        search_button.click()

        # Find the spanner icon element by its class name
        spanner_icon = wait.find_element(By.CLASS_NAME, "fa-light.fa-wrench")

        # Click on the spanner icon to open the manifest
        spanner_icon.click()

    def buildManifest(driver_response):
        searchForManifest(driver_response)


        pass


    def buildAndReleaseManifests(driver_response):
        searchForManifest(driver_response)
        pass

    if driver_response is None: 
        driver_response = fdi.initialize_driver()
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionOverrunReasonsTile(driver_response)    
    else: 
        try: 
            # Login and load Webpage
            gs.loginAndLoadHomePage(target_sys, username, password, driver_response, True)

            # Check user role and switch
            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
        
            # Load up 'Admin Screen' 
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)

            # Click and load up 'System Configuration' sub menu items 
            a.systemAdminLoadSubMenuItems(target_sys, headless_mode, user_type, username, password, driver_response, True)

            a.clickManifestSubMenuItem(driver_response)
            
            clickPageLoadSessionOverrunReasonsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Test env for automated functions
if __name__ == "__main__":
    target_sys = ''
    username = ''
    password = ''

    #batchProcessUserTypeTiles(target_sys, username, password, ['..\\excel_sheets\\user_tiles\\.xlsx'])

    #ut.dashboardReportsSkillsTile(target_sys, username, password, driver_response=None, optional_error_catch=None)
    #ut.dashboardReportSicknessPaidTile(target_sys, username, password, driver_response=None, optional_error_catch=None)
    #ut.homePageLoadAbsenceSummaryTile(target_sys, username, password, driver_response=None, optional_error_catch=None)

    #ut.managmentPageLoadBulkPatternRenewalTile(target_sys, username, password, driver_response=None, optional_error_catch=None)

    #ut.selfServicePageLoadMyAbsencesTile(target_sys, username, password, driver_response=None, optional_error_catch=None)

    for i in range(1, 212):
        print(i)

    
    ###################################################### HOME ######################################################## 
    #homePageLoadAbsenceSummaryTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_203
    #homePageLoadNextAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_204
    #homePageLoadNextShiftTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_34
    ###############################################END OF HOME TILES #################################################


    ############################################### MANAGMENT TILES ##################################################
    #managmentPageLoadRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_145
    #managmentPageLoadQuickEntryTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_151
    #managmentPageLoadScheduledRotasTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_79
    #managmentPageLoadScheduledJobsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_82
    #managmentPageLoadSkillsExpiryTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_5
    #managmentPageLoadSkillsExpiryTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_181
    #managmentPagePayrollTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_210
    #managmentPagePayrollTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_19
    #managmentPageLoadCarryForwardRequestsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_176
    #managmentPageLoadMoveOrTeminateStaffTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_208
    #managmentPageLoadBulkPatternRenewalTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_109    

    ###########################################FOR NOW, NOT TO BE INCLUDED IN NHSBT TEST##########################################
    #managmentPageBulkScheduledTimesheetsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_185
    #managmentPageBulkScheduledTimesheetsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_146
    ############################################### END OF MANAGMENT TILES ###############################################    

    ################################################## DATA PROCESSING TILES ######################################################
    #dataProcessingPageLoadESRGoImportTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_162
    #dataProcessingPageLoadESRExportTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_166
    #dataProcessingPageLoadNHSBTSessionDataImportTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_144
    #dataProcessingPageLoadDriverAllowanceUploadTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_155
    #dataProcessingPageLoadAnnualLeavePlansTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_160
    ################################################### END OF DATA PROCESSING TILES ######################################################    

    ################################################## SELF SERVICE TILES ######################################################## 
    #selfServicePageLoadMyRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_202
    #selfServicePageLoadMyLocationTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_14
    #selfServicePageLoadMyTeamRotaTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_179
    #selfServicePageLoadMyAvailabilitiesTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_13
    #selfServicePageLoadMyAbsencesTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_89
    #selfServicePageLoadCarryForwardRequestsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_176
    #selfServicePageLoadChangePasswordTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_59
    #selfServicePageLoadMyGDPRTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_123
    #selfServicePageLoadEmailOptOutTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_97
    ########################################### END OF SELF SERVICE TILES ###########################################    

    ############################################## REPORTS TILES ####################################################
    #reportsPageLoadMultiPostTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1107
    #reportsPageLoadBankStaffUsageTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1078
    #reportsPageLoadSkillsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_12
    #reportsPageLoadUnsubmittedSessionsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1101
    #reportsPageLoadNewStartersTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1075
    #reportsPageLoadAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1102
    #reportsPageLoadAwayFromHomeTeamTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1100
    #reportsPageLoadMyCalculationsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1074
    #reportsPageLoadHoursReportTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_8
    #reportsPageLoadPreviousSessionReportTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1093
    #reportsPageLoadDoubleSessionsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1072
    #reportsPageLoadEmployeeCalculationsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1068
    #reportsPageLoadBankStaffUtilTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1079
    #reportsExtraDutiesPageTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_REPORT_1071
    ################################################## END OF REPORTS TILES ######################################################    

    ############################################### DASHBOARD REPORTS TILES ######################################################
    #dashboardReportsSessionUnavailablityTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_9
    #dashboardReportsBankHoursPaidTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_3
    #dashboardReportsStaffingModelTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_8
    #dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_7
    #dashboardReportsSeshPlannedWithShortfallorSurplusTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_38
    #dashboardReportsSeshExpectedVSSeshPlannedTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_6
    #dashboardReportsSkillsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_1
    #dashboardReportSicknessPaidTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_5
    #dashboardReportAbsenceTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_4
    #dashboardReportAnnualLeaveBookByDayTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_39
    #dashboardReportAnnualLeaveBookVsAllowanceTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_40
    #dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_41
    #dashboardReportSessionOverrunReasonsTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_DASHBOARDREPORT_43
    #dashboardReportExportMultiToPDFTile(target_sys, username, password, driver_response=None, optional_error_catch=None) # HOMEPAGE_183
    ############################################### END OF DASHBOARD REPORTS TILES ################################################
