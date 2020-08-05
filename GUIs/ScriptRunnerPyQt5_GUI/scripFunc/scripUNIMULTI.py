import getpass
import os
import subprocess as sub
from subprocess import Popen as procPop
from pathlib import Path
from distutils.dir_util import copy_tree
from shlex import quote as shlex_quote
from sys import platform
import distro  # for figuring out what linux distro
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog

if platform == 'linux':
    import pwd
import configparser
import shutil

from PyUIs.hashgen import Ui_hashGEN

OS = distro.linux_distribution()
ops = OS[0]

config = configparser.ConfigParser()
config.read('config.ini')


# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

# Universal Updates
def update_os():
    # TODO: Have function also update all drivers
    if ops == 'Ubuntu' or ops == 'debian':
        command = 'sudo apt-get update && apt-get upgrade -y'
        procPop(command.split())
        command = 'sudo apt-get dist-upgrade'
        procPop(command.split())
        print('Updates Completed!')
    elif platform == 'darwin':
        command = 'sudo softwareupdate -i -a'
        procPop(command.split())
    elif ops == 'Manjaro Linux':
        command = 'sudo pacman -Syu'
        procPop(command.split())
    elif platform == 'win32':
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
        procPop(["powershell", "& {" + commands + "}"])
        print('Windows Update completed')
        print('Updating device drivers...')
        # FIXME: Need to find a way to confirm if the drivers are being updated
        command = """
$UpdateSvc = New-Object -ComObject Microsoft.Update.ServiceManager
$UpdateSvc.AddService2("7971f918-a847-4430-9279-4a52d1efe18d", 7,"")
        
#search and list all missing Drivers
$Session = New-Object -ComObject Microsoft.Update.Session           
$Searcher = $Session.CreateUpdateSearcher() 

$Searcher.ServiceID = '7971f918-a847-4430-9279-4a52d1efe18d'
$Searcher.SearchScope =  1 # MachineOnly
$Searcher.ServerSelection = 3 # Third Party

$Criteria = "IsInstalled=0 and Type='Driver' and ISHidden=0"
Write-Host('Searching Driver-Updates...') -Fore Green  
$SearchResult = $Searcher.Search($Criteria)          
$Updates = $SearchResult.Updates

#Show available Drivers

$Updates | select Title, DriverModel, DriverVerDate, Driverclass, DriverManufacturer | fl

#Download the Drivers from Microsoft

$UpdatesToDownload = New-Object -Com Microsoft.Update.UpdateColl
$updates | % { $UpdatesToDownload.Add($_) | out-null }
Write-Host('Downloading Drivers...')  -Fore Green  
$UpdateSession = New-Object -Com Microsoft.Update.Session
$Downloader = $UpdateSession.CreateUpdateDownloader()
$Downloader.Updates = $UpdatesToDownload
$Downloader.Download()

#Check if the Drivers are all downloaded and trigger the Installation

$UpdatesToInstall = New-Object -Com Microsoft.Update.UpdateColl
$updates | % { if($_.IsDownloaded) { $UpdatesToInstall.Add($_) | out-null } }

Write-Host('Installing Drivers...')  -Fore Green  
$Installer = $UpdateSession.CreateUpdateInstaller()
$Installer.Updates = $UpdatesToInstall
$InstallationResult = $Installer.Install()
if($InstallationResult.RebootRequired) {  
Write-Host('Reboot required! please reboot now..') -Fore Red  
} else { Write-Host('Done..') -Fore Green }
        """
        procPop(["powershell", "& {" + command + "}"])
    else:
        print('This command does not currently support this OS')


# Universal Search Media
def search_media():
    if platform == 'linux' or platform == 'darwin':
        procPop('touch /home/$USER/Desktop/LotTest.txt')
        extensions = (
            '.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma',
            '.aif', '.jar')
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
            '.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma',
            '.aif', '.jar')
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
def fwl():
    if platform == 'linux':
        commandtest = 'sudo ufw status'
        EXEC = procPop(commandtest.split(), stdout = sub.PIPE)
        stdout, _ = EXEC.communicate()
        output = stdout.decode('utf-8')

        if output == 'sudo: ufw: command not found':
            if ops == "Manjaro Linux":
                commandufw = 'sudo pacman -S ufw --noconfirm'
            else:
                commandufw = 'sudo apt install ufw -y'
            procPop(commandufw.split())
            command = 'sudo ufw enable'
            procPop(command.split())

        commandlog = 'sudo ufw status > firewallLOG.txt'
        os.system(shlex_quote(commandlog))
        with open('firewallLOG.txt', 'r') as f:
            for line in f:
                output = f.read()
        print('The following is the output of your original firewall settings:\n')
        print(output)

        print('-----------------------Firewall Settings Has Started-----------------------')
        # SSH
        ssh = config.get('Services', 'ssh')
        if ssh == 'yes':
            command = 'sudo ufw allow 22'
            procPop(command.split())
        elif ssh == 'no':
            command = 'sudo ufw deny 22'
            procPop(command.split())
        # FTP
        ftp = config.get('Services', 'ftp')
        if ftp == 'yes':
            command = 'sudo ufw allow 21'
            procPop(command.split())
        elif ftp == 'no':
            command = 'sudo ufw deny 21'
            procPop(command.split())
        # WEB
        web = config.get('Services', 'web')
        if web == 'yes':
            command = 'sudo ufw allow 80'
            procPop(command.split())
            https = config.get('Services', 'https')
        elif web == 'no':
            command = 'sudo ufw deny 80'
            procPop(command.split())
        # HTTPS
        https = config.get('Services', 'https')
        if https == 'yes':
            command = 'sudo ufw allow 443'
            procPop(command.split())
        elif https == 'no':
            command = 'sudo ufw deny 443'
            procPop(command.split())
        # Samba
        smb = config.get('Services', 'smb')
        if smb == 'yes':
            command = 'sudo ufw allow 139'
            procPop(command.split())
        elif smb == 'no':
            command = 'sudo ufw deny 139'
            procPop(command.split())
        # SQL
        sql = config.get('Services', 'sql')
        if sql == 'yes':
            command = 'sudo ufw allow 3306'
            procPop(command.split())
        elif sql == 'no':
            command = 'sudo ufw deny 3306'
            procPop(command.split())
        # Rsync
        rsnc = config.get('Services', 'rsnc')
        if rsnc == 'yes':
            command = 'sudo ufw allow 873'
            procPop(command.split())
        elif rsnc == 'no':
            command = 'sudo ufw deny 873'
            procPop(command.split())

        print(
            '------------------The Following Ports Have Been Closed Automatically-----------------')
        print('Port 19 has been closed to stop potential DoS attack')
        command = 'sudo ufw deny 19'
        procPop(command.split())
        print('Port 123 has been closed to stop potential trojans (NetController)')
        command = 'sudo ufw deny 123'
        procPop(command.split())
        print('Port 161 has been closed to stop SNMP functionality')
        command = 'sudo ufw deny 161'
        procPop(command.split())
        print('Port 162 has been closed to stop SNMPtrap functionality')
        command = 'sudo ufw deny 162'
        procPop(command.split())
        print('Port 1434 has been blocked to stop potential DoS attack')
        command = 'sudo ufw deny 1434'
        procPop(command.split())
        print('Port 23 has been denied due to Telnet functionality is not necessary')
        command = 'sudo ufw deny 23'
        procPop(command.split())

        # This next service should probably be asked during first time configurations

        # print('Port 53 has been closed to stop the use of DNS functionality since this is not a DNS Server')
        # command = 'sudo ufw deny 53'
        # procPop(command.split())

        print('--------------------Firewall Settings Have Finished-----------------------')
    elif platform == 'win32':
        print('-----------------------Firewall Settings Has Started-----------------------')
        ssh = config.get('Services', 'ssh')
        if ssh == 'yes':
            command = "netsh advfirewall firewall add rule name='ssh' dir=in action=allow protocol=TCP localport=22"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ssh' dir=out action=allow protocol=TCP localport=22"
            procPop(["powershell", "& {" + command + "}"])
        elif ssh == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=22"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ssh' dir=in action=block protocol=TCP localport=22"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ssh' dir=out action=block protocol=TCP localport=22"
            procPop(["powershell", "& {" + command + "}"])
        # FTP
        ftp = config.get('Services', 'ftp')
        if ftp == 'yes':
            command = "netsh advfirewall firewall add rule name='ftp' dir=in action=allow protocol=TCP localport=21"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ftp' dir=out action=allow protocol=TCP localport=21"
            procPop(["powershell", "& {" + command + "}"])
        elif ftp == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=21"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
            procPop(["powershell", "& {" + command + "}"])
        # WEB
        web = config.get('Services', 'web')
        if web == 'yes':
            command = "netsh advfirewall firewall add rule name='webserver' dir=in action=allow protocol=TCP localport=80"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='webserver' dir=out action=allow protocol=TCP localport=80"
            procPop(["powershell", "& {" + command + "}"])
        elif web == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=80"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='webserver' dir=in action=block protocol=TCP localport=80"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='webserver' dir=out action=block protocol=TCP localport=80"
            procPop(["powershell", "& {" + command + "}"])
        # HTTPS
        https = config.get('Services', 'https')
        if https == 'yes':
            command = "netsh advfirewall firewall add rule name='https' dir=in action=allow protocol=TCP localport=443"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='https' dir=out action=allow protocol=TCP localport=443"
            procPop(["powershell", "& {" + command + "}"])
        elif https == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=443"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='https' dir=in action=block protocol=TCP localport=443"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='https' dir=out action=block protocol=TCP localport=443"
            procPop(["powershell", "& {" + command + "}"])
        # Samba
        smb = config.get('Services', 'smb')
        if smb == 'yes':
            command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=allow protocol=TCP localport=139"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SAMBA' dir=out action=allow protocol=TCP localport=139"
            procPop(["powershell", "& {" + command + "}"])
        elif smb == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=139"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=block protocol=TCP localport=139"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SAMBA' dir=out action=block protocol=TCP localport=139"
            procPop(["powershell", "& {" + command + "}"])
        # SQL
        sql = config.get('Services', 'sql')
        if sql == 'yes':
            command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=allow protocol=TCP localport=3306"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=allow protocol=TCP localport=3306"
            procPop(["powershell", "& {" + command + "}"])
        elif sql == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3306"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=block protocol=TCP localport=3306"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=block protocol=TCP localport=3306"
            procPop(["powershell", "& {" + command + "}"])
        # Rsync
        rsnc = config.get('Services', 'rsnc')
        if rsnc == 'yes':
            command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=allow protocol=TCP localport=873"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=allow protocol=TCP localport=873"
            procPop(["powershell", "& {" + command + "}"])
        elif rsnc == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=873"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=block protocol=TCP localport=873"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=block protocol=TCP localport=873"
            procPop(["powershell", "& {" + command + "}"])
        # RDP
        rdp = config.get('Services', 'rdp')  # must block/allow port 5985 and 3389
        if rdp == 'yes':
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=5985"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=3389"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=5985"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=3389"
            procPop(["powershell", "& {" + command + "}"])
        elif rdp == 'no':
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=5985"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3389"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=5985"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=3389"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=5985"
            procPop(["powershell", "& {" + command + "}"])
            command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=3389"
            procPop(["powershell", "& {" + command + "}"])

        print(
            '------------------The Following Ports Have Been Closed Automatically-----------------')
        print('Port 19 has been closed to stop potential DoS attack')
        command = "netsh advfirewall firewall add rule name='port19BLOCK' dir=in action=block protocol=TCP localport=19"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port19BLOCK' dir=out action=block protocol=TCP localport=19"
        procPop(["powershell", "& {" + command + "}"])

        print('Port 123 has been closed to stop potential trojans (NetController)')
        command = "netsh advfirewall firewall add rule name='port123BLOCK' dir=in action=block protocol=TCP localport=123"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port123BLOCK' dir=out action=block protocol=TCP localport=123"
        procPop(["powershell", "& {" + command + "}"])

        print('Port 161 has been closed to stop SNMP functionality')
        command = "netsh advfirewall firewall add rule name='port161BLOCK' dir=in action=block protocol=TCP localport=161"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port161BLOCK' dir=out action=block protocol=TCP localport=161"
        procPop(["powershell", "& {" + command + "}"])

        print('Port 162 has been closed to stop SNMPtrap functionality')
        command = "netsh advfirewall firewall add rule name='port162BLOCK' dir=in action=block protocol=TCP localport=162"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port162BLOCK' dir=out action=block protocol=TCP localport=162"
        procPop(["powershell", "& {" + command + "}"])

        print('Port 1434 has been blocked to stop potential DoS attack')
        command = "netsh advfirewall firewall add rule name='port1434BLOCK' dir=in action=block protocol=TCP localport=1434"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port1434BLOCK' dir=out action=block protocol=TCP localport=1434"
        procPop(["powershell", "& {" + command + "}"])

        print('Port 23 has been denied due to Telnet functionality is not necessary')
        command = "netsh advfirewall firewall add rule name='port23BLOCK' dir=in action=block protocol=TCP localport=23"
        procPop(["powershell", "& {" + command + "}"])
        command = "netsh advfirewall firewall add rule name='port23BLOCK' dir=out action=block protocol=TCP localport=23"
        procPop(["powershell", "& {" + command + "}"])

        print('--------------------Firewall Settings Have Finished-----------------------')

    elif platform == 'darwin':
        print('This command is currently in developement')
    else:
        print('This command is currently in developement')


# TODO: Need to add way to easily create samba shares
#  Need easy way to edit ssh settings (going into services and doing it there takes to long. and it is complicated to explain how to get there)
def servSet(ssh, samba, web, apaweb, nginweb, ftp, proftpd, vsftpd):
    # TODO: Testing and making sure everything works correctly
    if platform == 'linux':
        if ops == 'Ubuntu' or ops == 'Debian':
            command = 'sudo apt install libpam-cracklib'
            procPop(command.split())
            command = 'sudo apt install wenglish'
            procPop(command.split())
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S libpam-cracklib'
            procPop(command.split())
            command = 'sudo pacman -S wenglish'
            procPop(command.split())
        if ssh == 'yes':
            shutil.copy('../configurations/linux_config_files/ssh_config',
                        '/etc/ssh/ssh_config')
            shutil.copy('../configurations/linux_config_files/sshd_config',
                        '/etc/ssh/sshd_config')
        if ftp == 'yes':
            if proftpd == 'yes':
                # first line of command creates a backup of the original configurations
                command = """sudo cp /etc/proftpd/proftpd.conf ~/Desktop/orig_proftpd.conf 
                             sudo mkdir /etc/proftpd/ssl
                             sudo openssl req -new -x509 -days 365 -nodes -out /etc/proftpd/ssl/proftpd.cert.pem -keyout /etc/proftpd/ssl/proftpd.key.pem
                             sudo systemctl restart proftpd.service
                             echo "TLS/SSL keys have been created for ProFTP server  | ${thedate}"
                          """
                procPop(command.split())
                shutil.copy('../configurations/linux_config_files/proftpd.conf',
                            '/etc/proftpd/proftpd.conf')
                shutil.copy('../configurations/linux_config_files/proftpTls_patch.conf',
                            '/etc/proftpd/tls.conf')
            if vsftpd == 'yes':
                # FIXME: Create and add vsftpd configuration
                pass

        if samba == 'yes':
            shutil.copy('../configurations/linux_config_files/smb.conf', '/etc/samba/smb.conf')

        if web == 'yes':
            if apaweb == 'yes':
                shutil.copy('../configurations/linux_config_files/apache2.conf',
                            '/etc/apache2/apache2.conf')
            elif nginweb == 'yes':
                shutil.copy('../configurations/linux_config_files/nginx.conf',
                            '/etc/nginx/nginx.conf')
            else:
                try:
                    raise ImportError(
                        'Web setting is set to yes but neither Apache nor Nginx were '
                        'selected. No web settings were configured.')
                except ImportError:
                    pass
    elif platform == 'win32':
        if samba == 'yes':
            featuresSMB = ["SmbDirect",
                           "SMB1Protocol",
                           "SMB1Protocol-Client",
                           "SMB1Protocol-Server",
                           "SMB1Protocol-Deprecation"]
            for i in range(0, len(featuresSMB)):
                command = 'Enable-WindowsOptionalFeature -Online -FeatureName ' + featuresSMB[
                    i] + ' -NoRestart'
                procPop(["powershell", "& {" + command + "}"])
        elif samba == 'no':
            featuresSMB = ["SmbDirect",
                           "SMB1Protocol",
                           "SMB1Protocol-Client",
                           "SMB1Protocol-Server",
                           "SMB1Protocol-Deprecation"]
            for i in range(0, len(featuresSMB)):
                command = 'Disable-WindowsOptionalFeature -Online -FeatureName ' + featuresSMB[
                    i] + ' -NoRestart'
                procPop(["powershell", "& {" + command + "}"])
        if ssh == 'yes':
            command = "Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
            procPop(["powershell", "& {" + command + "}"])
            command = "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
            procPop(["powershell", "& {" + command + "}"])
            print('Added / confirmed installation of openssh capability')
        elif ssh == 'no':
            command = "Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
            procPop(["powershell", "& {" + command + "}"])
            command = "Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
            procPop(["powershell", "& {" + command + "}"])
            print('removed openssh capability')


def basConf(rdp):
    if platform == 'win32':
        if rdp == 'yes':
            try:
                shutil.copy('../configurations/winCONF/win10StigsRDPy/win10secRDPallowed.inf',
                            'C:/win10secRDPallowed.inf')
                copy_tree('../configurations/winCONF/win10StigsRDPy/Group_Policy_Files/Machine',
                          r'c:\Windows\System32\GroupPolicy\Machine')
                copy_tree('../configurations/winCONF/win10StigsRDPy/Group_Policy_Files/User',
                          r'c:\Windows\System32\GroupPolicy\User')
                shutil.copy('../configurations/winCONF/win10StigsRDPy/Group_Policy_Files/gpt'
                            '.ini',
                            r'c:\Windows\System32\GroupPolicy\gpt.ini')
                print('Successfully copied Group Policy Settings')
            except IOError as e:
                print("Unable to copy file. %s" % e)
            path = 'C:/win10secRDPallowed.inf'
        elif rdp == 'no':
            try:
                shutil.copy('../configurations/winCONF/win10StigsRDPn/Windows10Template11_17'
                            '.inf',
                            r'c:\Windows10Template11_17.inf')
                copy_tree('../configurations/winCONF/win10StigsRDPn/gpoRDPn/Machine',
                          r'c:\Windows\System32\GroupPolicy\Machine')
                copy_tree('../configurations/winCONF/win10StigsRDPn/gpoRDPn/User',
                          r'c:\Windows\System32\GroupPolicy\User')
                shutil.copy('../configurations/winCONF/win10StigsRDPn/gpoRDPn/gpt.ini',
                            r'c:\Windows\System32\GroupPolicy\gpt.ini')
                print('Successfully copied Group Policy Settings')
            except IOError as e:
                print('Unable to copy file. %s' % e)
            path = 'C:/Windows10Template11_17.inf'
        else:
            raise ValueError('rdp should be either yes or no!')
        command = r"secedit /configure /db C:\\windows\\security\\local.sdb /cfg {0}".format(
            path)
        procPop(command.split())
        command = 'gpupdate'
        procPop(command)
        command = 'Enable-WindowsOptionalFeature –FeatureName "Internet-Explorer-Optional-amd64" -All –Online ' \
                  '-NoRestart '
        procPop(["powershell", "& {" + command + "}"])
        command = 'Enable-WindowsOptionalFeature –FeatureName ' \
                  '"Internet-Explorer-Optional-x86" -All –Online ' \
                  '-NoRestart '
        procPop(["powershell", "& {" + command + "}"])
        disableCOM = ["SimpleTCP",
                      "TFTP",
                      "TelnetClient",
                      "IIS-FTPServer",
                      "IIS-WebDAV",
                      "IIS-ManagementConsole",
                      "IIS-WebServer",
                      "WCF-Services45",
                      "WCF-TCP-PortSharing45",
                      "Printing-Foundation-Features",
                      "Printing-Foundation-InternetPrinting-Client",
                      "WorkFolders-Client",
                      "MicrosoftWindowsPowershellV2",
                      "MicrosoftWindowsPowershellV2Root"]
        for i in range(0, len(disableCOM)):
            command = 'Disable-WindowsOptionalFeature -Online -FeatureName ' + disableCOM[
                i] + ' -NoRestart'
            procPop(["powershell", "& {" + command + "}"])
        windowsCapabilitesDisable = ["RIP.Listener~~~~0.0.1.0",
                                     "SNMP.Client~~~~0.0.1.0"]
        for i in range(0, len(windowsCapabilitesDisable)):
            command = "Remove-WindowsCapability -Online -Name " + windowsCapabilitesDisable[i]
            procPop(["powershell", "& {" + command + "}"])

        def completed():
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! For the changes to take full effect please restart the computer!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()

        completed()
    elif platform == 'linux':
        if ops == 'Ubuntu' or ops == 'Debian':
            command = 'sudo apt install fail2ban'
            procPop(command.split())
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S fail2ban'
            procPop(command.split())

        shutil.copy('../configurations/linux_config_files/common-password',
                    '/etc/pam.d/common-password')
        shutil.copy('../configurations/linux_config_files/common-session',
                    '/etc/pam.d/common-session')
        shutil.copy('../configurations/linux_config_files/login', '/etc/pam.d/login')
        shutil.copy('../configurations/linux_config_files/other', '/etc/pam.d/other')
        # Removal of old ssh keys
        command = """thedate=$(date)
userlist2=( $(eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1) )
usersleft2=${#userlist2[@]}  #this variable is equivelent to the number of users in list $userlist
i=0
while [ $usersleft2 != 0 ]; do
sudo rm -r /home/${userlist2[$i]}/.ssh
echo "User ${userlist2[$i]} no longer has any SSH keys | ${thedate}"
let i=i+1
echo $i
let usersleft2=usersleft2-1
echo $usersleft2
sleep 0.5s
done"""
        procPop(command.split())
        gruname = 'wheel'
        command = 'sudo groupadd ' + gruname
        print(command)
        procPop(command.split())

        username = pwd.getpwuid(os.getuid()).pw_name
        group = 'wheel'
        if ops == 'Manjaro Linux':
            command = "sudo -S usermod --append --groups " + group + " " + username
        else:
            command = "sudo -S usermod -a -G " + group + " " + username
        os.system(shlex_quote(command))
        shutil.copy('../configurations/linux_config_files/su', '/etc/pam.d/su')


'''Removal of Prohibited Software.
    Before running through list of software to remove, you must ask user if there are any required applications.
    Give a list that pops up and have them check of programs from the list that they want to keep.'''


def rmProSoft():
    # Get-WmiObject -Class Win32_Product | Select-Object -Property Name
    # ^ will print out list of all installed programs.
    # TODO: Possibly have Charlotte work on this while I work on other parts
    #  Should be modular so more programs can be easily added.

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
    print(index)
    print(lindex)
    print('This command is currently in developement')


def hashCheck():
    class hashRUN(QDialog, Ui_hashGEN):

        hash_number = 0

        def __init__(self, parent = None):
            super(hashRUN, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(431, 179)
            self.setupUi(self)

            def fileselection():
                dialog = QFileDialog.getOpenFileName(self, 'Select file')
                self.fpath.setText(dialog[0])
                print(dialog[0])

            self.browsebutton.clicked.connect(fileselection)

            def hashMD5(selected):
                if selected:
                    self.hash_number = 0

            def hashsha1(selected):
                if selected:
                    self.hash_number = 1

            def hashsha256(selected):
                if selected:
                    self.hash_number = 2

            def hashsha384(selected):
                if selected:
                    self.hash_number = 3

            def hashsha512(selected):
                if selected:
                    self.hash_number = 4

            self.MD5radio.toggled.connect(hashMD5)
            self.SHA1radio.toggled.connect(hashsha1)
            self.SHA256radio.toggled.connect(hashsha256)
            self.SHA384radio.toggled.connect(hashsha384)
            self.SHA512radio.toggled.connect(hashsha512)

            def OUTPUTBOX(text):
                OUTPUT = QMessageBox()
                OUTPUT.setWindowTitle('Hey! Listen!')
                OUTPUT.setText(
                    "Hash has been successfully created.\nYou can copy the hash in Details.\n\n" + text)
                OUTPUT.setDetailedText(text)
                OUTPUT.setIcon(QMessageBox.Information)
                OUTPUT.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                OUTPUT.exec_()

            def hashchk(hash_number):
                if len(self.fpath.text()) != 0 and Path(self.fpath.text()).is_file():
                    linux_hash_types = ['md5sum', 'sha1sum', 'sha256sum', 'sha384sum', 'sha512sum']
                    windows_hash_types = ['MD5', 'SHA1', 'SHA256', 'SHA384', 'SHA512']
                    darwin_hash_types = ['md5', 'shasum -a 1', 'shasum -a 256', 'shasum -a 384',
                                         'shasum -a 512']

                    if platform == 'linux':
                        filepath = self.fpath.text()
                        command = r'sudo ' + linux_hash_types[hash_number] + ' ' + filepath
                        EXEC = procPop(command.split(), stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        OUTPUTBOX(output)
                    elif platform == 'darwin':
                        filepath = self.fpath.text()
                        command = r'sudo ' + darwin_hash_types[hash_number] + ' ' + filepath
                        EXEC = procPop(command.split(), stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        OUTPUTBOX(output)
                    elif platform == 'win32':
                        filepath = self.fpath.text()
                        EXEC = procPop(["powershell",
                                        "& {Get-Filehash '" + filepath + "' -Algorithm " +
                                        windows_hash_types[hash_number] + " | Format-List}"],
                                       stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        OUTPUTBOX(output)
                elif len(self.fpath.text()) == 0:
                    print('No file path entered')
                    ERROR_NO_FILEPATH = QMessageBox()
                    ERROR_NO_FILEPATH.setIcon(QMessageBox.Warning)
                    ERROR_NO_FILEPATH.setWindowTitle('Hey! Listen!')
                    ERROR_NO_FILEPATH.setText(
                        'ERROR: No File Path Found')
                    ERROR_NO_FILEPATH.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_FILEPATH.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    ERROR_NO_FILEPATH.exec_()
                elif not Path(self.fpath.text()).is_file():
                    print('No file path entered')
                    ERROR_FILE_NOT_FOUND = QMessageBox()
                    ERROR_FILE_NOT_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_FILE_NOT_FOUND.setWindowTitle('Hey! Listen!')
                    ERROR_FILE_NOT_FOUND.setText(
                        'ERROR: File Not Found Or Does Not Exist')
                    ERROR_FILE_NOT_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_FILE_NOT_FOUND.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    ERROR_FILE_NOT_FOUND.exec_()

            self.genhash.clicked.connect(lambda: hashchk(self.hash_number))

    widget = hashRUN()
    widget.exec_()
