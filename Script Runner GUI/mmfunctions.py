import glob
import os
import subprocess as sub
from sys import platform
# from Script_Runner import scriptrunnerGUI as srg


class mmfunc:
    def updates():
        if platform == 'Ubuntu' or platform == 'Debian':
            command = 'sudo screen -md apt update'
            command2 = 'sudo screen -md apt upgrade'
            sub.Popen(command.split())
            sub.Popen(command2.split())
            print('Updates Completed!')
        elif platform == 'darwin':
            command = 'sudo softwareupdate -i -a'
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
Remove-Item -path C:\PSWindowsUpdate.log"""
            sub.Popen(["powershell","& {" + commands + "}"])
            # Definitely is executing but it needs to be run as admin. Must figure out a way to do that.

            # print('This function (updates) does not currently support this OS.')
        else:
            print('This command does not currently support this OS')

    def srchmedia():
        extensions = ('.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
        for root, dirs, files in os.walk('/'):
            for filename in files:
                if any(filename.endswith(extension) for extension in extensions):
                    f = open('Q:\\Cyber Patriots\\my_scripts_and_STIGS\\Scripts\\CP_ScriptsREPAIR\\Script Runner GUI\\logTest.txt', 'a+')
                    filepath = os.path.join(root, filename)
                    f.write(filepath + '\n')
                    f.close()
                    print(filepath)
        print('Scan for unapproved media complete.')

    def alyn():
        if platform == 'Ubuntu' or platform == 'Debian':
            command='sudo apt install lynis -y'
            sub.call(command.split())
            command2='sudo lynis audit system'
            sub.call(command2.split())
        elif platform == 'win32':
            print('This function (alyn) does not currently support this OS.')
