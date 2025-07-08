import automated_test_functions as atf
import threading
import os
import sys
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
ascii_title_art = '''
╭━━╮╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭╮╱╭━━━╮    
┃╭╮┃╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╭╯╰╮╱╱╱╱╱╭╯┃╱┃╭━╮┃    
┃╰╯╰┳╮╭┳━━┫╰╯╰┳╮╭┳━┻╮╭╋━━┳━╮╰╮┃╱┃┃┃┃┃     
┃╭━╮┃┃┃┃╭╮┃╭━╮┃┃┃┃━━┫┃┃┃━┫╭╯╱┃┃╱┃┃┃┃┃    
┃╰━╯┃╰╯┃╰╯┃╰━╯┃╰╯┣━━┃╰┫┃━┫┃╱╭╯╰┳┫╰━╯┃    
╰━━━┻━━┻━╮┣━━━┻━━┻━━┻━┻━━┻╯╱╰━━┻┻━━━╯     
╱╱╱╱╱╱╱╭━╯┃                              
╱╱╱╱╱╱╱╰━━╯                              
'''

yellow_text = f"{Fore.YELLOW}"
white_text = f"{Fore.WHITE}"
red_text = f"{Fore.RED}"
orange_text = f"{Fore.GREEN}"

target_system = ''

# List of target system names - all dbs with an associated software instance
target_systems = [
    ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
]


username = ''
password = ''

################################################################

#########################UI FUNCTIONS###########################

# For colours outside the scope of colorama
def get_color_code(color):
    # Define ANSI escape codes for colors
    colors = {
        "BLACK": "\033[30m"
        , "WHITE": "\033[97m"
        , "RED": "\033[31m"
        , "GREEN": "\033[32m"
        , "BLUE": "\033[34m"
        , "YELLOW": "\033[33m"
        , "ORANGE": "\033[38;5;208m"
        , "PURPLE": "\033[35m"
        , "PINK": "\033[38;5;198m"
        , "GRAY_DARK": "\033[90m"
        , "GRAY_LIGHT": "\033[37m"
        , "RESET": "\033[0m"  # Reset to default color
    }

    # Check if the specified color is valid
    if color.upper() in colors:
        return colors[color.upper()]
    else:
        return ""  # Return an empty string if color is not recognized

def main_options_menu(): 
    print(yellow_text + f"Main Options Menu:")
    print(f"{yellow_text}1. {white_text}Singular Tests - Generic UI Stuff")
    print(f"{yellow_text}2. {white_text}Batch Processes")
    print(f"{yellow_text}3. {white_text}Overnight Processes")
    print(f"{yellow_text}q. {white_text}Quit 'BugBuster1.0'")


def singualr_test_case_options():
    print(yellow_text + f"Options Menu - [Single - Test Cases]:")
    print(f"{Fore.YELLOW}1{Fore.WHITE}. loginToUserAccount()")
    print(f"{Fore.YELLOW}2{Fore.WHITE}. loginAndLoadHomePage()")
    print(f"{Fore.YELLOW}3{Fore.WHITE}. checkInitialUserRole()")
    print(f"{Fore.YELLOW}4{Fore.WHITE}. checkHomePageloaded()")
    print(f"{Fore.YELLOW}5{Fore.WHITE}. homePageLoadAdminScreen()")
    print(f"{Fore.YELLOW}6{Fore.WHITE}. staffAdminLoadMenuOptions()")
    print(f"{Fore.YELLOW}7{Fore.WHITE}. staffAdminLoadEmployees()")   
    print(f"{Fore.YELLOW}7{Fore.WHITE}. startDateOverridemployee() *1 - 5yrs employment (202.5 hours) ")
    print(f"{Fore.YELLOW}7{Fore.WHITE}. startDateOverridemployee() *5 - 10yrs employment (217.5 hours) ")
    print(f"{Fore.YELLOW}7{Fore.WHITE}. startDateOverridemployee() *10+ yrs employment (247.5 hours) ")
    print(f"{Fore.YELLOW}q{Fore.WHITE}. Quit to 'Main Menu'")


def batch_test_case_options(): 
    print(get_color_code("PINK") + f"Note*{white_text} - Ensure excel file related to the test has been added to '/excel_sheets' folder")
    print(yellow_text + f"Options Menu - [Batch - Test Cases]:")
    print(f"{Fore.YELLOW}1{Fore.WHITE}. batchProcessEmployees()")
    print(f"{Fore.YELLOW}2{Fore.WHITE}. batchProcessUserTypeTiles()")
    print(f"{Fore.YELLOW}3{Fore.WHITE}. batchProcessStartDateOverrides()")
    print(f"{Fore.YELLOW}q{Fore.WHITE}. Quit to 'Main Menu'")


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


def processExcelSheets(title):
    excel_folder = 'bug_buster\\excel_sheets'
    valid_files = []
    valid_file_paths = []

    while(1):
        clear_console()
        print(title)
        print(yellow_text + "Selected Excel Files:" + white_text, valid_files)
        print(yellow_text + "Please enter the name of the Excel sheet you wish to process" + white_text)
        print("[" + get_color_code("PINK") + f"WARNING: {white_text}Please include the {yellow_text}.xlsx{white_text} file extension]: ")
        file_name = input()

        if file_name in valid_files: 
            clear_console()
            print(title)
            print(yellow_text + "Selected Excel Files:" + white_text, valid_files)
            print(f"{yellow_text}File '{white_text}{file_name}{yellow_text}' already selected")
            print(yellow_text + f"If you would like to add another file, press '{white_text}y{yellow_text}', otherwise press '{white_text}q{yellow_text}' to continue: {white_text}")
            while(1):
                validation = input()
    
                if validation == 'y': 
                    break
                elif validation == 'q': 
                    return valid_file_paths
                else: 
                    clear_console()
                    print(title)
                    print(get_color_code("PINK") + f"Invalid input: Please enter '{white_text}y{yellow_text}' to add another file or '{white_text}q{yellow_text}' to continue: {white_text}")
        else: 
            if not file_name:
                break  # Continue to the next section of code

            file_path = os.path.join(excel_folder, file_name)

            if os.path.exists(file_path) and os.path.isfile(file_path):
                valid_files.append(file_name)
                valid_file_paths.append(excel_folder + "\\" + file_name)
                clear_console()
                print(title)
                print(yellow_text + "Selected Excel Files:" + white_text, valid_files)
                print(yellow_text + f"If you would like to add another file, press '{white_text}y{yellow_text}', otherwise press '{white_text}q{yellow_text}' to continue: {white_text}")
                while(1):
                    validation = input()
    
                    if validation == 'y': 
                        break
                    elif validation == 'q': 
                        return valid_file_paths
                    else: 
                        clear_console()
                        print(title)
                        print(get_color_code("PINK") + f"Invalid input: Please enter '{white_text}y{yellow_text}' to add another file or '{white_text}q{yellow_text}' to continue: {white_text}")

            else:
                clear_console()
                print(title)
                print(yellow_text + "File " + get_color_code("PINK") + f"'{file_name}' {yellow_text}does not exist or is not a valid file.")
                print(f"If you would like to try again, press '{white_text}y{yellow_text}', otherwise press '{white_text}q{yellow_text}' to return back to the options menu: {white_text}")
                while(1): 
                    validation = input()

                    if validation.lower() == 'y':
                        clear_console()
                        break # Repeat the loop for another file
                    elif validation.lower() == 'q':
                        clear_console()
                        return False # Continue to the next section of code
                    else:
                        clear_console()
                        print(title)
                        print(get_color_code("PINK") + f"Invalid input: {yellow_text}Please enter '{white_text}y{yellow_text}' to add another file or '{white_text}q{yellow_text}' to continue: {white_text}")


def main():
    global wrong_input_flag 
    global wrong_input_flag2
    global no_of_tests

    right_input_flag = True
    wrong_input_flag = True
    wrong_input_flag2 = True
    no_of_tests = 4

    print(red_text + ascii_bug_art + white_text)
    print(ascii_title_art)
    print(yellow_text + "Please enter username: " + white_text) 
    username = input()
    print(yellow_text+ "Please enter password: " + white_text)
    password = input("")
    clear_console()
    

    while True:
        print(ascii_title_art)
        if wrong_input_flag:
            #print(username)
            #print(password)
            print(yellow_text + "Please enter Target System: " + white_text)
        else: 
            print(yellow_text + "Please enter an existing system: " + white_text)
        target_system = input()
        if target_system in target_systems:
            break
        else: 
            wrong_input_flag = False 
            clear_console()

    clear_console()
    
    while(1): 
        print(ascii_title_art)
        print(get_color_code("PINK") + f"Note*{white_text} - Successful tests dependant on stable internet connecton")
        print(get_color_code("PINK") + f"{yellow_text}Target system:{white_text} " + white_text + target_system + "\n")

        main_options_menu()

        if right_input_flag:
            print(yellow_text + "Please select the type of tests you want to perform: " + white_text)
            test_option = input()
        elif wrong_input_flag:
            print(yellow_text + "Please select the type of tests you want to perform:" + white_text)
            print(f"[{yellow_text}Message{white_text}: Enter an option within the scope that is defined]: ")
            test_option = input()
        elif wrong_input_flag == False:
            print(yellow_text + "Please select the type of tests you want to perform:" + white_text)
            print(f"[{yellow_text}Message{white_text}: Enter a number that corresponds to an option]: ")
            test_option = input()

        if test_option == '1': 
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1): 
                clear_console()
                # Create the Linux-style header
                print(ascii_title_art)
                print(get_color_code("PINK") + f"Note*{white_text} - Successful tests dependant on stable internet connecton")
                print(get_color_code("PINK") + f"{yellow_text}Target system:{white_text} " + white_text + target_system + "\n")
                singualr_test_case_options()

                if right_input_flag:
                    print(yellow_text + "Please select the repeat process you'd like to test: " + white_text)
                    test_option = input()
                elif wrong_input_flag:
                    print(yellow_text + "Please select the repeat process you'd like to test" + white_text)
                    print(f"[{yellow_text}Message{white_text}: Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(yellow_text + "Please select the repeat process you'd like to test" + white_text)
                    print(f"[{yellow_text}Message{white_text}: Enter a number that corresponds to an option]: ")
                    test_option = input()
                
                # Singular test case functions 
                if test_option == '1': 
                    # Checks to see if user can log in
                    thread = threading.Thread(target=atf.loginToUserAccount, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                    clear_console()

                elif test_option == '2': 
                    # Checks to see if user can log in
                    thread = threading.Thread(target=atf.loginAndLoadHomePage, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                    clear_console()

                elif test_option == '3':
                    # Checks user role is 'Root' user on load up 
                    thread = threading.Thread(target=atf.checkInitialUserRole, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")
                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                    clear_console()
                elif test_option == '4':
                    # Check homepage loads with tiles/correct text appearing.  
                    thread = threading.Thread(target=atf.checkHomePageloaded, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                elif test_option == '5': 
                    # Loads admin screen by clicking on 'Admin Button'
                    thread = threading.Thread(target=atf.homePageLoadAdminScreen, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                elif test_option == '6': 
                    # Loads 'Staff Admin' Menu options
                    thread = threading.Thread(target=atf.staffAdminLoadMenuOptions, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)
                elif test_option == '7':
                    # Clicks on employees menu option under 'Staff Admin' and loads employee tiles
                    thread = threading.Thread(target=atf.staffAdminLoadEmployees, args=(target_system, username, password)) # arguments expressed as a tuple 
                    thread.start()

                    print("Awaiting test results...")

                    # Capture the thread's standard output
                    sys.stdout.flush()  # Flush any pending output
                    thread.join() # Wait for the thread to complete

                    print("Test is complete!")
                    input(yellow_text + "Press Enter to clear the console." + white_text)

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

        
        elif test_option == '2':
            right_input_flag = True
            wrong_input_flag = True
            wrong_input_flag2 = True
            while(1):
                clear_console()
                # Create the Linux-style header
                print(ascii_title_art)
                print(get_color_code("PINK") + f"Note*{white_text} - Successful tests dependant on stable internet connecton")
                print(get_color_code("PINK") + f"{yellow_text}Target system:{white_text} " + white_text + target_system + "\n")
                batch_test_case_options()

                if right_input_flag:
                    print(yellow_text + "Please select the repeat process you'd like to test: " + white_text)
                    test_option = input()
                elif wrong_input_flag:
                    print(yellow_text + "Please select the repeat process you'd like to test" + white_text)
                    print(f"[{yellow_text}Message{white_text}: Enter an option within the scope that is defined]: ")
                    test_option = input()
                elif wrong_input_flag == False:
                    print(yellow_text + "Please select the repeat process you'd like to test" + white_text)
                    print(f"[{yellow_text}Message{white_text}: Enter a number that corresponds to an option]: ")
                    test_option = input()

                # Batch Process Functions 
                if test_option == '1':
                   excel_sheets = processExcelSheets(ascii_title_art)

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       thread = threading.Thread(target=atf.batchProcessEmployees, args=(target_system, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(yellow_text + "Press Enter to clear the console." + white_text)
                       clear_console()

                elif test_option == '2':
                   excel_sheets = processExcelSheets(ascii_title_art)

                   if excel_sheets == False: 
                       pass
                       clear_console()
                   else: 
                       thread = threading.Thread(target=atf.batchProcessUserTypeTiles, args=(target_system, username, password, excel_sheets)) # arguments expressed as a tuple 
                       thread.start()

                       print("Awaiting test results...")

                       # Capture the thread's standard output
                       sys.stdout.flush()  # Flush any pending output
                       thread.join() # Wait for the thread to complete

                       print("Test is complete!")
                       input(yellow_text + "Press Enter to clear the console." + white_text)
                       clear_console()

                #elif test_option == '3':
                #   excel_sheets = processExcelSheets(ascii_title_art)

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
            # will be an options to select between particular overnight processes or all of them. 
            print(red_text + ascii_bug_art)
            print(white_text + "Oh no, the overnight processes havent been implemented yet!!!")
            input(yellow_text + "Press Enter to clear the console." + white_text)
            clear_console()
            pass

        elif test_option == 'q'.lower() : 
            clear_console()
            print(ascii_title_art)
             
            print(yellow_text + 'Thank you for using BugBuster!')
            exit()

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