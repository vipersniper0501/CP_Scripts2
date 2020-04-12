# CP_Scripts2
DISCLAIMERS: This project is student made with inspiration from other projects such as the scripts made by Ethan Fowler from TEAM BYTE.
This script also uses Microsoft Sysinternals suite which is owned and created by Microsoft. I do not take any credit in the creation of that program. (_I don't want to get sued_)  

FYI- This will be mostly used for a backup location for my scripts and will not always have the most up to date versions.

### Dependancies

- GUI
  - Admin access
  - python3 (pre-installed on most Linux distros)
  - distro module (automatically installed with installer.py)

- Powershell Script
  - Admin access
  - Set-ExecutionPolicy Unrestricted

- Linux Scripts
  - Admin access


### Usage Instructions For GUI

1.) Navigate to Script_Runner.py as Administrator in either Powershell (windows) or Terminal (Linux)

2.) run ```python3 .\Script_Runner.py``` in Powershell or ```sudo python3 Script_Runner.py``` in Terminal

If you do not do it this way then quite a few commands will not work.


#Usage Instructions For Powershell Scripts:

1.)Run powershell as admin

2.)Navigate to location of script file through powershell ex: cd C:\Users\Michael\Downloads\

3.)In powershell type the following: Set-ExecutionPolicy Unrestricted          

Do this to allow the execution of scripts

4.)Once at the location where the script is located type the following: ./cyberWin10.ps1

Hit Enter

That is it! Good Luck!

Some of the commands might require for you to execute them twice if they did not show a list when they should have. I am currently working on fixing this problem.

#Usage Instructions For Linux Scripts

1.) Navigate to directory where script is located in terminal

2.) type without quotes : "sudo bash ./linux_Script.sh"

3.) The script is now running and you are now free to choose the commands to execute
