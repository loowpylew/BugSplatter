import f_driver_init as fdi 
import globals as gs
import menu_items as mi
import admin as a
import user_tiles as ut
import globals as gs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.ui import Select
from colorama import Fore, Style, init
from openpyxl import load_workbook
from datetime import datetime
import pandas as pd
import main as m 
import backend_processes as bp
import concurrent.futures
import time 

##GLOBALS##
already_processed_sub_sub_tabs = {}

################################################################## BATCH PROCESSES #####################################################################

# Creates new employees 
def batchProcessEmployees(target_sys, headless_mode, user_type, username, password, paths): 
    #try:
        # Initialize the WebDriver (use the appropriate driver for your browser)
        driver_response = fdi.initialize_driver(headless_mode)    

        # Call the login function to log in and open the Homepage
        gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

        # Check user role and switch
        gs.checkUserRoleAndSwitch(target_sys, headless_mode, user_type, username, password, driver_response, True)
        
        # Load up 'Admin Screen' 
        mi.homePageLoadAdminMenuItem(target_sys, headless_mode, user_type, username, password, driver_response, True)
         
        # Load up 'Staff Admin' Menu Options
        a.staffAdminLoadMenuOptions(target_sys, headless_mode, user_type, username, password, driver_response, True)
       
        # Locate and click the "Employees" button
        a.staffAdminLoadEmployees(target_sys, headless_mode, user_type, username, password, driver_response, True)

        # Used for all waits within this function after this line of code
        wait = WebDriverWait(driver_response, 10)

        if len(paths) >= 1: 
            for path in paths: 
                employee_data = pd.read_excel(path, sheet_name="employees")

                # Find all elements with class "inputLabel"

                for index, row in employee_data.iterrows():
                    # Now, locate and click the "plus" button to load up the "Create" button
                    plus_button = wait.until(EC.element_to_be_clickable((By.ID, "actionToggleIcon")))

                    # Scroll the element into view if needed
                    driver_response.execute_script("arguments[0].scrollIntoView();", plus_button)

                    # Click the element using execute_script directly
                     
                    driver_response.execute_script("arguments[0].click();", plus_button)

                    #plus_button.click()
                    
                    # Click the "Create" button to add a new employee
                    # Because there is no exact id/class match, the function fails
                    try: 
                        create_button = wait.until(EC.element_to_be_clickable((By.ID, "rfdrop_action_addnewdata")))
                        
                        # Scroll the element into view if needed
                        driver_response.execute_script("arguments[0].scrollIntoView();", create_button)

                        # Click the element using execute_script directly
                        
                        driver_response.execute_script("arguments[0].click();", create_button)
                        #create_button.click()
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
    #except Exception as e: 
        #driver_response.quit()
        #print(f"{Fore.RED}Test Failed{Fore.WHITE}")
        #print(e)


# Processes User Tiles
# If new user tiles added in the future, helpful to check what itemtags belong to which item menu and what tiles will appear under a specfic usertype. 
#select username, itemtag, itemname, tabname FROM (SELECT CONVERT(varchar, USERTYPEID) as usertype_id, USERNAME FROM rf_usertypes WHERE languageid = 2) u inner join rf_nav_homepage_items nh ON CHARINDEX(',' + USERTYPE_ID + ',', nh.usertypes) >= 1 
#JOIN rf_nav_homepage_tabs ht ON ht.TabID = nh.TABID ORDER BY username, tabname, itemname -- all items in a specific system. 
def batchProcessUserTypeTiles(target_sys, headless_mode, username, password, paths):

    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        "Homepage_1": [] # NOT USED
        , "Homepage_2": [ut.aboutDateandampTimeTile]
        , "Homepage_3": [] # NOT USED
        , "Homepage_4": [] # NOT USED
        , "Homepage_5": [ut.managmentPageLoadSkillsExpiryTile]
        , "Homepage_6": [] # NOT USED
        , "Homepage_7": [ut.selfServicePageLoadMyShiftSwapRequestsTile] 
        , "Homepage_8": [] # NOT USED
        , "Homepage_10": [] # NOT USED
        , "Homepage_11": [ut.aboutAboutUsTile]
        , "Homepage_12": [] # NOT USED
        , "Homepage_13": [ut.selfServicePageLoadMyAvailabilitiesTile]
        , "Homepage_14": [ut.selfServicePageLoadMyLocationsTile]
        , "Homepage_15": [ut.selfServicePageLoadMyDetailsTile] 
        , "Homepage_16": [ut.selfServicePageLoadRecentMessagesTile]
        , "Homepage_17": [ut.managmentPageLoadClockingsTile]
        , "Homepage_18": [ut.aboutLogoTile]
        , "Homepage_19": [ut.managmentPageLoadAbsenceRequestsTile]
        , "Homepage_20": [ut.selfServicePageLoadMyLeaveRequestsTile]
        , "Homepage_21": [ut.selfServicePageLoadMyRotaOldTile]
        , "Homepage_22": [ut.managmentPageLoadAdminOldTile]
        , "Homepage_23": [ut.aboutCurrentUsersLoggedInTile]
        , "Homepage_24": [] # Not USED
        , "Homepage_25": [ut.aboutLogoutTile]
        , "Homepage_26": [ut.managmentPageLoadRotaTile]
        , "Homepage_27": [] # NOT USED
        , "Homepage_28": [] # NOT USED
        , "Homepage_29": [ut.managmentPageLoadRotaChangesTile]
        , "Homepage_30": [] # NOT USED
        , "Homepage_31": [ut.selfServicePageLoadTravelExpensesTile]
        , "Homepage_32": [ut.managmentPageLoadExceptionsReportTile]
        , "Homepage_33": [ut.reportsPageLoadStandbyReportTile] # Only user tile that is used within 'Reports'
        , "Homepage_34": [ut.homePageLoadNextShiftTile]
        , "Homepage_35": [ut.managmentPageLoadLateStaffTile]
        , "Homepage_36": [ut.managmentPageLoadShortfallsAllocateTile]
        , "Homepage_37": [ut.managmentPageLoadMissedCheckCallsTile]
        , "Homepage_38": [ut.managmentPageLoadRefresherTrainingTile]
        , "Homepage_39": [ut.managmentPageLoadNoResponseUnconfirmedTile]
        , "Homepage_40": [ut.dataProcessingPageLoadSiteTrainingTile]
        , "Homepage_41": [ut.managmentPageLoadShortfallsOfferTile]
        , "Homepage_42": [] # NOT USED
        , "Homepage_43": [ut.dataProcessingPageLoadStandbyStaffTile]
        , "Homepage_44": [ut.dataProcessingPageLoadSiteEmailsTile]
        , "Homepage_45": [ut.managmentPageLoadPostponedTrainingTile]
        , "Homepage_46": [ut.dataProcessingPageLoadSiteSummaryEmailTile]
        , "Homepage_47": [ut.dataProcessingPageLoadReallocateTrainingTile]
        , "Homepage_48": [ut.managmentPageLoadFailedCheckCallsTile]
        , "Homepage_49": [ut.dataProcessingPageLoadDemandDataTile]
        , "Homepage_50": [] # NOT USED
        , "Homepage_51": [ut.bankPageLoadAgencyQuickRequestTile]
        , "Homepage_52": [ut.bankPageLoadAgencyAuthorisationsTile]
        , "Homepage_53": [ut.bankPageLoadAgencySearchOfferTile]
        , "Homepage_54": [ut.bankPageLoadAgencySearchTile]
        , "Homepage_55": [ut.selfServicePageLoadAgencyShiftsTile]
        , "Homepage_56": [ut.managmentPageLoadTimesheetsTile]
        , "Homepage_57": [ut.managmentPageLoadImportRotaDataTile]
        , "Homepage_58": [] # NOT USED
        , "Homepage_59": [ut.selfServicePageLoadChangePasswordTile]
        , "Homepage_60": [ut.managmentPageLoadPayrollSubmissionTile]
        , "Homepage_61": [ut.managmentPageLoadClockingsByPersonTile]
        , "Homepage_62": [ut.managmentPageLoadDataTransferFailuresTile]
        , "Homepage_63": [ut.managmentPageLoadMissedTasksTile]
        , "Homepage_64": [ut.selfServicePageLoadMyWorkPlanTile]
        , "Homepage_65": [ut.managmentPageLoadManagerWorkPlanTile]
        , "Homepage_68": [ut.managmentPageLoadAdminMessageBoardTile]
        , "Homepage_69": [ut.managmentPageLoadUnrecognizedMessagesTile]
        , "Homepage_70": [ut.managmentPageLoadNHSBTImportTile]
        , "Homepage_71": [ut.selfServicePageLoadRegisterMobileTile]
        , "Homepage_72": [ut.selfServicePageLoadAgencyFulfillTile]
        , "Homepage_73": [ut.managementPageLoadHubDemandTile]
        , "Homepage_74": [ut.managmentPageLoadNHSBTQuickEntryTile]
        , "Homepage_75": [ut.managmentPageLoadAgencyQuickAdminTile]
        , "Homepage_76": [ut.managmentPageLoadSectionTransfersTile]
        , "Homepage_77": [ut.bankPageLoadAgencyFulfilTile] # NOT USED
        , "Homepage_78": [ut.bankPageLoadAgencySearchAllocateTile] # NOT USED
        , "Homepage_79": [ut.dataProcessingPageLoadScheduledRotasTile]
        , "Homepage_80": [ut.managmentPageLoadHubStatusTile]
        , "Homepage_81": [ut.managmentPageLoadHubVisibilityTile]
        , "Homepage_82": [ut.dataProcessingPageLoadScheduledJobTile]
        , "Homepage_83": [ut.managmentPageLoadStaffQuickAdminTile]
        , "Homepage_84": [ut.selfServicePageLoadMyPayslipTile] # NOT USED
        , "Homepage_86": [ut.managmentPageLoadShiftSwapRequestsTile]
        , "Homepage_87": [ut.selfServicePageLoadMyPersonalDetailsTile] # NOT USED
        , "Homepage_88": [ut.selfServicePageLoadMyAnnualisedHoursTile] 
        , "Homepage_89": [ut.selfServicePageLoadMyAbsencesTile ]
        , "Homepage_90": [ut.dataProcessingPageLoadBudgetDataTile]
        , "Homepage_91": [] # NOT USED
        , "Homepage_92": [ut.dataProcessingPageLoadEventApprovalTile]
        , "Homepage_93": [ut.managmentPageLoadScenariosUploadTile]
        , "Homepage_94": [ut.managmentPageLoadGenerateLogBookNumbersTile]
        , "Homepage_95": [ut.selfServicePageLoadCasualShiftRequestsTile] 
        , "Homepage_96": [] # NOT USED
        , "Homepage_97": [ut.selfServicePageLoadEmailOptOutTile]
        , "Homepage_98": [ut.managmentPageLoadTrainingOverdueTile]
        , "Homepage_99": [ut.managmentPageLoad12HourUnfilledCasualsTile]
        , "Homepage_100": [] # NOT USED
        , "Homepage_102": [ut.bankPageLoadUnfilledShiftsTile]
        , "Homepage_103": [ut.managmentPageLoadWorkPlanReportTile]
        , "Homepage_104": [ut.bankPageLoadAgencyHoursTile]
        , "Homepage_105": [ut.managmentPageLoadMusterListTile]
        , "Homepage_106": [ut.selfServicePageLoadMySkillsExpiryTile]
        , "Homepage_107": [ut.selfServicePageLoadChatTile]
        , "Homepage_109": [ut.managmentPageLoadBulkPatternRenewalTile]
        , "Homepage_110": [ut.selfServicePageLoadLoginShortcutTile]
        , "Homepage_111": [ut.managmentPageLoadSimulateUsersTile]
        , "Homepage_112": [ut.managmentPageLoadApplicantsTile]
        , "Homepage_113": [ut.managmentPageLoadTrainingTile]
        , "Homepage_114": [ut.selfServicePageLoadDocumentUploadTile]
        , "Homepage_115": [ut.managmentPageLoadDocumentApprovalTile]
        , "Homepage_116": [ut.managmentPageLoadCMCallBacksTile ]
        , "Homepage_117": [ut.managmentPageLoadDetailsApprovalTile]
        , "Homepage_118": [ut.managmentPageLoadMVLieuTile ]
        , "Homepage_119": [ut.managmentPageLoadSwedishDerogationTile ]
        , "Homepage_120": [ut.managmentPageLoadMyCMCallBacksTile]
        , "Homepage_121": [ut.managmentPageLoadPlacementConfirmationsTile]
        , "Homepage_122": [ut.managmentPageLoadSEHolidayTile]
        , "Homepage_123": [ut.selfServicePageLoadMyGDPRTile]
        , "Homepage_124": [ut.aboutGDPRTermsTile]
        , "Homepage_125": [ut.aboutPrivacyStatementTile]
        , "Homepage_126": [ut.managmentPageLoadSEAccruedTile]
        , "Homepage_127": [ut.managmentPageLoadSEUnpaidHolidayTile]
        , "Homepage_128": [ut.selfServicePageLoadMySEHolidayManagementTile]
        , "Homepage_129": [ut.selfServicePageLoadMySEAccrualManagementTile]
        , "Homepage_130": [ut.selfServicePageLoadMySEUnpaidHolidayManagementTile]
        , "Homepage_131": [ut.managmentPageLoadStaffFeedbackTile]
        , "Homepage_132": [ut.dataProcessingPageLoadSailingDataUploadTile]
        , "Homepage_133": [ut.dataProcessingPageLoadKABAClockListTile]
        , "Homepage_134": [ut.managmentPageLoadLieuMgmtHoursTile]
        , "Homepage_135": [ut.managmentPageLoadLieuMgmtDaysTile]
        , "Homepage_136": [ut.managmentPageLoadWageAmendmentsTile]
        , "Homepage_137": [ut.dataProcessingPageLoadAnnualLeavePlanUploadTile]
        , "Homepage_138": [ut.bankPageLoadFeederDataUploaderTile]
        , "Homepage_139": [ut.bankPageLoadTourDataUploaderTile]
        , "Homepage_140": [ut.managmentPageLoadBillingTile]
        , "Homepage_141": [ut.managmentPageLoadTestSplitDropListPageTile]
        , "Homepage_142": [ut.managmentPageLoadInterchangeScreensTile]
        , "Homepage_143": [ut.managmentPageLoadSupportPortalTile]
        , "Homepage_144": [ut.dataProcessingPageLoadNHSBTSessionDataImportTile]
        , "Homepage_145": [ut.managmentPageLoadRotaTile2]
        , "Homepage_146": [ut.managmentPageLoadScheduleTimesheetsTile]
        , "Homepage_147": [ut.managmentPageLoadCheckSingleTeamCalculationTile]
        , "Homepage_149": [ut.managmentPageLoadSubmitAllTimesheetsTile]
        , "Homepage_150": [ut.managmentPageLoadNHSBTImportTile]
        , "Homepage_151": [ut.managmentPageLoadNHSBTQuickEntryTile2]
        , "Homepage_153": [ut.managmentPageLoadDownloadESRFilesTile]
        , "Homepage_155": [ut.dataProcessingPageLoadDriverAllowanceUploadTile]
        , "Homepage_160": [ut.dataProcessingPageLoadAnnualLeavePlanUploadTile]
        , "Homepage_161": [ut.managmentPageLoadTimesheetRunsTile]
        , "Homepage_162": [ut.dataProcessingPageLoadESRGoImportTile]
        , "Homepage_163": [ut.managmentPageLoadAnnualLeaveAdjustmentsTile]
        , "Homepage_164": [ut.managmentPageLoadDaysAccrualTestingTile]
        , "Homepage_165": [ut.managmentPageLoadHoursAccrualTestingTile]
        , "Homepage_166": [ut.dataProcessingPageLoadESRExportTile]
        , "Homepage_167": [ut.selfServicePageLoadCarryForwardRequestTile]
        , "Homepage_168": [ut.managmentPageLoadCarryForwardRequestsTile]
        , "Homepage_169": [ut.managmentPageLoadYearAnnualLeaveAdjustmentsTile]
        , "Homepage_171": [] # NOT USED
        , "Homepage_172": [ut.bankPageLoadHRDataTile]
        , "Homepage_173": [ut.managmentPageLoadHolsHMgmtHoursTile]
        , "Homepage_174": [ut.managmentPageLoadHolsDMgmtDaysTile]
        , "Homepage_175": [ut.managmentPageLoadMyTeamRotaTile]
        , "Homepage_176": [ut.selfServicePageLoadCarryForwardRequestsTile]
        , "Homepage_177": [ut.managmentPageLoadCarryForwardRequestsTile2]
        , "Homepage_178": [ut.managmentPageLoadHolidayManagementTile]
        , "Homepage_179": [ut.selfServicePageLoadMyTeamRotaTile]
        , "Homepage_180": [ut.managmentPageLoadTimesheetTestingTile]
        , "Homepage_181": [ut.managmentPageLoadAbsenceAdjustmentsTile]
        , "Homepage_182": [ut.managmentPageLoadBulkAbsenceBookingTile]
        , "Homepage_183": [ut.dashboardReportExportMultiToPDFTile]
        , "Homepage_184": [ut.managmentPageLoadLockTileTestTile]
        , "Homepage_185": [ut.managmentPageLoadBulkScheduleTimesheetsTile]
        , "Homepage_187": [ut.managmentPageLoadManagerApprovalTile]
        , "Homepage_188": [ut.selfServicePageLoadMyTimesheetsTile] # NOT USED
        , "Homepage_189": [ut.selfServicePageLoadMyClockingsTile] 
        , "Homepage_190": [ut.managmentPageLoadDetailsForApprovalTile]
        , "Homepage_194": [ut.managmentPageLoadMobileRotaTile]
        , "Homepage_195": [ut.aboutFullScreenTile]
        , "Homepage_196": [ut.aboutExitFullScreenTile]
        , "Homepage_197": [ut.managmentPageLoadInvoiceDisplayTestTile]
        , "Homepage_198": [ut.managmentPageLoadInvoicingTile]
        , "Homepage_199": [ut.managmentPageLoadNextraMobileTile]
        , "Admin": [mi.homePageLoadAdminMenuItem]  # Admin - actually a button and is part of the menu options so differs in respects to not having a 'HOMEPAGE_200' tile id name 
        , "Homepage_201": [ut.managmentPageLoadKnowledgeHubTile]
        , "Homepage_202": [ut.selfServicePageLoadMyRotaTile]
        , "Homepage_203": [ut.homePageLoadAbsenceSummaryTile]
        , "Homepage_204": [ut.homePageLoadNextAbsenceTile]
        , "Homepage_205": [] # NOT IN USE
        , "Homepage_206": [ut.managmentPageLoadDGRotaTestTile]
        , "Homepage_207": [ut.selfServicePageLoadTakeMyPhotoTile] # NOT IN USE
        , "Homepage_208": [ut.managmentPageLoadMoveTerminateStaffTile]
        , "Homepage_209": [ut.managmentPageLoadTimesheetApprovalTile]
        , "Homepage_210": [ut.managmentPageLoadPayrollTile]
        , "Homepage_211": [ut.dataProcessingPageLoadShortfallsImportTile]
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
                        driver_response = fdi.initialize_driver(headless_mode)    

                        # Retrieve the function from object_processors
                        #target_func = object_processors[object]

                        for target_func in object_processors[object]:
                            try:
                                # Call the retrieved function
                                ut.global_web_object_processor(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                                #processing_functions(target_func, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                            except Exception as e:
                                print("Error finding Web_Object: ")
                                print(e)
                                
                        driver_response.quit()    

        excel_writer.close()    

        print("[Batch Process Complete]")


# Batch Process Reports
# # If new report added in the future, helpful to check what itemtags belong to which item menu and what tiles will appear under a specfic usertype. 
# SELECT ReportName, username FROM (SELECT CONVERT(varchar, USERTYPEID) as usertype_id, USERNAME FROM rf_usertypes WHERE languageid = 2) u inner join rf_Reports dr ON CHARINDEX(',' + USERTYPE_ID + ',', dr.HomepageUserTypes) >= 1 
def batchProcessUserTypeReports(target_sys, headless_mode, username, password, paths):
    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        "homepage_report_1": [ut.reportsPageLoadLaneUsageTile]
        , "homepage_report_2": [ut.reportsPageLoadAbsenceTile]
        , "homepage_report_3": [ut.reportsPageLoadRegisterTile]
        , "homepage_report_4": [ut.reportsPageLoadSkills2Tile]
        , "homepage_report_5": [ut.reportsPageLoadMessagesTile]
        , "homepage_report_6": [ut.reportsPageLoadPayrollTile]
        , "homepage_report_7": [ut.reportsPageLoadEnhancementsTile]
        , "homepage_report_8": [ut.reportsPageLoadHoursReportTile]
        , "homepage_report_9": [ut.reportsPageLoadAbsence2Tile]
        , "homepage_report_10": [ut.reportsPageLoadClockingAttendanceTile]
        , "homepage_report_11": [ut.reportsPageLoadAttendanceTile]
        , "homepage_report_12": [ut.reportsPageLoadSkillsTile]
        , "homepage_report_13": [ut.reportsPageLoadShortfallsTile]
        , "homepage_report_14": [ut.reportsPageLoadContractedHoursTile]
        , "homepage_report_15": [ut.reportsPageLoadStaffShortfallsTile]
        , "homepage_report_16": [ut.reportsPageLoadStaffClockingsTile]
        , "homepage_report_17": [ut.reportsPageLoadRejectedLeaveTile]
        , "homepage_report_18": [ut.reportsPageLoadYearlyPlannerTile]
        , "homepage_report_19": [ut.reportsPageLoadBradfordFactorTile]
        , "homepage_report_20": [ut.reportsPageLoadHubDemandActualTile]
        , "homepage_report_21": [ut.reportsPageLoadHubVisibilityTile]
        , "homepage_report_22": [ut.reportsPageLoadSectionTransfersTile]
        , "homepage_report_23": [ut.reportsPageLoadAgencyOnsiteTile]
        , "homepage_report_24": [ut.reportsPageLoadInactiveStaffTile]
        , "homepage_report_25": [ut.reportsPageLoadAgencyHoursTile]
        , "homepage_report_26": [ut.reportsPageLoadAgencyApprovalsTile]
        , "homepage_report_27": [ut.reportsPageLoadAuthorisationRequestsTile]
        , "homepage_report_28": [ut.reportsPageLoadDemandQuickEntryTile]
        , "homepage_report_29": [ut.reportsPageLoadNeuvenDataExportTile]
        , "homepage_report_30": [ut.reportsPageLoadClockingOverrideBufferTile]
        , "homepage_report_31": [ut.reportsPageLoadDailyUpdateLogTile]
        , "homepage_report_32": [ut.reportsPageLoadHolidaySlotsTile]
        , "homepage_report_1032": [ut.reportsPageLoadViewedRostersTile]
        , "homepage_report_1034": [ut.reportsPageLoadDayRosterTile]
        , "homepage_report_1035": [ut.reportsPageLoadSelfServiceYearlyPlannerTile]
        , "homepage_report_1036": [ut.reportsPageLoadMyHolidaySlotsTile]
        , "homepage_report_1037": [ut.reportsPageLoadCrewManagementTile]
        , "homepage_report_1038": [ut.reportsPageLoadJobListTile]
        , "homepage_report_1039": [ut.reportsPageLoadAccruedAbsenceHoursTile]
        , "homepage_report_1040": [ut.reportsPageLoadWTDReportTile]
        , "homepage_report_1041": [ut.reportsPageLoadEmployeeGroupsTile]
        , "homepage_report_1042": [ut.reportsPageLoadCrewSailingListTile]
        , "homepage_report_1043": [ut.reportsPageLoadLastWorkingShiftTile]
        , "homepage_report_1044": [ut.reportsPageLoadDidNotAttendTile]
        , "homepage_report_1045": [ut.reportsPageLoadLieuVsContractedTile]
        , "homepage_report_1046": [ut.reportsPageLoadWTDTile]
        , "homepage_report_1047": [ut.reportsPageLoadCasualHolidayAccrualTile]
        , "homepage_report_1048": [ut.reportsPageLoadActivityPlansTile]
        , "homepage_report_1049": [ut.reportsPageLoadAgencyHoursSummaryTile]
        , "homepage_report_1051": [ut.reportsPageLoadWTDNewTile]
        , "homepage_report_1052": [ut.reportsPageLoadColumnPickerTestTile]
        , "homepage_report_1053": [ut.reportsPageLoadSelfServiceActivityTile]
        , "homepage_report_1054": [ut.reportsPageLoadKabaClockingReportTile]
        , "homepage_report_1058": [ut.reportsPageLoadBonusesTile]
        , "homepage_report_1059": [ut.reportsPageLoadDeductionsTile]
        , "homepage_report_1060": [ut.reportsPageLoadStaffFeedbackTile]
        , "homepage_report_1061": [ut.reportsPageLoadWorkUndertakenTile]
        , "homepage_report_1062": [ut.reportsPageLoadNewWorkAddedTile]
        , "homepage_report_1063": [ut.reportsPageLoadBillableHoursDataDumpTile]
        , "homepage_report_1064": [ut.reportsPageLoadDriversFeederListTile] 
        , "homepage_report_1065": [ut.reportsPageLoadDriversCoachPassengersListTile]
        , "homepage_report_1066": [ut.reportsPageLoadDriversReturnsDeparturesAnalysisTile]
        , "homepage_report_1067": [ut.reportsPageLoadDriversEventsChangesTile]
        , "homepage_report_1068": [ut.reportsPageLoadEmployeeCalculationsTile]
        , "homepage_report_1069": [ut.reportsPageLoadTeamCalculationsTile]
        , "homepage_report_1070": [ut.reportsPageLoadWeeklyHoursTile]
        , "homepage_report_1071": [ut.reportsPageLoadExtraDutiesTile]
        , "homepage_report_1072": [ut.reportsPageLoadDoubleSessionsTile] 
        , "homepage_report_1073": [ut.reportsPageLoadPayReturnTile]
        , "homepage_report_1074": [ut.reportsPageLoadMyCalculationsTile]
        , "homepage_report_1075": [ut.reportsPageLoadNewStartersTile]
        , "homepage_report_1077": [ut.reportsPageLoadResearchDevTile]
        , "homepage_report_1078": [ut.reportsPageLoadBankStaffUsageTile]
        , "homepage_report_1079": [ut.reportsPageLoadBankStaffUtilisationTile] 
        , "homepage_report_1080": [ut.reportsPageLoadExtraSessionsReasonsTile] 
        , "homepage_report_1081": [ut.reportsPageLoadInterfaceChangesTile]
        , "homepage_report_1083": [ut.reportsPageLoadChartTestTile]
        , "homepage_report_1087": [ut.reportsPageLoadProjectWorkAuditTile]
        , "homepage_report_1088": [ut.reportsPageLoadActiveCompletedProjectsTile]
        , "homepage_report_1089": [ut.reportsPageLoadBillableHoursTile]
        , "homepage_report_1090": [ut.reportsPageLoadBillableHoursBreakdownTile]
        , "homepage_report_1091": [ut.reportsPageLoadSpentTimeTile]
        , "homepage_report_1092": [ut.reportsPageLoadAccruedDaysTile]
        , "homepage_report_1093": [ut.reportsPageLoadPrevSessionsReportTile]
        , "homepage_report_1094": [ut.reportsPageLoadSupportPortalCategoryTile]
        , "homepage_report_1095": [ut.reportsPageLoadBilledDaysTile]
        , "homepage_report_1096": [ut.reportsPageLoadMonthViewTile]
        , "homepage_report_1098": [ut.reportsPageLoadPOPayrollAbsenceTile]
        , "homepage_report_1099": [ut.reportsPageLoadTheLiarTile]
        , "homepage_report_1100": [ut.reportsPageLoadStaffSessionsOutsideHomeTeamTile]
        , "homepage_report_1101": [ut.reportsPageLoadUnsubmittedSessionsTile]
        , "homepage_report_1102": [ut.reportsPageLoadAbsenceTile]
        , "homepage_report_1103": [ut.reportsPageLoadSicknessTile]
        , "homepage_report_1104": [ut.reportsPageLoadChairmanReportTile]
        , "homepage_report_1105": [ut.reportsPageLoadJacicnthaChartFunctionalityTile]
        , "homepage_report_1106": [ut.reportsPageLoadStatsTile]
        , "homepage_report_1107": [ut.reportsPageLoadMultiPostTile]
        , "homepage_report_1108": [ut.reportsPageLoadWeeklyHoursTile]
        , "homepage_report_1109": [ut.reportsPageLoadSurveyorWorkBreakdownTile]
        , "homepage_report_1110": [ut.reportsPageLoadWorkAbsenceApprovalRejectionBreakdownTile]
        , "homepage_report_1111": [ut.reportsPageLoadDelegationReportTile]
        , "homepage_report_1112": [ut.reportsPageLoadTimesheetChangesTile]
        , "homepage_report_1113": [ut.reportsPageLoadSicknessTriggerPointTile]
        , "homepage_report_1114": [ut.reportsPageLoadAttendanceInfoTile]
        , "homepage_report_1115": [ut.reportsPageLoadDayAllocationTile]
        , "homepage_report_1116": [ut.reportsPageLoadRoleAllocationTile]
    }

    web_objects = [
        "homepage_report_1", "homepage_report_2", "homepage_report_3", "homepage_report_4", "homepage_report_5",
        "homepage_report_6", "homepage_report_7", "homepage_report_8", "homepage_report_9", "homepage_report_10",
        "homepage_report_11", "homepage_report_12", "homepage_report_13", "homepage_report_14", "homepage_report_15",
        "homepage_report_16", "homepage_report_17", "homepage_report_18", "homepage_report_19", "homepage_report_20",
        "homepage_report_21", "homepage_report_22", "homepage_report_23", "homepage_report_24", "homepage_report_25",
        "homepage_report_26", "homepage_report_27", "homepage_report_28", "homepage_report_29", "homepage_report_30",
        "homepage_report_31", "homepage_report_32", "homepage_report_1032", "homepage_report_1034", "homepage_report_1035",
        "homepage_report_1036", "homepage_report_1037", "homepage_report_1038", "homepage_report_1039", "homepage_report_1040",
        "homepage_report_1041", "homepage_report_1042", "homepage_report_1043", "homepage_report_1044", "homepage_report_1045",
        "homepage_report_1046", "homepage_report_1047", "homepage_report_1048", "homepage_report_1049", "homepage_report_1051",
        "homepage_report_1052", "homepage_report_1053", "homepage_report_1054", "homepage_report_1058", "homepage_report_1059",
        "homepage_report_1060", "homepage_report_1061", "homepage_report_1062", "homepage_report_1063", "homepage_report_1064",
        "homepage_report_1065", "homepage_report_1066", "homepage_report_1067", "homepage_report_1068", "homepage_report_1069",
        "homepage_report_1070", "homepage_report_1071", "homepage_report_1072", "homepage_report_1073", "homepage_report_1074",
        "homepage_report_1075", "homepage_report_1077", "homepage_report_1078", "homepage_report_1079", "homepage_report_1080",
        "homepage_report_1081", "homepage_report_1083", "homepage_report_1087", "homepage_report_1088", "homepage_report_1089",
        "homepage_report_1090", "homepage_report_1091", "homepage_report_1092", "homepage_report_1093", "homepage_report_1094",
        "homepage_report_1095", "homepage_report_1096", "homepage_report_1098", "homepage_report_1099", "homepage_report_1100",
        "homepage_report_1101", "homepage_report_1102", "homepage_report_1103", "homepage_report_1104", "homepage_report_1105",
        "homepage_report_1106", "homepage_report_1107", "homepage_report_1108","homepage_report_1109", "homepage_report_1110" ,
        "homepage_report_1111", "homepage_report_1112", "homepage_report_1113", "homepage_report_1114" ,"homepage_report_1115" ,
        "homepage_report_1116"
   ]

    
    
    for path in paths:
        df = pd.read_excel(path, sheet_name="reports", engine='openpyxl', header=1)
        
        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\reports\\output_files\\{target_sys}_reports.xlsx'
        

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name="reports", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets["reports"]    

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
                        driver_response = fdi.initialize_driver(headless_mode)    

                        # Retrieve the function from object_processors
                        for target_func in object_processors[object]:
                            try:
                                # Call the retrieved function
                                ut.global_web_object_processor(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                            except Exception as e:
                                print("Error finding Web_Object: ")
                                print(e)
                        driver_response.quit()    

        excel_writer.close()    

        print("[Batch Process Complete]")

# Batch Process Dashboard Reports
# Useful to find what reports will appear under a specific usertype.
# SELECT reporttitle, username FROM (SELECT CONVERT(varchar, USERTYPEID) as usertype_id, USERNAME FROM rf_usertypes WHERE languageid = 2) u inner join rf_Dashboard_Reports_Definition dr ON CHARINDEX(',' + USERTYPE_ID + ',', dr.ReportUsertypeList) >= 1 
def batchProcessUserTypeDashboardReports(target_sys, headless_mode, username, password, paths): 
    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        "homepage_dashboardreport_1": [ut.dashboardReportsSkillsTile]
        , "homepage_dashboardreport_2": [ut.dashboardReportsShortfallsTile]
        , "homepage_dashboardreport_3": [ut.dashboardReportsBankHoursPaidTile]
        , "homepage_dashboardreport_4": [ut.dashboardReportSessionOverrunReasonsTile]
        , "homepage_dashboardreport_5": [ut.dashboardReportSicknessPaidTile]
        , "homepage_dashboardreport_6": [ut.dashboardReportsSeshExpectedVSSeshPlannedTile]
        , "homepage_dashboardreport_7": [ut.dashboardReportsSeshOperateddWithSeshShortfallOrSurplusTile]
        , "homepage_dashboardreport_8": [ut.dashboardReportsStaffingModelTile]
        , "homepage_dashboardreport_9": [ut.dashboardReportsSessionUnavailablityTile]
        , "homepage_dashboardreport_15": [ut.dashboardReportTestAbsenceDropListTile]
        , "homepage_dashboardreport_16": [ut.dashboardReportShortfallsReportTile]
        , "homepage_dashboardreport_17": [ut.dashboardReportRejectedLeaveTile]
        , "homepage_dashboardreport_18": [ut.dashboardReportContractedHoursTile]
        , "homepage_dashboardreport_19": [ut.dashboardReportSkillsListTile]
        , "homepage_dashboardreport_20": [ut.dashboardReportSkillsSummaryTile]
        , "homepage_dashboardreport_32": [ut.dashboardReportTestLeavePeriodDropListTile]
        , "homepage_dashboardreport_33": [ut.dashboardReportAbsenceTile]
        , "homepage_dashboardreport_34": [ut.dashboardReportAbsenceAllowanceTile]
        , "homepage_dashboardreport_35": [ut.dashboardReportCarryForwardRequestsTile]
        , "homepage_dashboardreport_36": [ut.dashboardReportClockingReportsTile]
        , "homepage_dashboardreport_37": [ut.dashboardReportHolidaySlotsTile]
        , "homepage_dashboardreport_38": [ut.dashboardReportSessionsPlannedWithShortfallOrSurplusTile]
        , "homepage_dashboardreport_39": [ut.dashboardReportAnnualLeaveBookByDayTile]
        , "homepage_dashboardreport_40": [ut.dashboardReportAnnualLeaveBookVsAllowanceTile]
        , "homepage_dashboardreport_41": [ut.dashboardReportEmployeeAnnualLeaveAllowanceVsBookedTile]
        , "homepage_dashboardreport_43": [ut.dashboardReportSessionOverrunReasonsTile]
    }

    web_objects = [
        "homepage_dashboardreport_1", "homepage_dashboardreport_2", "homepage_dashboardreport_3", "homepage_dashboardreport_4", "homepage_dashboardreport_5",
        "homepage_dashboardreport_6", "homepage_dashboardreport_7", "homepage_dashboardreport_8", "homepage_dashboardreport_9", "homepage_dashboardreport_15",
        "homepage_dashboardreport_16", "homepage_dashboardreport_17", "homepage_dashboardreport_18", "homepage_dashboardreport_19", "homepage_dashboardreport_20",
        "homepage_dashboardreport_32", "homepage_dashboardreport_33", "homepage_dashboardreport_34", "homepage_dashboardreport_35", "homepage_dashboardreport_36",
        "homepage_dashboardreport_37", "homepage_dashboardreport_38", "homepage_dashboardreport_39", "homepage_dashboardreport_40", "homepage_dashboardreport_41",
        "homepage_dashboardreport_43"
    ]
    
    
    for path in paths:
        df = pd.read_excel(path, sheet_name="dashboard_reports", engine='openpyxl', header=1)
        
        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\dashboard_reports\\output_files\\{target_sys}_dashboard_reports.xlsx'
        

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name="dashboard_reports", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets["dashboard_reports"]    

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
                        driver_response = fdi.initialize_driver(headless_mode)    

                        # Retrieve the function from object_processors
                        for target_func in object_processors[object]:
                            try:
                                # Call the retrieved function
                                ut.global_web_object_processor(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)
                            except Exception as e:
                                print("Error finding Web_Object: ")
                                print(e)
                        driver_response.quit()    

        excel_writer.close()    

        print("[Batch Process Complete]")


#################################################################  ADMIN TABS ###################################################################
# To Note * - Multi excel sheet processing and con-current usertype/location processing:
# peforms better with graphics card, higer memory. Subject to following errors (pc's less than 8gb ram, cpu processor older than i5 generation): 
# GPU - insuffcient resources 
# oom - out of memory

# Excel Processor instances - Process that gets called con - currently for each usertype/location - used to colour excel sheet accordingly. 
#                             Retains state of already coloured cell where the permutation existed instead of being overwritten i.e coloured 'red'
#                             in the case a permuation is checked and finds that the web object does not exist for that permuation.
 

# Main Menu Tabs Excel Processor - con-currently process all user/locations for a given tab
# * No permutation checks need to be made here as with the other tab batch processes as we only perform one to one matches with the tabs that belong
# to a given function call that performs the check for a given usertype/location. Therefore we are only required to color the excel sheet accordingly 
# as opposed to performing pre - matched permutation checks. Hence no class is needed to retain the 'already processed tab'.
def process_location_main_menu_tabs(web_objects, user_type, object_processors, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format):
    for web_object_index, object in enumerate(web_objects, start=1):
        try:
            if object in object_processors:
                driver_response = fdi.initialize_driver(headless_mode)    
                print("--------------------------------")
                print("Number of WebObjects: ", len(web_objects))
                print("Web Object Index: ", web_object_index)
                
                
                for target_func in object_processors[object]:
                    worksheet, tab, cell_state, return_value = gs.global_web_object_processor_main_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object, worksheet, df, green_format, red_format)

                    if return_value == True and cell_state == 'X': 
                        worksheet.write(index + 1, df.columns.get_loc(tab), 'X', green_format)
                       
                    elif return_value == False and cell_state == 'X': 
                        worksheet.write(index + 1, df.columns.get_loc(tab), 'X', red_format)
                    elif return_value == True and cell_state == '': 
                        worksheet.write(index + 1, df.columns.get_loc(tab), '', red_format)    
                    else:
                        pass

                driver_response.quit()

            else: 
                # This will just pass everytime we loop through each object in object_processors until the object matches.
                pass
            
        except Exception as e:
            driver_response.quit()

            print("Error finding Web_Object: ")
            print(e)
            print('^')
            print("Tab does not exist:")
            print("MainMenuTab: ", object)
              
# Batch Process Admin - Main Menu Tabs 
def batchProcessUserTypeAdminMainMenuTabs(target_sys, headless_mode, username, password, paths, client): 

    start_time = time.time()

    #print("batchProcessUserTypeAdminMainMenuTabs")
    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        "Agencies": [a.adminLoadMenuTabs]
        , "Archive": [a.adminLoadMenuTabs]
        , "DNA": [a.adminLoadMenuTabs]
        , "Event": [a.adminLoadMenuTabs]
        , "Events": [a.adminLoadMenuTabs]
        , "External Hire": [a.adminLoadMenuTabs]
        , "Groups": [a.adminLoadMenuTabs]
        , "Home": [a.adminLoadMenuTabs]
        , "Invoicing": [a.adminLoadMenuTabs]
        , "Location Admin": [a.adminLoadMenuTabs]
        , "Pattern Management": [a.adminLoadMenuTabs]
        , "Planning": [a.adminLoadMenuTabs]
        , "Rota Admin": [a.adminLoadMenuTabs]
        , "Scenarios": [a.adminLoadMenuTabs]
        , "Staff Admin": [a.adminLoadMenuTabs]
        , "Staff Admin - UNUSED": [a.adminLoadMenuTabs]
        , "System Admin": [a.adminLoadMenuTabs]
        , "System Configuration": [a.adminLoadMenuTabs]
        , "Tours & Feeders": [a.adminLoadMenuTabs]
        , "Vehicles": [a.adminLoadMenuTabs]
    }

    web_objects = [
        "Agencies", "Archive", "DNA", "Event", "Events",
        "External Hire", "Groups", "Home", "Invoicing", "Location Admin",
        "Pattern Management", "Planning", "Rota Admin", "Scenarios", "Staff Admin",
        "Staff Admin - UNUSED", "System Admin", "System Configuration", "Tours & Feeders ", "Vehicles"
                                                 
    ]

    # Will use to outline total webobjects that will be processed for a given usertype 
    no_of_web_objects = len(web_objects)

    for path in paths:

        print(f"Processing Excel sheet '{path}'...")
        df = pd.read_excel(path, sheet_name=f"{client}", engine='openpyxl', header=0)
        
        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\admin_nav\\main_menu_tabs\\main_menu_tabs_final_output\\{target_sys}_main_menu_options.xlsx'
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name=f"{client}", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets[f"{client}"]    

        # Auto-adjust columns' width
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_width)
       

        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})

        try: 
          with concurrent.futures.ThreadPoolExecutor() as executor:
              futures = []
              for index, row in df.iterrows():
                  user_types = row['FullLocationNames'].split(', ')
                  for user_type in user_types:
                      #print(user_type)
                      futures.append(executor.submit(process_location_main_menu_tabs, web_objects, user_type, object_processors, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format))
              # Wait for all futures to complete     
              concurrent.futures.wait(futures)
        except Exception as e:
            # Handle any exceptions that occur during the process
            print("An error occurred:", e)

        # Write to Excel, print completion message, etc.
        excel_writer.close()    
        print(f"\n[Batch Process Complete - Main Menu Tabs for Excel sheet {path}]")
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print("[Execution time:", elapsed_time, "seconds")  


# Sub Menu Tabs Excel Processor - con-currently process all user/locations for a given tab
class ExcelProcessorSubMenuTabs:
    def __init__(self):
        self.already_processed_sub_tabs = {}


    def process_location_sub_tabs(self, web_objects, user_type, object_processors, obj_type, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format):
        for web_object_index, object in enumerate(web_objects, start=1):
            try:
                if object[obj_type] in object_processors:
                    driver_response = fdi.initialize_driver(headless_mode)    
                    print("--------------------------------")
                    #print("\nUser Type: ", user_type) 
                    print("Number of WebObjects: ", len(web_objects))
                    print("Web Object Index: ", web_object_index)
                    #print("      .")
                    #print("      .")
                    #print("      .")
                    #print("MainMenuTab: ", object['MainMenuTab'])
                    #print("SubMenuTab: ", object['SubMenuTab']) 
                    #print(f"{obj_type}: ", object[obj_type], "\n") 
                    #print("--------------------------------")
                    
                    for target_func in object_processors[object[obj_type]]:
                        #gs.global_web_object_processor_sub_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object['MainMenuTab'], object['SubMenuTab'], object[obj_type], worksheet, df, green_format, red_format)
                        worksheet, tab, cell_state, return_value = gs.global_web_object_processor_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object['MainMenuTab'], object[obj_type], worksheet, df, green_format, red_format)
                        #print(worksheet, tab, cell_state, return_value)

                        # These checks will make sure permutations that contain the same tabs for a given usertype/location dont get overwritten
                        # with the wrong colour in the excel sheet as it will check the tab even once it has matched correctly and found the webobject. 
                        # This is unavoidable as we don't have a list of all the actual permutations that exist in the front end for any given system. 
                        if return_value == True and cell_state == 'X': 
                            if (user_type, object[obj_type]) not in self.already_processed_sub_tabs.items():
                                self.already_processed_sub_sub_tabs[user_type] = object[obj_type]
                                worksheet.write(index + 1, df.columns.get_loc(tab), 'X', green_format)
                            else:
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type[object[obj_type]])
                                pass
                        elif return_value == False and cell_state == 'X': 
                             if (user_type, object[obj_type]) in self.already_processed_sub_tabs.items():
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type, object[obj_type])
                                pass
                             else:
                                worksheet.write(index + 1, df.columns.get_loc(tab), 'X', red_format)
                        elif return_value == True and cell_state == '': 
                            if (user_type, object[obj_type]) not in self.already_processed_sub_tabs.items():
                                self.already_processed_sub_sub_tabs[user_type] = object[obj_type]
                                worksheet.write(index + 1, df.columns.get_loc(tab), '', red_format)
                            else:
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type[object[obj_type]])
                                pass
                        else:
                            pass

                    driver_response.quit()

                else: 
                    # This will just pass everytime we loop through each object in object_processors until the object matches.
                    pass
                
            except Exception as e:
                driver_response.quit()

                print("Error finding Web_Object: ")
                print(e)
                
                print('^')
                print("Tab does not exist for permutation:")
                print("MainMenuTab: ", object['MainMenuTab'])
                print("SubMenuTab: ", object['SubMenuTab']) 

# Sub Sub Tabs Excel Processor - con-currently process all user/locations for a given tab
def batchProcessUserTypeAdminSubMenuTabs(target_sys, headless_mode, username, password, conn_string, paths, client):

    start_time = time.time()

    #print("batchProcessUserTypeAdminSubMenuTabs")
    # Define a mapping from object names to their corresponding processing functions
    object_processors = {   
        "(Archive) Area" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Areas" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Bestway Group " : [a.adminLoadSubMenuTabs]
        ,"(Archive) Department" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Floor" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Level 1" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Level 2" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Level 3" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Level 4" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Level 5" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Location" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Locations" : [a.adminLoadSubMenuTabs]
        ,"(Archive) NOT REQUIRED" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Rota" : [a.adminLoadSubMenuTabs]
        ,"(Archive) Staff" : [a.adminLoadSubMenuTabs]
        ,"A list of Shift Mask Grouping clipboards" : [a.adminLoadSubMenuTabs]
        ,"Absence Type Groups" : [a.adminLoadSubMenuTabs]
        ,"Absence Types" : [a.adminLoadSubMenuTabs]
        ,"Additional Info" : [a.adminLoadSubMenuTabs]
        ,"Agency" : [a.adminLoadSubMenuTabs]
        ,"Airport Lanes" : [a.adminLoadSubMenuTabs]
        ,"Area" : [a.adminLoadSubMenuTabs]
        ,"Area Archive" : [a.adminLoadSubMenuTabs]
        ,"Areas" : [a.adminLoadSubMenuTabs]
        ,"Bestway Group " : [a.adminLoadSubMenuTabs]
        ,"Blood Donation" : [a.adminLoadSubMenuTabs]
        ,"Blood Donation Archive" : [a.adminLoadSubMenuTabs]
        ,"Business" : [a.adminLoadSubMenuTabs]
        ,"Business<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Candidates" : [a.adminLoadSubMenuTabs]
        ,"Client" : [a.adminLoadSubMenuTabs]
        ,"Client Site Portfolios" : [a.adminLoadSubMenuTabs]
        ,"Clients" : [a.adminLoadSubMenuTabs]
        ,"Clients (Area)" : [a.adminLoadSubMenuTabs]
        ,"Clinic Appointments" : [a.adminLoadSubMenuTabs]
        ,"Coaches" : [a.adminLoadSubMenuTabs]
        ,"Company" : [a.adminLoadSubMenuTabs]
        ,"Company Archive" : [a.adminLoadSubMenuTabs]
        ,"Contract" : [a.adminLoadSubMenuTabs]
        ,"Contracts" : [a.adminLoadSubMenuTabs]
        ,"Corporate" : [a.adminLoadSubMenuTabs]
        ,"Corporate Archive" : [a.adminLoadSubMenuTabs]
        ,"Corporate<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Country" : [a.adminLoadSubMenuTabs]
        ,"Country<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Database Errors" : [a.adminLoadSubMenuTabs]
        ,"DataCapture Admin" : [a.adminLoadSubMenuTabs]
        ,"Dataset Admin" : [a.adminLoadSubMenuTabs]
        ,"Day Profile" : [a.adminLoadSubMenuTabs]
        ,"Day Profile Set" : [a.adminLoadSubMenuTabs]
        ,"Department" : [a.adminLoadSubMenuTabs]
        ,"Department<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Departmentyyy" : [a.adminLoadSubMenuTabs]
        ,"Depts Active" : [a.adminLoadSubMenuTabs]
        ,"Depts Archive" : [a.adminLoadSubMenuTabs]
        ,"Directorate" : [a.adminLoadSubMenuTabs]
        ,"Directorate<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"DNA Admin" : [a.adminLoadSubMenuTabs]
        ,"Employee Group" : [a.adminLoadSubMenuTabs]
        ,"Employee Group Archive" : [a.adminLoadSubMenuTabs]
        ,"Employee Groups" : [a.adminLoadSubMenuTabs]
        ,"Employees" : [a.adminLoadSubMenuTabs]
        ,"Equipment Active" : [a.adminLoadSubMenuTabs]
        ,"Equipment Archive" : [a.adminLoadSubMenuTabs]
        ,"Event Groups" : [a.adminLoadSubMenuTabs]
        ,"Fixed" : [a.adminLoadSubMenuTabs]
        ,"Fixed Roles CC" : [a.adminLoadSubMenuTabs]
        ,"Fixed Roles CD WB" : [a.adminLoadSubMenuTabs]
        ,"Floor" : [a.adminLoadSubMenuTabs]
        ,"Gangs" : [a.adminLoadSubMenuTabs]
        ,"Group Archive" : [a.adminLoadSubMenuTabs]
        ,"Groups Active" : [a.adminLoadSubMenuTabs]
        ,"Groups Archive" : [a.adminLoadSubMenuTabs]
        ,"Head Office" : [a.adminLoadSubMenuTabs]
        ,"Hierarchy" : [a.adminLoadSubMenuTabs]
        ,"Hirers Active" : [a.adminLoadSubMenuTabs]
        ,"Hirers Archive" : [a.adminLoadSubMenuTabs]
        ,"Holiday Group" : [a.adminLoadSubMenuTabs]
        ,"Holiday Group Archive" : [a.adminLoadSubMenuTabs]
        ,"Holiday Groups" : [a.adminLoadSubMenuTabs]
        ,"HolidayGroups" : [a.adminLoadSubMenuTabs]
        ,"Homepage Items" : [a.adminLoadSubMenuTabs]
        ,"Homepage Menu" : [a.adminLoadSubMenuTabs]
        ,"Javascript Admin" : [a.adminLoadSubMenuTabs]
        ,"Jobs" : [a.adminLoadSubMenuTabs]
        ,"JS Locations" : [a.adminLoadSubMenuTabs]
        ,"Language Labels" : [a.adminLoadSubMenuTabs]
        ,"Level 1" : [a.adminLoadSubMenuTabs]
        ,"Level 2" : [a.adminLoadSubMenuTabs]
        ,"Level 3" : [a.adminLoadSubMenuTabs]
        ,"Level 4" : [a.adminLoadSubMenuTabs]
        ,"Level 5" : [a.adminLoadSubMenuTabs]
        ,"List Of Agencies" : [a.adminLoadSubMenuTabs]
        ,"List of Agency Employees" : [a.adminLoadSubMenuTabs]
        ,"List of Agency Staff" : [a.adminLoadSubMenuTabs]
        ,"List of all Lane Clipboards" : [a.adminLoadSubMenuTabs]
        ,"List of all Locations" : [a.adminLoadSubMenuTabs]
        ,"List of all Skill Clipboards" : [a.adminLoadSubMenuTabs]
        ,"List of Chutes" : [a.adminLoadSubMenuTabs]
        ,"List of Clinics" : [a.adminLoadSubMenuTabs]
        ,"List Of Contact Labels" : [a.adminLoadSubMenuTabs]
        ,"List of Divisions" : [a.adminLoadSubMenuTabs]
        ,"List of Employees" : [a.adminLoadSubMenuTabs]
        ,"List of Events" : [a.adminLoadSubMenuTabs]
        ,"List of Fixed Requirements" : [a.adminLoadSubMenuTabs]
        ,"List of Groups" : [a.adminLoadSubMenuTabs]
        ,"List of Location Labels" : [a.adminLoadSubMenuTabs]
        ,"List of Locations" : [a.adminLoadSubMenuTabs]
        ,"List of Model Event Staff" : [a.adminLoadSubMenuTabs]
        ,"List of Patients" : [a.adminLoadSubMenuTabs]
        ,"List of Shearings Drivers Staff" : [a.adminLoadSubMenuTabs]
        ,"List of Shearings Hotel Staff" : [a.adminLoadSubMenuTabs]
        ,"List of Staff Skills" : [a.adminLoadSubMenuTabs]
        ,"List of Usertypes" : [a.adminLoadSubMenuTabs]
        ,"Lists of people" : [a.adminLoadSubMenuTabs]
        ,"Local Authorities" : [a.adminLoadSubMenuTabs]
        ,"Location" : [a.adminLoadSubMenuTabs]
        ,"Location Category" : [a.adminLoadSubMenuTabs]
        ,"Location Category<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Location<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Locations" : [a.adminLoadSubMenuTabs]
        ,"Main Offices" : [a.adminLoadSubMenuTabs]
        ,"Managers" : [a.adminLoadSubMenuTabs]
        ,"Manifest Admin" : [a.adminLoadSubMenuTabs]
        ,"MAT Active" : [a.adminLoadSubMenuTabs]
        ,"MAT Archive" : [a.adminLoadSubMenuTabs]
        ,"My Email Templates" : [a.adminLoadSubMenuTabs]
        ,"NHSBT Root" : [a.adminLoadSubMenuTabs]
        ,"NHSBT Root Archive" : [a.adminLoadSubMenuTabs]
        ,"NOT REQUIRED" : [a.adminLoadSubMenuTabs]
        ,"Nurses" : [a.adminLoadSubMenuTabs]
        ,"Operations" : [a.adminLoadSubMenuTabs]
        ,"Pattern Groups" : [a.adminLoadSubMenuTabs]
        ,"Pay Support" : [a.adminLoadSubMenuTabs]
        ,"Planned Event" : [a.adminLoadSubMenuTabs]
        ,"PortRoot" : [a.adminLoadSubMenuTabs]
        ,"PortRootActive" : [a.adminLoadSubMenuTabs]
        ,"PortRootArchive" : [a.adminLoadSubMenuTabs]
        ,"Project Ref No." : [a.adminLoadSubMenuTabs]
        ,"Projects" : [a.adminLoadSubMenuTabs]
        ,"Region" : [a.adminLoadSubMenuTabs]
        ,"Region Archive" : [a.adminLoadSubMenuTabs]
        ,"Regions Active" : [a.adminLoadSubMenuTabs]
        ,"Requirements" : [a.adminLoadSubMenuTabs]
        ,"Role Sets" : [a.adminLoadSubMenuTabs]
        ,"Roles" : [a.adminLoadSubMenuTabs]
        ,"Rota" : [a.adminLoadSubMenuTabs]
        ,"Rota Periods" : [a.adminLoadSubMenuTabs]
        ,"Scenarios" : [a.adminLoadSubMenuTabs]
        ,"Scenarios Root" : [a.adminLoadSubMenuTabs]
        ,"School Grade Active" : [a.adminLoadSubMenuTabs]
        ,"School Grade Archive" : [a.adminLoadSubMenuTabs]
        ,"School Plans" : [a.adminLoadSubMenuTabs]
        ,"School Site Active" : [a.adminLoadSubMenuTabs]
        ,"School Site Archive" : [a.adminLoadSubMenuTabs]
        ,"Schools Active" : [a.adminLoadSubMenuTabs]
        ,"Schools Archive" : [a.adminLoadSubMenuTabs]
        ,"ScotMid Head Office" : [a.adminLoadSubMenuTabs]
        ,"Section Ref No." : [a.adminLoadSubMenuTabs]
        ,"Sectors" : [a.adminLoadSubMenuTabs]
        ,"Senior Sisters" : [a.adminLoadSubMenuTabs]
        ,"Sessions" : [a.adminLoadSubMenuTabs]
        ,"Sessions Archive" : [a.adminLoadSubMenuTabs]
        ,"Shift Availability" : [a.adminLoadSubMenuTabs]
        ,"Shift Patterns" : [a.adminLoadSubMenuTabs]
        ,"Shift Priorities" : [a.adminLoadSubMenuTabs]
        ,"Shift Times" : [a.adminLoadSubMenuTabs]
        ,"Skill Sets" : [a.adminLoadSubMenuTabs]
        ,"Skills" : [a.adminLoadSubMenuTabs]
        ,"SLAs" : [a.adminLoadSubMenuTabs]
        ,"Staff" : [a.adminLoadSubMenuTabs]
        ,"Star" : [a.adminLoadSubMenuTabs]
        ,"Stored Procedures and Functions" : [a.adminLoadSubMenuTabs]
        ,"Stores Active" : [a.adminLoadSubMenuTabs]
        ,"Sub Depts Active" : [a.adminLoadSubMenuTabs]
        ,"Sub Depts Archive" : [a.adminLoadSubMenuTabs]
        ,"Sub-Division" : [a.adminLoadSubMenuTabs]
        ,"System Admin" : [a.adminLoadSubMenuTabs]
        ,"System Configuration" : [a.adminLoadSubMenuTabs]
        ,"TA Rule Sets" : [a.adminLoadSubMenuTabs]
        ,"TA Rules" : [a.adminLoadSubMenuTabs]
        ,"Team" : [a.adminLoadSubMenuTabs]
        ,"Team Archive" : [a.adminLoadSubMenuTabs]
        ,"Template Admin" : [a.adminLoadSubMenuTabs]
        ,"Training Centres" : [a.adminLoadSubMenuTabs]
        ,"Training Centres Archive" : [a.adminLoadSubMenuTabs]
        ,"Types of Clipboards" : [a.adminLoadSubMenuTabs]
        ,"User Skills" : [a.adminLoadSubMenuTabs]
        ,"Usertypes" : [a.adminLoadSubMenuTabs]
        ,"Venue" : [a.adminLoadSubMenuTabs]
        ,"Venue Archive" : [a.adminLoadSubMenuTabs]
        ,"Venues Active" : [a.adminLoadSubMenuTabs]
        ,"Venues Archive" : [a.adminLoadSubMenuTabs]
        ,"Vessel Department" : [a.adminLoadSubMenuTabs]
        ,"Vessel Department<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Vessel Sub-Department" : [a.adminLoadSubMenuTabs]
        ,"Vessel Sub-Department<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"Vessels" : [a.adminLoadSubMenuTabs]
        ,"Vessels<br>Archive" : [a.adminLoadSubMenuTabs]
        ,"WebScripts Admin" : [a.adminLoadSubMenuTabs]
        ,"Website Admin" : [a.adminLoadSubMenuTabs]
        ,"Working Location Active" : [a.adminLoadSubMenuTabs]
        ,"Workplace" : [a.adminLoadSubMenuTabs]
        ,"Zones" : [a.adminLoadSubMenuTabs]
    }


    # This will establish an array of key value pairs where there is a submenu option in use which belongs to a given main menu option. 
    # Will likely not contain every sub menu tab in a given system as is not in use. 
    # Therefore will not check for the existence of a tab that is not marked with an 'X' as it could not be in use through the front end as it has not been configured in the backend. 
    # The arrays purpose is to act as a map with all the pinpoints marked so we know where we need to navigate to. If we get there and the tab doesnt exist, there is a potential front end issue. 
    # This differs from usertiles as we did not auto populate our excel sheets using backend configuration, hence we would check for the existence of a tile even if it wasnt labelled with an 'X'
    # as we possibly may have missed a webobject that should appear for a give usertype/location name.  
    web_objects = bp.getCorrespondingMainMenuAndSubMenuTabsForAGivenSystem(conn_string)

    # Will use to outline total webobjects that will be processed for a given usertype 
    no_of_web_objects = len(web_objects)

    obj_type = 'SubMenuTab' # Object type we want to target

    for path in paths:
        # Create a new instance of ExcelProcessor - will be used to retain submenu tabs that have already been confirmed as existing.
        #                                         - will skip over evaluation and updating colour of cell in the case this condition has already been met. 
        #                                         - This is because there a multiple permutations that are evluated for the associated main menu and sub menu tabs.   
        excel_processor = ExcelProcessorSubMenuTabs()
        
        print(f"Processing Excel sheet '{path}'...")
        df = pd.read_excel(path, sheet_name=f"{client}", engine='openpyxl', header=0)
        
        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\admin_nav\\sub_menu_tabs\\sub_menu_tabs_final_output\\{target_sys.lower}_sub_menu_options.xlsx'
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name="sub menu", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets["sub menu"]    

        # Auto-adjust columns' width
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_width)
       

        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})

        try: 
          with concurrent.futures.ThreadPoolExecutor() as executor:
              futures = []
              for index, row in df.iterrows():
                  user_types = row['FullLocationNames'].split(', ')
                  for user_type in user_types:
                      #print(user_type)
                      futures.append(executor.submit(excel_processor.process_location_sub_tabs, web_objects, user_type, object_processors, obj_type, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format))
              # Wait for all futures to complete     
              concurrent.futures.wait(futures)
        except Exception as e:
            # Handle any exceptions that occur during the process
            print("An error occurred:", e)

        # Write to Excel, print completion message, etc.
        excel_writer.close()    
        print(f"\n[Batch Process Complete - Sub Menu Tabs for Excel sheet {path}]")
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print("[Execution time:", elapsed_time, "seconds")  

        excel_writer.close()    

        print("[Batch Process Complete]")


class ExcelProcessorSubSubTabs:
    def __init__(self):
        self.already_processed_sub_sub_tabs = {}

    def process_location_sub_sub_tabs(self, web_objects, user_type, object_processors, obj_deriv_table, obj_type, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format):
        for web_object_index, object in enumerate(web_objects, start=1):
            try:
                if object[obj_type] in object_processors[obj_deriv_table]:

                    driver_response = fdi.initialize_driver(headless_mode)
                    print("--------------------------------")
                    #print("\nUser Type: ", user_type) 
                    print("Number of WebObjects: ", len(web_objects))
                    print("Web Object Index: ", web_object_index)
                    #print("      .")
                    #print("      .")
                    #print("      .")
                    #print("MainMenuTab: ", object['MainMenuTab'])
                    #print("SubMenuTab: ", object['SubMenuTab']) 
                    #print(f"{obj_type}: ", object[obj_type], "\n") 
                    #print("--------------------------------")
                    
                    for target_func in object_processors[obj_deriv_table][object[obj_type]]:
                        #gs.global_web_object_processor_sub_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object['MainMenuTab'], object['SubMenuTab'], object[obj_type], worksheet, df, green_format, red_format)
                        worksheet, tab, cell_state, return_value = gs.global_web_object_processor_sub_sub_menu_tabs(target_func, headless_mode, target_sys, username, password, driver_response, user_type, index, row, object['MainMenuTab'], object['SubMenuTab'], object[obj_type], worksheet, df, green_format, red_format)
                        #print(worksheet, tab, cell_state, return_value)

                        # These checks will make sure permutations that contain the same tabs for a given usertype/location dont get overwritten
                        # with the wrong colour in the excel sheet as it will check the tab even once it has matched correctly and found the webobject. 
                        # This is unavoidable as we don't have a list of all the actual permutations that exist in the front end for any given system. 
                        if return_value == True and cell_state == 'X': 
                            if (user_type, object[obj_type]) not in self.already_processed_sub_sub_tabs.items():
                                self.already_processed_sub_sub_tabs[user_type] = object[obj_type]
                                worksheet.write(index + 1, df.columns.get_loc(tab), 'X', green_format)
                            else:
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type[object[obj_type]])
                                pass
                        elif return_value == False and cell_state == 'X': 
                             if (user_type, object[obj_type]) in self.already_processed_sub_sub_tabs.items():
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type, object[obj_type])
                                pass
                             else:
                                worksheet.write(index + 1, df.columns.get_loc(tab), 'X', red_format)
                        elif return_value == True and cell_state == '': 
                            if (user_type, object[obj_type]) not in self.already_processed_sub_sub_tabs.items():
                                self.already_processed_sub_sub_tabs[user_type] = object[obj_type]
                                worksheet.write(index + 1, df.columns.get_loc(tab), '', red_format)
                            else:
                                #print(already_processed_sub_sub_tabs)
                                #print(user_type[object[obj_type]])
                                pass
                        else:
                            pass

                    driver_response.quit()

                else: 
                    # This will just pass everytime we loop through each object in object_processors until the object matches.
                    pass
                
            except Exception as e:
                driver_response.quit()

                print("Error finding Web_Object: ")
                print(e)
                
                print('^')
                print("Tab does not exist for permutation:")
                print("MainMenuTab: ", object['MainMenuTab'])
                print("SubMenuTab: ", object['SubMenuTab']) 
                print(f"{obj_type}: ", object[obj_type], "\n") 

# Batch Process Admin - Sub Sub Menu Tabs
def batchProcessUserTypeAdminSubSubMenuTabs(target_sys, headless_mode, username, password, conn_string, paths, client, meta_tab_type=None):
    
    #print("batchProcessUserTypeAdminSubSubMenuTabs")
    
    start_time = time.time()

    # Define a mapping from object names to their corresponding processing functions
    object_processors = { 
        "rf_Contacts_Tabs": {
            "1.test": [a.adminLoadSubSubMenuTabs]
            ,"1.test" : [a.adminLoadSubSubMenuTabs]
            ,"Days Off": [a.adminLoadSubSubMenuTabs]
            ,"Access Roles": [a.adminLoadSubSubMenuTabs]
            ,"Additional"	: [a.adminLoadSubSubMenuTabs]
            ,"Ad-Hoc Rates": [a.adminLoadSubSubMenuTabs]
            ,"Agency Document Checklist": [a.adminLoadSubSubMenuTabs]
            ,"Attendance Info": [a.adminLoadSubSubMenuTabs]
            ,"Clocking": [a.adminLoadSubSubMenuTabs]
            ,"Contract": [a.adminLoadSubSubMenuTabs]
            ,"Departments"	: [a.adminLoadSubSubMenuTabs]
            ,"Deprecated": [a.adminLoadSubSubMenuTabs]
            ,"Details": [a.adminLoadSubSubMenuTabs]
            ,"Documents": [a.adminLoadSubSubMenuTabs]
            ,"Kaba": [a.adminLoadSubSubMenuTabs]
            ,"Locations"	: [a.adminLoadSubSubMenuTabs]
            ,"Mileage Type": [a.adminLoadSubSubMenuTabs]
            ,"Notes": [a.adminLoadSubSubMenuTabs]
            ,"OBS Info": [a.adminLoadSubSubMenuTabs]
            ,"Open People": [a.adminLoadSubSubMenuTabs]
            ,"Payroll": [a.adminLoadSubSubMenuTabs]
            ,"Personal": [a.adminLoadSubSubMenuTabs]
            ,"Personal Contacts": [a.adminLoadSubSubMenuTabs]
            ,"Sectors / Types": [a.adminLoadSubSubMenuTabs]
            ,"Self Service": [a.adminLoadSubSubMenuTabs]
            ,"Documents": [a.adminLoadSubSubMenuTabs]
            ,"Shift Mask" : [a.adminLoadSubSubMenuTabs]
            ,"Groupings": [a.adminLoadSubSubMenuTabs]
            ,"Skills": [a.adminLoadSubSubMenuTabs]
            ,"SLA Addtional Detail": [a.adminLoadSubSubMenuTabs]
            ,"SLA Departments": [a.adminLoadSubSubMenuTabs]
            ,"SLA Detail": [a.adminLoadSubSubMenuTabs]
            ,"SLA Locations": [a.adminLoadSubSubMenuTabs]
            ,"Vehicle Details": [a.adminLoadSubSubMenuTabs]
        }
        , "rf_Location_Tabs": { 
              "Demand Engine Settings": [a.adminLoadSubSubMenuTabs]
              , "Event List": [a.adminLoadSubSubMenuTabs]
              , "Holiday Group Includes": [a.adminLoadSubSubMenuTabs]
              , "Member list": [a.adminLoadSubSubMenuTabs]
              , "Allocated Muster": [a.adminLoadSubSubMenuTabs]
              , "System Branding": [a.adminLoadSubSubMenuTabs]
              , "Pre and Post": [a.adminLoadSubSubMenuTabs]
              , "Timezones": [a.adminLoadSubSubMenuTabs]
              , "Element Codes": [a.adminLoadSubSubMenuTabs]
              , "Allowances": [a.adminLoadSubSubMenuTabs]
              , "Price Rates": [a.adminLoadSubSubMenuTabs]
              , "Budget Collation": [a.adminLoadSubSubMenuTabs]
              , "Rule Sets": [a.adminLoadSubSubMenuTabs]
              , "Hours Budgets": [a.adminLoadSubSubMenuTabs]
              , "Copy Event": [a.adminLoadSubSubMenuTabs]
              , "Port Info": [a.adminLoadSubSubMenuTabs]
              , "Notes": [a.adminLoadSubSubMenuTabs]
              , "Mileage Type": [a.adminLoadSubSubMenuTabs]
              , "Configuration": [a.adminLoadSubSubMenuTabs]
              , "Work Places": [a.adminLoadSubSubMenuTabs]
              , "Mileage Override": [a.adminLoadSubSubMenuTabs]
              , "Clocking": [a.adminLoadSubSubMenuTabs]
              , "Agency Rates": [a.adminLoadSubSubMenuTabs]
              , "FTE Hours": [a.adminLoadSubSubMenuTabs]
              , "Auto Publish Rota": [a.adminLoadSubSubMenuTabs]
              , "Role/Rates": [a.adminLoadSubSubMenuTabs]
              , "Additional Details": [a.adminLoadSubSubMenuTabs]
              , "Clocking Settings": [a.adminLoadSubSubMenuTabs]
              , "Agency Tiers": [a.adminLoadSubSubMenuTabs]
              , "Establishments": [a.adminLoadSubSubMenuTabs]
              , "Shift Pattern": [a.adminLoadSubSubMenuTabs]
              , "Days Off": [a.adminLoadSubSubMenuTabs]
              , "Event Builder": [a.adminLoadSubSubMenuTabs]
              , "Special Days": [a.adminLoadSubSubMenuTabs]
              , "Minimum Staffing Template": [a.adminLoadSubSubMenuTabs]
              , "Shifts": [a.adminLoadSubSubMenuTabs]
              , "Additional Details": [a.adminLoadSubSubMenuTabs]
              , "Documents": [a.adminLoadSubSubMenuTabs]
              , "Mileage Rates": [a.adminLoadSubSubMenuTabs]
              , "Additional NHSBT": [a.adminLoadSubSubMenuTabs]
              , "Leave Period": [a.adminLoadSubSubMenuTabs]
              , "Preview": [a.adminLoadSubSubMenuTabs]
              , "Regular Event": [a.adminLoadSubSubMenuTabs]
              , "Linked Events": [a.adminLoadSubSubMenuTabs]
              , "Rates": [a.adminLoadSubSubMenuTabs]
              , ",56,75, Block Leave Days": [a.adminLoadSubSubMenuTabs]
              , "Job Codes": [a.adminLoadSubSubMenuTabs]
              , "Notifications": [a.adminLoadSubSubMenuTabs]
              , "Vessel Info": [a.adminLoadSubSubMenuTabs]
              , "SLAS": [a.adminLoadSubSubMenuTabs]
              , "Holiday Type": [a.adminLoadSubSubMenuTabs]
              , "Timesheet Configuration": [a.adminLoadSubSubMenuTabs]
              , "Tax Rates": [a.adminLoadSubSubMenuTabs]
              , "Budgets": [a.adminLoadSubSubMenuTabs]
              , "Logo": [a.adminLoadSubSubMenuTabs]
              , "Billing Client": [a.adminLoadSubSubMenuTabs]
              , "Demand Metrics": [a.adminLoadSubSubMenuTabs]
              , "Demand Data": [a.adminLoadSubSubMenuTabs]
              , "NEW_TAB": [a.adminLoadSubSubMenuTabs]
              , "Equipment": [a.adminLoadSubSubMenuTabs]
              , "Apply": [a.adminLoadSubSubMenuTabs]
              , "Test.Days Off": [a.adminLoadSubSubMenuTabs]
              , "Financial Document Details": [a.adminLoadSubSubMenuTabs]
        }
        , "rf_Absence_Types_Tabs": {
              "Configuration": [a.adminLoadSubSubMenuTabs]
              , "Primary Reason": [a.adminLoadSubSubMenuTabs]
              , "Secondary Reason": [a.adminLoadSubSubMenuTabs]
        }
        , "rf_Shift_Mask_Tabs": { 
            "Details": [a.adminLoadSubSubMenuTabs]
            , "Shift Alternatives": [a.adminLoadSubSubMenuTabs]
        }
    }


    # This will establish an array of key value pairs where there is a subsubmenu tab  which belongs to submenu tab which belongs to a given main menu tab. 
    # Will likely not contain every subsub menu tab/sub menu tab in a given system as is not in use. 
    # Therefore will not check for the existence of a tab that is not marked with an 'X' as it could not be in use through the front end as it has not been configured in the backend. 
    # The arrays purpose is to act as a map with all the pinpoints marked so we know where we need to navigate to. If we get there and the tab doesnt exist, there is a potential front end issue. 
    # This differs from usertiles as we did not auto populate our excel sheets using backend configuration, hence we would check for the existence of a tile even if it wasnt labelled with an 'X'
    # as we possibly may have missed a webobject that should appear for a give usertype/location name.  
    web_objects = bp.getCorrespondingMainMenuAndSubMenuTabsForAGivenSystemAndSubSubMenuTabs(conn_string)

    # Will use to outline total webobjects that will be processed for a given usertype 
    no_of_web_objects = len(web_objects)


    def process_excel_sheet(path, meta_tab_type=None):

        # If we pass just path and a manually inputted meta_tab_type then we ignore
        if meta_tab_type != None:
            pass
        # Otherwise, the path pass will contain both the path and the meta data type associated with it
        else: 
            path, meta_tab_type = path

        # Create a new instance of ExcelProcessor for each Excel sheet
        excel_processor = ExcelProcessorSubSubTabs()
        
        print(f"Processing Excel sheet '{path}'...")
        df = pd.read_excel(path, sheet_name=f"{client}", engine='openpyxl', header=0)

        # Define the output file path, overwriting if it already exists
        output_path =  f'..\\excel_sheets\\admin_nav\\sub_sub_menu_tabs\\sub_sub_menu_tabs_final_output\\{target_sys.lower()}_sub_sub_{meta_tab_type.lower()}_menu_tabs.xlsx'
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        df.to_excel(excel_writer, sheet_name=f"{meta_tab_type}", index=False)
        workbook = excel_writer.book
        worksheet = excel_writer.sheets[f"{meta_tab_type}"] 


        # Auto-adjust columns' width
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_width)

        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})

        if meta_tab_type == 'CONTACT': 
            obj_deriv_table = 'rf_Contacts_Tabs'
            obj_type = 'SubSubMenuContactTab'
        elif meta_tab_type == 'LOCATION': 
            obj_deriv_table = 'rf_Location_Tabs'
            obj_type = 'SubSubMenuTabLocTab'
        elif meta_tab_type == 'ABSENCE':
            obj_deriv_table = 'rf_Absence_Types_Tabs'
            obj_type = 'SubSubMenuTabAbsenceType'
        elif meta_tab_type == 'SHIFTMASK':
            obj_deriv_table = 'rf_Shift_Mask_Tabs'
            obj_type = 'SubSubMenuTabShiftMask'

        try: 
          with concurrent.futures.ThreadPoolExecutor() as executor:
              futures = []
              for index, row in df.iterrows():
                  user_types = row['FullLocationNames'].split(', ')
                  for user_type in user_types:
                      #print(user_type)
                      futures.append(executor.submit(excel_processor.process_location_sub_sub_tabs, web_objects, user_type, object_processors, obj_deriv_table, obj_type, target_sys, headless_mode, username, password, index, row, worksheet, df, green_format, red_format))
              # Wait for all futures to complete     
              concurrent.futures.wait(futures)
        except Exception as e:
            # Handle any exceptions that occur during the process
            print("An error occurred:", e)

        # Write to Excel, print completion message, etc.
        excel_writer.close()    
        print(f"\n[Batch Process Complete - {meta_tab_type} Tabs for Excel sheet {path}]")
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print("[Execution time:", elapsed_time, "seconds")
    
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each Excel sheet processing task to the executor
        futures = [executor.submit(process_excel_sheet, path, meta_tab_type) for path in paths]
       
        # Wait for all futures to complete
        concurrent.futures.wait(futures)

    print(f"\n[End of Processing]")
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("\nExecution time:", elapsed_time, "seconds")


# Will process all 'Admin' Tabs for a given language
def batch_process_all_admin_tabs(target_sys, headless_mode, username, password, conn_string, client):
    
    # We initially run the excel setup functions for all tab types
    main_menu_path, sub_menu_path, contact_path, loc_path, absence_path, shiftmask_path = bp.populateExcelSheetsWithAllTabTypes(conn_string, client)

    # Paths for created excel sheets for different functions
    paths_for_main_menu_tabs = main_menu_path
    paths_for_sub_menu_tabs = sub_menu_path
    paths_for_sub_sub_menu_tabs = paths_for_sub_sub_menu_tabs = [(contact_path, 'CONTACT')
                                                                 , (loc_path, 'LOCATION')
                                                                 , (absence_path, 'ABSENCE')
                                                                 , (shiftmask_path, 'SHIFTMASK')
                                                                ]
    

    # Batch process functions along with their corresponding paths
    batch_processes = [
        (batchProcessUserTypeAdminMainMenuTabs, paths_for_main_menu_tabs),
        (batchProcessUserTypeAdminSubMenuTabs, paths_for_sub_menu_tabs),
        (batchProcessUserTypeAdminSubSubMenuTabs, paths_for_sub_sub_menu_tabs)
    ]

    #for process, paths in batch_processes:
    #    print("Process: ", process, "Paths:", paths)
    #for path, meta_tab_type in paths:
    #    print("Path:", path, "Meta Tab Type:", meta_tab_type)

    # We then run each batch process on its own thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each Excel sheet processing task to the executor
        futures = []
        for process, paths in batch_processes:
            #print("Process: ", process, "Paths:", paths)
            #print(paths)
            #print(True)

            # Only batch process that doesn't require a connection string
            if process == batchProcessUserTypeAdminMainMenuTabs:
                array_plug_in = [paths] # Has to be in this format as excel sheets processed as a list of strings in an array
                futures.append(
                    executor.submit(process, target_sys, headless_mode, username, password, array_plug_in, client)
                )      
            elif process == batchProcessUserTypeAdminSubMenuTabs:
                array_plug_in = [paths]
                futures.append(
                    executor.submit(process, target_sys, headless_mode, username, password, conn_string, array_plug_in, client)
                )  
            # Only batch process that has its paths in array format by default - array format contains tuple comma seperated list
            else:
                futures.append(
                    executor.submit(process, target_sys, headless_mode, username, password, conn_string, paths, client)
                )                            
        try:
            # Concurrent execution code
            concurrent.futures.wait(futures)
            print(futures)
        except Exception as e:
            print("Exception occurred during concurrent execution:", e)
            # Handle the exception appropriately


#Batch process 
############################################################### END OF ADMIN TABS ##################################################################

# [Future batch processes]:

# Management Tabs
# Data Processing Tabs
# Bank Tabs
# Self Service Tabs
# Reports Tabs
# Reports Dashboard Tabs
# About Tabs

if __name__ == "__main__" : 

    target_sys = ''
    target_sys_db = '' + '_SQL'
    client = ""
    meta_tab_type = 'CONTACT'
    #meta_tab_type = 'LOCATION'
    #meta_tab_type = 'ABSENCE'
    #meta_tab_type = 'SHIFTMASK'

    ascii_title_art = "BugSplatter - Test Environment"

    #excel_sheets = m.processExcelSheets(ascii_title_art, client)

    #print(excel_sheets)

    headless_mode = m.setHeadlessMode(target_sys)

    ### redfining for readability within the connection string
    db = target_sys_db

    ### Will fetch dns/port based on default target system given to bugSplatter on inital startup
    server = bp.get_server_auto(db)

    ### Temporarily assign for backend connection
    username = ""
    password = "!"

    conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'


    ### reassign for front end connection
    username = '' # 'your_username'
    password = '' # 'your_password'

    #batchProcessUserTypeAdminMainMenuTabs(target_sys, headless_mode, username, password, excel_sheets, client)
    #batchProcessUserTypeAdminSubMenuTabs(target_sys, headless_mode, username, password, conn_string, excel_sheets, client)
    #batchProcessUserTypeAdminSubSubMenuTabs(target_sys, headless_mode, username, password, conn_string, excel_sheet, client, meta_tab_type)
    batch_process_all_admin_tabs(target_sys, headless_mode, username, password, conn_string, client)

