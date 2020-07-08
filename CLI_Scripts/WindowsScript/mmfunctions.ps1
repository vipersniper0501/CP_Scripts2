
function srchmdia {
    Clear-Host
    get-childitem -Path C:\Users\* -Recurse -Force -Include *.flv, *.mp4, *.avi, *.wmv, *.mov, *.png, *.jpg, *.tif, *.gif, *.mp3, *.wmv, *.wma, *.aif, *.jar
}

function enblbit {
    Clear-Host
    manage-bde -status
    $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
    manage-bde -protectors -add -pw $drv
    manage-bde -on $drv
}

function winupd {
    Clear-Host
    Write-Output("Installing module PSWindowsUpdate if not already installed... ")
    Install-Module PSWindowsUpdate
    Write-Output("PSWindowsUpdate is now installed.")
    Write-Output("")
    Write-Output("Getting Windows Updates...")
    Import-Module PSWindowsUpdate
    $updates = Invoke-Command -ScriptBlock { Get-Wulist -verbose }
    $updatenumber = ($updates.kb).count
    if ($null -ne $updates)
    {
        Get-WindowsUpdate -AcceptAll -Install | Out-File C:\PSWindowsUpdate.log
        do
        {
            $updatestatus = Get-Content c:\PSWindowsUpdate.log
            "Currently processing the following update:"
            Get-Content c:\PSWindowsUpdate.log | select-object -last 1
            Start-Sleep -Seconds 10
            $ErrorActionPreference = 'SilentlyContinue'
            $installednumber = ([regex]::Matches($updatestatus, "Installed" )).count
            $ErrorActionPreference = ‘Continue’
        }until ( $installednumber -eq $updatenumber)
    }
    Remove-Item -path C:\PSWindowsUpdate.log
}

function serv { #UNCOMPLETED
    Clear-Host
    Write-Output("")
    servyn = Read-Host -Prompt 'Would you like to disable services? [y/n] '
    if ($servyn -eq 'y'){
        rdpyn = Read-Host -Prompt 'IMPORTANT: Is Remote Desktop Services required from the readme? [y/n] '
        if ($rdpyn -eq 'y'){
            $servicelist =
            Set-Service -Name
        } else {

        }
    } else {
        main_menu
    }
}

function rall {
    srchmdia
    Write-Output("Please go through output and delete all prohibited media...")

}
