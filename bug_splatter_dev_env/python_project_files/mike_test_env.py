import globals as gs
import menu_items as mi
import admin as sa
import f_driver_init as fdi 
from selenium.webdriver.support.ui import WebDriverWait
from colorama import Fore, Style, init

def test_container_name_refresh(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None):
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
            
            sa.staffAdminLoadMenuOptions(target_sys, headless_mode, user_type, username, password, driver_response, True)


            
            clickManifestSubMenuItem(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def staffAdminLoadSkillSets(target_sys, headless_mode, user_type, username, password, driver_response=None, optional_error_catch=None): 
    def clickSkillSetsButton(driver_response): 
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
        clickSkillSetsButton(driver_response)
    else: 
        try: 
            gs.loginAndLoadHomePage(target_sys, headless_mode, username, password, driver_response, True)

            gs.checkUserRoleAndSwitch(driver_response, target_sys, user_type)
           
            mi.homePageLoadAdminMenuItem(target_sys, headless_mode, username, password, driver_response, True)

            sa.staffAdminLoadMenuOptions(target_sys, headless_mode, username, password, driver_response, True)

            clickSkillSetsButton(driver_response)

            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)


def clickSkillSetsButton(driver_response): 
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



#if __name__ == "__main__":