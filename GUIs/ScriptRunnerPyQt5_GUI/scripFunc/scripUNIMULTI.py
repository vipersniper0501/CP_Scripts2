import getpass
import os
import subprocess as sub
import sys
from distutils.dir_util import copy_tree
from shlex import quote as shlex_quote
from sys import platform

import distro  # for figuring out what linux distro

if platform == 'linux':
    import pwd
import configparser
import shutil
from PyQt5 import QtGui
from PyUIs.hashgen import Ui_hashGEN
from PyQt5.QtWidgets import *

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
    # Universal Updates
    def updateos(self):
        # TODO: Have function also update all drivers
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
            os.system(shlex_quote(commandlog))
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

    def servSet(self, ssh, samba, web, apaweb, nginweb, ftp, proftpd, vsftpd):
        # TODO: Testing and making sure everything works correctly
        if platform == 'linux':
            if ops == 'Ubuntu' or ops == 'Debian':
                command = 'sudo apt install libpam-cracklib'
                sub.Popen(command.split())
                command = 'sudo apt install wenglish'
                sub.Popen(command.split())
            elif ops == 'Manjaro Linux':
                command = 'sudo pacman -S libpam-cracklib'
                sub.Popen(command.split())
                command = 'sudo pacman -S wenglish'
                sub.Popen(command.split())
            if ssh == 'yes':
                shutil.copy('../configurations/linux_config_files/ssh_config', '/etc/ssh/ssh_config')
                shutil.copy('../configurations/linux_config_files/sshd_config', '/etc/ssh/sshd_config')
            if ftp == 'yes':
                if proftpd == 'yes':
                    # first line of command creates a backup of the original configurations
                    command = """sudo cp /etc/proftpd/proftpd.conf ~/Desktop/orig_proftpd.conf 
                                 sudo mkdir /etc/proftpd/ssl
                                 sudo openssl req -new -x509 -days 365 -nodes -out /etc/proftpd/ssl/proftpd.cert.pem -keyout /etc/proftpd/ssl/proftpd.key.pem
                                 sudo systemctl restart proftpd.service
                                 echo "TLS/SSL keys have been created for ProFTP server  | ${thedate}"
                              """
                    sub.Popen(command.split())
                    shutil.copy('../configurations/linux_config_files/proftpd.conf', '/etc/proftpd/proftpd.conf')
                    shutil.copy('../configurations/linux_config_files/proftpTls_patch.conf', '/etc/proftpd/tls.conf')
                if vsftpd == 'yes':
                    pass

            if samba == 'yes':
                shutil.copy('../configurations/linux_config_files/smb.conf', '/etc/samba/smb.conf')

            if web == 'yes':
                if apaweb == 'yes':
                    shutil.copy('../configurations/linux_config_files/apache2.conf', '/etc/apache2/apache2.conf')
                elif nginweb == 'yes':
                    shutil.copy('../configurations/linux_config_files/nginx.conf', '/etc/nginx/nginx.conf')
                else:
                    try:
                        raise ImportError(
                            'Web setting is set to yes but neither Apache or Nginx were selected. No web settings were configured.')
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
                    command = 'Enable-WindowsOptionalFeature -Online -FeatureName ' + featuresSMB[i] + ' -NoRestart'
                    sub.call(["powershell", "& {" + command + "}"])
            elif samba == 'no':
                featuresSMB = ["SmbDirect",
                               "SMB1Protocol",
                               "SMB1Protocol-Client",
                               "SMB1Protocol-Server",
                               "SMB1Protocol-Deprecation"]
                for i in range(0, len(featuresSMB)):
                    command = 'Disable-WindowsOptionalFeature -Online -FeatureName ' + featuresSMB[i] + ' -NoRestart'
                    sub.call(["powershell", "& {" + command + "}"])
            if ssh == 'yes':
                command = "Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
                sub.call(["powershell", "& {" + command + "}"])
                command = "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
                sub.call(["powershell", "& {" + command + "}"])
                print('Added / confirmed installation of openssh capability')
            elif ssh == 'no':
                command = "Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
                sub.call(["powershell", "& {" + command + "}"])
                command = "Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
                sub.call(["powershell", "& {" + command + "}"])
                print('removed openssh capability')

    # Still needs Linux configurations
    # Need to add way to easily create samba shares
    # Need easy way to edit ssh settings (going into services and doing it there takes to long. and it is complicated to explain how to get there)

    def basConf(self, rdp):
        if platform == 'win32':
            def cptree(src, dst, symlinks=False, ignore=None):
                for item in os.listdir(src):
                    s = os.path.join(src, item)
                    d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    shutil.copy2(s, d)

            if rdp == 'yes':
                try:
                    shutil.copy('./configurations/winCONF/win10StigsRDPy/win10secRDPallowed.inf',
                                'C:/win10secRDPallowed.inf')
                    copy_tree('./configurations/winCONF/win10StigsRDPy/Group_Policy_Files/Machine',
                              r'c:\Windows\System32\GroupPolicy\Machine')
                    copy_tree('./configurations/winCONF/win10StigsRDPy/Group_Policy_Files/User',
                              r'c:\Windows\System32\GroupPolicy\User')
                    shutil.copy('./configurations/winCONF/win10StigsRDPy/Group_Policy_Files/gpt.ini',
                                r'c:\Windows\System32\GroupPolicy\gpt.ini')
                    print('Successfully copied Group Policy Settings')
                except IOError as e:
                    print("Unable to copy file. %s" % e)
                path = 'C:/win10secRDPallowed.inf'
            elif rdp == 'no':
                try:
                    shutil.copy('./configurations/winCONF/win10StigsRDPn/Windows10Template11_17.inf',
                                'C:/Windows10Template11_17.inf')
                    copy_tree('./configurations/winCONF/win10StigsRDPn/gpoRDPn/Machine',
                              r'c:\Windows\System32\GroupPolicy\Machine')
                    copy_tree('./configurations/winCONF/win10StigsRDPn/gpoRDPn/User',
                              r'c:\Windows\System32\GroupPolicy\User')
                    shutil.copy('./configurations/winCONF/win10StigsRDPn/gpoRDPn/gpt.ini',
                                r'c:\Windows\System32\GroupPolicy\gpt.ini')
                    print('Successfully copied Group Policy Settings')
                except IOError as e:
                    print('Unable to copy file. %s' % e)
                path = 'C:/Windows10Template11_17.inf'
            else:
                raise ValueError('rdp should be either yes or no!')
            command = r"secedit /configure /db C:\\windows\\security\\local.sdb /cfg {0}".format(path)
            sub.call(command.split())
            command = 'gpupdate'
            sub.call(command)
            command = 'Enable-WindowsOptionalFeature –FeatureName "Internet-Explorer-Optional-amd64" -All –Online ' \
                      '-NoRestart '
            sub.call(["powershell", "& {" + command + "}"])
            disableCOM = ["SimpleTCP",
                          "TFTP",
                          "TelnetClient",
                          "IIS-FTPServer",
                          "IIS-WebDAV",
                          "IIS-WebServer",
                          "WCF-Services45",
                          "WCF-TCP-PortSharing45",
                          "Printing-Foundation-Features",
                          "Printing-Foundation-InternetPrinting-Client",
                          "WorkFolders-Client",
                          "MicrosoftWindowsPowershellV2",
                          "MicrosoftWindowsPowershellV2Root"]
            for i in range(0, len(disableCOM)):
                command = 'Disable-WindowsOptionalFeature -Online -FeatureName ' + disableCOM[i] + ' -NoRestart'
                sub.call(["powershell", "& {" + command + "}"])
            windowsCapabilitesDisable = ["RIP.Listener~~~~0.0.1.0",
                                         "SNMP.Client~~~~0.0.1.0"]
            for i in range(0, len(windowsCapabilitesDisable)):
                command = "Remove-WindowsCapability -Online -Name " + windowsCapabilitesDisable[i]
                sub.call(["powershell", "& {" + command + "}"])

            '''
            def completed():
                HEY = QMessageBox()
                HEY.setWindowTitle('Hey! Listen!')
                HEY.setText("Hey! For the changes to take full effect please restart the computer!")
                HEY.setIcon(QMessageBox.Critical)
                HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = HEY.exec_()
            completed()
            '''

        elif platform == 'linux':
            if ops == 'Ubuntu' or ops == 'Debian':
                command = 'sudo apt install fail2ban'
                sub.Popen(command.split())
            elif ops == 'Manjaro Linux':
                command = 'sudo pacman -S fail2ban'
                sub.Popen(command.split())

            shutil.copy('../configurations/linux_config_files/common-password', '/etc/pam.d/common-password')
            shutil.copy('../configurations/linux_config_files/common-session', '/etc/pam.d/common-session')
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
            sub.Popen(command.split())
            gruname = 'wheel'
            command = 'sudo groupadd ' + gruname
            print(command)
            sub.Popen(command.split())

            username = pwd.getpwuid(os.getuid()).pw_name
            group = 'wheel'
            if ops == 'Manjaro Linux':
                command = "sudo -S usermod --append --groups " + group + " " + username
            else:
                command = "sudo -S usermod -a -G " + group + " " + username
            os.system(shlex_quote(command))
            shutil.copy('../configurations/linux_config_files/su', '/etc/pam.d/su')

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
                self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
                self.setupUi(self)

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
                    OUTPUT.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
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
