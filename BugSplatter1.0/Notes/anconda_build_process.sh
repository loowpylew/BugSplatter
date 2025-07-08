# Create an environment to download all your modules etc specific to the project at hand
conda create --name bugSplatter python=3.8

# Navigate into your environment
conda activate bugSplatter

# Navigate to where your main.py file is housed
cd into ./python_project_files/

# install pyinstaller - module used to compile project into an .exe
pip install pyinstaller

# install all your modules from the requirements file
pip install -r ./Notes/req.txt

# compile the main.py file into an .exe to see if the build was successful 
pyinstaller main.py

# run after compilation to see if the program doesnt bomb out. 
python main.py

# Convert file into into exe with and name the the .exe as well as giving it an icon
pyinstaller --onefile --name=bugSplatter1.0 --icon=icon.ico ./python_project_files/main.py

# If you need to remove environment
conda env remove --name your_environment_name