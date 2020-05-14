# CP_Scripts2
DISCLAIMERS: This project is student made with inspiration from other projects such as the scripts made by Ethan Fowler from TEAM BYTE.
This script also uses Microsoft Sysinternals suite which is owned and created by Microsoft. I do not take any credit in the creation of that program. (_I don't want to get sued_)  

FYI- This will be mostly used for a backup location for my scripts and will not always have the most up to date versions.

### Dependancies

- GUI
  - Admin access

- Powershell Script
  - Admin access
  - Set-ExecutionPolicy Unrestricted

- Linux Scripts
  - Admin access

### How to compile GUI
Make sure you have the correct version of Pyinstaller:
`pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz`

Run `pip install auto-py-to-exe` to install the compiler.

For executables that work on Windows:	Run auto-py-to-exe on a windows machine

For executables that work with linux:   Run auto-py-to-exe on a Linux/Unix machine


1.) Move all files that are to be converted into a .exe onto the desktop.

2.) open powershell/terminal as admin and type `auto-py-to-exe`

3.) In `Script Location` in the newly opened window, put in the location of the .py file that launches the GUI

4.) Under Additional Files, add all folders and files that are to be used in the script

5.) Under Advanced, change Output Directory to the desktop to easily locate the newly created .exe file

6.) Hit `Convert .PY TO .EXE`

7.) your newly created .exe file should now have been created and added to the desktop



https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi



### Usage Instructions For CLI Powershell Scripts:

1.)Run Powershell as Admin

2.)Navigate to location of script file through powershell ex: `cd C:\Users\Michael\Downloads\`

3.)In powershell type the following: `Set-ExecutionPolicy Unrestricted`          

Do this to allow the execution of scripts

4.)Once at the location where the script is located type the following: `./cyberWin10.ps1`

Hit Enter

That is it! Good Luck!

Some of the commands might require for you to execute them twice if they did not show a list when they should have. 
I am currently working on fixing this problem.

### Usage Instructions For Linux CLI Scripts

1.) Navigate to directory where script is located in terminal

2.) Type the following: `sudo bash ./linux_Script.sh`

3.) The script is now running and you are now free to choose the commands to execute


## Version Numbers

1.0.0.0

**First Number:** used for releases

**Second Number:** used for Feature Updates Ex: New command has been completed and works as supposed to.

**Third Number:** used for patches and updates that are working towards a new feature. Also updated when code has been
edited to become more efficient.

**Fourth Number:** used for minor updates. Usually finding a typo or quick edits. Or, if a file was forgotten when pushing
to GitHub.

**NOTE:** When ever a version number has been updated, all of the numbers to the right of the changed number is set to zero.