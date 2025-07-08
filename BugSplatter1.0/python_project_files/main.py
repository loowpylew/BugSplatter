import globals as gs
import batch_processes as bp
import admin as a 
import user_tiles as ut
import menu_items as mi 
import threading
import f_driver_init as fdi
import os
import sys
import json
import pandas as pd
import option_menus as om
import system_admin as sa
import backend_processes as backps
import nav_homepage_items as nhi
from colorama import Fore, Style, init



# Initialize colorama - only provides the colours RED, YELLOW, GREEN, BLUE, WHITE
init()

##########################GLOBALS###############################

# Splattered bug art 
ascii_bug_art = '''                                                                                   
                                                  .+:                                               
                                                  +%:                                               
                                                 .@*                                                
                                                 -%:  ..     .:    .                                
                                           :     +. .   . :-:.:.+::#.                               
                                      .=+-      :-    -. .*@%: .*-.-    .=                          
                                      =@@%:  .. =. =:.**-.%@@-  .   :   .-                          
                               .:     *@@@- :#=:#**%**%@#.#@%:      .                               
                               ..     -@@@#+@@@%@@@@@@@@@==+:.-      .-..                           
                                      .#@%@@@@@@@@@@@@@@@@#-.#@:     @@=                            
                                  :.. +@@@@@@@@@@@@@@@@@@@@@@@@#:    *#-                            
                                 :*=+ =@@@@@@@@@@@@@@@@@@@@@@@@@%:    .                             
                                  -== -@@@@*@@@@@@@%*@@@@@@@%%@@%-:-+. .:.                          
                               .+  .  #@@@@*=#@@@@@%=@@@@@@++%@@@%%#+   :-                          
                                .    =@@@@@@%==%@@@#-%@@@#-*@@@@@@@:                                
                                   -+@@@@@@@@@**@@@+:#@@@=%@@@@@@@%:                                
                                 .*@@@@@@@@@@@*#@*:  .=@@=%@@@@@@@@#=    :                          
                               ..:+#@@@@@@@@@@*#@#.   =@@*#@@@@@@@#=+==+=.                          
                           :=::=: .*@@@@@@@@@@*+*#-  .+**=%@@@@@@@*:@@@@@-                          
                           :#%%#  :%@@@@@@@@@@@#+-.   :=*%@@@@@@@@@-+#*@@-                          
                            -%@=  =@@@@@@@@%*=:.        ..-+#@@@@@@#. .-=.                          
                          .  .*= .*@@@@@*-.      :    ..      .=%@@@= :.                            
                              :--=%@@@@@=.    .:=-:  .-=-.     :*@@@-.**:                           
                             ..-.+@@@@@@@*=-.-+++*.   =+=*+::-=#@@@@:-@*.                           
                            . :+ .#@@@@@@@@%:%#+%-    .%*+%+*@@@@@@@*#@*.                           
                               ..+%@@@@@@@@@-%+%%.     *@*+**@@@@@@@@@@@#.                          
                                 =@@@@@@@@@*=#+@#      -@%+#+%@@@@@@@@@@+.                          
                                 .*@@@@@@%==@%+@#      -@%+@#-#@@@@%@@#-..                          
                            .*=   -%@@@@#=#@@%+%%      =@#+@@@=+@@@@*+:-:                           
                            :%#   .*@@@@*#@@@@*#@.     *@*#@@@@*%@@@-  =-.                          
                            .--   .=@@@@@@@@@@*#@=    .%@+#@@@@@@@@@--  .:                          
                                   -@@@@@@@@@@*#@%    =@@*#@@@@@@%==%%.  :                          
                                    =@@@@@@@@%+@@@=  .#@@%=@@@@@@%: %@-. :                          
                                     %@@@@@@@+#@@@@:.+@@@@**@@@@@@*....                             
                                 ..-*@@@@@@@*+@@@@@@%@@@@@%+%@@@@*++*=:                             
                          :     .+#%@@%@@@@#=@@@@@@@@@@@@@@*+@@@@+.=%@- .                           
                          =.    .%@#=*-+@@@+%@@@@@@@@@@@@@@@*%@@@@-=-+:                             
                          .      =*: ...-+@@@@@@@@@@@@@@@@@@@@@%+#-: .                              
                                          =@@@@@@@@@@@@@@@@@@@@* ++  =                              
                                           -%@@@@@@@@@@@@@@@@@@%: ..                                
                               -     .      .=%@@%###=:*@@@@@@@@: .+ ::                             
                              .=      ..     .*%=::.. :@@@@%@@@%:=-: :-.                            
                                      :-     -#+.:.   .==+--+*@@*#+  :-:.                           
                                       .     *@*. -#+.       .*@#=-  *:.                            
                                             -*:  *@%:         ::*@: :                              
                                                  -%+.     .+** .*@:  .:                            
                                                            +@@: :=.:                               
                                                         .  .+*.                                                                                     
'''


# Text to be encapsulated within a Linux-style header
ascii_title_art = f'''{om.color_text("orange")}
⠀⠀⠀⢀⡀⢢⡜⣦⢳⡴⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡸⢮⢝⣦⡀⠀⠀⡀⠁⠛⡶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⢲⡝⠀⠈⠲⣝⢦⡀⢸⡇⠀⠈⢯⡆⠀⠀⠀⠀⠀{om.color_text("orange")}⢀⣀⠀⠀⣀⠀⠀⣀⣀⣀⣀⡀⠀⣀⡀⠀⢀⣀⠀⢀⣀⣀⣀⣀⠀⢀⣀⣀⣀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀{om.color_text("orange")}
⠠⣟⠀⠀⠀⡷⣌⠳⣝⢮⡓⠀⠀⢘⡷⠀⠀⠀⠀⠀{om.color_text("white")}⢨⣿⣦⡀⣿⡃⠀⣽⡟⠛⠛⡁⠀⠘⣷⣤⡾⠃⠀⠘⠛⣿⠛⠋⠀⢸⣿⠛⠛⣷⠀⠀⠀⣾⢿⣇⠀⠀⠀{om.color_text("orange")}
⠐⣯⠄⠀⠀⡽⡎⡷⣌⠳⣍⠀⠀⢸⡞⠀⠀⠀⠀⠀{om.color_text("white")}⢨⣿⠘⢷⣿⡅⠀⢾⡟⢛⠛⡁⠀⠠⣼⠿⣧⡀⠀⠀⠀⣿⡁⠀⠀⢸⡿⠾⣿⡋⠀⠀⣾⣯⣤⣿⣆⠀⠀{om.color_text("orange")}
⠐⠸⣧⡀⠀⠻⡄⠙⢮⡳⣄⠀⢠⢷⠉⠀⠀⠀⠀ {om.color_text("orange")}⠈⠛⠀⠈⠛⠀⠀⠛⠛⠛⠛⠃⠀⠛⠋⠀⠙⠓⠀⠀⠀⠛⠀⠀⠀⠘⠛⠀⠙⠛⠂⠘⠛⠀⠁⠈⠛⠀⠀{om.color_text("orange")}
⠀⠀⠑⢻⣤⣀⡁⢀⠀⡙⢮⡳⠏⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠃⠛⠭⠛⡙⠂⠁⠀⠀⠀⠀⠀    {om.color_text("orange")}Bug Splatter {om.color_text("blue")}- {om.color_text("white")}1.0⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''


target_system = ''

# List of target system names - all dbs with an associated software instance
target_systems = [
    "{Place name of database here minus the '_SQL' part of string}",
    "",
    ""
]


username = ''
password = ''

################################################################

#########################UI FUNCTIONS###########################
class ValueWrapper:
    def __init__(self, value):
        self.value = value

    def isInt(self):
        try:
            return int(self.value)
        except ValueError:
            return False


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def setHeadlessMode(target_system):
    print(om.color_text("orange") + "Please enter either '" + om.color_text("white") + "y" + om.color_text("orange") + "' to activate " + om.color_text("blue") + "'--headless', " + om.color_text("white") + "'n'" + om.color_text("orange") + "' for " + om.color_text("blue") + "'--chrome browser'" + om.color_text("orange") + ": " + om.color_text("white"))
    while(1):
        headless_mode = input()
        if headless_mode == 'y'.lower(): 
            headless_mode = True
            break
        elif headless_mode =='n'.lower():
            headless_mode = False
            break
        else: 
            clear_console()
            print(ascii_title_art)
            print(om.color_text("blue") + f"Current system: " + om.color_text("white") + target_system + "\n")
            print(om.color_text("orange") + "Please try again and enter either '" + om.color_text("white") + "y" + om.color_text("orange") + "'n' to activate " +  om.color_text("blue") + "'--headless', " + om.color_text("white") + "n" + om.color_text("orange") + "' for " +  om.color_text("blue") + "'--chrome browser': " + om.color_text("orange") + ": " + om.color_text("white"))
    
    return headless_mode

def specify_usertype(): 
    print(om.color_text("orange") + "Please specify the usertype you wish to test this operation in ")
    print(om.color_text("white")  + "[" + om.color_text("yellow") + "WARNING: " + om.color_text("white") + "If the usertype is entered wrong, the process will fail]: ")
    usertype = input()

    return usertype


def processExcelSheets(title, target_sheet_name=None):
    excel_folder = '..\\excel_sheets'
    valid_files = []
    valid_file_paths = []

    while True:
        clear_console()
        print(title)
        print(om.color_text("yellow") + "Note* " + om.color_text("white") + "- Excel sheets related to the process must be closed to prevent excel access error")
        print(om.color_text("blue") + "Selected Excel Files:" + om.color_text("white"), valid_files)
        print(om.color_text("orange") + "Please enter the name of the Excel sheet you wish to process" + om.color_text("white"))
        print("[" + om.color_text("yellow") + f"WARNING: " + om.color_text("orange") + "Please include the " + om.color_text("blue") + ".xlsx " + om.color_text("orange") + "file extension]: " + om.color_text("white"))
        file_name = input()

        #if not file_name:
        #    break  # Continue to the next section of code

        file_found = False

        # Use os.walk to search through all subdirectories
        for root, dirs, files in os.walk(excel_folder):
            for file in files:
                if file == file_name:
                    file_path = os.path.join(root, file_name)

                    if target_sheet_name is not None:
                        xl = pd.ExcelFile(file_path)
                        sheet_names = xl.sheet_names
                        if target_sheet_name not in sheet_names:
                            continue

                    valid_files.append(file_name)
                    valid_file_paths.append(file_path)
                    file_found = True
                    clear_console()
                    print(title)
                    print(om.color_text("blue") + "Selected Excel Files:" + om.color_text("white"), valid_files)
                    print(om.color_text("orange") + f"If you would like to add another file, press '" + om.color_text("white") + "y" + om.color_text("orange") + ", otherwise press '"+ om.color_text("white") + "q" + "'" + om.color_text("orange") + " to continue: " + om.color_text("white"))
                    while True:
                        validation = input()

                        if validation == 'y':
                            break
                        elif validation == 'q':
                            return valid_file_paths
                        else:
                            clear_console()
                            print(title)
                            print(om.color_text("red") + f"Invalid input: " + om.color_text("orange") + "Please enter '" + om.color_text("white") + "y" + om.color_text("orange") + "' to add another file or '" + om.color_text("white") + "q" + om.color_text("orange") + "' to continue: " + om.color_text("white"))

        if not file_found:
            clear_console()
            print(title)
            print(om.color_text("orange") + "File " + om.color_text("red") + f"'{file_name}' " + om.color_text("orange") + "does not exist or is not a valid file.")
            print(f"If you would like to try again, press '" + om.color_text("white") + "y" + om.color_text("orange") + "', otherwise press '" + om.color_text("white") + "q" + om.color_text("orange") + "' to return back to the options menu: " + om.color_text("white"))
            while True:
                validation = input()

                if validation.lower() == 'y':
                    clear_console()
                    break  # Repeat the loop for another file
                elif validation.lower() == 'q':
                    clear_console()
                    return False  # Continue to the next section of code
                else:
                    clear_console()
                    print(title)
                    print(om.color_text("red") + f"Invalid input: " + om.color_text("orange") + "Please enter '" + om.color_text("white") + "y" + om.color_text("orange") + "' to add another file or '" + om.color_text("white") + "q" + om.color_text("orange") + "' to continue: " + om.color_text("white"))


def main():
    global wrong_input_flag 
    global wrong_input_flag2
    global no_of_tests

    right_input_flag = True
    wrong_input_flag = True
    wrong_input_flag2 = True
    no_of_tests = 4

    print(om.color_text("red") + ascii_bug_art + om.color_text("white"))
    print(ascii_title_art)
    #print(ascii_title_art)
    print(om.color_text("blue") + "\nPlease enter username: " + om.color_text("white")) 
    username = input()
    print(om.color_text("blue") + "Please enter password: " + om.color_text("white"))
    password = input()
    clear_console()
    

    while True:
        print(ascii_title_art)
        if wrong_input_flag:
            #print(username)
            #print(password)
            print(om.color_text("blue") + "Please enter Target System: " + om.color_text("white"))
        else: 
            print(om.color_text("blue") + "Please enter an existing system: " + om.color_text("white"))
        target_system = input()
        if target_system in target_systems:
            break
        else: 
            wrong_input_flag = False 
            clear_console()

    clear_console()
    
    while(1): 
        print(ascii_title_art)
        print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Successful tests dependant on stable internet connecton")
        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")

        om.main_options_menu()

        if right_input_flag:
            print(om.color_text("orange") + "Please select the type of tests you want to perform: " + om.color_text("white"))
            test_option = input()
        elif wrong_input_flag:
            print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: ")
            test_option = input()
        elif wrong_input_flag == False:
            print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter a number that corresponds to an option]: ")
            test_option = input()

        if test_option == '1': 
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1): 
                clear_console()
                # Create the Linux-style header
                print(ascii_title_art)
                print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Successful tests dependant on stable internet connecton")
                print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                om.singular_test_case_options()

                if right_input_flag:
                    print(om.color_text("orange") + "Please select the repeat process you'd like to test: " + om.color_text("white"))
                    test_option = input()
                elif wrong_input_flag:
                    print(om.color_text("orange") + "Please select the repeat process you'd like to test" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(om.color_text("orange")+ "Please select the repeat process you'd like to test" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: ")
                    test_option = input()

                if test_option == '1': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                    
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None

                    no_of_tests = 8

                    non_usertype_funcs = {
                        "gs.loginToUserAccount"
                        , "gs.loginAndLoadHomePage"
                        , "gs.checkInitialUserRole" 
                    }

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        om.generic_options_menu()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange")+ "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\generic.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)
                         
                        for key in test_options:
                            if key == 'q'.lower(): 
                                exit_flag = True
                            
                            if key in data["generic"] and exit_flag != True:

                                if headless_count == 0: 
                                    headless_mode = setHeadlessMode(target_system)

                                function_to_call = eval(data["generic"][key][0])
                                
                                # Special case where some functions in globals.js dont share the no. of function paramters as every other function across the board
                                function_str = (data["generic"][key][0])
                                if function_str in non_usertype_funcs:  
                                    thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, username, password)) # arguments expressed as a tuple
                                    pass
                                else: 
                                    user_type = specify_usertype()

                                    thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, user_type, username, password))

                                    
                                headless_count += 1

                                print("[" + str(function_to_call) + "]")

                                thread.start()

                                print("Awaiting test results...")

                                # Capture the thread's standard output
                                sys.stdout.flush()  # Flush any pending output
                                thread.join() # Wait for the thread to complete

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                            
                            # Resets count so that youre asked whether you want to run headless or not aswell as the userype you wish to perform the test in.
                            headless_count = 0
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break   
                           

                if test_option == '2': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                    
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None

                    no_of_tests = 8

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        om.menu_item_options()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange")+ "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\menu_items.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)
                         
                        for key in test_options:
                            if key == 'q'.lower(): 
                                exit_flag = True
                            
                            if key in data["menu_items"] and exit_flag != True:
                                if headless_count == 0: 
                                    user_type = specify_usertype()

                                    headless_mode = setHeadlessMode(target_system)
                                    
                                headless_count += 1
                                
                                function_to_call = eval(data["menu_items"][key][0])
                                print("[" + str(function_to_call) + "]")
                                
                                thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, user_type, username, password)) # arguments expressed as a tuple 
                                thread.start()

                                print("Awaiting test results...")

                                # Capture the thread's standard output
                                sys.stdout.flush()  # Flush any pending output
                                thread.join() # Wait for the thread to complete

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                            
                            # Resets count so that youre asked whether you want to run headless or not aswell as the userype you wish to perform the test in.
                            headless_count = 0
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break   
                elif test_option == '3':
                    pass
         
                elif test_option == '4': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                    
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None


                    no_of_tests = 175

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")

                        om.singular_user_tile_options()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange")+ "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\user_tiles.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)
                         
                        for key in test_options:
                            if key == 'q'.lower(): 
                                exit_flag = True
                            
                            if key in data["user_tiles"] and exit_flag != True:
                                if headless_count == 0: 
                                    headless_mode = setHeadlessMode(target_system)

                                    user_type = specify_usertype()
                                    
                                headless_count += 1
                                
                                function_to_call = eval(data["user_tiles"][key][0])
                                print("[" + str(function_to_call) + "]")
                                # Loads 'Staff Admin' Menu options
                                thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, user_type, username, password)) # arguments expressed as a tuple 
                                thread.start()

                                print("Awaiting test results...")

                                # Capture the thread's standard output
                                sys.stdout.flush()  # Flush any pending output
                                thread.join() # Wait for the thread to complete

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break          
                elif test_option == '5': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                    
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None

                    no_of_tests = 160

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        om.singular_report_tile_options()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange")+ "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\reports.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)
                         
                        for key in test_options:
                            if key == 'q'.lower(): 
                                exit_flag = True
                            
                            if key in data["reports"] and exit_flag != True:
                                if headless_count == 0: 
                                    user_type = specify_usertype()

                                    headless_mode = setHeadlessMode(target_system)
                                    
                                headless_count += 1
                                
                                function_to_call = eval(data["reports"][key][0])
                                print("[" + str(function_to_call) + "]")
                                
                                thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, user_type, username, password)) # arguments expressed as a tuple 
                                thread.start()

                                print("Awaiting test results...")

                                # Capture the thread's standard output
                                sys.stdout.flush()  # Flush any pending output
                                thread.join() # Wait for the thread to complete

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                            
                            # Resets count so that youre asked whether you want to run headless or not aswell as the userype you wish to perform the test in.
                            headless_count = 0
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break   
                           
                elif test_option == '6': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                    
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None

                    no_of_tests = 160

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        om.singular_dashboard_reports_tile_options()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange")+ "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\dashboard_reports.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)
                         
                        for key in test_options:
                            if key == 'q'.lower(): 
                                exit_flag = True
                            
                            if key in data["dashboard_reports"] and exit_flag != True:
                                if headless_count == 0: 
                                    user_type = specify_usertype()

                                    headless_mode = setHeadlessMode(target_system)
                                    
                                headless_count += 1
                                
                                function_to_call = eval(data["dashboard_reports"][key][0])
                                print("[" + str(function_to_call) + "]")
                                
                                thread = threading.Thread(target=function_to_call, args=(target_system, headless_mode, user_type, username, password)) # arguments expressed as a tuple 
                                thread.start()

                                print("Awaiting test results...")

                                # Capture the thread's standard output
                                sys.stdout.flush()  # Flush any pending output
                                thread.join() # Wait for the thread to complete

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                            
                            # Resets count so that youre asked whether you want to run headless or not aswell as the userype you wish to perform the test in.
                            headless_count = 0
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break   
                           
                elif test_option == 'q'.lower(): 
                    clear_console()
                    break

                else:
                    test_option = ValueWrapper(test_option)
                    if test_option.isInt() > no_of_tests: 
                        right_input_flag = False
                        wrong_input_flag = True
                        clear_console()
                    else: 
                        right_input_flag = False
                        wrong_input_flag = False
                        clear_console()

        
        elif test_option == '2':
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1):
                clear_console()
                # Create the Linux-style header
                print(ascii_title_art)
                print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Successful tests dependant on stable internet connecton")

                print(om.color_text("yellow") + "\nNote*")
                #print(om.color_text("white") + "Your system will have to be setup to have the following usertype configuration: " + om.color_text("orange") + "/Notes/usertypes_list.md\n")
                
                om.batch_test_case_options()

                if right_input_flag:
                    print(om.color_text("orange") + "Please select the repeat process you'd like to test: " + om.color_text("white"))
                    test_option = input()
                elif wrong_input_flag:
                    print(om.color_text("orange")+ "Please select the repeat process you'd like to test" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(om.color_text("orange") + "Please select the repeat process you'd like to test" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter a number that corresponds to an option]: ")
                    test_option = input()

                # Batch Process Functions 
                if test_option == '1':
                   excel_sheets = processExcelSheets(ascii_title_art, "employees")

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       headless_mode = setHeadlessMode(target_system)

                       user_type = specify_usertype()

                       thread = threading.Thread(target=bp.batchProcessEmployees, args=(target_system, headless_mode, user_type, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                       clear_console()

                elif test_option == '2':
                   excel_sheets = processExcelSheets(ascii_title_art, "tiles")

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       
                       headless_mode = setHeadlessMode(target_system)

                       thread = threading.Thread(target=bp.batchProcessUserTypeTiles, args=(target_system, headless_mode, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                       clear_console()
                elif test_option == '3':
                   excel_sheets = processExcelSheets(ascii_title_art, "reports")

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       
                       headless_mode = setHeadlessMode(target_system)

                       thread = threading.Thread(target=bp.batchProcessUserTypeReports, args=(target_system, headless_mode, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                       clear_console()
                elif test_option == '4':
                   excel_sheets = processExcelSheets(ascii_title_art, "dashboard_reports")

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       thread = threading.Thread(target=bp.batchProcessUserTypeDashboardReports, args=(target_system, headless_mode, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                       clear_console()

                #############################
                # Yet to be developed fully #
                #############################
                #5. Fetch [Admin] - Main Menu Tabs
                #6. Fetch [Admin] - Sub Menu Tabs
                #7. Fetch [Admin] - Sub Sub Menu Tabs
                #8. Fetch [Admin] All Tabs
                #############################

                elif test_option == '9':

                    system_upgraded = None # We set to none in the case we want to compare the difference between 
                                           # the /source and /system excel sheets. 
                    
                    headless_mode = setHeadlessMode(target_system)

                    config_file = '..\\excel_sheets\\nav_homepage_items\\configs\\nav_homepage_items_config.xlsx'

                    while(1): 
                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        
                        print(om.color_text("orange") + "\n#####GET HOMEPAGE MENU OBJECTS#####" + om.color_text("white"))
                        print("If you would like to run for the old version of the system, enter '" + om.color_text("orange") + "o" + om.color_text("white") + "' otherwise, enter '" +  om.color_text("orange") + "u" + om.color_text("white") +"' for upgraded version")
                        print("Otherwise enter '" + om.color_text("orange") + "d" + om.color_text("white") + "' to compare differences between the old and upgraded system: ")
                        user_input = input()
                        if user_input == 'o'.lower(): 
                            system_upgraded = False 
                            break
                            # Get Homepage Menu object - system before upgrade
                        elif user_input == 'u'.lower(): 
                            system_upgraded = True
                            break
                        elif user_input == 'd'.lower(): 
                            break
                        else: 
                            print("Invalid input. Please enter '" + om.color_text("orange") + "o" + om.color_text("white")  +"', '" + om.color_text("orange") + "u" + om.color_text("white") + "', or '" + om.color_text("orange") + "d" + om.color_text("white") + "'.")


                    if system_upgraded != None:
                        thread = threading.Thread(target=nhi.get_homepage_menu_objects_state, args=(target_system, headless_mode, username, password, system_upgraded, config_file)) # arguments expressed as a tuple 
                        thread.start()
                    else:
                        thread = threading.Thread(target=nhi.system_compare_versions) # arguments expressed as a tuple 
                        thread.start()
                    
                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                    clear_console()
                
                #elif test_option == '?':
                #   excel_sheets = processExcelSheets(ascii_title_art, "?")

                #   if excel_sheets == False: 
                #       pass
                #       clear_console()
                #   else: 
                #       thread = threading.Thread(target=atf.batchProcessStartDateOverrides, args=(target_system, username, password, excel_sheets)) # arguments expressed as a tuple 
                #       thread.start()

                #       print("Awaiting test results...")

                #       # Capture the thread's standard output
                #       sys.stdout.flush()  # Flush any pending output
                #       thread.join() # Wait for the thread to complete

                #       print("Test is complete!")
                #       input(yellow_text + "Press Enter to clear the console." + white_text)
                #       clear_console()
                    
                elif test_option == 'q'.lower() : 
                    clear_console()
                    break
                else:
                    test_option = ValueWrapper(test_option)
                    if test_option.isInt() > no_of_tests: 
                        right_input_flag = False
                        wrong_input_flag = True
                        clear_console()
                    else: 
                        right_input_flag = False
                        wrong_input_flag = False
                        clear_console()
            
            
        elif test_option == '3':
            clear_console()
            print(ascii_title_art)
            # will be an options to select between particular overnight processes or all of them. 
            print(om.color_text("red") + ascii_bug_art + om.color_text("white"))
            print(om.color_text("white") + "Oh no, the overnight processes havent been implemented yet!!!")
            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
            clear_console()
            pass

        # System Administration
        elif test_option == '4': 
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1):
                clear_console()
                print(ascii_title_art)
                print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Successful updates dependant on stable internet connecton")
                print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")

                om.system_administration_options()

                if right_input_flag:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform: " + om.color_text("white"))
                    test_option = input()
                elif wrong_input_flag:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter a number that corresponds to an option]: ")
                    test_option = input()

                
                # Build and Release Manifests 
                if test_option == '1': 
                    right_input_flag = True
                    wrong_input_flag = True
                    wrong_input_flag2 = True
                     
                    headless_count = 0
                    out_of_scope = False
                    exit_flag = False

                    headless_mode = None

                    no_of_tests = 13 # Defines number of test options

                    while(1): 

                        if exit_flag == True: 
                            right_input_flag = True
                            wrong_input_flag = True
                            wrong_input_flag2 = True
                            clear_console()
                            break

                        clear_console()
                        # Create the Linux-style header
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                        om.manifest_options()
    
                        if right_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()
                        elif wrong_input_flag == False:
                            print(om.color_text("orange") + "Please select the repeat process/processes you'd like to test" + om.color_text("white"))
                            print(f"[" + om.color_text("white") + "Message: " + om.color_text("yellow") + "Enter a number that corresponds to an option]: " + om.color_text("white"))
                            test_options = input().replace(",", " ").split()

                        # Read the JSON file
                        with open('..\\json_config\\system_admin.json', 'r') as file:
                            # Parse JSON data
                            data = json.load(file)

                        if test_options != 'q': 

                            print("\n" + om.color_text("orange") + "Would you like to deploy for all systems: [" + om.color_text("white") + "NextraDev, NextraPreRelease, NextraTest_v4_2, NextraRelease_Candidate" + om.color_text("orange") + "]")
                            print(om.color_text("orange") + "Enter '" + om.color_text("white") + "y" + om.color_text("orange") + "' for yes, '" + om.color_text("white") + "n" + om.color_text("orange") + "' for no:" + om.color_text("white"))
                            user_input = input().lower()

                            while(1): 
                                if user_input == 'y' or user_input == 'n': 
                                    break
                                else: 
                                    clear_console()
                                    print(ascii_title_art)
                                    print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                                    print("\n" + om.color_text("orange") + "Would you like to deploy for all systems: [" + om.color_text("white") + "NextraDev, NextraPreRelease, NextraTest_v4_2, NextraRelease_Candidate" + om.color_text("orange") + "]")
                                    print(om.color_text("orange") + "Enter '" + om.color_text("white") + "y" + om.color_text("orange") + "' for yes, '" + om.color_text("white") + "n" + om.color_text("orange") + "' for no:" + om.color_text("white"))
                                    user_input = input().lower()
                            
                            headless_mode = setHeadlessMode(target_system)

                            print("\n") # spacing between headless mode output and usertype prompt output

                            print(om.color_text("orange") + "Current default in NextraDev: " + om.color_text("white") + "System Administrator - Corporate")
                            user_type = specify_usertype()
                                    
                        else: 
                            user_input = 'q' 
                            pass

                        if test_options == ['17']: 
                            test_options = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16"
                            test_options.replace(",", " ").split()
                        else: 
                            pass

                        for key in test_options:
                            print(key)
                            if key == 'q'.lower(): 
                                exit_flag = True
                            else: 
                                pass
                            
                            if key in data["sys_admin"] and exit_flag != True: 
                                while(1): 
                                    # This will allow for all systems to undergo the build and release process on all systems
                                    if user_input == 'y': 
                                        target_systems_to_deploy = ["NextraDev", "NextraPreRelease", "NextraTest_v4_2", "NextraRelease_Candidate"]
                                        for target_sys in target_systems_to_deploy:
                                            target_system = target_sys 

                                            # Special case* 
                                            # Instead of specifying a different function, we'll just pass the option as a parameter as we will just have 1 function to perform all our logic
                                            index = data["sys_admin"][key]# removed eval as we a not working with indivisual fucntiosn as strings in this instance.

                                            if index == 'unknown': 
                                                print("\n" + om.color_text("orange") + "Please enter the name of the manifest you wish to process" + om.color_text("white"))
                                                print("[" + om.color_text("yellow") + "WARNING: " + om.color_text("white") + "If you enter a manifest that does not exist, the release and build will fail]: ")
                                                index = input()

                                                print("\n" + om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                                            else: 
                                                print("\n" + om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")

                                            print("\n[" + om.color_text("orange") + "Manifest to Build and Release: " + om.color_text("white") + str(index) + "]")
                                            # Loads 'Staff Admin' Menu options
                                            thread = threading.Thread(target=sa.buildAndReleaseManifests, args=(target_system, headless_mode, user_type, username, password, index)) # arguments expressed as a tuple 
                                            thread.start()

                                            print("Awaiting test results...")

                                            # Capture the thread's standard output
                                            sys.stdout.flush()  # Flush any pending output
                                            thread.join() # Wait for the thread to complete

                                        break
                                    elif user_input == 'n': 
                                        # Special case* 
                                        # Instead of specifying a different function, we'll just pass the option as a parameter as we will just have 1 function to perform all our logic
                                        index = data["sys_admin"][key]# removed eval as we a not working with indivisual fucntiosn as strings in this instance.

                                        if index == 'unknown': 
                                                print("\n" + om.color_text("orange") + "Please enter the name of the manifest you wish to process" + om.color_text("white"))
                                                print("[" + om.color_text("yellow") + "WARNING: " + om.color_text("white") + "If you enter a manifest that does not exist, the release and build will fail]: ")
                                                index = input()

                                                print("\n" + om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                                        else: 
                                            print("\n" + om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")
                                        
                                        print("\n[" + om.color_text("orange") + "Manifest to Build and Release: " + om.color_text("white") + str(index) + "]")
                                        # Loads 'Staff Admin' Menu options
                                        thread = threading.Thread(target=sa.buildAndReleaseManifests, args=(target_system, headless_mode, user_type, username, password, index)) # arguments expressed as a tuple 
                                        thread.start()

                                        print("Awaiting test results...")

                                        # Capture the thread's standard output
                                        sys.stdout.flush()  # Flush any pending output
                                        thread.join() # Wait for the thread to complete
                                        break
                                    elif user_input == 'q': 
                                        break

                                print("Test is complete!")
                            else: 
                                out_of_scope = True
                        
                        if exit_flag == False and out_of_scope != True:
                            input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                        else: 
                            pass
                       
                        for key in test_options:
                           try:
                               to_int = int(key)
                               if to_int > no_of_tests: 
                                   right_input_flag = False
                                   wrong_input_flag = True
                                   clear_console()   
                           except:
                               right_input_flag = False
                               wrong_input_flag = False
                               clear_console()
                               break             
                elif test_option == '2':
                    clear_console()
                    while True:
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Current Target system: " + om.color_text("white") + target_system + "\n")
                        if wrong_input_flag:
                            print(om.color_text("blue") + "Please enter Target System: " + om.color_text("white"))
                        else: 
                            print(om.color_text("blue") + "Please enter an existing system: " + om.color_text("white"))
                        target_sys = input()

                        if target_sys in target_systems:
                            target_system = target_sys
                            break
                        else: 
                            wrong_input_flag = False 
                            clear_console()

                elif test_option == '3':
                    clear_console()
                    print(ascii_title_art)
                    print(om.color_text("blue") + f"Current Target system: " + om.color_text("white") + target_system + "\n")
                    print(om.color_text("red") + ascii_bug_art + om.color_text("white"))
                    print(ascii_title_art)
                    print(om.color_text("blue") + "\nPlease enter username: " + om.color_text("white")) 
                    username = input()
                    print(om.color_text("blue") + "Please enter password: " + om.color_text("white"))
                    password = input()
                    clear_console()
                elif test_option == 'q'.lower(): 
                    clear_console()
                    break
    
                elif test_option == '4': 
                    clear_console()
                    while(1): 
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Current Target system: " + om.color_text("white") + target_system + "\n")
                        print(om.color_text("Orange") + "\nDB SERVER LIST - DNS/PORT")
                        print(om.color_text("Blue") + "--------------------------------------------------------------" + om.color_text("white"))
                        sa.get_db_server_list()
                        print(om.color_text("Blue") + "--------------------------------------------------------------" + om.color_text("white"))

                        # Prompt for user input
                        user_input = input("Press '" + om.color_text("orange") + "q" + om.color_text("white") + "' to quit or press Enter to refresh: \n").strip()

                        if user_input.lower() == 'q':
                            break
                        else: 
                            clear_console()
                elif test_option == '5':
                    clear_console()
                    while(1): 
                        print(ascii_title_art)
                        print(om.color_text("blue") + f"Current Target system: " + om.color_text("white") + target_system + "\n")
                        print(om.color_text("Orange") + "\nWEB SERVER LIST - DNS/PORT")
                        print(om.color_text("Blue") + "--------------------------------------------------------------" + om.color_text("white"))
                        sa.get_web_server_list()
                        print(om.color_text("Blue") + "--------------------------------------------------------------" + om.color_text("white"))

                        # Prompt for user input
                        user_input = input("Press '" + om.color_text("orange") + "q" + om.color_text("white") + "' to quit or press Enter to refresh: \n").strip()

                        if user_input.lower() == 'q':
                            break
                        else: 
                            clear_console()
                else:
                    test_option = ValueWrapper(test_option)
                    if test_option.isInt() > no_of_tests: 
                        right_input_flag = False
                        wrong_input_flag = True
                        clear_console()
                    else: 
                        right_input_flag = False
                        wrong_input_flag = False
                        clear_console()

        elif test_option == '5': 
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1):
                clear_console()
                print(ascii_title_art)
                print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Successful updates dependant on stable internet connecton")
                print(om.color_text("blue") + f"Target system: " + om.color_text("white") + target_system + "\n")

                om.backend_process_options()

                if right_input_flag:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform: " + om.color_text("white"))
                    test_option = input()
                elif wrong_input_flag:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(om.color_text("orange") + "Please select the type of tests you want to perform:" + om.color_text("white"))
                    print(f"[" + om.color_text("yellow") + "Message: " + om.color_text("white") + "Enter a number that corresponds to an option]: ")
                    test_option = input()

                
                # Build and Release Manifests 
                if test_option == '1': 

                    target_system_SQL = target_system + '_SQL'

                    thread = threading.Thread(target=backps.checkTimesheetRuns, args=(target_system_SQL, None, None, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                    clear_console()
                elif test_option == '2': 

                   target_system_SQL = target_system + '_SQL'
                   # Will add some checks in the furure to make sure it matches anmd or is simlar to the LanguageName in rf_language
                   print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Client name must be very similiar to how it is specified in the db i.e. | LanguageName |")
                   print("Please enter the name of client you wish to create the excelsheet for: ")
                   client = input()

                   # redfining for readability within the connection string
                   db = target_system_SQL
                   # Will fetch dns/port based on default target system given to bugSplatter on inital startup
                   server = backps.get_server_auto(db)

                   conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'
                   folder_path = "..\\excel_sheets\\admin_nav\\main_menu_tabs\\"
                   filename = f"main_menu_options_{client.lower()}.xlsx"
                   fullpath = os.path.join(folder_path, filename)

                   thread = threading.Thread(target=backps.populateExcelSheetWithExpecrfNavTypesTabs, args=(conn_string, fullpath, client)) # arguments expressed as a tuple 
                   thread.start()

                   print("Awaiting test results...")

                   # Capture the thread's standard output
                   sys.stdout.flush()  # Flush any pending output
                   thread.join() # Wait for the thread to complete

                   print("Test is complete!")
                   input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                   clear_console()

                elif test_option == '3': 
                   target_system_SQL = target_system + '_SQL'
                   # Will add some checks in the furure to make sure it matches anmd or is simlar to the LanguageName in rf_language
                   print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Client name must be very similiar to how it is specified in the db i.e. | LanguageName |")
                   print("Please enter the name of client you wish to create the excelsheet for: ")
                   client = input()

                   # redfining for readability within the connection string
                   db = target_system_SQL
                   # Will fetch dns/port based on default target system given to bugSplatter on inital startup
                   server = backps.get_server_auto(db)

                   conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'
                   folder_path = "..\\excel_sheets\\admin_nav\\sub_menu_tabs\\"
                   filename = f"main_menu_options_{client.lower()}.xlsx"
                   fullpath = os.path.join(folder_path, filename)

                   thread = threading.Thread(target=backps.populateExcelSheetWithExpecrfNavTypesTabs, args=(conn_string, fullpath, client)) # arguments expressed as a tuple 
                   thread.start()

                   print("Awaiting test results...")

                   # Capture the thread's standard output
                   sys.stdout.flush()  # Flush any pending output
                   thread.join() # Wait for the thread to complete

                   print("Test is complete!")
                   input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                   clear_console()
                elif test_option == '4': 

                   target_system_SQL = target_system + '_SQL'
                   # Will add some checks in the furure to make sure it matches anmd or is simlar to the LanguageName in rf_language
                   print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Client name must be very similiar to how it is specified in the db i.e. | LanguageName |")
                   print("Please enter the name of client you wish to create the excelsheet for: ")
                   client = input()

                   # redfining for readability within the connection string
                   db = target_system_SQL
                   # Will fetch dns/port based on default target system given to bugSplatter on inital startup
                   server = backps.get_server_auto(db)

                   conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'

                   thread = threading.Thread(target=backps.populateExcelSheetsWithAllExpecSubSubsTabs, args=(conn_string, client)) # arguments expressed as a tuple 
                   thread.start()

                   print("Awaiting test results...")

                   # Capture the thread's standard output
                   sys.stdout.flush()  # Flush any pending output
                   thread.join() # Wait for the thread to complete

                   print("Test is complete!")
                   input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                   clear_console()

                elif test_option == '5': 

                   target_system_SQL = target_system + '_SQL'
                   # Will add some checks in the furure to make sure it matches anmd or is simlar to the LanguageName in rf_language
                   print(om.color_text("yellow") + f"Note*" + om.color_text("white") + " - Client name must be very similiar to how it is specified in the db i.e. | LanguageName |")
                   print("Please enter the name of client you wish to create the excelsheet for: ")
                   client = input()

                   # redfining for readability within the connection string
                   db = target_system_SQL
                   # Will fetch dns/port based on default target system given to bugSplatter on inital startup
                   server = backps.get_server_auto(db)

                   conn_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={db};UID={username};PWD={password}'

                   thread = threading.Thread(target=backps.populateExcelSheetsWithAllTabTypes, args=(conn_string, client)) # arguments expressed as a tuple 
                   thread.start()

                   print("Awaiting test results...")

                   # Capture the thread's standard output
                   sys.stdout.flush()  # Flush any pending output
                   thread.join() # Wait for the thread to complete

                   print("Test is complete!")
                   input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                   clear_console()
                
                elif test_option == '6': 
                    # Input the hostname of the server instance you want to connect to 
                    server = backps.get_server()

                    print(om.color_text("orange") + "\nPlease input the store procedure you wish to find: " + om.color_text("white"))
                    stored_proc_name = input() #sp_GetDDL

                    thread = threading.Thread(target=backps.check_stored_proc_exists, args=(server, username, password, stored_proc_name)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(om.color_text("orange") + "Press Enter to clear the console." + om.color_text("white"))
                    clear_console()
                
                
                elif test_option == 'q'.lower() : 
                    clear_console()
                    break
                else:
                    test_option = ValueWrapper(test_option)
                    if test_option.isInt() > no_of_tests: 
                        right_input_flag = False
                        wrong_input_flag = True
                        clear_console()
                    else: 
                        right_input_flag = False
                        wrong_input_flag = False
                        clear_console()
                
        elif test_option == 'q'.lower(): 
            clear_console()
            print(om.color_text("red") + ascii_bug_art + om.color_text("white"))
            print(om.color_text("orange") + "Thank you for using BugSplatter!!!")
            break
        else:
            test_option = ValueWrapper(test_option)
            if test_option.isInt() > no_of_tests: 
                right_input_flag = False
                wrong_input_flag = True
                clear_console()
            else: 
                right_input_flag = False
                wrong_input_flag = False
                clear_console()


if __name__ == "__main__":
    main()
    