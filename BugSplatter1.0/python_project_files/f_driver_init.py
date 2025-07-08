from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.service import Service
import os
import sys
import logging


# Only implement in compiled build 
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def initialize_driver(headless_mode):
    # Set the path to the Chromium binary
    chromium_binary_path = '..\Win_x64_1135619_chrome-win\chrome-win\chrome.exe'  # Replace with the actual path on your system
    
    # Set Chrome driver path
    chrome_driver_path = os.path.join(os.getcwd(), "..\chromedriver_win32\chromedriver.exe")

    # Create Chrome options and set browser capabilities
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromium_binary_path  # Specify the Chromium binary path
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--headless")

    if headless_mode:
       # If headless mode is requested, add the headless argument
       chrome_options.add_argument("--headless")
       chrome_options.add_argument("--window-size=1920,1080") # Common and provides a good balance between size and compatibility for most websites.

    # Create the Chrome service with the path to ChromeDriver
    chrome_service = ChromeService(executable_path=chrome_driver_path, log_path="chromedriver.log")

    # Set the desired log level to suppress DevTools messages
    logging.basicConfig(level=logging.ERROR)

    try:
        # Initialize the Chrome WebDriver with the service and options
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    except Exception as e:
        raise e
    return driver