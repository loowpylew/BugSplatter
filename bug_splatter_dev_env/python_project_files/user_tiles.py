import f_driver_init as fdi
import globals as gs
import menu_items as mi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style, init
from openpyxl import load_workbook
from selenium.common.exceptions import TimeoutException
import pandas as pd 
import numpy as np

####################################### TARGET FUNCTIONS - SPECIFIC USER TILE #####################################

##################################################### HOME ######################################################## 
# Dashboard Absence Summary - target function
def homePageLoadAbsenceSummaryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 

    def clickAbsenceSummaryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_summary_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_203')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_summary_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_summary_tile)
        
        #absence_summary_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickAbsenceSummaryTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickAbsenceSummaryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Next Absence - target function
def homePageLoadNextAbsenceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 

    def clickNextAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        next_absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_204')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", next_absence_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", next_absence_tile)
        
        
        #next_absence_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickNextAbsenceTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickNextAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Next Shift - target function
def homePageLoadNextShiftTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 

    def clickNextShiftTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        next_shift_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_34')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", next_shift_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", next_shift_tile)
        
        
        #next_shift_tile.click()


    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickNextShiftTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickNextShiftTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

##############################################END OF HOME TILES #################################################


############################################## MANAGEMENT TILES ##################################################
# Skills Expiry - Management
def managmentPageLoadSkillsExpiryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSkillsExpiryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        skills_expiry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_5')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", skills_expiry_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", skills_expiry_tile)

        #skills_expiry_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSkillsExpiryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSkillsExpiryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Clockings - Management
def managmentPageLoadClockingsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickClockingsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        clockings_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_17')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", clockings_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", clockings_tile)

        #clockings_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickClockingsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickClockingsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Absence Requests - Management
def managmentPageLoadAbsenceRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAbsenceRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        absence_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_19')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_requests_tile)

        #absence_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAbsenceRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAbsenceRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# AdminOld - Management
def managmentPageLoadAdminOldTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAdminOldTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        admin_old_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_22')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", admin_old_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", admin_old_tile)

        #admin_old_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAdminOldTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAdminOldTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Rota - Management
def managmentPageLoadRotaTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_26')))
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", rota_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", rota_tile)

        #rota_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRotaTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Rota Changes - Management
def managmentPageLoadRotaChangesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRotaChangesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        rota_changes_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_29')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", rota_changes_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", rota_changes_tile)

        #rota_changes_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRotaChangesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRotaChangesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Exceptions Report - Management
def managmentPageLoadExceptionsReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickExceptionsReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        exceptions_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_32')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", exceptions_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", exceptions_report_tile)

        #exceptions_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickExceptionsReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickExceptionsReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Late Staff - Management
def managmentPageLoadLateStaffTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLateStaffTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        late_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_35')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", late_staff_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", late_staff_tile)

        #late_staff_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLateStaffTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLateStaffTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shortfalls Allocate - Management
def managmentPageLoadShortfallsAllocateTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickShortfallsAllocateTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        shortfalls_allocate_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_36')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_allocate_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_allocate_tile)

        #shortfalls_allocate_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickShortfallsAllocateTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickShortfallsAllocateTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Missed Check Calls - Management
def managmentPageLoadMissedCheckCallsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMissedCheckCallsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        missed_check_calls_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_37')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", missed_check_calls_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", missed_check_calls_tile)

        #missed_check_calls_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMissedCheckCallsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMissedCheckCallsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Refresher Training - Management
def managmentPageLoadRefresherTrainingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRefresherTrainingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        refresher_training_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_38')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", refresher_training_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", refresher_training_tile)

        #refresher_training_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRefresherTrainingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRefresherTrainingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# No Response/ Unconfirmed - Management
def managmentPageLoadNoResponseUnconfirmedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNoResponseUnconfirmedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        no_response_unconfirmed_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_39')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", no_response_unconfirmed_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", no_response_unconfirmed_tile)

        #no_response_unconfirmed_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNoResponseUnconfirmedTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNoResponseUnconfirmedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shortfalls Offer - Management
def managmentPageLoadShortfallsOfferTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickShortfallsOfferTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        shortfalls_offer_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_41')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_offer_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_offer_tile)

        #shortfalls_offer_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickShortfallsOfferTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickShortfallsOfferTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Postponed Training - Management
def managmentPageLoadPostponedTrainingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPostponedTrainingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        postponed_training_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_45')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", postponed_training_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", postponed_training_tile)

        #postponed_training_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPostponedTrainingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPostponedTrainingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Failed Check Calls - Management
def managmentPageLoadFailedCheckCallsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickFailedCheckCallsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        failed_check_calls_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_48')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", failed_check_calls_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", failed_check_calls_tile)

        #failed_check_calls_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickFailedCheckCallsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickFailedCheckCallsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Timesheets - Management
def managmentPageLoadTimesheetsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTimesheetsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_56')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", timesheets_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", timesheets_tile)

        #timesheets_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTimesheetsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTimesheetsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Import Rota Data - Management
def managmentPageLoadImportRotaDataTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickImportRotaDataTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        import_rota_data_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_57')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", import_rota_data_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", import_rota_data_tile)

        #import_rota_data_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickImportRotaDataTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickImportRotaDataTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Payroll Submission - Management
def managmentPageLoadPayrollSubmissionTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPayrollSubmissionTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        payroll_submission_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_60')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", payroll_submission_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", payroll_submission_tile)

        #payroll_submission_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPayrollSubmissionTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPayrollSubmissionTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Clockings By Person - Management
def managmentPageLoadClockingsByPersonTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickClockingsByPersonTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        clockings_by_person_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_61')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", clockings_by_person_tile)

        #clockings_by_person_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickClockingsByPersonTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickClockingsByPersonTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Data Transfer Failures - Management
def managmentPageLoadDataTransferFailuresTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDataTransferFailuresTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        data_transfer_failures_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_62')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", data_transfer_failures_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", data_transfer_failures_tile)

        #data_transfer_failures_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDataTransferFailuresTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDataTransferFailuresTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Missed Tasks - Management
def managmentPageLoadMissedTasksTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMissedTasksTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        missed_tasks_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_63')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", missed_tasks_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", missed_tasks_tile)

        #missed_tasks_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMissedTasksTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMissedTasksTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Manager Work Plan - Management
def managmentPageLoadManagerWorkPlanTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickManagerWorkPlanTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        manager_work_plan_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_65')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", manager_work_plan_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", manager_work_plan_tile)

        #manager_work_plan_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickManagerWorkPlanTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickManagerWorkPlanTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Admin Message Board - Management
def managmentPageLoadAdminMessageBoardTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAdminMessageBoardTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        admin_message_board_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_68')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", admin_message_board_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", admin_message_board_tile)
        
        #admin_message_board_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAdminMessageBoardTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAdminMessageBoardTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Unrecognized Messages - Management
def managmentPageLoadUnrecognizedMessagesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickUnrecognizedMessagesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        unrecognized_messages_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_69')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", unrecognized_messages_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", unrecognized_messages_tile)

        #unrecognized_messages_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickUnrecognizedMessagesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickUnrecognizedMessagesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# NHSBT Import - Management
def managmentPageLoadNHSBTImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNHSBTImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nhsbt_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_70')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nhsbt_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nhsbt_import_tile)

        #nhsbt_import_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNHSBTImportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNHSBTImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Hub Demand - Management
def managementPageLoadHubDemandTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHubDemandTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hub_demand_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_73')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hub_demand_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hub_demand_tile)

        #hub_demand_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHubDemandTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHubDemandTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# NHSBT Quick Entry - Management
def managmentPageLoadNHSBTQuickEntryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNHSBTQuickEntryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nhsbt_quick_entry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_74')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nhsbt_quick_entry_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nhsbt_quick_entry_tile)

        #nhsbt_quick_entry_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNHSBTQuickEntryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNHSBTQuickEntryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Quick Admin - Management
def managmentPageLoadAgencyQuickAdminTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyQuickAdminTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_quick_admin_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_75')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_quick_admin_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_quick_admin_tile)

        #agency_quick_admin_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyQuickAdminTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyQuickAdminTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Section Transfers - Management
def managmentPageLoadSectionTransfersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSectionTransfersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        section_transfers_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_76')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", section_transfers_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", section_transfers_tile)

        #section_transfers_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSectionTransfersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSectionTransfersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hub Status - Management
def managmentPageLoadHubStatusTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHubStatusTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hub_status_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_80')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hub_status_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hub_status_tile)

        #hub_status_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHubStatusTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHubStatusTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hub Visibility - Management
def managmentPageLoadHubVisibilityTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHubVisibilityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hub_visibility_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_81')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hub_visibility_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hub_visibility_tile)

        #hub_visibility_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHubVisibilityTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHubVisibilityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Staff Quick Admin - Management
def managmentPageLoadStaffQuickAdminTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffQuickAdminTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_quick_admin_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_83')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_quick_admin_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_quick_admin_tile)

        #staff_quick_admin_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffQuickAdminTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffQuickAdminTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shift Swap Requests - Management
def managmentPageLoadShiftSwapRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickShiftSwapRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        shift_swap_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_86')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shift_swap_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shift_swap_requests_tile)

        #shift_swap_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickShiftSwapRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickShiftSwapRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Scenarios Upload - Management
def managmentPageLoadScenariosUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickScenariosUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        scenarios_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_93')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", scenarios_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", scenarios_upload_tile)

        #scenarios_upload_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickScenariosUploadTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickScenariosUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Generate Log Book Numbers - Management
def managmentPageLoadGenerateLogBookNumbersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickGenerateLogBookNumbersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        generate_log_book_numbers_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_94')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", generate_log_book_numbers_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", generate_log_book_numbers_tile)

        #generate_log_book_numbers_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickGenerateLogBookNumbersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickGenerateLogBookNumbersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Training Overdue - Management
def managmentPageLoadTrainingOverdueTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTrainingOverdueTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        training_overdue_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_98')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", training_overdue_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", training_overdue_tile)

        #training_overdue_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTrainingOverdueTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTrainingOverdueTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# 12 Hour Unfilled Casuals - Management
def managmentPageLoad12HourUnfilledCasualsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def click12HourUnfilledCasualsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        unfilled_casuals_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_99')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", unfilled_casuals_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", unfilled_casuals_tile)

        #unfilled_casuals_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        click12HourUnfilledCasualsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            click12HourUnfilledCasualsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Work Plan Report - Management
def managmentPageLoadWorkPlanReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWorkPlanReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        work_plan_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_103')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", work_plan_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", work_plan_report_tile)

        #work_plan_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWorkPlanReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWorkPlanReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Muster List - Management
def managmentPageLoadMusterListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMusterListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        muster_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_105')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", muster_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", muster_list_tile)

        #muster_list_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMusterListTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMusterListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Bulk Pattern Renewal - Management
def managmentPageLoadBulkPatternRenewalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBulkPatternRenewalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bulk_pattern_renewal_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_109')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bulk_pattern_renewal_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bulk_pattern_renewal_tile)

        #bulk_pattern_renewal_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBulkPatternRenewalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBulkPatternRenewalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Simulate Users - Management
def managmentPageLoadSimulateUsersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSimulateUsersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        simulate_users_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_111')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", simulate_users_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", simulate_users_tile)

        #simulate_users_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSimulateUsersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSimulateUsersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Applicants - Management
def managmentPageLoadApplicantsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickApplicantsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        applicants_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_112')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", applicants_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", applicants_tile)

        #applicants_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickApplicantsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickApplicantsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Training - Management
def managmentPageLoadTrainingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTrainingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        training_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_113')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", training_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", training_tile)

        #training_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTrainingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTrainingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Document Approval - Management
def managmentPageLoadDocumentApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDocumentApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        document_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_115')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", document_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", document_approval_tile)

        #document_approval_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDocumentApprovalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDocumentApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# CM Call Backs - Management
def managmentPageLoadCMCallBacksTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCMCallBacksTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        cm_call_backs_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_116')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", cm_call_backs_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", cm_call_backs_tile)

        #cm_call_backs_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCMCallBacksTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCMCallBacksTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Details Approval - Management
def managmentPageLoadDetailsApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDetailsApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        details_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_117')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", details_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", details_approval_tile)

        #details_approval_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDetailsApprovalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDetailsApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# MV Lieu - Management
def managmentPageLoadMVLieuTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMVLieuTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        mv_lieu_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_118')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", mv_lieu_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", mv_lieu_tile)

        #mv_lieu_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMVLieuTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMVLieuTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Swedish Derogation - Management
def managmentPageLoadSwedishDerogationTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSwedishDerogationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        swedish_derogation_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_119')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", swedish_derogation_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", swedish_derogation_tile)

        #swedish_derogation_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSwedishDerogationTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSwedishDerogationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My CM Call Backs - Management
def managmentPageLoadMyCMCallBacksTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyCMCallBacksTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_cm_call_backs_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_120')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_cm_call_backs_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_cm_call_backs_tile)

        #my_cm_call_backs_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyCMCallBacksTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyCMCallBacksTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Placement Confirmations - Management
def managmentPageLoadPlacementConfirmationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPlacementConfirmationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        placement_confirmations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_121')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", placement_confirmations_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", placement_confirmations_tile)

        #placement_confirmations_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPlacementConfirmationsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPlacementConfirmationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# SE Holiday - Management
def managmentPageLoadSEHolidayTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSEHolidayTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        se_holiday_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_122')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", se_holiday_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", se_holiday_tile)

        #se_holiday_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSEHolidayTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSEHolidayTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# SE Accrued - Management
def managmentPageLoadSEAccruedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSEAccruedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        se_accrued_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_126')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", se_accrued_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", se_accrued_tile)

        #se_accrued_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSEAccruedTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSEAccruedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# SE Unpaid Holiday - Management
def managmentPageLoadSEUnpaidHolidayTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSEUnpaidHolidayTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        se_unpaid_holiday_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_127')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", se_unpaid_holiday_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", se_unpaid_holiday_tile)

        #se_unpaid_holiday_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSEUnpaidHolidayTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSEUnpaidHolidayTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Staff Feedback - Management
def managmentPageLoadStaffFeedbackTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffFeedbackTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_feedback_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_131')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_feedback_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_feedback_tile)

        #staff_feedback_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffFeedbackTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffFeedbackTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Lieu Mgmt (Hours) - Management
def managmentPageLoadLieuMgmtHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLieuMgmtHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        lieu_mgmt_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_134')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", lieu_mgmt_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", lieu_mgmt_hours_tile)

        #lieu_mgmt_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLieuMgmtHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLieuMgmtHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Lieu Mgmt (Days) - Management
def managmentPageLoadLieuMgmtDaysTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLieuMgmtDaysTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        lieu_mgmt_days_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_135')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", lieu_mgmt_days_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", lieu_mgmt_days_tile)

        #lieu_mgmt_days_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLieuMgmtDaysTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLieuMgmtDaysTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Wage Amendments - Management
def managmentPageLoadWageAmendmentsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWageAmendmentsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        wage_amendments_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_136')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", wage_amendments_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", wage_amendments_tile)

        wage_amendments_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWageAmendmentsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWageAmendmentsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Billing - Management
def managmentPageLoadBillingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBillingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        billing_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_140')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", billing_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", billing_tile)

        #billing_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBillingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBillingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Test Split Drop List Page - Management
def managmentPageLoadTestSplitDropListPageTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTestSplitDropListPageTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        test_split_drop_list_page_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_141')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", test_split_drop_list_page_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", test_split_drop_list_page_tile)

        #test_split_drop_list_page_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTestSplitDropListPageTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTestSplitDropListPageTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Interchange Screens - Management
def managmentPageLoadInterchangeScreensTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickInterchangeScreensTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        interchange_screens_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_142')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", interchange_screens_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", interchange_screens_tile)

        #interchange_screens_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickInterchangeScreensTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickInterchangeScreensTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Support Portal - Management
def managmentPageLoadSupportPortalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSupportPortalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        support_portal_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_143')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", support_portal_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", support_portal_tile)

        #support_portal_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSupportPortalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSupportPortalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Rota - Management
def managmentPageLoadRotaTile2(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_145')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", rota_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", rota_tile)

        #rota_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRotaTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Schedule Timesheets - Management
def managmentPageLoadScheduleTimesheetsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickScheduleTimesheetsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        schedule_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_146')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", schedule_timesheets_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", schedule_timesheets_tile)

        #schedule_timesheets_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickScheduleTimesheetsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickScheduleTimesheetsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Check A Single Team Calculation - Management
def managmentPageLoadCheckSingleTeamCalculationTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCheckSingleTeamCalculationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        check_single_team_calculation_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_147')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", check_single_team_calculation_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", check_single_team_calculation_tile)

        #check_single_team_calculation_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCheckSingleTeamCalculationTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCheckSingleTeamCalculationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Submit All Timesheets - Management
def managmentPageLoadSubmitAllTimesheetsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSubmitAllTimesheetsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        submit_all_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_149')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", submit_all_timesheets_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", submit_all_timesheets_tile)

        #submit_all_timesheets_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSubmitAllTimesheetsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSubmitAllTimesheetsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# NHSBT Import - Management
def managmentPageLoadNHSBTImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNHSBTImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nhsbt_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_150')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nhsbt_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nhsbt_import_tile)

        #nhsbt_import_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNHSBTImportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNHSBTImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# NHSBT Quick Entry - Management
def managmentPageLoadNHSBTQuickEntryTile2(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNHSBTQuickEntryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nhsbt_quick_entry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_151')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nhsbt_quick_entry_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nhsbt_quick_entry_tile)

        #nhsbt_quick_entry_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNHSBTQuickEntryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNHSBTQuickEntryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Download ESR Files - Management
def managmentPageLoadDownloadESRFilesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDownloadESRFilesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        download_esr_files_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_153')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", download_esr_files_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", download_esr_files_tile)
        
        #download_esr_files_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDownloadESRFilesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDownloadESRFilesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Timesheet Runs - Management
def managmentPageLoadTimesheetRunsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTimesheetRunsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        timesheet_runs_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_161')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", timesheet_runs_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", timesheet_runs_tile)

        #timesheet_runs_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTimesheetRunsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTimesheetRunsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave Adjustments - Management
def managmentPageLoadAnnualLeaveAdjustmentsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAnnualLeaveAdjustmentsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        annual_leave_adjustments_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_163')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_adjustments_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_adjustments_tile)

        #annual_leave_adjustments_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAnnualLeaveAdjustmentsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAnnualLeaveAdjustmentsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# DAYS Accrual Testing - Management
def managmentPageLoadDaysAccrualTestingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDaysAccrualTestingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        days_accrual_testing_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_164')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", days_accrual_testing_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", days_accrual_testing_tile)

        #days_accrual_testing_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDaysAccrualTestingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDaysAccrualTestingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# HOURS Accrual Testing - Management
def managmentPageLoadHoursAccrualTestingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHoursAccrualTestingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hours_accrual_testing_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_165')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hours_accrual_testing_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hours_accrual_testing_tile)

        #hours_accrual_testing_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHoursAccrualTestingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHoursAccrualTestingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Carry Forward Requests - Management
def managmentPageLoadCarryForwardRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        carry_forward_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_168')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", carry_forward_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", carry_forward_requests_tile)

        #carry_forward_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCarryForwardRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Year Annual Leave Adjustments - Management
def managmentPageLoadYearAnnualLeaveAdjustmentsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickYearAnnualLeaveAdjustmentsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        year_annual_leave_adjustments_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_169')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", year_annual_leave_adjustments_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", year_annual_leave_adjustments_tile)

        #year_annual_leave_adjustments_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickYearAnnualLeaveAdjustmentsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickYearAnnualLeaveAdjustmentsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hols (H) Mgmt (Hours) - Management
def managmentPageLoadHolsHMgmtHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHolsHMgmtHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hols_h_mgmt_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_173')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hols_h_mgmt_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hols_h_mgmt_hours_tile)

        #hols_h_mgmt_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHolsHMgmtHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHolsHMgmtHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hols (D) Mgmt (Days) - Management
def managmentPageLoadHolsDMgmtDaysTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHolsDMgmtDaysTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hols_d_mgmt_days_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_174')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hols_d_mgmt_days_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hols_d_mgmt_days_tile)

        #hols_d_mgmt_days_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHolsDMgmtDaysTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHolsDMgmtDaysTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# My Team Rota - Management
def managmentPageLoadMyTeamRotaTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyTeamRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_team_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_175')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_team_rota_tile )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_team_rota_tile )

        #my_team_rota_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyTeamRotaTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyTeamRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Carry Forward Requests - Management
def managmentPageLoadCarryForwardRequestsTile2(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        carry_forward_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_177')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", carry_forward_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", carry_forward_requests_tile)

        #carry_forward_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCarryForwardRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Holiday Management - Management
def managmentPageLoadHolidayManagementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHolidayManagementTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        holiday_management_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_178')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", holiday_management_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", holiday_management_tile)

        #holiday_management_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHolidayManagementTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHolidayManagementTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Timesheet Testing - Management
def managmentPageLoadTimesheetTestingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTimesheetTestingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        timesheet_testing_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_180')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", timesheet_testing_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", timesheet_testing_tile)

        #timesheet_testing_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTimesheetTestingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTimesheetTestingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Absence Adjustments - Management
def managmentPageLoadAbsenceAdjustmentsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAbsenceAdjustmentsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        absence_adjustments_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_181')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_adjustments_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_adjustments_tile)

        #absence_adjustments_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAbsenceAdjustmentsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAbsenceAdjustmentsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Bulk Absence Booking - Management
def managmentPageLoadBulkAbsenceBookingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBulkAbsenceBookingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bulk_absence_booking_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_182')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bulk_absence_booking_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bulk_absence_booking_tile)

        #bulk_absence_booking_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBulkAbsenceBookingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBulkAbsenceBookingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Lock tile test - Management
def managmentPageLoadLockTileTestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLockTileTestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        lock_tile_test_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_184')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", lock_tile_test_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", lock_tile_test_tile)

        #lock_tile_test_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLockTileTestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLockTileTestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Bulk Schedule Timesheets - Management
def managmentPageLoadBulkScheduleTimesheetsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBulkScheduleTimesheetsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bulk_schedule_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_185')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bulk_schedule_timesheets_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bulk_schedule_timesheets_tile)

        #bulk_schedule_timesheets_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBulkScheduleTimesheetsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBulkScheduleTimesheetsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Manager Approval - Management
def managmentPageLoadManagerApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickManagerApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        manager_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_187')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();",  manager_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  manager_approval_tile)

        #manager_approval_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickManagerApprovalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickManagerApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Details For Approval - Management
def managmentPageLoadDetailsForApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDetailsForApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        details_for_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_190')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", details_for_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", details_for_approval_tile)

        #details_for_approval_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDetailsForApprovalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDetailsForApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Mobile Rota - Management
def managmentPageLoadMobileRotaTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMobileRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        mobile_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_194')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", mobile_rota_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", mobile_rota_tile)

        #mobile_rota_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMobileRotaTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMobileRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Invoice Display Test - Management
def managmentPageLoadInvoiceDisplayTestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickInvoiceDisplayTestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        invoice_display_test_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_197')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", invoice_display_test_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", invoice_display_test_tile)

        #invoice_display_test_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickInvoiceDisplayTestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickInvoiceDisplayTestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Invoicing - Management
def managmentPageLoadInvoicingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickInvoicingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        invoicing_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_198')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", invoicing_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", invoicing_tile)

        #invoicing_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickInvoicingTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickInvoicingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# NextraMobile - Management
def managmentPageLoadNextraMobileTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNextraMobileTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nextra_mobile_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_199')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nextra_mobile_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nextra_mobile_tile)

        #nextra_mobile_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNextraMobileTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNextraMobileTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(e)


# Knowledge Hub - Management
def managmentPageLoadKnowledgeHubTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickKnowledgeHubTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        knowledge_hub_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_201')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();",  knowledge_hub_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  knowledge_hub_tile)

        #knowledge_hub_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickKnowledgeHubTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickKnowledgeHubTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# DG Rota TEST - Management
def managmentPageLoadDGRotaTestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDGRotaTestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        dg_rota_test_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_206')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", dg_rota_test_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", dg_rota_test_tile)

        #dg_rota_test_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDGRotaTestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDGRotaTestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Move/Terminate Staff - Management
def managmentPageLoadMoveTerminateStaffTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMoveTerminateStaffTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        move_terminate_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_208')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", move_terminate_staff_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", move_terminate_staff_tile)

        #move_terminate_staff_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMoveTerminateStaffTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMoveTerminateStaffTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Timesheet Approval - Management
def managmentPageLoadTimesheetApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTimesheetApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        timesheet_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_209')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", timesheet_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", timesheet_approval_tile)

        #timesheet_approval_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTimesheetApprovalTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTimesheetApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Payroll - Management
def managmentPageLoadPayrollTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPayrollTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        payroll_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_210')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", payroll_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", payroll_tile)

        #payroll_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPayrollTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadManagmentMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPayrollTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
############################################## END OF MANAGMENT TILES ###############################################

################################################# DATA PROCESSING ######################################################

# Site Training - target function 
def dataProcessingPageLoadSiteTrainingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadSiteTrainingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        site_training_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_40')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", site_training_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", site_training_tile)

        #site_training_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadSiteTrainingTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadSiteTrainingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Standby Staff - target function 
def dataProcessingPageLoadStandbyStaffTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadStandbyStaffTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        standby_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_43')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", standby_staff_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", standby_staff_tile)

        #standby_staff_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadStandbyStaffTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadStandbyStaffTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Site Emails - target function 
def dataProcessingPageLoadSiteEmailsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadSiteEmailsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        site_emails_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_44')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", site_emails_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", site_emails_tile)

        #site_emails_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadSiteEmailsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadSiteEmailsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Site Summary Email - target function 
def dataProcessingPageLoadSiteSummaryEmailTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadSiteSummaryEmailTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        site_summary_email_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_46')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", site_summary_email_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", site_summary_email_tile)

        #site_summary_email_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadSiteSummaryEmailTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadSiteSummaryEmailTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Reallocate Training - target function 
def dataProcessingPageLoadReallocateTrainingTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadReallocateTrainingTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        reallocate_training_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_47')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", reallocate_training_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", reallocate_training_tile)

        #reallocate_training_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadReallocateTrainingTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadReallocateTrainingTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Demand Data - target function 
def dataProcessingPageLoadDemandDataTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadDemandDataTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        demand_data_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_49')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", demand_data_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", demand_data_tile)

        #demand_data_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadDemandDataTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadDemandDataTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Scheduled Rotas - target function 
def dataProcessingPageLoadScheduledRotasTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadScheduledRotasTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        scheduled_rotas_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_79')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", scheduled_rotas_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", scheduled_rotas_tile)
        
        #scheduled_rotas_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadScheduledRotasTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadScheduledRotasTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Scheduled Job - target function 
def dataProcessingPageLoadScheduledJobTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadScheduledJobTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        scheduled_job_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_82')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", scheduled_job_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", scheduled_job_tile)

        #scheduled_job_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadScheduledJobTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadScheduledJobTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Budget Data - target function 
def dataProcessingPageLoadBudgetDataTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadBudgetDataTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        budget_data_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_90')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", budget_data_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", budget_data_tile)

        #budget_data_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadBudgetDataTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadBudgetDataTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Event Approval - target function 
def dataProcessingPageLoadEventApprovalTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadEventApprovalTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        event_approval_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_92')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", event_approval_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", event_approval_tile)
        #event_approval_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadEventApprovalTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadEventApprovalTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Sailing Data Upload - target function 
def dataProcessingPageLoadSailingDataUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadSailingDataUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        sailing_data_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_132')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sailing_data_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", sailing_data_upload_tile)

        #sailing_data_upload_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadSailingDataUploadTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadSailingDataUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# KABA Clock list - target function 
def dataProcessingPageLoadKABAClockListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadKABAClockListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        kaba_clock_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_133')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", kaba_clock_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", kaba_clock_list_tile)

        #kaba_clock_list_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadKABAClockListTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadKABAClockListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave Plan Upload - target function 
def dataProcessingPageLoadAnnualLeavePlanUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadAnnualLeavePlanUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        annual_leave_plan_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_137')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_plan_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_plan_upload_tile)

        #annual_leave_plan_upload_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadAnnualLeavePlanUploadTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadAnnualLeavePlanUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# NHSBT Session Data Import - target function 
def dataProcessingPageLoadNHSBTSessionDataImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadNHSBTSessionDataImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        nhsbt_session_data_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_144')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", nhsbt_session_data_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", nhsbt_session_data_import_tile)

        #nhsbt_session_data_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadNHSBTSessionDataImportTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadNHSBTSessionDataImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Driver Allowance Upload - target function 
def dataProcessingPageLoadDriverAllowanceUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadDriverAllowanceUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        driver_allowance_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_155')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", driver_allowance_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", driver_allowance_upload_tile)

        #driver_allowance_upload_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadDriverAllowanceUploadTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadDriverAllowanceUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave Plan Upload - target function 
def dataProcessingPageLoadAnnualLeavePlanUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadAnnualLeavePlanUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        annual_leave_plan_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_160')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_plan_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_plan_upload_tile)

        #annual_leave_plan_upload_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadAnnualLeavePlanUploadTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadAnnualLeavePlanUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# ESR GO Import - target function 
def dataProcessingPageLoadESRGoImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadESRGoImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_162')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", esr_go_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", esr_go_import_tile)

        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadESRGoImportTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadESRGoImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# ESR Export - target function 
def dataProcessingPageLoadESRExportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadESRExportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        esr_export_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_166')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", esr_export_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", esr_export_tile)

        #esr_export_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadESRExportTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadESRExportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shortfalls Import - target function 
def dataProcessingPageLoadShortfallsImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    
    def clickPageLoadShortfallsImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        shortfalls_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_211')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_import_tile)

        #shortfalls_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickPageLoadShortfallsImportTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadDataProcessingMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadShortfallsImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

################################################## END OF DATA PROCESSING TILES ######################################################

###################################################### BANK TILES ###########################################################

# P&O Demand Data Import - target function
def bankPageLoadPAndODemandDataImportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPAndODemandDataImportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        po_demand_data_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_171')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", po_demand_data_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", po_demand_data_import_tile)

        #po_demand_data_import_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPAndODemandDataImportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPAndODemandDataImportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Search (Allocate) - target function
def bankPageLoadAgencySearchAllocateTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencySearchAllocateTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_search_allocate_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_78')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_search_allocate_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_search_allocate_tile)

        #agency_search_allocate_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencySearchAllocateTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencySearchAllocateTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Fulfil - target function
def bankPageLoadAgencyFulfilTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyFulfilTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_fulfil_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_77')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_fulfil_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_fulfil_tile)

        #agency_fulfil_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyFulfilTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyFulfilTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Agency Authorisations - Bank
def bankPageLoadAgencyAuthorisationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyAuthorisationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_authorisations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_52')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_authorisations_tile)

        # Click the element using execute_script directly
        #driver_response.execute_script("arguments[0].click();", agency_authorisations_tile)

        agency_authorisations_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyAuthorisationsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyAuthorisationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Hours - Bank
def bankPageLoadAgencyHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_104')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_hours_tile)

        #agency_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Agency Quick Request - Bank
def bankPageLoadAgencyQuickRequestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyQuickRequestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_quick_request_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_51')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_quick_request_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_quick_request_tile)

        #agency_quick_request_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyQuickRequestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyQuickRequestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Agency Search - Bank
def bankPageLoadAgencySearchTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencySearchTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_search_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_54')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_search_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_search_tile)

        #agency_search_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencySearchTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencySearchTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Search (Offer) - Bank
def bankPageLoadAgencySearchOfferTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencySearchOfferTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_search_offer_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_53')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_search_offer_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_search_offer_tile)

        #agency_search_offer_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencySearchOfferTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencySearchOfferTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Feeder Data Uploader - Bank
def bankPageLoadFeederDataUploaderTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickFeederDataUploaderTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        feeder_data_uploader_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_138')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", feeder_data_uploader_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", feeder_data_uploader_tile)
        
        #feeder_data_uploader_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickFeederDataUploaderTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickFeederDataUploaderTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# HR Data - Bank
def bankPageLoadHRDataTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHRDataTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hr_data_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_172')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hr_data_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hr_data_tile)

        #hr_data_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHRDataTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHRDataTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Tour Data Uploader - Bank
def bankPageLoadTourDataUploaderTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTourDataUploaderTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        tour_data_uploader_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_139')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", tour_data_uploader_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", tour_data_uploader_tile)

        #tour_data_uploader_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTourDataUploaderTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTourDataUploaderTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Unfilled Shifts - Bank
def bankPageLoadUnfilledShiftsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickUnfilledShiftsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        unfilled_shifts_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_102')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", unfilled_shifts_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", unfilled_shifts_tile)

        #unfilled_shifts_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickUnfilledShiftsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadBankMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickUnfilledShiftsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
################################################### END OF BANK TILES #######################################################
################################################# SELF SERVICE TILES ######################################################## 
# My Work Plan - Self-Service
def selfServicePageLoadMyWorkPlanTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyWorkPlanTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_work_plan_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_64')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_work_plan_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_work_plan_tile)

        #my_work_plan_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyWorkPlanTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyWorkPlanTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Payslip (MAG) - target function
def selfServicePageLoadMyPayslipTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyPayslipTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_payslip_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_84')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_payslip_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_payslip_tile)

        #my_payslip_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyPayslipTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyPayslipTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Personal Details - target function
def selfServicePageLoadMyPersonalDetailsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyPersonalDetailsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_personal_details_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_87')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_personal_details_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_personal_details_tile)

        #my_personal_details_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyPersonalDetailsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyPersonalDetailsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# My Timesheets - target function
def selfServicePageLoadMyTimesheetsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyTimesheetsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_timesheets_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_188')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_timesheets_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_timesheets_tile)

        #my_timesheets_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyTimesheetsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyTimesheetsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Rota - target function
def selfServicePageLoadMyRotaTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_202')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();",  my_rota_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  my_rota_tile)
        
        #my_rota_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyRotaTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Take my photo - target function
def selfServicePageLoadTakeMyPhotoTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTakeMyPhotoTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        take_my_photo_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_207')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", take_my_photo_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", take_my_photo_tile)

        #take_my_photo_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTakeMyPhotoTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTakeMyPhotoTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# My Shift Swap Requests - Self-Service
def selfServicePageLoadMyShiftSwapRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyShiftSwapRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_shift_swap_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_7')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_shift_swap_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_shift_swap_requests_tile)

        #my_shift_swap_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyShiftSwapRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)

            clickMyShiftSwapRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Locations - target function
def selfServicePageLoadMyLocationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyLocationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_location_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_14')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_location_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_location_tile)
        
        #my_location_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyLocationTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyLocationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Details - Self-Service
def selfServicePageLoadMyDetailsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyDetailsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_details_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_15')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_details_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_details_tile)

        #my_details_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyDetailsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyDetailsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Recent Messages - Self-Service
def selfServicePageLoadRecentMessagesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRecentMessagesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        recent_messages_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_16')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", recent_messages_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", recent_messages_tile)

        #recent_messages_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRecentMessagesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRecentMessagesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Leave Requests - Self-Service
def selfServicePageLoadMyLeaveRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyLeaveRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_leave_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_20')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_leave_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_leave_requests_tile)

        #my_leave_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyLeaveRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyLeaveRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My RotaOLD - Self-Service
def selfServicePageLoadMyRotaOldTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyRotaOldTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_rota_old_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_21')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_rota_old_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_rota_old_tile)

        #my_rota_old_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyRotaOldTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyRotaOldTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Travel Expenses - Self-Service
def selfServicePageLoadTravelExpensesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTravelExpensesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        travel_expenses_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_31')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", travel_expenses_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", travel_expenses_tile)
        
        #travel_expenses_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTravelExpensesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTravelExpensesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Shifts - Self-Service
def selfServicePageLoadAgencyShiftsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyShiftsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_shifts_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_55')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_shifts_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_shifts_tile)

        #agency_shifts_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyShiftsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyShiftsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Register Mobile - Self-Service
def selfServicePageLoadRegisterMobileTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRegisterMobileTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        register_mobile_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_71')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", register_mobile_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", register_mobile_tile)

        #register_mobile_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRegisterMobileTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRegisterMobileTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Fulfill - Self-Service
def selfServicePageLoadAgencyFulfillTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyFulfillTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_fulfill_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_72')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_fulfill_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_fulfill_tile)

        #agency_fulfill_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyFulfillTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyFulfillTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Annualised Hours - Self-Service
def selfServicePageLoadMyAnnualisedHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyAnnualisedHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_annualised_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_88')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_annualised_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_annualised_hours_tile)

        #my_annualised_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyAnnualisedHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyAnnualisedHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Casual Shift Requests - Self-Service
def selfServicePageLoadCasualShiftRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCasualShiftRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        casual_shift_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_95')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", casual_shift_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", casual_shift_requests_tile)

        #casual_shift_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCasualShiftRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCasualShiftRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Skills Expiry - Self-Service
def selfServicePageLoadMySkillsExpiryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMySkillsExpiryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_skills_expiry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_106')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_skills_expiry_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_skills_expiry_tile)

        #my_skills_expiry_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMySkillsExpiryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMySkillsExpiryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Login Shortcut - Self-Service
def selfServicePageLoadLoginShortcutTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLoginShortcutTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        login_shortcut_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_110')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", login_shortcut_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", login_shortcut_tile)

        #login_shortcut_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLoginShortcutTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLoginShortcutTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Document Upload - Self-Service
def selfServicePageLoadDocumentUploadTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDocumentUploadTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        document_upload_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_114')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", document_upload_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", document_upload_tile)
        
        #document_upload_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDocumentUploadTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDocumentUploadTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My SE Holiday Management - Self-Service
def selfServicePageLoadMySEHolidayManagementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMySEHolidayManagementTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_se_holiday_management_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_128')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_se_holiday_management_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_se_holiday_management_tile)

        #my_se_holiday_management_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMySEHolidayManagementTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMySEHolidayManagementTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Carry Forward Request - Self-Service
def selfServicePageLoadCarryForwardRequestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCarryForwardRequestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        carry_forward_request_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_167')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", carry_forward_request_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", carry_forward_request_tile)

        #carry_forward_request_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCarryForwardRequestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCarryForwardRequestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My SE Accrual Management - Self-Service
def selfServicePageLoadMySEAccrualManagementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMySEAccrualManagementTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_se_accrual_management_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_129')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_se_accrual_management_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_se_accrual_management_tile)

        #my_se_accrual_management_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMySEAccrualManagementTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMySEAccrualManagementTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My SE Unpaid Holiday Management - Self-Service
def selfServicePageLoadMySEUnpaidHolidayManagementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMySEUnpaidHolidayManagementTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_se_unpaid_holiday_management_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_130')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_se_unpaid_holiday_management_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_se_unpaid_holiday_management_tile)

        #my_se_unpaid_holiday_management_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMySEUnpaidHolidayManagementTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMySEUnpaidHolidayManagementTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Clockings - Self-Service
def selfServicePageLoadMyClockingsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyClockingsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_clockings_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_189')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_clockings_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_clockings_tile)

        #my_clockings_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyClockingsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyClockingsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Chat - Self-Service
def selfServicePageLoadChatTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickChatTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        chat_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_107')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", chat_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", chat_tile)

        #chat_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickChatTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickChatTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Team Rota - target function
def selfServicePageLoadMyTeamRotaTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyTeamRotaTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_team_rota_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_179')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_team_rota_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_team_rota_tile)
        
        #my_team_rota_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyTeamRotaTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyTeamRotaTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Availabilities - target function
def selfServicePageLoadMyAvailabilitiesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyAvailabilitiesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_availability_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_13')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_availability_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_availability_tile)
        
        #my_availability_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyAvailabilitiesTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyAvailabilitiesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My Absences - target function
def selfServicePageLoadMyAbsencesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyAbsencesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_89')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", esr_go_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", esr_go_import_tile)

        #esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyAbsencesTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyAbsencesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Carry Forward Requests - target function
def selfServicePageLoadCarryForwardRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_176')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", esr_go_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", esr_go_import_tile)

        esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadCarryForwardRequestsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Change Password - target function
def selfServicePageLoadChangePasswordTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadChangePasswordTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        esr_go_import_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_59')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", esr_go_import_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", esr_go_import_tile)

        #esr_go_import_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadChangePasswordTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadChangePasswordTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# My GDPR - target function
def selfServicePageLoadMyGDPRTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadMyGDPRTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        my_gdpr_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_123')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_gdpr_tile )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_gdpr_tile)
        
        #my_gdpr_tile .click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadMyGDPRTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadMyGDPRTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Email Opt Out - target function
def selfServicePageLoadEmailOptOutTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadEmailOptOutTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        email_opt_out_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_97')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", email_opt_out_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", email_opt_out_tile)
        
        #email_opt_out_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadEmailOptOutTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadSelfServiceMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadEmailOptOutTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

########################################## END OF SELF SERVICE TILES ###########################################

############################################# REPORTS TILES ####################################################

# Lane Usage - target function
def reportsPageLoadLaneUsageTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLaneUsageTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        lane_usage_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", lane_usage_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", lane_usage_tile)

        #lane_usage_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickLaneUsageTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLaneUsageTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Absence - target function
def reportsPageLoadAbsenceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_2')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_tile)

        #absence_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
        clickAbsenceTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Register - target function
def reportsPageLoadRegisterTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRegisterTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        register_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_3')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", register_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", register_tile)

        #register_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRegisterTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRegisterTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# SKILLS 2 - target function
def reportsPageLoadSkills2Tile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSkills2Tile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        skills2_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_4')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", skills2_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", skills2_tile)

        #skills2_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSkills2Tile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSkills2Tile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Messages - target function
def reportsPageLoadMessagesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMessagesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        messages_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_5')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", messages_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", messages_tile)

        #messages_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMessagesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMessagesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Payroll - target function
def reportsPageLoadPayrollTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPayrollTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        payroll_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_6')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", payroll_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", payroll_tile)
        
        #payroll_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPayrollTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPayrollTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Enhancements - target function
def reportsPageLoadEnhancementsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickEnhancementsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        enhancements_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_7')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", enhancements_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", enhancements_tile)

        #enhancements_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickEnhancementsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickEnhancementsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hours Report - target function
def reportsPageLoadHoursReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHoursReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hours_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_8')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hours_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hours_report_tile)

        #hours_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHoursReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHoursReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence - target function
def reportsPageLoadAbsence2Tile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAbsence2Tile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        absence2_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_9')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence2_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence2_tile)

        #absence2_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAbsence2Tile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAbsence2Tile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Clocking Attendance - target function
def reportsPageLoadClockingAttendanceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickClockingAttendanceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        clocking_attendance_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_10')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", clocking_attendance_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", clocking_attendance_tile)

        #clocking_attendance_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickClockingAttendanceTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickClockingAttendanceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Attendance - target function
def reportsPageLoadAttendanceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAttendanceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        attendance_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_11')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", attendance_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", attendance_tile)

        #attendance_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAttendanceTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAttendanceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Skills - target function
def reportsPageLoadSkillsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSkillsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        skills_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_12')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", skills_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", skills_tile)
        
        #skills_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSkillsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSkillsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shortfalls - target function
def reportsPageLoadShortfallsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickShortfallsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        shortfalls_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_13')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_tile)

        #shortfalls_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickShortfallsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickShortfallsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Contracted Hours - target function
def reportsPageLoadContractedHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickContractedHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        contracted_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_14')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", contracted_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", contracted_hours_tile)

        #contracted_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickContractedHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickContractedHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Staff Shortfalls - target function
def reportsPageLoadStaffShortfallsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffShortfallsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_shortfalls_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_15')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_shortfalls_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_shortfalls_tile)

        #staff_shortfalls_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffShortfallsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffShortfallsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Staff Clockings - target function
def reportsPageLoadStaffClockingsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffClockingsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_clockings_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_16')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_clockings_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_clockings_tile)

        #staff_clockings_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffClockingsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffClockingsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Rejected Leave - target function
def reportsPageLoadRejectedLeaveTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRejectedLeaveTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        rejected_leave_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_17')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", rejected_leave_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", rejected_leave_tile)

        #rejected_leave_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRejectedLeaveTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRejectedLeaveTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Yearly Planner - target function
def reportsPageLoadYearlyPlannerTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickYearlyPlannerTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        yearly_planner_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_18')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", yearly_planner_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", yearly_planner_tile)

        #yearly_planner_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickYearlyPlannerTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickYearlyPlannerTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Bradford Factor - target function
def reportsPageLoadBradfordFactorTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBradfordFactorTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bradford_factor_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_19')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bradford_factor_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  bradford_factor_tile)

        #bradford_factor_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBradfordFactorTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBradfordFactorTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hub Demand / Actual - target function
def reportsPageLoadHubDemandActualTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHubDemandActualTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hub_demand_actual_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_20')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hub_demand_actual_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hub_demand_actual_tile)

        #hub_demand_actual_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHubDemandActualTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHubDemandActualTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Hub Visibility - target function
def reportsPageLoadHubVisibilityTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHubVisibilityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        hub_visibility_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_21')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", hub_visibility_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", hub_visibility_tile)

        #hub_visibility_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHubVisibilityTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHubVisibilityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Section Transfers - target function
def reportsPageLoadSectionTransfersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSectionTransfersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        section_transfers_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_22')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", section_transfers_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", section_transfers_tile)

        #section_transfers_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSectionTransfersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSectionTransfersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Agency Onsite - target function
def reportsPageLoadAgencyOnsiteTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyOnsiteTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_onsite_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_23')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_onsite_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_onsite_tile)

        #agency_onsite_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyOnsiteTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyOnsiteTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Inactive Staff - target function
def reportsPageLoadInactiveStaffTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickInactiveStaffTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        inactive_staff_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_24')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", inactive_staff_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", inactive_staff_tile)

        #inactive_staff_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickInactiveStaffTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickInactiveStaffTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Agency Hours - target function
def reportsPageLoadAgencyHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_25')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_hours_tile)

        #agency_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Agency Approvals - target function
def reportsPageLoadAgencyApprovalsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyApprovalsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_approvals_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_26')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();",  agency_approvals_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  agency_approvals_tile)

        #agency_approvals_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyApprovalsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyApprovalsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Authorisation Requests - target function
def reportsPageLoadAuthorisationRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAuthorisationRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        auth_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_27')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", auth_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", auth_requests_tile)

        #auth_requests_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAuthorisationRequestsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAuthorisationRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Demand Quick Entry - target function
def reportsPageLoadDemandQuickEntryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDemandQuickEntryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        demand_quick_entry_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_28')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", demand_quick_entry_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", demand_quick_entry_tile)

        #demand_quick_entry_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDemandQuickEntryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDemandQuickEntryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Neuven Data Export - target function
def reportsPageLoadNeuvenDataExportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNeuvenDataExportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        neuven_data_export_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_29')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", neuven_data_export_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", neuven_data_export_tile)

        #neuven_data_export_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNeuvenDataExportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNeuvenDataExportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Clocking Override Buffer - target function
def reportsPageLoadClockingOverrideBufferTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickClockingOverrideBufferTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        clocking_override_buffer_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_30')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", clocking_override_buffer_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", clocking_override_buffer_tile)

        #clocking_override_buffer_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickClockingOverrideBufferTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickClockingOverrideBufferTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Daily Update Log - target function
def reportsPageLoadDailyUpdateLogTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDailyUpdateLogTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        daily_update_log_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_31')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", daily_update_log_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", daily_update_log_tile)

        #daily_update_log_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDailyUpdateLogTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDailyUpdateLogTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Holiday Slots - target function
def reportsPageLoadHolidaySlotsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickHolidaySlotsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        holiday_slots_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_32')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", holiday_slots_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", holiday_slots_tile)

        #holiday_slots_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickHolidaySlotsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickHolidaySlotsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Standby Report - target function
# Only user tile that is used within 'Reports'
def reportsPageLoadStandbyReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStandbyReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        standby_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_33')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", standby_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", standby_report_tile)

        #standby_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStandbyReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStandbyReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Viewed Rosters - target function
def reportsPageLoadViewedRostersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickViewedRostersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        viewed_rosters_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1032')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", viewed_rosters_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", viewed_rosters_tile)

        #viewed_rosters_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickViewedRostersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickViewedRostersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Day Roster - target function
def reportsPageLoadDayRosterTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDayRosterTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        day_roster_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1034')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", day_roster_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", day_roster_tile)

        #day_roster_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDayRosterTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDayRosterTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Self-Service Yearly Planner - target function
def reportsPageLoadSelfServiceYearlyPlannerTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSelfServiceYearlyPlannerTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        self_service_yearly_planner_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1035')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", self_service_yearly_planner_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", self_service_yearly_planner_tile)

        #self_service_yearly_planner_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSelfServiceYearlyPlannerTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSelfServiceYearlyPlannerTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# My Holiday Slots - target function
def reportsPageLoadMyHolidaySlotsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyHolidaySlotsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_holiday_slots_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1036')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_holiday_slots_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_holiday_slots_tile)

        #my_holiday_slots_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyHolidaySlotsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyHolidaySlotsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Crew Management - target function
def reportsPageLoadCrewManagementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCrewManagementTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        crew_management_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1037')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", crew_management_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", crew_management_tile)

        #crew_management_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCrewManagementTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCrewManagementTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Job List - target function
def reportsPageLoadJobListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickJobListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        job_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1038')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", job_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", job_list_tile)

        #job_list_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickJobListTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickJobListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Accrued Absence Hours - target function
def reportsPageLoadAccruedAbsenceHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAccruedAbsenceHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        accrued_absence_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1039')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", accrued_absence_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", accrued_absence_hours_tile)

        #accrued_absence_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAccruedAbsenceHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAccruedAbsenceHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# WTD Report - target function
def reportsPageLoadWTDReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWTDReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        wtd_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1040')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", wtd_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", wtd_report_tile)

        #wtd_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWTDReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWTDReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Employee Groups - target function
def reportsPageLoadEmployeeGroupsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickEmployeeGroupsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        employee_groups_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1041')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", employee_groups_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", employee_groups_tile)

        #employee_groups_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickEmployeeGroupsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickEmployeeGroupsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Crew Sailing List - target function
def reportsPageLoadCrewSailingListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCrewSailingListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        crew_sailing_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1042')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", crew_sailing_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", crew_sailing_list_tile)

        #crew_sailing_list_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCrewSailingListTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCrewSailingListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Last Working Shift - target function
def reportsPageLoadLastWorkingShiftTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLastWorkingShiftTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        last_working_shift_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1043')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", last_working_shift_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", last_working_shift_tile)

        #last_working_shift_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLastWorkingShiftTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLastWorkingShiftTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Did Not Attend - target function
def reportsPageLoadDidNotAttendTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDidNotAttendTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        did_not_attend_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1044')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", did_not_attend_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", did_not_attend_tile)

        did_not_attend_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDidNotAttendTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDidNotAttendTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Lieu vs Contracted - target function
def reportsPageLoadLieuVsContractedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickLieuVsContractedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        lieu_vs_contracted_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1045')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", lieu_vs_contracted_tile )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", lieu_vs_contracted_tile )

        #lieu_vs_contracted_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickLieuVsContractedTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickLieuVsContractedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# WTD - target function
def reportsPageLoadWTDTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWTDTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        wtd_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1046')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", wtd_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", wtd_tile)

        wtd_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWTDTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWTDTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Casual Holiday Accrual - target function
def reportsPageLoadCasualHolidayAccrualTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickCasualHolidayAccrualTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        casual_holiday_accrual_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1047')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", casual_holiday_accrual_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", casual_holiday_accrual_tile)

        #casual_holiday_accrual_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickCasualHolidayAccrualTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickCasualHolidayAccrualTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Activity Plans - target function
def reportsPageLoadActivityPlansTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickActivityPlansTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        activity_plans_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1048')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", activity_plans_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", activity_plans_tile)

        #activity_plans_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickActivityPlansTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickActivityPlansTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Agency Hours Summary - target function
def reportsPageLoadAgencyHoursSummaryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAgencyHoursSummaryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        agency_hours_summary_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1049')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", agency_hours_summary_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", agency_hours_summary_tile)

        #agency_hours_summary_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAgencyHoursSummaryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAgencyHoursSummaryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# WTD New - target function
def reportsPageLoadWTDNewTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWTDNewTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        wtd_new_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1051')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", wtd_new_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", wtd_new_tile)

        #wtd_new_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWTDNewTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWTDNewTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Column Picker Test - target function
def reportsPageLoadColumnPickerTestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickColumnPickerTestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        column_picker_test_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1052')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", column_picker_test_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", column_picker_test_tile)

        #column_picker_test_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickColumnPickerTestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickColumnPickerTestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Self Service Activity - target function
def reportsPageLoadSelfServiceActivityTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSelfServiceActivityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        self_service_activity_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1053')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", self_service_activity_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", self_service_activity_tile)

        #self_service_activity_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSelfServiceActivityTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSelfServiceActivityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Kaba Clocking Report - target function
def reportsPageLoadKabaClockingReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickKabaClockingReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        kaba_clocking_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1054')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();",  kaba_clocking_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();",  kaba_clocking_report_tile)
        
        #kaba_clocking_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickKabaClockingReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickKabaClockingReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Bonuses - target function
def reportsPageLoadBonusesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBonusesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bonuses_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1058')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bonuses_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bonuses_tile)

        #bonuses_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBonusesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBonusesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Deductions - target function
def reportsPageLoadDeductionsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDeductionsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        deductions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1059')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", deductions_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", deductions_tile)

        #deductions_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDeductionsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDeductionsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Staff Feedback - target function
def reportsPageLoadStaffFeedbackTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffFeedbackTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_feedback_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1060')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_feedback_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_feedback_tile)

        #staff_feedback_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffFeedbackTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffFeedbackTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Work Undertaken - target function
def reportsPageLoadWorkUndertakenTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWorkUndertakenTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        work_undertaken_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1061')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", work_undertaken_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", work_undertaken_tile)

        #work_undertaken_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWorkUndertakenTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWorkUndertakenTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# New Work Added - target function
def reportsPageLoadNewWorkAddedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNewWorkAddedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        new_work_added_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1062')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", new_work_added_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", new_work_added_tile)

        #new_work_added_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNewWorkAddedTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNewWorkAddedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Billable Hours Data Dump - target function
def reportsPageLoadBillableHoursDataDumpTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBillableHoursDataDumpTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        billable_hours_data_dump_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1063')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", billable_hours_data_dump_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", billable_hours_data_dump_tile)

        #billable_hours_data_dump_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBillableHoursDataDumpTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBillableHoursDataDumpTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Drivers Feeder List - target function
def reportsPageLoadDriversFeederListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDriversFeederListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        drivers_feeder_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1064')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", drivers_feeder_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", drivers_feeder_list_tile)

        #drivers_feeder_list_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDriversFeederListTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDriversFeederListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Drivers Coach Passengers List - target function
def reportsPageLoadDriversCoachPassengersListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDriversCoachPassengersListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        drivers_coach_passengers_list_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1065')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", drivers_coach_passengers_list_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", drivers_coach_passengers_list_tile)

        #drivers_coach_passengers_list_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDriversCoachPassengersListTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDriversCoachPassengersListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Drivers Returns Departures Analysis - target function
def reportsPageLoadDriversReturnsDeparturesAnalysisTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDriversReturnsDeparturesAnalysisTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        drivers_returns_departures_analysis_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1066')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", drivers_returns_departures_analysis_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", drivers_returns_departures_analysis_tile)

        #drivers_returns_departures_analysis_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDriversReturnsDeparturesAnalysisTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDriversReturnsDeparturesAnalysisTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Drivers Events Changes - target function
def reportsPageLoadDriversEventsChangesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDriversEventsChangesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        drivers_events_changes_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1067')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", drivers_events_changes_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", drivers_events_changes_tile)

        #drivers_events_changes_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDriversEventsChangesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDriversEventsChangesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Employee Calculations - target function
def reportsPageLoadEmployeeCalculationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickEmployeeCalculationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        employee_calculations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1068')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", employee_calculations_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", employee_calculations_tile)

        #employee_calculations_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickEmployeeCalculationsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickEmployeeCalculationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Team Calculations - target function
def reportsPageLoadTeamCalculationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTeamCalculationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        team_calculations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1069')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", team_calculations_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", team_calculations_tile)

        #team_calculations_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTeamCalculationsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTeamCalculationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Weekly Hours - target function
def reportsPageLoadWeeklyHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWeeklyHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        weekly_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1070')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", weekly_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", weekly_hours_tile)

        #weekly_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWeeklyHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWeeklyHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Extra Duties - target function
def reportsPageLoadExtraDutiesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickExtraDutiesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        extra_duties_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1071')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", extra_duties_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", extra_duties_tile)

        #extra_duties_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickExtraDutiesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickExtraDutiesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Double Sessions - target function
def reportsPageLoadDoubleSessionsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDoubleSessionsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        double_sessions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1072')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", double_sessions_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", double_sessions_tile)

        #double_sessions_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDoubleSessionsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDoubleSessionsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Pay Return - target function
def reportsPageLoadPayReturnTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPayReturnTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        pay_return_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1073')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", pay_return_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", pay_return_tile)

        #pay_return_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPayReturnTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPayReturnTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# My Calculations - target function
def reportsPageLoadMyCalculationsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMyCalculationsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        my_calculations_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1074')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", my_calculations_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", my_calculations_tile)

        #my_calculations_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMyCalculationsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMyCalculationsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# New Starters - target function
def reportsPageLoadNewStartersTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickNewStartersTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        new_starters_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1075')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", new_starters_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", new_starters_tile)

        #new_starters_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickNewStartersTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickNewStartersTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Research and Development - target function
def reportsPageLoadResearchDevTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickResearchDevTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        research_dev_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1077')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", research_dev_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", research_dev_tile)

        #research_dev_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickResearchDevTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickResearchDevTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank Staff Usage - target function
def reportsPageLoadBankStaffUsageTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBankStaffUsageTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bank_staff_usage_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1078')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bank_staff_usage_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bank_staff_usage_tile)

        #bank_staff_usage_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBankStaffUsageTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBankStaffUsageTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Bank Staff Utilisation - target function
def reportsPageLoadBankStaffUtilisationTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBankStaffUtilisationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        bank_staff_utilisation_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1079')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bank_staff_utilisation_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bank_staff_utilisation_tile)

        #bank_staff_utilisation_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBankStaffUtilisationTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBankStaffUtilisationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Extra Sessions Reasons - target function
def reportsPageLoadExtraSessionsReasonsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickExtraSessionsReasonsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        extra_sessions_reasons_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1080')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", extra_sessions_reasons_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", extra_sessions_reasons_tile)

        #extra_sessions_reasons_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickExtraSessionsReasonsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickExtraSessionsReasonsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Interface Changes following Payroll Submission - target function
def reportsPageLoadInterfaceChangesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickInterfaceChangesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        interface_changes_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1081')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", interface_changes_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", interface_changes_tile)

        #interface_changes_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickInterfaceChangesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickInterfaceChangesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Chart Test - target function
def reportsPageLoadChartTestTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickChartTestTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        chart_test_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1083')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", chart_test_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", chart_test_tile)

        #chart_test_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickChartTestTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickChartTestTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Project Work Audit - target function
def reportsPageLoadProjectWorkAuditTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickProjectWorkAuditTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        project_work_audit_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1087')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", project_work_audit_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", project_work_audit_tile)

        #project_work_audit_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickProjectWorkAuditTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickProjectWorkAuditTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Active/Completed Project Graphs - target function
def reportsPageLoadActiveCompletedProjectsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickActiveCompletedProjectsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        active_completed_projects_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1088')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", active_completed_projects_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", active_completed_projects_tile)

        #active_completed_projects_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickActiveCompletedProjectsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickActiveCompletedProjectsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Billable Hours - target function
def reportsPageLoadBillableHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBillableHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        billable_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1089')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", billable_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", billable_hours_tile)

        #billable_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBillableHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBillableHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Billable Hours Breakdown - target function
def reportsPageLoadBillableHoursBreakdownTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBillableHoursBreakdownTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        billable_hours_breakdown_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1090')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", billable_hours_breakdown_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", billable_hours_breakdown_tile)

        #billable_hours_breakdown_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBillableHoursBreakdownTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBillableHoursBreakdownTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Spent Time - target function
def reportsPageLoadSpentTimeTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSpentTimeTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        spent_time_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1091')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", spent_time_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", spent_time_tile)

        #spent_time_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSpentTimeTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSpentTimeTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Accrued Days - target function
def reportsPageLoadAccruedDaysTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAccruedDaysTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        accrued_days_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1092')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", accrued_days_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", accrued_days_tile)

        #accrued_days_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAccruedDaysTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAccruedDaysTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Previous Sessions Report for Adjustments - target function
def reportsPageLoadPrevSessionsReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPrevSessionsReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        prev_sessions_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1093')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", prev_sessions_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", prev_sessions_report_tile)

        #prev_sessions_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPrevSessionsReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPrevSessionsReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Support Portal Category - target function
def reportsPageLoadSupportPortalCategoryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSupportPortalCategoryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        support_portal_category_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1094')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", support_portal_category_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", support_portal_category_tile)

        #support_portal_category_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSupportPortalCategoryTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSupportPortalCategoryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Billed Days - target function
def reportsPageLoadBilledDaysTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickBilledDaysTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        billed_days_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1095')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", billed_days_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", billed_days_tile)

        #billed_days_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickBilledDaysTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickBilledDaysTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Month View - target function
def reportsPageLoadMonthViewTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMonthViewTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        month_view_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1096')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", month_view_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", month_view_tile)
        
        #month_view_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMonthViewTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMonthViewTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# P&O Payroll Absence Export - target function
def reportsPageLoadPOPayrollAbsenceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPOPayrollAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        po_payroll_absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1098')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", po_payroll_absence_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", po_payroll_absence_tile)

        #po_payroll_absence_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPOPayrollAbsenceTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPOPayrollAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# The Liar - target function
def reportsPageLoadTheLiarTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTheLiarTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        the_liar_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1099')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", the_liar_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", the_liar_tile)

        #the_liar_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTheLiarTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTheLiarTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Staff working sessions outside their home team - target function
def reportsPageLoadStaffSessionsOutsideHomeTeamTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStaffSessionsOutsideHomeTeamTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        staff_sessions_outside_home_team_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1100')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staff_sessions_outside_home_team_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staff_sessions_outside_home_team_tile)

        #staff_sessions_outside_home_team_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStaffSessionsOutsideHomeTeamTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStaffSessionsOutsideHomeTeamTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Unsubmitted Sessions - target function
def reportsPageLoadUnsubmittedSessionsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickUnsubmittedSessionsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        unsubmitted_sessions_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1101')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", unsubmitted_sessions_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", unsubmitted_sessions_tile)

        #unsubmitted_sessions_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickUnsubmittedSessionsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickUnsubmittedSessionsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence - target function
def reportsPageLoadAbsenceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1102')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_tile)

        #absence_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAbsenceTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sickness - target function
def reportsPageLoadSicknessTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSicknessTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        sickness_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1103')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sickness_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", sickness_tile)

        #sickness_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSicknessTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSicknessTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Chairman's Report - target function
def reportsPageLoadChairmanReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickChairmanReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        chairman_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1104')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", chairman_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", chairman_report_tile)

        #chairman_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickChairmanReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickChairmanReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Jacicntha Testing Chart Functionality - target function
def reportsPageLoadJacicnthaChartFunctionalityTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickJacicnthaChartFunctionalityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        jacicntha_chart_functionality_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1105')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", jacicntha_chart_functionality_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", jacicntha_chart_functionality_tile)

        #jacicntha_chart_functionality_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickJacicnthaChartFunctionalityTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickJacicnthaChartFunctionalityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Stats - target function
def reportsPageLoadStatsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickStatsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        stats_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1106')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", stats_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", stats_tile)

        #stats_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickStatsTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickStatsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Multi-post - target function
def reportsPageLoadMultiPostTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickMultiPostTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        multi_post_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1107')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", multi_post_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", multi_post_tile)

        #multi_post_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickMultiPostTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickMultiPostTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Weekly Hours - target function
def reportsPageLoadWeeklyHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWeeklyHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        weekly_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1108')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", weekly_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", weekly_hours_tile)

        #weekly_hours_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWeeklyHoursTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWeeklyHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Surveyor Work Breakdown - target function
def reportsPageLoadSurveyorWorkBreakdownTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSurveyorWorkBreakdownTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        surveyor_work_breakdown_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1109')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", surveyor_work_breakdown_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", surveyor_work_breakdown_tile)

        #surveyor_work_breakdown_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSurveyorWorkBreakdownTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSurveyorWorkBreakdownTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Work and Absence Approval/Rejection Breakdown - target function
def reportsPageLoadWorkAbsenceApprovalRejectionBreakdownTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickWorkAbsenceApprovalRejectionBreakdownTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        work_absence_approval_rejection_breakdown_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1110')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", work_absence_approval_rejection_breakdown_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", work_absence_approval_rejection_breakdown_tile)

        #work_absence_approval_rejection_breakdown_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickWorkAbsenceApprovalRejectionBreakdownTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickWorkAbsenceApprovalRejectionBreakdownTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Delegation Report - target function
def reportsPageLoadDelegationReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDelegationReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        delegation_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1111')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", delegation_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", delegation_report_tile)

        #delegation_report_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDelegationReportTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDelegationReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Timesheet Changes - target function
def reportsPageLoadTimesheetChangesTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickTimesheetChangesTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        timesheet_changes_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1112')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", timesheet_changes_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", timesheet_changes_tile)

        #timesheet_changes_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickTimesheetChangesTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickTimesheetChangesTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sickness Trigger Point - target function
def reportsPageLoadSicknessTriggerPointTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickSicknessTriggerPointTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        sickness_trigger_point_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1113')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sickness_trigger_point_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", sickness_trigger_point_tile)

        #sickness_trigger_point_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickSicknessTriggerPointTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickSicknessTriggerPointTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Attendance Info - target function
def reportsPageLoadAttendanceInfoTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickAttendanceInfoTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
        
        attendance_info_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1114')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", attendance_info_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", attendance_info_tile)

        #attendance_info_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickAttendanceInfoTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickAttendanceInfoTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Day Allocation - target function
def reportsPageLoadDayAllocationTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickDayAllocationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        day_allocation_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1115')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", day_allocation_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", day_allocation_tile)

        #day_allocation_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickDayAllocationTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickDayAllocationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Role Allocation - target function
def reportsPageLoadRoleAllocationTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickRoleAllocationTile(driver_response):
        wait = WebDriverWait(driver_response, 10)

        role_allocation_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_REPORT_1116')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", role_allocation_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", role_allocation_tile)

        #role_allocation_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickRoleAllocationTile(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadReportsMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickRoleAllocationTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

################################################# END OF REPORTS TILES ######################################################

############################################## DASHBOARD REPORTS TILES ######################################################

# Session Working Unavailability Breakdown - target fucntion
def dashboardReportsSessionUnavailablityTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSessionUnavailablityTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_unavailablity_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_9')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", session_unavailablity_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", session_unavailablity_tile)
        
        #session_unavailablity_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionUnavailablityTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSessionUnavailablityTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Shortfalls - Target function 
def dashboardReportsShortfallsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadShortfallsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        shortfalls_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_2')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_tile)
        
        #shortfalls_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadShortfallsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadShortfallsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Bank Hours Paid - Target function 
def dashboardReportsBankHoursPaidTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadBankHoursPaidTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        bank_hours_paid_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_3')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", bank_hours_paid_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", bank_hours_paid_tile)
        
        #bank_hours_paid_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadBankHoursPaidTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadBankHoursPaidTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Session Staffing Planned Above and Below BD Staffing Model (Non-Nurses) - Target function 
def dashboardReportsStaffingModelTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadStaffingModelTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        staffing_model_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_8')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", staffing_model_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", staffing_model_tile)
        
        #staffing_model_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadStaffingModelTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadStaffingModelTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sessions Operated with Shortfall or Surplus - Target function 
def dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        operated_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_7')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", operated_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", operated_tile)
        
        #operated_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSeshOperateddWithSeshShortfallTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Sessions Expected Vs Sessions Planned - Target function 
def dashboardReportsSeshExpectedVSSeshPlannedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        expected_vs_planned_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_6')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", expected_vs_planned_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", expected_vs_planned_tile)

        #expected_vs_planned_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSeshExpectedVSSeshPlannedTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Skills - Target function 
def dashboardReportsSkillsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSkillsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        skills_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_1')))
        
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", skills_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", skills_tile)

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSkillsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSkillsTile(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sickness Paid - target function 
def dashboardReportSicknessPaidTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadtSicknessPaidTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        sickness_paid_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_5')))
        
        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sickness_paid_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", sickness_paid_tile)

        #sickness_paid_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadtSicknessPaidTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadtSicknessPaidTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Absence Reason Breakdown - target function 
def dashboardReportAbsenceReasonBreakDownTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAbsenceReasonBreakdownTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_reason_brkdown_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_4')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_reason_brkdown_tile )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_reason_brkdown_tile )
        
        #absence_reason_brkdown_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAbsenceReasonBreakdownTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAbsenceReasonBreakdownTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


#Test Absence Droplists - target function 
def dashboardReportTestAbsenceDropListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadTestAbsenceDropListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        test_absence_droplist_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_15')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", test_absence_droplist_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", test_absence_droplist_tile)
        
        #test_absence_droplist_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadTestAbsenceDropListTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadTestAbsenceDropListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave booked by Day  - target function 
def dashboardReportAnnualLeaveBookByDayTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAnnualLeaveBookByDayTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_book_by_day_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_39')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_book_by_day_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_book_by_day_tile)
        
        #annual_leave_book_by_day_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAnnualLeaveBookByDayTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAnnualLeaveBookByDayTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Annual Leave Booked vgs. Allowance - target function 
def dashboardReportAnnualLeaveBookVsAllowanceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_book_vs_allow_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_40')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_book_vs_allow_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_book_vs_allow_tile)
        
        #annual_leave_book_vs_allow_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAnnualLeaveBookVsAllowanceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Employee Annual Leave Allowance vs. Booked - target function 
def dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        annual_leave_allow_vs_booked_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_41')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", annual_leave_allow_vs_booked_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", annual_leave_allow_vs_booked_tile)
        
        #annual_leave_allow_vs_booked_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadEmployeeAnnualLeaveAllowanceVsBookedeTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Session Overrun Reasons - target function 
def dashboardReportSessionOverrunReasonsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSessionOverrunReasonsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_overrun_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_43')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", session_overrun_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", session_overrun_tile)
        
        #session_overrun_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionOverrunReasonsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSessionOverrunReasonsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# To Note* - One off case where a usertile i.e. 'HOMEPAGE_?' Tag is used within Dashboards report 
# Dashboard Export Multi to PDF - target function 
def dashboardReportExportMultiToPDFTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadExportMultiToPDFTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        session_overrun_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_183')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", session_overrun_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", session_overrun_tile)
        
        #session_overrun_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadExportMultiToPDFTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadExportMultiToPDFTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Shortfalls Report - target function 
def dashboardReportShortfallsReportTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadShortfallsReportTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        shortfalls_report_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_16')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", shortfalls_report_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", shortfalls_report_tile)
        
        #shortfalls_report_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadShortfallsReportTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadShortfallsReportTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Rejected Leave - target function
def dashboardReportRejectedLeaveTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadRejectedLeaveTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        rejected_leave_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_17')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", rejected_leave_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", rejected_leave_tile)
        
        #rejected_leave_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadRejectedLeaveTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadRejectedLeaveTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Contracted Hours -target function
def dashboardReportContractedHoursTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadContractedHoursTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        contracted_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_18')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", contracted_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", contracted_hours_tile)
        
        contracted_hours_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadContractedHoursTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadContractedHoursTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)

# Skills - List - Target Function 
def dashboardReportSkillsListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSkillsListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        contracted_hours_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_19')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", contracted_hours_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", contracted_hours_tile)
        
        #contracted_hours_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSkillsListTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSkillsListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Skills Summary - Target Function 
def dashboardReportSkillsSummaryTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSkillsSummaryTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        skills_summary_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_20')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", skills_summary_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", skills_summary_tile)
        
        #skills_summary_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSkillsSummaryTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSkillsSummaryTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Test LeavePeriod Droplist - Target Function 
def dashboardReportTestLeavePeriodDropListTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadTestLeavePeriodDropListTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        test_leave_period_droplist_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_32')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", test_leave_period_droplist_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", test_leave_period_droplist_tile)
        
        #test_leave_period_droplist_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadTestLeavePeriodDropListTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadTestLeavePeriodDropListTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence - Target Function 
def dashboardReportAbsenceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAbsenceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_33')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_tile)
        
        #absence_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAbsenceTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAbsenceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Absence Allowance - Target Function 
def dashboardReportAbsenceAllowanceTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAbsenceAllowanceTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        absence_allowance_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_34')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", absence_allowance_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", absence_allowance_tile)
        
        #absence_allowance_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAbsenceAllowanceTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAbsenceAllowanceTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Carry Forward Requests - Target Function 
def dashboardReportCarryForwardRequestsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadCarryForwardRequestsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        carry_forward_requests_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_35')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", carry_forward_requests_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", carry_forward_requests_tile)
        
        #carry_forward_requests_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadCarryForwardRequestsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadCarryForwardRequestsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Clocking Reports - Target Function 
def dashboardReportClockingReportsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadClockingReportsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        clocking_reports_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_36')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", clocking_reports_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", clocking_reports_tile)
        
        #clocking_reports_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadClockingReportsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadClockingReportsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)



# Holiday Slots - Target Function 
def dashboardReportHolidaySlotsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadHolidaySlotsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        holiday_slots_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_37')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", holiday_slots_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", holiday_slots_tile)
        
        #holiday_slots_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadHolidaySlotsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadHolidaySlotsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Sessions Planned with Shortfall or Surplus - target function
def dashboardReportSessionsPlannedWithShortfallOrSurplusTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadSessionsPlannedWithShortfallOrSurplusTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        sesh_plan_shrt_sur_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_DASHBOARDREPORT_38')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", sesh_plan_shrt_sur_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", sesh_plan_shrt_sur_tile)
        
        #sesh_plan_shrt_sur_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadSessionsPlannedWithShortfallOrSurplusTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadReportsDashboardMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadSessionsPlannedWithShortfallOrSurplusTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
############################################## END OF DASHBOARD REPORTS TILES ################################################

#########################################################  ABOUT TILES #############################################################

# Date &amp; Time - target function
def aboutDateandampTimeTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadDateAndampTimeTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        date_and_amp_time_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_2')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", date_and_amp_time_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", date_and_amp_time_tile)
        
        #date_and_amp_time_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadDateAndampTimeTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadDateAndampTimeTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# About Us - target function
def aboutAboutUsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadAboutUsTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        about_us_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_11')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", about_us_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", about_us_tile)
        
        #about_us_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadAboutUsTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadAboutUsTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Logo - target function
def aboutLogoTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadLogoTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        logo_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_18')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", logo_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", logo_tile)
        
        #logo_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadLogoTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadLogoTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Current Users Logged In
def aboutCurrentUsersLoggedInTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):

    
    def clickPageLoadCurrentUsersLoggedInTile(driver_response):
        wait = WebDriverWait(driver_response, 10)
          
        current_usrs_logged_in_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_23')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", current_usrs_logged_in_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", current_usrs_logged_in_tile)
        
        #current_usrs_logged_in_tile.click()

    if driver_response is None: 
        driver_response = fdi.initialize_driver(headless_mode)
    else: 
        pass

    if optional_error_catch is not None:
       clickPageLoadCurrentUsersLoggedInTile(driver_response)    
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)

            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            
            clickPageLoadCurrentUsersLoggedInTile(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Logout
def aboutLogoutTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPageLoadItem(driver_response):
        wait = WebDriverWait(driver_response, 10)

        logout_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_25')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", logout_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", logout_tile)
        
        #logout_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPageLoadItem(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadItem(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# GDPR Terms and Conditions
def aboutGDPRTermsTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPageLoadItem(driver_response):
        wait = WebDriverWait(driver_response, 10)

        gdpr_terms_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_124')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", gdpr_terms_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", gdpr_terms_tile)
        
        #gdpr_terms_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPageLoadItem(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadItem(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Privacy Statement
def aboutPrivacyStatementTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPageLoadItem(driver_response):
        wait = WebDriverWait(driver_response, 10)

        privacy_statement_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_125')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", privacy_statement_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", privacy_statement_tile)

        #privacy_statement_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPageLoadItem(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadItem(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Full Screen
def aboutFullScreenTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPageLoadItem(driver_response):
        wait = WebDriverWait(driver_response, 10)

        full_screen_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_195')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", full_screen_tile )

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", full_screen_tile )

        #full_screen_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPageLoadItem(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadItem(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


# Exit Full Screen
def aboutExitFullScreenTile(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
    def clickPageLoadItem(driver_response):
        wait = WebDriverWait(driver_response, 10)

        exit_full_screen_tile = wait.until(EC.element_to_be_clickable((By.ID, 'HOMEPAGE_196')))

        # Scroll the element into view if needed
        driver_response.execute_script("arguments[0].scrollIntoView();", exit_full_screen_tile)

        # Click the element using execute_script directly
        driver_response.execute_script("arguments[0].click();", exit_full_screen_tile)

        #exit_full_screen_tile.click()

    if driver_response is None:
        driver_response = fdi.initialize_driver(headless_mode)
    else:
        pass

    if optional_error_catch is not None:
        clickPageLoadItem(driver_response)
    else:
        try:
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
            mi.homePageLoadAboutMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
            clickPageLoadItem(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e:
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


####################################################### END OF ABOUT TILES #############################################################
########################################### USER ROLE CHECKER FOR BATCH PROCESS TESTS #########################################
def checkUserRoleAndSwitch(driver_response, target_sys, user_type):
    
    drop_list_xpath = '/html/body/section/div[2]/div/div[1]/select' # Indexing remains consistant across systems for class="switchroleDropList" <select> element.
   
    # Can customise usertype configuration accordingly - in most cases, we'll only ever need to test root level usertypes/locations.
    desired_user_type = {
        "": {
                '{Place Name of usertype here as displayed front end}': f"{drop_list_xpath}/option[text()='{Place Name of usertype here as displayed front end}']"
        }
    }    
      
    # Wait for the page to load (you may need to adjust the wait time)
    WebDriverWait(driver_response, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'select')))

    # Find the <select> element with class "switchroleDropList"
    select_element = driver_response.find_element(By.CLASS_NAME, 'switchroleDropList')

    # Get the text of the selected option
    selected_option = select_element.find_element(By.CSS_SELECTOR, 'option:checked')
    
    user_role = selected_option.text.strip()

    print(user_role)

    
    try: 
        # will need to change so that shortened usertype in excel sheet is equal to the text in user role i.e. 
        # create a list of usertypes as shown in the bnbrwoser thhat match with the shortend versions i.e. 
        #usertype_list_excel_accom = { 
        #    Administrator (NHSBT): System Administrator - Corporate
        #}

        # if user_role == usertype_list_excel_accom[usertype]
        # pass

        if target_sys in desired_user_type: 
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
    except: 
        print(f"User type doesn't exist for current system: {target_sys}")
        return False
    
###################################################################################################################################################################

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
homePageLoadAbsenceSummaryTile.tag = ["HOME", "HOME Tile - Absence Summary"] # HOMEPAGE_203
homePageLoadNextAbsenceTile.tag = ["HOME", "HOME Tile - Next Absence"] # HOMEPAGE_204
homePageLoadNextShiftTile.tag = ["HOME", "HOME Tile - Next Shift"] # HOMEPAGE_34
#mi.homePageLoadAdminMenuItem.tag = [] # HOMEPAGE_200 - not used in a conventional sense

# Tags for functions in the ADMIN section
# Special case where admin menu item has a tag asscoiated with it i.e. HOMEPAGE_200 
# Just doesn't need to be checked 
# Doesn't require this check unless stated otherwise  

# Tags for functions in the MANAGEMENT section

managmentPageLoadSkillsExpiryTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Skills Expiry"] #HOMEPAGE_5
managmentPageLoadClockingsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Clockings"] #HOMEPAGE_17
managmentPageLoadAbsenceRequestsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Absence Requests"] #HOMEPAGE_19
managmentPageLoadAdminOldTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Admin Old"] #HOMEPAGE_22
managmentPageLoadRotaTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Rota"] #HOMEPAGE_26
managmentPageLoadRotaChangesTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Rota Changes"] #HOMEPAGE_29
managmentPageLoadExceptionsReportTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Exceptions Report"] #HOMEPAGE_32
managmentPageLoadLateStaffTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Late Staff"] #HOMEPAGE_35
managmentPageLoadShortfallsAllocateTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Shortfalls Allocate"] #HOMEPAGE_36
managmentPageLoadMissedCheckCallsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Missed Check Calls"] #HOMEPAGE_37
managmentPageLoadRefresherTrainingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Refresher Training"] #HOMEPAGE_38
managmentPageLoadNoResponseUnconfirmedTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - No Response Unconfirmed"] #HOMEPAGE_39
managmentPageLoadShortfallsOfferTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Shortfalls Offer"] #HOMEPAGE_41
managmentPageLoadPostponedTrainingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Postponed Training"] #HOMEPAGE_45
managmentPageLoadFailedCheckCallsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Failed Check Calls"] #HOMEPAGE_48
managmentPageLoadTimesheetsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Timesheets"] #HOMEPAGE_56
managmentPageLoadImportRotaDataTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Import Rota Data"] #HOMEPAGE_57
managmentPageLoadPayrollSubmissionTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Payroll Submission"] #HOMEPAGE_60
managmentPageLoadClockingsByPersonTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Clockings By Person"] #HOMEPAGE_61
managmentPageLoadDataTransferFailuresTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Data Transfer Failures"] #HOMEPAGE_62
managmentPageLoadMissedTasksTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Missed Tasks"] #HOMEPAGE_63
managmentPageLoadManagerWorkPlanTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Manager Work Plan"] #HOMEPAGE_65
managmentPageLoadAdminMessageBoardTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Admin Message Board"] #HOMEPAGE_68
managmentPageLoadUnrecognizedMessagesTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Unrecognized Messages"] #HOMEPAGE_69
managmentPageLoadNHSBTImportTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - NHSBT Import"] #HOMEPAGE_70
managementPageLoadHubDemandTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hub Demand"] #HOMEPAGE_73
managmentPageLoadNHSBTQuickEntryTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - NHSBT Quick Entry"] #HOMEPAGE_74
managmentPageLoadAgencyQuickAdminTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Agency Quick Admin"] #HOMEPAGE_75
managmentPageLoadSectionTransfersTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Section Transfers"] #HOMEPAGE_76
managmentPageLoadHubStatusTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hub Status"] #HOMEPAGE_80
managmentPageLoadHubVisibilityTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hub Visibility"] #HOMEPAGE_81
managmentPageLoadStaffQuickAdminTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Staff Quick Admin"] #HOMEPAGE_83
managmentPageLoadShiftSwapRequestsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Shift Swap Requests"] #HOMEPAGE_86
managmentPageLoadScenariosUploadTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Scenarios Upload"] #HOMEPAGE_93
managmentPageLoadGenerateLogBookNumbersTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Generate Log Book Numbers"] #HOMEPAGE_94
managmentPageLoadTrainingOverdueTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Training Overdue"] #HOMEPAGE_98
managmentPageLoad12HourUnfilledCasualsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - 12-Hour Unfilled Casuals"] #HOMEPAGE_99
managmentPageLoadWorkPlanReportTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Work Plan Report"] #HOMEPAGE_103
managmentPageLoadMusterListTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Muster List"] #HOMEPAGE_105
managmentPageLoadBulkPatternRenewalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Bulk Pattern Renewal"] #HOMEPAGE_109
managmentPageLoadSimulateUsersTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Simulate Users"] #HOMEPAGE_111
managmentPageLoadApplicantsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Applicants"] #HOMEPAGE_112
managmentPageLoadTrainingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Training"] #HOMEPAGE_113
managmentPageLoadDocumentApprovalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Document Approval"] #HOMEPAGE_115
managmentPageLoadCMCallBacksTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - CM Call Backs"] #HOMEPAGE_116
managmentPageLoadDetailsApprovalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Details Approval"] #HOMEPAGE_117
managmentPageLoadMVLieuTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - MV Lieu"] #HOMEPAGE_118
managmentPageLoadSwedishDerogationTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Swedish Derogation"] #HOMEPAGE_119
managmentPageLoadMyCMCallBacksTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - My CM Call Backs"] #HOMEPAGE_120
managmentPageLoadPlacementConfirmationsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Placement Confirmations"] #HOMEPAGE_121
managmentPageLoadSEHolidayTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - SE Holiday"] #HOMEPAGE_122
managmentPageLoadSEAccruedTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - SE Accrued"] #HOMEPAGE_126
managmentPageLoadSEUnpaidHolidayTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - SE Unpaid Holiday"] #HOMEPAGE_127
managmentPageLoadStaffFeedbackTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Staff Feedback"] #HOMEPAGE_131
managmentPageLoadLieuMgmtHoursTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Lieu Mgmt Hours"] #HOMEPAGE_134
managmentPageLoadLieuMgmtDaysTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Lieu Mgmt Days"] #HOMEPAGE_135
managmentPageLoadWageAmendmentsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Wage Amendments"] #HOMEPAGE_136
managmentPageLoadBillingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Billing"] #HOMEPAGE_140
managmentPageLoadTestSplitDropListPageTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Test Split Drop List Page"] #HOMEPAGE_141
managmentPageLoadInterchangeScreensTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Interchange Screens"] #HOMEPAGE_142
managmentPageLoadSupportPortalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Support Portal"] #HOMEPAGE_143
managmentPageLoadRotaTile2.tag = ["MANAGEMENT", "MANAGEMENT Tile - Rota"] #HOMEPAGE_145
managmentPageLoadScheduleTimesheetsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Schedule Timesheets"] #HOMEPAGE_146
managmentPageLoadCheckSingleTeamCalculationTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Check Single Team Calculation"] #HOMEPAGE_147
managmentPageLoadSubmitAllTimesheetsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Submit All Timesheets"] #HOMEPAGE_149
managmentPageLoadNHSBTImportTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - NHSBT Import"] #HOMEPAGE_150
managmentPageLoadNHSBTQuickEntryTile2.tag = ["MANAGEMENT", "MANAGEMENT Tile - NHSBT Quick Entry"] #HOMEPAGE_151
managmentPageLoadDownloadESRFilesTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Download ESR Files"] #HOMEPAGE_153
managmentPageLoadTimesheetRunsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Timesheet Runs"] #HOMEPAGE_161
managmentPageLoadAnnualLeaveAdjustmentsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Annual Leave Adjustments"] #HOMEPAGE_163
managmentPageLoadDaysAccrualTestingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Days Accrual Testing"] #HOMEPAGE_164
managmentPageLoadHoursAccrualTestingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hours Accrual Testing"] #HOMEPAGE_165
managmentPageLoadCarryForwardRequestsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Carry Forward Requests"] #HOMEPAGE_168
managmentPageLoadYearAnnualLeaveAdjustmentsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Year Annual Leave Adjustments"] #HOMEPAGE_169
managmentPageLoadHolsHMgmtHoursTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hols H Mgmt Hours"] #HOMEPAGE_173
managmentPageLoadHolsDMgmtDaysTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Hols D Mgmt Days"] #HOMEPAGE_174
managmentPageLoadMyTeamRotaTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - My Team Rota"] #HOMEPAGE_175
managmentPageLoadCarryForwardRequestsTile2.tag = ["MANAGEMENT", "MANAGEMENT Tile - Carry Forward Requests"] #HOMEPAGE_177
managmentPageLoadHolidayManagementTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Holiday Management"] #HOMEPAGE_178
managmentPageLoadTimesheetTestingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Timesheet Testing"] #HOMEPAGE_180
managmentPageLoadAbsenceAdjustmentsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Absence Adjustments"] #HOMEPAGE_181
managmentPageLoadBulkAbsenceBookingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Bulk Absence Booking"] #HOMEPAGE_182
managmentPageLoadLockTileTestTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Lock Tile Test"] #HOMEPAGE_184
managmentPageLoadBulkScheduleTimesheetsTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Bulk Schedule Timesheets"] #HOMEPAGE_185
managmentPageLoadManagerApprovalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Manager Approval"] #HOMEPAGE_187
managmentPageLoadDetailsForApprovalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Details For Approval"] #HOMEPAGE_190
managmentPageLoadMobileRotaTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Mobile Rota"] #HOMEPAGE_194
managmentPageLoadInvoiceDisplayTestTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Invoice Display Test"] #HOMEPAGE_197
managmentPageLoadInvoicingTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Invoicing"] #HOMEPAGE_198
managmentPageLoadNextraMobileTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Nextra Mobile"] #HOMEPAGE_199
managmentPageLoadKnowledgeHubTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Knowledge Hub"] #HOMEPAGE_201
managmentPageLoadDGRotaTestTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - DG Rota Test"] #HOMEPAGE_206
managmentPageLoadMoveTerminateStaffTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Move Terminate Staff"] #HOMEPAGE_208
managmentPageLoadTimesheetApprovalTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Timesheet Approval"] #HOMEPAGE_209
managmentPageLoadPayrollTile.tag = ["MANAGEMENT", "MANAGEMENT Tile - Payroll"] #HOMEPAGE_210

# Tags for functions in the BANK section
bankPageLoadAgencyAuthorisationsTile.tag = ["BANK", "BANK Tile - Agency Authorisations"] #HOMEPAGE_52
bankPageLoadAgencyHoursTile.tag = ["BANK", "BANK Tile - Agency Hours"] #HOMEPAGE_104
bankPageLoadAgencyQuickRequestTile.tag = ["BANK", "BANK Tile - Agency Quick Request"] #HOMEPAGE_51
bankPageLoadAgencySearchTile.tag = ["BANK", "BANK Tile - Agency Search"] #HOMEPAGE_54
bankPageLoadAgencySearchOfferTile.tag = ["BANK", "BANK Tile - Agency Search Offer"] #HOMEPAGE_53
bankPageLoadFeederDataUploaderTile.tag = ["BANK", "BANK Tile - Feeder Data Uploader"] #HOMEPAGE_138
bankPageLoadHRDataTile.tag = ["BANK", "BANK Tile - HR Data"] #HOMEPAGE_172
bankPageLoadTourDataUploaderTile.tag = ["BANK", "BANK Tile - Tour Data Uploader"] #HOMEPAGE_139
bankPageLoadUnfilledShiftsTile.tag = ["BANK", "BANK Tile - Unfilled Shifts"] #HOMEPAGE_102
bankPageLoadAgencyFulfilTile.tag = ["BANK", "BANK Tile - Agency Fulfil"] #HOMEPAGE_77
bankPageLoadAgencySearchAllocateTile.tag = ["BANK", "BANK Tile - Agency Search Allocate"] #HOMEPAGE_78
bankPageLoadPAndODemandDataImportTile.tag = ["BANK", "BANK Tile - P&O Demand Data Import"] #HOMEPAGE_171

# Tags for functions in the DATA PROCESSING section
dataProcessingPageLoadSiteTrainingTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Site Training"] #HOMEPAGE_40
dataProcessingPageLoadStandbyStaffTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Standby Staff"] #HOMEPAGE_43
dataProcessingPageLoadSiteEmailsTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Site Emails"] #HOMEPAGE_44
dataProcessingPageLoadSiteSummaryEmailTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Site Summary Email"] #HOMEPAGE_46
dataProcessingPageLoadReallocateTrainingTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Reallocate Training"] #HOMEPAGE_47
dataProcessingPageLoadDemandDataTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Demand Data"] #HOMEPAGE_49
dataProcessingPageLoadScheduledRotasTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Scheduled Rotas"] #HOMEPAGE_79
dataProcessingPageLoadScheduledJobTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Scheduled Job"] #HOMEPAGE_82
dataProcessingPageLoadBudgetDataTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Budget Data"] #HOMEPAGE_90
dataProcessingPageLoadEventApprovalTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Event Approval"] #HOMEPAGE_92
dataProcessingPageLoadSailingDataUploadTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Sailing Data Upload"] #HOMEPAGE_132
dataProcessingPageLoadKABAClockListTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - KABA Clock List"] #HOMEPAGE_133
dataProcessingPageLoadAnnualLeavePlanUploadTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Annual Leave Plan Upload"] #HOMEPAGE_137
dataProcessingPageLoadNHSBTSessionDataImportTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - NHSBT Session Data Import"] #HOMEPAGE_144
dataProcessingPageLoadDriverAllowanceUploadTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Driver Allowance Upload"] #HOMEPAGE_155
dataProcessingPageLoadAnnualLeavePlanUploadTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Annual Leave Plan Upload"] #HOMEPAGE_160
dataProcessingPageLoadESRGoImportTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - ESR Go Import"] #HOMEPAGE_162
dataProcessingPageLoadESRExportTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - ESR Export"] #HOMEPAGE_166
dataProcessingPageLoadShortfallsImportTile.tag = ["DATA PROCESSING", "DATA PROCESSING Tile - Shortfalls Import"] #HOMEPAGE_211

# Tags for functions in the SELF SERVICE section
selfServicePageLoadMyWorkPlanTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Work Plan"] #HOMEPAGE_64
selfServicePageLoadMyPayslipTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Payslip"] #HOMEPAGE_84
selfServicePageLoadMyPersonalDetailsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Personal Details"] #HOMEPAGE_87
selfServicePageLoadMyTimesheetsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Timesheets"] #HOMEPAGE_188
selfServicePageLoadMyRotaTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Rota"] #HOMEPAGE_202
selfServicePageLoadTakeMyPhotoTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Take My Photo"] #HOMEPAGE_207
selfServicePageLoadMyShiftSwapRequestsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Shift Swap Requests"] #HOMEPAGE_7
selfServicePageLoadMyLocationsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Locations"] #HOMEPAGE_14
selfServicePageLoadMyDetailsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Details"] #HOMEPAGE_15
selfServicePageLoadRecentMessagesTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Recent Messages"] #HOMEPAGE_16
selfServicePageLoadMyLeaveRequestsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Leave Requests"] #HOMEPAGE_20
selfServicePageLoadMyRotaOldTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Rota Old"] #HOMEPAGE_21
selfServicePageLoadTravelExpensesTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Travel Expenses"] #HOMEPAGE_31
selfServicePageLoadAgencyShiftsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Agency Shifts"] #HOMEPAGE_55
selfServicePageLoadRegisterMobileTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Register Mobile"] #HOMEPAGE_71
selfServicePageLoadAgencyFulfillTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Agency Fulfill"] #HOMEPAGE_72
selfServicePageLoadMyAnnualisedHoursTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Annualised Hours"] #HOMEPAGE_88
selfServicePageLoadCasualShiftRequestsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Casual Shift Requests"] #HOMEPAGE_95
selfServicePageLoadMySkillsExpiryTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Skills Expiry"] #HOMEPAGE_106
selfServicePageLoadLoginShortcutTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Login Shortcut"] #HOMEPAGE_110
selfServicePageLoadDocumentUploadTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Document Upload"] #HOMEPAGE_114
selfServicePageLoadMySEHolidayManagementTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My SE Holiday Management"] #HOMEPAGE_128
selfServicePageLoadCarryForwardRequestTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Carry Forward Request"] #HOMEPAGE_167
selfServicePageLoadMySEAccrualManagementTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My SE Accrual Management"] #HOMEPAGE_129
selfServicePageLoadMySEUnpaidHolidayManagementTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My SE Unpaid Holiday Management"] #HOMEPAGE_130
selfServicePageLoadMyClockingsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Clockings"] #HOMEPAGE_189
selfServicePageLoadChatTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Chat"] #HOMEPAGE_107
selfServicePageLoadMyTeamRotaTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Team Rota"] #HOMEPAGE_179
selfServicePageLoadMyAvailabilitiesTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Availabilities"] #HOMEPAGE_13
selfServicePageLoadMyAbsencesTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My Absences"] #HOMEPAGE_89
selfServicePageLoadCarryForwardRequestsTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Carry Forward Requests"] #HOMEPAGE_176
selfServicePageLoadChangePasswordTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Change Password"] #HOMEPAGE_59
selfServicePageLoadMyGDPRTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - My GDPR"] #HOMEPAGE_123
selfServicePageLoadEmailOptOutTile.tag = ["SELF SERVICE", "SELF SERVICE Tile - Email Opt Out"] #HOMEPAGE_97

# Tags for functions in the REPORTS section
reportsPageLoadLaneUsageTile.tag = ["REPORTS", "REPORTS Tile - Lane Usage"] #HOMEPAGE_REPORT_1
reportsPageLoadAbsenceTile.tag = ["REPORTS", "REPORTS Tile - Absence"] #HOMEPAGE_REPORT_2
reportsPageLoadRegisterTile.tag = ["REPORTS", "REPORTS Tile - Register"] #HOMEPAGE_REPORT_3
reportsPageLoadSkills2Tile.tag = ["REPORTS", "REPORTS Tile - Skills2"] #HOMEPAGE_REPORT_4
reportsPageLoadMessagesTile.tag = ["REPORTS", "REPORTS Tile - Messages"] #HOMEPAGE_REPORT_5
reportsPageLoadPayrollTile.tag = ["REPORTS", "REPORTS Tile - Payroll"] #HOMEPAGE_REPORT_6
reportsPageLoadEnhancementsTile.tag = ["REPORTS", "REPORTS Tile - Enhancements"] #HOMEPAGE_REPORT_7
reportsPageLoadHoursReportTile.tag = ["REPORTS", "REPORTS Tile - Hours Report"] #HOMEPAGE_REPORT_8
reportsPageLoadAbsence2Tile.tag = ["REPORTS", "REPORTS Tile - Absence2"] #HOMEPAGE_REPORT_9
reportsPageLoadClockingAttendanceTile.tag = ["REPORTS", "REPORTS Tile - Clocking Attendance"] #HOMEPAGE_REPORT_10
reportsPageLoadAttendanceTile.tag = ["REPORTS", "REPORTS Tile - Attendance"] #HOMEPAGE_REPORT_11
reportsPageLoadSkillsTile.tag = ["REPORTS", "REPORTS Tile - Skills"] #HOMEPAGE_REPORT_12
reportsPageLoadShortfallsTile.tag = ["REPORTS", "REPORTS Tile - Shortfalls"] #HOMEPAGE_REPORT_13
reportsPageLoadContractedHoursTile.tag = ["REPORTS", "REPORTS Tile - Contracted Hours"] #HOMEPAGE_REPORT_14
reportsPageLoadStaffShortfallsTile.tag = ["REPORTS", "REPORTS Tile - Staff Shortfalls"] #HOMEPAGE_REPORT_15
reportsPageLoadStaffClockingsTile.tag = ["REPORTS", "REPORTS Tile - Staff Clockings"] #HOMEPAGE_REPORT_16
reportsPageLoadRejectedLeaveTile.tag = ["REPORTS", "REPORTS Tile - Rejected Leave"] #HOMEPAGE_REPORT_17
reportsPageLoadYearlyPlannerTile.tag = ["REPORTS", "REPORTS Tile - Yearly Planner"] #HOMEPAGE_REPORT_18
reportsPageLoadBradfordFactorTile.tag = ["REPORTS", "REPORTS Tile - Bradford Factor"] #HOMEPAGE_REPORT_19
reportsPageLoadHubDemandActualTile.tag = ["REPORTS", "REPORTS Tile - Hub Demand Actual"] #HOMEPAGE_REPORT_20
reportsPageLoadHubVisibilityTile.tag = ["REPORTS", "REPORTS Tile - Hub Visibility"] #HOMEPAGE_REPORT_21
reportsPageLoadSectionTransfersTile.tag = ["REPORTS", "REPORTS Tile - Section Transfers"] #HOMEPAGE_REPORT_22
reportsPageLoadAgencyOnsiteTile.tag = ["REPORTS", "REPORTS Tile - Agency Onsite"] #HOMEPAGE_REPORT_23
reportsPageLoadInactiveStaffTile.tag = ["REPORTS", "REPORTS Tile - Inactive Staff"] #HOMEPAGE_REPORT_24
reportsPageLoadAgencyHoursTile.tag = ["REPORTS", "REPORTS Tile - Agency Hours"] #HOMEPAGE_REPORT_25
reportsPageLoadAgencyApprovalsTile.tag = ["REPORTS", "REPORTS Tile - Agency Approvals"] #HOMEPAGE_REPORT_26
reportsPageLoadAuthorisationRequestsTile.tag = ["REPORTS", "REPORTS Tile - Authorisation Requests"] #HOMEPAGE_REPORT_27
reportsPageLoadDemandQuickEntryTile.tag = ["REPORTS", "REPORTS Tile - Demand Quick Entry"] #HOMEPAGE_REPORT_28
reportsPageLoadNeuvenDataExportTile.tag = ["REPORTS", "REPORTS Tile - Neuven Data Export"] #HOMEPAGE_REPORT_29
reportsPageLoadClockingOverrideBufferTile.tag = ["REPORTS", "REPORTS Tile - Clocking Override Buffer"] #HOMEPAGE_REPORT_30
reportsPageLoadDailyUpdateLogTile.tag = ["REPORTS", "REPORTS Tile - Daily Update Log"] #HOMEPAGE_REPORT_31
reportsPageLoadHolidaySlotsTile.tag = ["REPORTS", "REPORTS Tile - Holiday Slots"] #HOMEPAGE_REPORT_32
reportsPageLoadStandbyReportTile.tag = ["REPORTS", "REPORTS Tile - Standby Report"] #HOMEPAGE_REPORT_33
reportsPageLoadViewedRostersTile.tag = ["REPORTS", "REPORTS Tile - Viewed Rosters"] #HOMEPAGE_REPORT_1032
reportsPageLoadDayRosterTile.tag = ["REPORTS", "REPORTS Tile - Day Roster"] #HOMEPAGE_REPORT_1034
reportsPageLoadSelfServiceYearlyPlannerTile.tag = ["REPORTS", "REPORTS Tile - Self-Service Yearly Planner"] #HOMEPAGE_REPORT_1035
reportsPageLoadMyHolidaySlotsTile.tag = ["REPORTS", "REPORTS Tile - My Holiday Slots"] #HOMEPAGE_REPORT_1036
reportsPageLoadCrewManagementTile.tag = ["REPORTS", "REPORTS Tile - Crew Management"] #HOMEPAGE_REPORT_1037
reportsPageLoadJobListTile.tag = ["REPORTS", "REPORTS Tile - Job List"] #HOMEPAGE_REPORT_1038
reportsPageLoadAccruedAbsenceHoursTile.tag = ["REPORTS", "REPORTS Tile - Accrued Absence Hours"] #HOMEPAGE_REPORT_1039
reportsPageLoadWTDReportTile.tag = ["REPORTS", "REPORTS Tile - WTD Report"] #HOMEPAGE_REPORT_1040
reportsPageLoadEmployeeGroupsTile.tag = ["REPORTS", "REPORTS Tile - Employee Groups"] #HOMEPAGE_REPORT_1041
reportsPageLoadCrewSailingListTile.tag = ["REPORTS", "REPORTS Tile - Crew Sailing List"] #HOMEPAGE_REPORT_1042
reportsPageLoadLastWorkingShiftTile.tag = ["REPORTS", "REPORTS Tile - Last Working Shift"] #HOMEPAGE_REPORT_1043
reportsPageLoadDidNotAttendTile.tag = ["REPORTS", "REPORTS Tile - Did Not Attend"] #HOMEPAGE_REPORT_1044
reportsPageLoadLieuVsContractedTile.tag = ["REPORTS", "REPORTS Tile - Lieu Vs Contracted"] #HOMEPAGE_REPORT_1045
reportsPageLoadWTDTile.tag = ["REPORTS", "REPORTS Tile - WTD"] #HOMEPAGE_REPORT_1046
reportsPageLoadCasualHolidayAccrualTile.tag = ["REPORTS", "REPORTS Tile - Casual Holiday Accrual"] #HOMEPAGE_REPORT_1047
reportsPageLoadActivityPlansTile.tag = ["REPORTS", "REPORTS Tile - Activity Plans"] #HOMEPAGE_REPORT_1048
reportsPageLoadAgencyHoursSummaryTile.tag = ["REPORTS", "REPORTS Tile - Agency Hours Summary"] #HOMEPAGE_REPORT_1049
reportsPageLoadWTDNewTile.tag = ["REPORTS", "REPORTS Tile - WTD New"] #HOMEPAGE_REPORT_1051
reportsPageLoadColumnPickerTestTile.tag = ["REPORTS", "REPORTS Tile - Column Picker Test"] #HOMEPAGE_REPORT_1052
reportsPageLoadSelfServiceActivityTile.tag = ["REPORTS", "REPORTS Tile - Self-Service Activity"] #HOMEPAGE_REPORT_1053
reportsPageLoadKabaClockingReportTile.tag = ["REPORTS", "REPORTS Tile - Kaba Clocking Report"] #HOMEPAGE_REPORT_1054
reportsPageLoadBonusesTile.tag = ["REPORTS", "REPORTS Tile - Bonuses"] #HOMEPAGE_REPORT_1058
reportsPageLoadDeductionsTile.tag = ["REPORTS", "REPORTS Tile - Deductions"] #HOMEPAGE_REPORT_1059
reportsPageLoadStaffFeedbackTile.tag = ["REPORTS", "REPORTS Tile - Staff Feedback"] #HOMEPAGE_REPORT_1060
reportsPageLoadWorkUndertakenTile.tag = ["REPORTS", "REPORTS Tile - Work Undertaken"] #HOMEPAGE_REPORT_1061
reportsPageLoadNewWorkAddedTile.tag = ["REPORTS", "REPORTS Tile - New Work Added"] #HOMEPAGE_REPORT_1062 
reportsPageLoadBillableHoursDataDumpTile.tag = ["REPORTS", "REPORTS Tile - Billable Hours Data Dump"] #HOMEPAGE_REPORT_1063
reportsPageLoadDriversFeederListTile.tag = ["REPORTS", "REPORTS Tile - Drivers Feeder List"] #HOMEPAGE_REPORT_1064 
reportsPageLoadDriversCoachPassengersListTile.tag = ["REPORTS", "REPORTS Tile - Drivers Coach Passengers List"] #HOMEPAGE_REPORT_1065
reportsPageLoadDriversReturnsDeparturesAnalysisTile.tag = ["REPORTS", "REPORTS Tile - Drivers Returns Departures Analysis"] #HOMEPAGE_REPORT_1066
reportsPageLoadDriversEventsChangesTile.tag = ["REPORTS", "REPORTS Tile - Drivers Events Changes"] #HOMEPAGE_REPORT_1067
reportsPageLoadEmployeeCalculationsTile.tag = ["REPORTS", "REPORTS Tile - Employee Calculations"] #HOMEPAGE_REPORT_1068
reportsPageLoadTeamCalculationsTile.tag = ["REPORTS", "REPORTS Tile - Team Calculations"] #HOMEPAGE_REPORT_1069
reportsPageLoadWeeklyHoursTile.tag = ["REPORTS", "REPORTS Tile - Weekly Hours"] #HOMEPAGE_REPORT_1070
reportsPageLoadExtraDutiesTile.tag = ["REPORTS", "REPORTS Tile - Extra Duties"] #HOMEPAGE_REPORT_1071
reportsPageLoadDoubleSessionsTile.tag = ["REPORTS", "REPORTS Tile - Double Sessions"] #HOMEPAGE_REPORT_1072
reportsPageLoadPayReturnTile.tag = ["REPORTS", "REPORTS Tile - Pay Return"] #HOMEPAGE_REPORT_1073
reportsPageLoadMyCalculationsTile.tag = ["REPORTS", "REPORTS Tile - My Calculations"] #HOMEPAGE_REPORT_1074
reportsPageLoadNewStartersTile.tag = ["REPORTS", "REPORTS Tile - New Starters"] #HOMEPAGE_REPORT_1075
reportsPageLoadResearchDevTile.tag = ["REPORTS", "REPORTS Tile - Research & Development"] #HOMEPAGE_REPORT_1077
reportsPageLoadBankStaffUsageTile.tag = ["REPORTS", "REPORTS Tile - Bank Staff Usage"] #HOMEPAGE_REPORT_1078
reportsPageLoadBankStaffUtilisationTile.tag = ["REPORTS", "REPORTS Tile - Bank Staff Utilisation"] #HOMEPAGE_REPORT_1079
reportsPageLoadExtraSessionsReasonsTile.tag = ["REPORTS", "REPORTS Tile - Extra Sessions Reasons"] #HOMEPAGE_REPORT_1080
reportsPageLoadInterfaceChangesTile.tag = ["REPORTS", "REPORTS Tile - Interface Changes"] #HOMEPAGE_REPORT_1081
reportsPageLoadChartTestTile.tag = ["REPORTS", "REPORTS Tile - Chart Test"] #HOMEPAGE_REPORT_1083
reportsPageLoadProjectWorkAuditTile.tag = ["REPORTS", "REPORTS Tile - Project Work Audit"] #HOMEPAGE_REPORT_1087
reportsPageLoadActiveCompletedProjectsTile.tag = ["REPORTS", "REPORTS Tile - Active Completed Projects"] #HOMEPAGE_REPORT_1088
reportsPageLoadBillableHoursTile.tag = ["REPORTS", "REPORTS Tile - Billable Hours"] #HOMEPAGE_REPORT_1089
reportsPageLoadBillableHoursBreakdownTile.tag = ["REPORTS", "REPORTS Tile - Billable Hours Breakdown"] #HOMEPAGE_REPORT_1090
reportsPageLoadSpentTimeTile.tag = ["REPORTS", "REPORTS Tile - Spent Time"] #HOMEPAGE_REPORT_1091 
reportsPageLoadAccruedDaysTile.tag = ["REPORTS", "REPORTS Tile - Accrued Days"] #HOMEPAGE_REPORT_1092
reportsPageLoadPrevSessionsReportTile.tag = ["REPORTS", "REPORTS Tile - Previous Sessions Report"] #HOMEPAGE_REPORT_1093
reportsPageLoadSupportPortalCategoryTile.tag = ["REPORTS", "REPORTS Tile - Support Portal Category"] #HOMEPAGE_REPORT_1094
reportsPageLoadBilledDaysTile.tag = ["REPORTS", "REPORTS Tile - Billed Days"] #HOMEPAGE_REPORT_1095
reportsPageLoadMonthViewTile.tag = ["REPORTS", "REPORTS Tile - Month View"] #HOMEPAGE_REPORT_1096
reportsPageLoadPOPayrollAbsenceTile.tag = ["REPORTS", "REPORTS Tile - PO Payroll Absence"] #HOMEPAGE_REPORT_1098
reportsPageLoadTheLiarTile.tag = ["REPORTS", "REPORTS Tile - The Liar"] #HOMEPAGE_REPORT_1099
reportsPageLoadStaffSessionsOutsideHomeTeamTile.tag = ["REPORTS", "REPORTS Tile - Staff Sessions Outside Home Team"] #HOMEPAGE_REPORT_1100
reportsPageLoadUnsubmittedSessionsTile.tag = ["REPORTS", "REPORTS Tile - Unsubmitted Sessions"] #HOMEPAGE_REPORT_1101
reportsPageLoadAbsenceTile.tag = ["REPORTS", "REPORTS Tile - Absence"] #HOMEPAGE_REPORT_1102
reportsPageLoadSicknessTile.tag = ["REPORTS", "REPORTS Tile - Sickness"] #HOMEPAGE_REPORT_1103
reportsPageLoadChairmanReportTile.tag = ["REPORTS", "REPORTS Tile - Chairman Report"] #HOMEPAGE_REPORT_1104
reportsPageLoadJacicnthaChartFunctionalityTile.tag = ["REPORTS", "REPORTS Tile - Jacicntha Chart Functionality"] #HOMEPAGE_REPORT_1105
reportsPageLoadStatsTile.tag = ["REPORTS", "REPORTS Tile - Stats"] #HOMEPAGE_REPORT_1106
reportsPageLoadMultiPostTile.tag = ["REPORTS", "REPORTS Tile - Multi Post"] #HOMEPAGE_REPORT_1107
reportsPageLoadWeeklyHoursTile.tag = ["REPORTS", "REPORTS Tile - Weekly Hours"] #HOMEPAGE_REPORT_1108
reportsPageLoadSurveyorWorkBreakdownTile.tag = ["REPORTS", "REPORTS Tile - Surveyor Work Breakdown"] #HOMEPAGE_REPORT_1109 
reportsPageLoadWorkAbsenceApprovalRejectionBreakdownTile.tag = ["REPORTS", "REPORTS Tile - Work Absence Approval Rejection Breakdown"] #HOMEPAGE_REPORT_1110
reportsPageLoadDelegationReportTile.tag = ["REPORTS", "REPORTS Tile - Delegation Report"] #HOMEPAGE_REPORT_1111
reportsPageLoadTimesheetChangesTile.tag = ["REPORTS", "REPORTS Tile - Timesheet Changes"] #HOMEPAGE_REPORT_1112
reportsPageLoadSicknessTriggerPointTile.tag = ["REPORTS", "REPORTS Tile - Sickness Trigger Point"] #HOMEPAGE_REPORT_1113
reportsPageLoadAttendanceInfoTile.tag = ["REPORTS", "REPORTS Tile - Attendance Info"] #HOMEPAGE_REPORT_1114
reportsPageLoadDayAllocationTile.tag = ["REPORTS", "REPORTS Tile - Day Allocation"] #HOMEPAGE_REPORT_1115
reportsPageLoadRoleAllocationTile.tag = ["REPORTS", "REPORTS Tile - Role Allocation"] #HOMEPAGE_REPORT_1116


# Tags for functions in the DASHBOARD REPORTS section
dashboardReportsSessionUnavailablityTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Session Unavailability"] #HOMEPAGE_DASHBOARDREPORT_9
dashboardReportsShortfallsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Shortfalls"] #HOMEPAGE_DASHBOARDREPORT_2
dashboardReportsBankHoursPaidTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Bank Hours Paid"] #HOMEPAGE_DASHBOARDREPORT_3
dashboardReportsStaffingModelTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Staffing Model"] #HOMEPAGE_DASHBOARDREPORT_8
dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Session Operated with Shortfall or Surplus"] #HOMEPAGE_DASHBOARDREPORT_7
dashboardReportsSeshExpectedVSSeshPlannedTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Session Expected vs Planned"] #HOMEPAGE_DASHBOARDREPORT_6
dashboardReportsSkillsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Skills"] #HOMEPAGE_DASHBOARDREPORT_1
dashboardReportSicknessPaidTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Sickness Paid"] #HOMEPAGE_DASHBOARDREPORT_5
dashboardReportAbsenceReasonBreakDownTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Absence Reason Breakdown"] #HOMEPAGE_DASHBOARDREPORT_4
dashboardReportTestAbsenceDropListTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Test Absence Dropdown List"] #HOMEPAGE_DASHBOARDREPORT_15 
dashboardReportAnnualLeaveBookByDayTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Annual Leave Book by Day"] #HOMEPAGE_DASHBOARDREPORT_39
dashboardReportAnnualLeaveBookVsAllowanceTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Annual Leave Book vs Allowance"] #HOMEPAGE_DASHBOARDREPORT_40
dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Employee Annual Leave Allowance vs Booked"] #HOMEPAGE_DASHBOARDREPORT_41
dashboardReportSessionOverrunReasonsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Session Overrun Reasons"] #HOMEPAGE_DASHBOARDREPORT_43
dashboardReportExportMultiToPDFTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Export Multi to PDF"] #HOMEPAGE_183
dashboardReportShortfallsReportTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Shortfalls Report"] #HOMEPAGE_DASHBOARDREPORT_16
dashboardReportRejectedLeaveTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Rejected Leave"] #HOMEPAGE_DASHBOARDREPORT_17
dashboardReportContractedHoursTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Contracted Hours"] #HOMEPAGE_DASHBOARDREPORT_18
dashboardReportSkillsListTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Skills List"] #HOMEPAGE_DASHBOARDREPORT_19
dashboardReportSkillsSummaryTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Skills Summary"] #HOMEPAGE_DASHBOARDREPORT_20
dashboardReportTestLeavePeriodDropListTile.tag = ["DASHBOARD REPORTS Tile - DASHBOARD REPORTS", "Test Leave Period Dropdown List"] #HOMEPAGE_DASHBOARDREPORT_32
dashboardReportAbsenceTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Absence"] #HOMEPAGE_DASHBOARDREPORT_33
dashboardReportAbsenceAllowanceTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Absence Allowance"] #HOMEPAGE_DASHBOARDREPORT_34
dashboardReportCarryForwardRequestsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Carry Forward Requests"] #HOMEPAGE_DASHBOARDREPORT_35
dashboardReportClockingReportsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Clocking Reports"] #HOMEPAGE_DASHBOARDREPORT_36
dashboardReportHolidaySlotsTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Holiday Slots"] #HOMEPAGE_DASHBOARDREPORT_37
dashboardReportSessionsPlannedWithShortfallOrSurplusTile.tag = ["DASHBOARD REPORTS", "DASHBOARD REPORTS Tile - Sessions Planned with Shortfall or Surplus"] #HOMEPAGE_DASHBOARDREPORT_38

# Tags for functions in the ABOUT section
aboutDateandampTimeTile.tag = ["ABOUT", "ABOUT Tile - Date and Time"] #HOMEPAGE_2
aboutAboutUsTile.tag = ["ABOUT", "ABOUT Tile - About Us"] #HOMEPAGE_11 
aboutLogoTile.tag = ["ABOUT", "ABOUT Tile - Logo"] #HOMEPAGE_18 
aboutCurrentUsersLoggedInTile.tag = ["ABOUT", "ABOUT Tile - Current Users Logged In"] #HOMEPAGE_23
aboutLogoutTile.tag = ["ABOUT", "ABOUT Tile - Logout"] #HOMEPAGE_25
aboutGDPRTermsTile.tag = ["ABOUT", "ABOUT Tile - GDPR Terms"] #HOMEPAGE_124
aboutPrivacyStatementTile.tag = ["ABOUT", "ABOUT Tile - Privacy Statement"] #HOMEPAGE_125
aboutFullScreenTile.tag = ["ABOUT", "Full Screen"] #HOMEPAGE_195
aboutExitFullScreenTile.tag = ["ABOUT", "Exit Full Screen"] #HOMEPAGE_196


# Logs into system, updates the user role and checks function meta data. 
def target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response):
    # Call the login function to log in and open the Homepage
    gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

    # Check user role, switch if not the desired target
    if checkUserRoleAndSwitch(driver_response, target_sys, user_type) == True: 
        user_role_perm_check = True
    else: 
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
# If an 'X' is present present within a cell, will colour RED to signify it does not exist for that usertype
# If a cell is empty, will check if the web object exists or not. 
# If it does exist for that usertype, will leave as is, otherwise will highlight green to signify it should not exist for that usertype 
# Perfecto!
def global_web_object_processor(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format): 
    cell = row[object]
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
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}' tile does not exist or have issues as stated above{Fore.WHITE}")
            # Update the Excel sheet with 'X' (empty space) and apply the red format.
            worksheet.write(index + 1, df.columns.get_loc(object), 'X', red_format)
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, driver_response, True)
            if web_element_exists(web_object):
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}' exists{Fore.WHITE}")
                # Update the Excel sheet with 'X' and apply the green format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', green_format)
            else:
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}' does not exist{Fore.WHITE}")
                # Update the Excel sheet with 'X and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), 'X', red_format)

    elif pd.isna(cell): #  the NaN values are of type float, not a string
        try:
            # Set Web Object Search variable flag to false to indicate no failure has occured. If no errors occure in the try/catch, it will attempt to scrape the target web object. 
            # The functions below are used to navigate to our target and may not always apply to a specific user role within our target system. 
            web_obj_sch = True

            #print(target_func.tag)

            user_role_perm_check = target_object_initial_checks(target_func, headless_mode, target_sys, username, password, user_type, driver_response)
         
        except: 
            print(f"{Fore.RED}Likely Error: {Fore.WHITE}Webdriver could not find a specific web object leading up to the target web object within your code i.e. <h1>, class='', id=''")
            print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web objects leading up to the '{target_func.tag[1]}' tile does not exist or has issues as stated above{Fore.WHITE}")
            web_obj_sch = False

        if web_obj_sch == True and user_role_perm_check == True: 
            # Replace 'web_object' with the actual method you use to find the web element
            web_object = lambda: target_func(target_sys, headless_mode, user_type, username, password, driver_response, True)
            if web_element_exists(web_object):                                              #{target_func.tag[1]} replace when all fucntions have been implemented
                print(f"{Fore.RED}User type '{Fore.WHITE}{user_type}{Fore.RED}': Web object '{target_func.tag[1]}' should not exist{Fore.WHITE}")
                # Update the Excel sheet with ' ' (empty space) and apply the red format.
                worksheet.write(index + 1, df.columns.get_loc(object), '', red_format)
            else:
                print(f"{Fore.GREEN}User type '{Fore.WHITE}{user_type}{Fore.GREEN}': Web object '{target_func.tag[1]}' does not exist{Fore.WHITE}")

####################################################################END OF WRAPPER FUNCTION######################################################################