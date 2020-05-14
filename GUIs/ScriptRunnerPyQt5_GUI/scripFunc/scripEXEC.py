import os
import subprocess as sub
from sys import platform
import getpass
from threading import *
import distro  # for figuring out what linux distro
import configparser
import shutil
from PyQt5 import QtGui
from PyUIs.hashgen import Ui_hashGEN
from PyUIs.enblebit import Ui_bitlockerGUI
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

OS = distro.linux_distribution()
ops = OS[0]

config = configparser.ConfigParser()
config.read('config.ini')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ScriptRunnerFunc:
    def test():
        print('Hello World')

    # Universal Updates
    def updateos(self):
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
            # command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./mmfucntions.ps1\";", "&winupd"
            # sub.Popen(command)
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
            sub.Popen(["powershell", "& {" + commands + "}"])
            # Definitely is executing but it needs to be run as admin. Must figure out a way to do that.

            # print('This function (updates) does not currently support this OS.')
        else:
            print('This command does not currently support this OS')

    # Universal Search Media
    def srchmedia(self):
        if platform == 'linux' or platform == 'darwin':
            extensions = (
                '.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
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
            extensions = (
                '.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
            for root, dirs, files in os.walk('C:\\Users\\'):
                for filename in files:
                    if any(filename.endswith(extension) for extension in extensions):
                        f = open('C:\\Users\\' + getpass.getuser() + '\\Desktop\\logTest.txt', 'a+')
                        # f = open('/home/' + getpass.getuser() + '/Desktop/LogTest.txt', 'a+')
                        filepath = os.path.join(root, filename)
                        f.write(filepath + '\n')
                        f.close()
                        print(filepath)
            print('Scan for unapproved media complete.')

    # linux and windows firewall settings. Can only change Mac firewall through GUI
    def fwl(self):
        if platform == 'linux':

            commandtest = 'sudo ufw status'
            EXEC = sub.Popen(commandtest.split(), stdout=sub.PIPE)
            stdout, _ = EXEC.communicate()
            output = stdout.decode('utf-8')

            if output == 'sudo: ufw: command not found':
                if ops == "Manjaro Linux":
                    commandufw = 'sudo pacman -S ufw --noconfirm'
                else:
                    commandufw = 'sudo apt install ufw -y'
                sub.call(commandufw.split())
                command = 'sudo ufw enable'
                sub.Popen(command.split())

            commandlog = 'sudo ufw status > firewallLOG.txt'
            os.system(commandlog)
            with open('firewall.txt', 'r') as f:
                for line in f:
                    output = f.read()
            print('The following is the output of your original firewall settings:\n')
            print(output)

            print('-----------------------Firewall Settings Has Started-----------------------')
            # SSH
            ssh = config.get('Services', 'ssh')
            if ssh == 'yes':
                command = 'sudo ufw allow 22'
                sub.Popen(command.split())
            elif ssh == 'no':
                command = 'sudo ufw deny 22'
                sub.Popen(command.split())
            # FTP
            ftp = config.get('Services', 'ftp')
            if ftp == 'yes':
                command = 'sudo ufw allow 21'
                sub.Popen(command.split())
            elif ftp == 'no':
                command = 'sudo ufw deny 21'
                sub.Popen(command.split())
            # WEB
            web = config.get('Services', 'web')
            if web == 'yes':
                command = 'sudo ufw allow 80'
                sub.Popen(command.split())
                https = config.get('Services', 'https')
            elif web == 'no':
                command = 'sudo ufw deny 80'
                sub.Popen(command.split())
            # HTTPS
            https = config.get('Services', 'https')
            if https == 'yes':
                command = 'sudo ufw allow 443'
                sub.Popen(command.split())
            elif https == 'no':
                command = 'sudo ufw deny 443'
                sub.Popen(command.split())
            # Samba
            smb = config.get('Services', 'smb')
            if smb == 'yes':
                command = 'sudo ufw allow 139'
                sub.Popen(command.split())
            elif smb == 'no':
                command = 'sudo ufw deny 139'
                sub.Popen(command.split())
            # SQL
            sql = config.get('Services', 'sql')
            if sql == 'yes':
                command = 'sudo ufw allow 3306'
                sub.Popen(command.split())
            elif sql == 'no':
                command = 'sudo ufw deny 3306'
                sub.Popen(command.split())
            # Rsync
            rsnc = config.get('Services', 'rsnc')
            if rsnc == 'yes':
                command = 'sudo ufw allow 873'
                sub.Popen(command.split())
            elif rsnc == 'no':
                command = 'sudo ufw deny 873'
                sub.Popen(command.split())

            print('------------------The Following Ports Have Been Closed Automatically-----------------')
            print('Port 19 has been closed to stop potential DoS attack')
            command = 'sudo ufw deny 19'
            sub.Popen(command.split())
            print('Port 123 has been closed to stop potential trojans (NetController)')
            command = 'sudo ufw deny 123'
            sub.Popen(command.split())
            print('Port 161 has been closed to stop SNMP functionality')
            command = 'sudo ufw deny 161'
            sub.Popen(command.split())
            print('Port 162 has been closed to stop SNMPtrap functionality')
            command = 'sudo ufw deny 162'
            sub.Popen(command.split())
            print('Port 1434 has been blocked to stop potential DoS attack')
            command = 'sudo ufw deny 1434'
            sub.Popen(command.split())
            print('Port 23 has been denied due to Telnet functionality is not necessary')
            command = 'sudo ufw deny 23'
            sub.Popen(command.split())

            # This next service should probably be asked during first time configurations

            # print('Port 53 has been closed to stop the use of DNS functionality since this is not a DNS Server')
            # command = 'sudo ufw deny 53'
            # sub.Popen(command.split())

            print('--------------------Firewall Settings Have Finished-----------------------')

        elif platform == 'win32':
            print('-----------------------Firewall Settings Has Started-----------------------')
            ssh = config.get('Services', 'ssh')
            if ssh == 'yes':
                command = "netsh advfirewall firewall add rule name='ssh' dir=in action=allow protocol=TCP localport=22"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=out action=allow protocol=TCP localport=22"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif ssh == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=22"
                sub.call(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=in action=block protocol=TCP localport=22"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=out action=block protocol=TCP localport=22"
                sub.Popen(["powershell", "& {" + command + "}"])
            # FTP
            ftp = config.get('Services', 'ftp')
            if ftp == 'yes':
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=allow protocol=TCP localport=21"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=out action=allow protocol=TCP localport=21"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif ftp == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=21"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
                sub.Popen(["powershell", "& {" + command + "}"])
            # WEB
            web = config.get('Services', 'web')
            if web == 'yes':
                command = "netsh advfirewall firewall add rule name='webserver' dir=in action=allow protocol=TCP localport=80"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=out action=allow protocol=TCP localport=80"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif web == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=80"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=in action=block protocol=TCP localport=80"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=out action=block protocol=TCP localport=80"
                sub.Popen(["powershell", "& {" + command + "}"])
            # HTTPS
            https = config.get('Services', 'https')
            if https == 'yes':
                command = "netsh advfirewall firewall add rule name='https' dir=in action=allow protocol=TCP localport=443"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dire=out action=allow protocol=TCP localport=443"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif https == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=443"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dir=in action=block protocol=TCP localport=443"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dire=out action=block protocol=TCP localport=443"
                sub.Popen(["powershell", "& {" + command + "}"])
            # Samba
            smb = config.get('Services', 'smb')
            if smb == 'yes':
                command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=allow protocol=TCP localport=139"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dire=out action=allow protocol=TCP localport=139"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif smb == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=139"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=block protocol=TCP localport=139"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dire=out action=block protocol=TCP localport=139"
                sub.Popen(["powershell", "& {" + command + "}"])
            # SQL
            sql = config.get('Services', 'sql')
            if sql == 'yes':
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=allow protocol=TCP localport=3306"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=allow protocol=TCP localport=3306"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif sql == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3306"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=block protocol=TCP localport=3306"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=block protocol=TCP localport=3306"
                sub.Popen(["powershell", "& {" + command + "}"])
            # Rsync
            rsnc = config.get('Services', 'rsnc')
            if rsnc == 'yes':
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=allow protocol=TCP localport=873"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=allow protocol=TCP localport=873"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif rsnc == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=873"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=block protocol=TCP localport=873"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=block protocol=TCP localport=873"
                sub.Popen(["powershell", "& {" + command + "}"])
            # RDP
            rdp = config.get('Services', 'rdp')  # must block/allow port 5985 and 3389
            if rdp == 'yes':
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=5985"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=3389"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=5985"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=3389"
                sub.Popen(["powershell", "& {" + command + "}"])
            elif rdp == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=5985"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3389"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=5985"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=3389"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=5985"
                sub.Popen(["powershell", "& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=3389"
                sub.Popen(["powershell", "& {" + command + "}"])

            print('------------------The Following Ports Have Been Closed Automatically-----------------')
            print('Port 19 has been closed to stop potential DoS attack')
            command = "netsh advfirewall firewall add rule name='port19BLOCK' dir=in action=block protocol=TCP localport=19"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port19BLOCK' dir=out action=block protocol=TCP localport=19"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('Port 123 has been closed to stop potential trojans (NetController)')
            command = "netsh advfirewall firewall add rule name='port123BLOCK' dir=in action=block protocol=TCP localport=123"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port123BLOCK' dir=out action=block protocol=TCP localport=123"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('Port 161 has been closed to stop SNMP functionality')
            command = "netsh advfirewall firewall add rule name='port161BLOCK' dir=in action=block protocol=TCP localport=161"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port161BLOCK' dir=out action=block protocol=TCP localport=161"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('Port 162 has been closed to stop SNMPtrap functionality')
            command = "netsh advfirewall firewall add rule name='port162BLOCK' dir=in action=block protocol=TCP localport=162"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port162BLOCK' dir=out action=block protocol=TCP localport=162"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('Port 1434 has been blocked to stop potential DoS attack')
            command = "netsh advfirewall firewall add rule name='port1434BLOCK' dir=in action=block protocol=TCP localport=1434"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port1434BLOCK' dir=out action=block protocol=TCP localport=1434"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('Port 23 has been denied due to Telnet functionality is not necessary')
            command = "netsh advfirewall firewall add rule name='port23BLOCK' dir=in action=block protocol=TCP localport=23"
            sub.Popen(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='port23BLOCK' dir=out action=block protocol=TCP localport=23"
            sub.Popen(["powershell", "& {" + command + "}"])

            print('--------------------Firewall Settings Have Finished-----------------------')

        elif platform == 'darwin':
            print('This command is currently in developement')
        else:
            print('This command is currently in developement')

    def servSet(self):
        print('This command is currently in developement')

    # Only works with linux. Other OS's must use a third party Ex: Malwarebytes
    def malRem(self):
        if platform == 'linux':
            if ops == 'Manjaro Linux':
                command = 'sudo pacman -S clamav -y'
                sub.Popen(command.split())
            else:
                command = 'sudo apt install clamav -y'
                sub.Popen(command.split())
            command = ['sudo freshclam', 'sudo touch CLAMresults.txt',
                       'sudo clamscan -r --remove / | tee CLAMresults.txt']
            for i in range(0, 3):
                sub.Popen(command[i].split())
        else:
            print('This command is currently in developement')

    # Only works on Linux (Maybe Mac. Need to test)
    def alyn(self):
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt install lynis -y'
            sub.Popen(command.split())
            command = 'sudo touch auditRESULTS.txt'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
            sub.Popen(command2.split())
        elif ops == 'darwin':
            print('This function does not currently support this OS')
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S lynis --noconfirm'
            sub.Popen(command.split())
            command = 'sudo touch auditRESULTS.txt'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
            sub.Popen(command2.split())
        elif platform == 'win32':
            print('This function does not currently support this OS.')

    # Still needs Linux configurations
    def basConf(self, rdp):
        if platform == 'win32':
            if rdp == 'yes':
                path = 'win10StigsRDPn/Windows10Template11_17.inf'
                try:
                    shutil.copy('./winCONF/win10StigsRDPy/Machine', r'c:\Windows\System32\GroupPolicy\Machine')
                    shutil.copy('./winCONF/win10StigsRDPy/User', r'c:\Windows\System32\GroupPolicy\User')
                    shutil.copy('../winCONF/win10StigsRDPy/gpt.ini', r'c:\Windows\System32\GroupPolicy\GPT.INI')
                except IOError as e:
                    print("Unable to copy file. %s" % e)
            elif rdp == 'no':
                path = 'win10StigsRDPy/win10secRDPallowed.inf'
                try:
                    shutil.copy('../winCONF/win10StigsRDPn/Machine', r'c:\Windows\System32\GroupPolicy\Machine')
                    shutil.copy('../winCONF/win10StigsRDPn/User', r'c:\Windows\System32\GroupPolicy\User')
                    shutil.copy('../winCONF/win10StigsRDPn/gpt.ini', r'c:\Windows\System32\GroupPolicy\GPT.INI')
                    print('Successfully installed Group Policy Settings')
                except IOError as e:
                    print('Unable to copy file. %s' % e)
            else:
                raise ValueError('rdp should be either yes or no!')
            command = 'secedit.exe /configure /db %windir%\\security\\local.sdb /cfg ../winCONF/' + path
            sub.Popen(command.split())
            command = 'Enable-WindowsOptionalFeature –FeatureName "Internet-Explorer-Optional-amd64" -All –Online'
            sub.Popen(["powershell", "& {" + command + "}"])

            # Must also uninstall all other prohibited features

        elif platform == 'linux':
            if rdp == 'yes':
                print('Settings that include remote desktops will be configured')
            elif rdp == 'no':
                print('Settings that do not include remote desktops will be configured.')
            else:
                raise NameError('There has been an error in the Configuration file. RDP mus be either yes or no')

        print('This command is currently in developement')

    '''
    Removal of Prohibited Software.
    Before running through list of software to remove, you must ask user if there are any required applications.
    Give a list that pops up and have them check of programs from the list that they want to keep. 
    '''

    def rmProSoft(self):

        # Get-WmiObject -Class Win32_Product | Select-Object -Property Name
        # ^ will print out list of all installed programs.

        index = ['uTorrent',
                 'BitTorrent',
                 'Nmap',
                 'Kodi',
                 'Chicken Invaders',
                 'KNCTR',
                 'Real Player',
                 'Driver Support',
                 'Wireshark',
                 'Angry IP Scanner',
                 'Itunes',
                 'TeamViewer',
                 'Ophcrack',
                 'Driver Update',
                 'Rainbowcrack',
                 'Home Web Server',
                 'Nginx',
                 'Apache2',
                 'Driver Booster',
                 'Arcade Lines',
                 'Lazesoft',
                 'Vistumbler',
                 'Radmin Server',
                 'Garden Planner',
                 'VirtualDJ8',
                 'BitTornado',
                 'NetBus Pro',
                 'Abyss Web Server',
                 'Cain and Abel',
                 'John the Ripper',
                 'Open TFTP server',
                 'Reveal Keylogger',
                 'Endless Sky',
                 'World Forge service',
                 'Postgresql',
                 'Zenmap',
                 'Freeciv Kismet']

        lindex = ['bittorrent',
                  'nmap',
                  'kodi',
                  'wireshark']
        print('This command is currently in developement')

    def hashCheck(self):
        class hashRUN(QDialog, Ui_hashGEN):

            hashnumber = 0

            def __init__(self, parent=None):
                super(hashRUN, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/pictures/cup2.png'))
                self.setupUi(self)

                # name = [self.MD5radio, self.SHA1radio, self.SHA256radio, self.SHA384radio, self.SHA512radio]
                # func = [self.MD5, self.sha1, self.sha256, self.sha384, self.sha512]
                # for i in range(0,5):
                #    name[i].toggled.connect(func[i])

                def fileselection():
                    dialog = QFileDialog.getOpenFileName(self, 'Select file')
                    self.fpath.setText(dialog[0])
                    print(dialog[0])

                self.browsebutton.clicked.connect(fileselection)

                def hashMD5(selected):
                    if selected:
                        print('test')
                        self.hashnumber = 0

                def hashsha1(selected):
                    if selected:
                        self.hashnumber = 1

                def hashsha256(selected):
                    if selected:
                        self.hashnumber = 2

                def hashsha384(selected):
                    if selected:
                        self.hashnumber = 3

                def hashsha512(selected):
                    if selected:
                        self.hashnumber = 4

                self.MD5radio.toggled.connect(hashMD5)
                self.SHA1radio.toggled.connect(hashsha1)
                self.SHA256radio.toggled.connect(hashsha256)
                self.SHA384radio.toggled.connect(hashsha384)
                self.SHA512radio.toggled.connect(hashsha512)

                def OUTPUTBOX(text):
                    OUTPUT = QMessageBox()
                    OUTPUT.setWindowTitle('Hey! Listen!')
                    OUTPUT.setText("Hash has been successfully created.\nYou can copy the hash in Details.\n\n" + text)
                    OUTPUT.setDetailedText(text)
                    OUTPUT.setIcon(QMessageBox.Information)
                    OUTPUT.setWindowIcon(QtGui.QIcon(':/Pictures/pictures/HEY.png'))
                    x = OUTPUT.exec_()

                def hashchk(hashnumber):
                    linhashtypes = ['MD5', 'sha1sum', 'sha256sum', 'sha384sum', 'sha512sum']
                    winhashtypes = ['MD5', 'SHA1', 'SHA256', 'SHA384', 'SHA512']

                    if platform == 'linux' or platform == 'darwin':
                        filepath = self.fpath.text()
                        command = r'sudo ' + linhashtypes[hashnumber] + ' ' + filepath
                        EXEC = sub.Popen(command.split(), stdout=sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        OUTPUTBOX(output)
                    elif platform == 'win32':
                        print(winhashtypes[hashnumber])
                        filepath = self.fpath.text()
                        command = r'Get-Filehash ' + filepath + ' -Algorithm ' + winhashtypes[
                            hashnumber] + ' | Format-List'
                        print(command)
                        EXEC = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        OUTPUTBOX(output)

                self.genhash.clicked.connect(lambda: hashchk(self.hashnumber))

        def callhash():
            widget = hashRUN()
            widget.exec_()

        callhash()

    ######### Windows Only Functions ########

    # NEED TO TEST 
    def BITLOCKER(self):

        class bitRUN(QDialog, Ui_bitlockerGUI):
            def __init__(self, parent=None):
                super(bitRUN, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/pictures/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):

                def ENCRYPT(x):
                    command = """
$pass = ConvertTo-SecureString '""" + self.encrypPASS.text() + """' -AsPlainText -Force
Enable-BitLocker """ + x + """ -PasswordProtector $pass"""
                    print(command)
                    #sub.Popen(["powershell", "& {" + command + "}"])

                decryptSTATUS = []
                command = 'Get-BitLockerVolume'
                EXEC = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
                stdout, _ = EXEC.communicate()
                output = stdout.decode("utf-8")
                output2 = output.split('\n')
                i = 7
                while True:
                    try:
                        # print(output2[i])
                        output3 = output2[i].split()
                        # print(output3)
                        decryptSTATUS.append(output3[1])
                        decryptSTATUS.append(output3[3])
                        i = i + 1
                    except Exception as e:
                        # print('Controlled exit of loop: ' + str(e))
                        break
                print(decryptSTATUS)
                buttons = [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4,
                           self.radioButton_5, self.radioButton_6, self.radioButton_7]

                self.selectedDRIVE = ''

                def STATUSCHECK(i):
                    # print(i)
                    self.selectedDRIVE = i
                    # print('selected drive: ' + self.selectedDRIVE)
                    index = decryptSTATUS.index(i)
                    status = index + 1
                    if decryptSTATUS[status] == 'FullyDecrypted':
                        self.label_4.setText('FullyDecrypted')
                        self.label_4.setStyleSheet('Color: red')
                    else:
                        self.label_4.setText('Encrypted')
                        self.label_4.setStyleSheet('Color: green')

                driveLETTER = []

                def cancelbutton():
                    self.close()

                self.radioButton.toggled.connect(lambda: STATUSCHECK(driveLETTER[0]))
                self.radioButton_2.toggled.connect(lambda: STATUSCHECK(driveLETTER[1]))
                self.radioButton_3.toggled.connect(lambda: STATUSCHECK(driveLETTER[2]))
                self.radioButton_4.toggled.connect(lambda: STATUSCHECK(driveLETTER[3]))
                self.radioButton_5.toggled.connect(lambda: STATUSCHECK(driveLETTER[4]))
                self.radioButton_6.toggled.connect(lambda: STATUSCHECK(driveLETTER[5]))
                self.enblBIT.clicked.connect(lambda: threader(ENCRYPT(self.selectedDRIVE)))
                self.cancelbutton.clicked.connect(cancelbutton)

                i = 0
                x = 0
                while True:
                    try:
                        buttons[i].setText(decryptSTATUS[x])
                        # print('i: ' + str(i))
                        # print('x: ' + str(x))
                        # print(decryptSTATUS[x])
                        # print(len(decryptSTATUS))
                        driveLETTER.append(decryptSTATUS[x])
                        # print(driveLETTER[i])
                        x = x + 2
                        i = i + 1
                        if x == len(decryptSTATUS):
                            while i != len(buttons):
                                # print('if')
                                buttons[i].setText('<No Drive Found>')
                                buttons[i].setEnabled(False)
                                i = i + 1
                        else:
                            continue

                    except Exception as e:
                        # print('Controlled exit of loop: ' + str(e))
                        break

                ''' 
                command = """
                $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
                manage-bde -protectors -add -pw $drv
                manage-bde -on $drv"""
                '''

        def threader(com):
            try:
                threader = Thread(target=com)
                threader.start()
            except Exception as e:
                print(e)
                print('Could not start thread')

        def callBITRUN():
            widget = bitRUN()
            widget.exec_()

        callBITRUN()