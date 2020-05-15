import os
import subprocess as sub
from sys import platform
import getpass
from threading import *
# from Script_Runner import scriptrunnerGUI as srg

import distro #for figuring out what linux distro

#global variables
OS = distro.linux_distribution()
ops = OS[0]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class mmfunc:
    def updates():
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt update && upgrade -y'
            sub.Popen(command.split())
            print('Updates Completed!')
        elif platform == 'darwin':
            command = 'sudo softwareupdate -i -a'
            sub.Popen(command.split())
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -Syu'
            sub.Popen(command.split())
        elif platform == 'win32':
            #command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./mmfucntions.ps1\";", "&winupd"
            #sub.Popen(command)
            commands = """ Write-Host("Installing module PSWindowsUpdate if not already installed... ")
            Install-Module PSWindowsUpdate
            Write-Host("PSWindowsUpdate is now installed.")
            Write-Host("")
            Write-Host("Getting Windows Updates...")
            Import-Module PSWindowsUpdate
            $updates = Invoke-Command -ScriptBlock {Get-Wulist -verbose}
            $updatenumber = ($updates.kb).count
            if ($null -ne $updates){
                Get-WindowsUpdate -AcceptAll -Install | Out-File C:\PSWindowsUpdate.log
                do {$updatestatus = Get-Content c:\PSWindowsUpdate.log
                    "Currently processing the following update:"
                    Get-Content c:\PSWindowsUpdate.log | select-object -last 1
                    Start-Sleep -Seconds 10
                    $ErrorActionPreference = 'SilentlyContinue'
                    $installednumber = ([regex]::Matches($updatestatus, "Installed" )).count
                    $ErrorActionPreference = ‘Continue’
                }until ( $installednumber -eq $updatenumber)
            }
            Remove-Item -path C:\PSWindowsUpdate.log -ErrorAction SilentlyContinue
            Write-Host("")
            Write-Host("All updates are installed!")"""
            sub.Popen(["powershell","& {" + commands + "}"])
            # Definitely is executing but it needs to be run as admin. Must figure out a way to do that.

            # print('This function (updates) does not currently support this OS.')
        else:
            print('This command does not currently support this OS')

    def srchmedia():
        if platform == 'linux' or platform == 'darwin':
            extensions = ('.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
            for root, dirs, files in os.walk('/home/'):
                for filename in files:
                    if any(filename.endswith(extension) for extension in extensions):
                        # f = open('Q:\\Cyber Patriots\\my_scripts_and_STIGS\\Scripts\\CP_ScriptsREPAIR\\Script Runner GUI\\logTest.txt', 'a+')
                        f = open('/home/' + getpass.getuser() + '/Desktop/LogTest.txt', 'a+')
                        filepath = os.path.join(root, filename)
                        f.write(filepath + '\n')
                        f.close()
                        print(filepath)
            print('Scan for unapproved media complete.')
        elif platform == 'win32':
            extensions = ('.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
            for root, dirs, files in os.walk('C:\\Users\\'):
                for filename in files:
                    if any(filename.endswith(extension) for extension in extensions):
                        f = open('C:\\Users\\' + getpass.getuser() + '\\Desktop\\logTest.txt', 'a+')
                        #f = open('/home/' + getpass.getuser() + '/Desktop/LogTest.txt', 'a+')
                        filepath = os.path.join(root, filename)
                        f.write(filepath + '\n')
                        f.close()
                        print(filepath)
            print('Scan for unapproved media complete.')

    def fwl():
        print('This command is currently in developement')

    def servSet():
        print('This command is currently in developement')

    def malRem():
        print('This command is currently in developement')

    def alyn():
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt install lynis -y'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system'
            sub.Popen(command2.split())
        elif ops == 'darwin':
            print('This function does not currently support this OS')
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S lynis'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system'
            sub.Popen(command2.split())
        elif platform == 'win32':
            print('This function (alyn) does not currently support this OS.')

    def basConf():
        print('This command is currently in developement')

    def rmProCont():
        print('This command is currently in developement')



class ThreadmmFunc():
    def threaderSRCH(self):
        try:
            self.threader = Thread(target=mmfunc.srchmedia)
            self.threader.start()
        except Exception as e:
            print(e)
            #print(com)
            print('Could not start thread')

    def threaderUPDT(self):
        try:
            self.threader = Thread(target=mmfunc.updates)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderFWL(self):
        try:
            self.threader = Thread(target=mmfunc.fwl)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderServ(self):
        try:
            self.threader = Thread(target=mmfunc.servSet)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderMALREM(self):
        try:
            self.threader = Thread(target=mmfunc.malRem)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderALYN(self):
        try:
            self.threader = Thread(target=mmfunc.alyn)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderBASEconf(self):
        try:
            self.threader = Thread(target=mmfunc.basconf)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def threaderRMproCont(self):
        try:
            self.threader = Thread(target=mmfunc.rmProCont)
            self.threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')
