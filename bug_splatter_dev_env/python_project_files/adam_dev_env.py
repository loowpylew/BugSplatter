import f_driver_init as fdi # File that connects to Driver
import globals as gs # File that holds functions to perform generic tasks - use 'gs' as an alias to call funtions from file i.e. gs.gs.loginToUserAccount(target_sys, username, password, driver_response, True)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init

# Before starting anything, make a Github account and i can add you as a collaborator so that you can access the BugBuster Project.
# If you dont know how to do this, then there are multiple youtube videos and online sources you can find to get you in the swing of all things Github. 

# This is a private repo for obvious reasons -
# so that any old folk can't just use our code for their own personal consumption/steal. 

# From here, you'll be able to clone the project to your local pc and make changes to this file. 
# This file will exist within the following folder '/bug_splatter_dev_env/python_project_files/adam_dev_env.py 
# Please do not attempt at editing any other files as these are part of the project build.


# You'll also need to download: 

# - Chromium 
# - ChromeDriver 

# Of which can be downloaded from a demo build on our sharepoint: 
# You will need an account to access this so potentially talk to Gen to get that done for you. 

# These files will have to be copied as seperate folders outside of the /python_projects_file in order for the functions to call the browser i.e. 

# Folder structure we want to replicate so that all folders/files are in the correct location in order to run code: 

#/BugSplatter - ROOT level folder 
#    /python_projects_file
#    /excel_sheets
#    /json_config
#    /chromedriver_win_32
#    /Winx64_1135619_chome-win
#    etc...

# Pretty much, once you've copied the repo to a file location on your local pc and downloaded the BugBuster1.0.zip from sharepoint. 
# Create a folder called /BugSplatter and copy everything from /bug_splatter_dev_env into /BugSplatter root level folder.
# Then unzip BugBuster1.0.zip and copy both /chromedriver_win_32 and /Winx64_1135619_chome-win within /BugSplatter root level folder
# You should now have a working environment which you can use to run new fucntions within this file. 
# Id suggest using visual studio code as it is the development envirnment used to write BugSplatter. 

# You will likely get a load of errors upon trying to run this file, this is because you will not have python installed: 
# Verison i have on my work PC: Python 3.11.5
# Once you install python of which there are many tutorials online on how to do, you will have to use a command called pip to install work packages as you can see are called 
# at the begining of the file like so: 
# command to enter in the terminal: 
# pip install -r req.txt or whereever you decide to put the txt file, in my case: 
#                                                                                 then pip install -r req.txt                                                                       
# This file should be copied over from bugsplatter_dev_env and is housed within bug_splatter_dev_env/Notes/req.txt
# In order to run the file prompt the following in vs studio terminal: 

# Naviagte to where the file is housed: 
# 
# Then run the file: 
# python adam_dev_env.py



# Main takeaways: 
#  How to structure a singular function as shown below
#  File that holds generic functions 'globals.py' will be the main focus unless you wanna create more complicated functions i.e. batch processes and overnight processes. 
#  To Note* Only edit this file. If you want to use existing functions to plug into a singular function you're creating, search for the function in the files within 
#           'python_project_folders'. Pretty much, you can call functions from the project build in this function if there is some repeat fucntionality you need to use i.e. login
#            Once you've made functions you deem to be useful, I will review and add to the project for use.  
# Run your functions within the main loop 'if __name__ == "__main__' to test them. 
# If you don't understand the structure, use chatgbt to explain it to you in depth, but i'm sure you'll understand it pretty easily. 

# The purpose of this structure is so that we can plug the function in other fucntions without disturbing the runtime of a new function
# as well as to create the function to report back whether the test was succesful or not. 


# Example function
# Login and Load Homepage 
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
        gs.loginToUserAccount(target_sys, username, password, driver_response, True) # Always specify true when using an external function to avoid locla host timeouts.
        loginAndLoadHomePage(driver_response)
    else: 
        try: 
            gs.loginToUserAccount(target_sys, username, password, driver_response, True) # Always specify true when using an external function to avoid local host timeouts.
            loginAndLoadHomePage(driver_response)
            driver_response.quit()
            print(f"{Fore.GREEN}Test Successful{Fore.WHITE}")
        except Exception as e: 
            driver_response.quit()
            print(f"{Fore.RED}Test Failed{Fore.WHITE}")
            print(e)
    


# This is where you can run your functions to test 
# Copy full file path of 'python_project_files'
# Open terminal and navigate to the directory i.e. ''
# Run 'python adam_dev_env.py" and the function will run
if __name__ == "__main__":

    target_sys = '' # Place the system you want to test in here, you can find a list of names in 'Target System List file in notes
    username = ''
    password = '!'

    # Call your completed function
    loginAndLoadHomePage(target_sys, username, password, driver_response=None, optional_error_catch=None)