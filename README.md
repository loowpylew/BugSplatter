# BugSplatter  
**Application Overview: Web Development Unit Tester**

<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
  <img src="https://github.com/user-attachments/assets/f414617d-bb84-470d-9e21-76e798bab14d" alt="Image 1" style="width: 400px; margin-right: 20px;">
  <img src="https://github.com/user-attachments/assets/66e6ce8f-311d-4fd7-8040-d4db1a9032c0" alt="Image 2" style="width: 420px; height: 655px;">
</div>

---

BugSplatter is a Python-based application designed for automating unit testing processes in web development. At its core, it leverages Selenium modules to interact with a Chromium-based web browser. Its interface operates via a terminal-style display, such as Visual Studio Code’s integrated terminal or a Linux-style command prompt. 

To streamline testing workflows, BugSplatter has been packaged into an executable using **Anaconda**. This eliminates the need for the implementation team to install Python, import modules, or set up a development environment. This approach ensures testers can execute the application seamlessly without navigating to the `main.py` file.  

For developers, BugSplatter is optimized to allow rapid prototyping and testing directly in the console, avoiding the overhead of repeatedly converting the application into an executable for every small code change.

---

## **Key Features and Use Cases**  

### **Automated Testing**
1. **Excel Comparisons**  
   - Validates the consistency of tiles and submenus across systems, ensuring that schema, table, and data changes are correctly applied.  
   - Reduces time-consuming manual checks and eliminates the risk of human error in verifying data and object presence in the front-end.  

2. **Single Test Cases**  
   - Addresses discrepancies between development and production environments, often arising from client-specific configurations.  
   - Provides tailored test cases for verifying data or UI changes for specific client needs.  

3. **Batch Testing**  
   - Facilitates bulk validation of backend-to-frontend consistency by automating checks for large datasets.  
   - Executes repetitive tasks for hundreds or thousands of rows efficiently.  

### **Regular Maintenance Tasks**  
- Automates routine processes such as rebuilding JavaScript files to ensure DOM updates reflect recent changes.  
- Streamlines deployments across multiple systems by automating repetitive browser tasks, such as navigating and updating files.

---

## **Technical Specifications**

### **Chromium and ChromeDriver Integration**  
- Chromium (`Win_x64_1135619_chrome-win`) and ChromeDriver (`Chromedriver_win32`) are required for full functionality.  
- These files exceed GitHub's 100MB single-file limit and are excluded from the repository.  
  - **For development purposes**: Download these files directly from links provided in `.dev_setup_file.md` (located in `/bug_buster_dev_env` or `/bug_buster_build_env`).  
  - **For general users**: A zipped version, including these dependencies, is available on SharePoint for internal distribution.  

---

## **Project Structure**  

### **Development and Build Environments**  
1. **Development Environment (`/bug_buster_dev_env`)**  
   - Core location for ongoing development.  
   - Contains scripts such as `main.py` and `automated_test_function.py` for adding or updating functionality.  

2. **Build Environment (`/bug_buster_build_env`)**  
   - A replica of the development environment, with additional folders generated during the executable packaging process using Anaconda and PyInstaller.  
   - Includes `/build`, `/dist`, and `bugbuster1.0.spec`.  
   - Demo executable (`/BugSplatter1.0`) is available here but excludes the required Chromium and ChromeDriver folders.

---

### **Supporting Files and Directories**  

- **`/command_tool_globals`**  
   - Includes `wget.exe` for automated file downloads during setup.  
   - Contains utilities such as BFG Repo Cleaner (for addressing Git cache issues) in case large files are reintroduced to the repository.  

- **`/installs`**  
   - Houses executables for Git Large File Storage (LFS) and related setup files for managing large files exceeding GitHub’s limits.  

---

## **Setup and Deployment**

1. For testing or deployment without code changes:  
   - Use the prepackaged `.exe` file along with the zipped version of Chromium and ChromeDriver available on SharePoint.  

2. For developers modifying the source code:  
   - Use the development environment and ensure dependencies, including Chromium and ChromeDriver, are manually downloaded as per `.dev_setup_file.md`.  

3. To address Git cache issues:  
   - Utilize the BFG Repo Cleaner executable located in `/command_tool_globals` and follow the provided setup script for efficient file cleanup.  

---

### **Future Considerations**  
- If GitHub’s storage limitations become a bottleneck, the application includes prebuilt utilities for transitioning to Git Large File Storage (LFS).  
- The repository structure and setup files are designed to support smooth scalability and transition to paid GitHub plans, if needed.

---

BugSplatter optimizes web development unit testing by automating repetitive and error-prone tasks, enhancing testing efficiency, and supporting seamless deployments across systems. Its modular design ensures flexibility for both development and production needs.
