function tcpview {
    Clear-Host
    Write-Host("")
    Write-Host("What it does: This application scans the system for open ports and sockets and tells you who the owner is, what made it, and what type it is.")
    Write-Host("")
    $tcpviewyn = Read-Host -Prompt "Would you like to use the application TCP Viewer from Microsoft's System Internals Suite?  [y/n]  "
    if ($tcpviewyn -eq 'y'){
        $homepath = Get-Location
        $whoami = $env:USERNAME
        Set-Location C:\Users\$whoami\Desktop\SysinternalsSuite
        Write-Host("Starting TCP Viewer...")
    } else {
        sysintmenu
    }
}

function rotkit {
    Clear-Host
    Write-Host("")
    Write-Host("What it does: Finds out the size of each Registry and its usage.")
    Write-Host("")
    $rootyn =  Read-Host -Prompt "Would you like to use the application Registry Size Usage Reporter from Microsoft's System Internals Suite?  [y/n]  "
    if ($rootyn -eq 'y'){
        $homepath = Get-Location
        $whoami = $env:USERNAME
        Set-Location C:\Users\$whoami\Desktop\SysinternalsSuite
        Write-Host("Starting Root Kit Revealer...")
        ./ru.exe HKEY_CLASSES_ROOT
        ./ru.exe HKEY_CURRENT_USER
        ./ru.exe HKEY_LOCAL_MACHINE
        ./ru.exe HKEY_USERS
        ./ru.exe HKEY_CURRENT_CONFIG
        Write-Host("")
        Write-Host("")
        Write-Host("")
        $output = Read-Host -Prompt 'Would you like to have this sent to a file on your desktop? [y/n] '
        if ($output -eq 'y'){
            ./ru.exe HKEY_CLASSES_ROOT | Out-File C:\Users\$whoami\Desktop\registrysizelog.txt
            ./ru.exe HKEY_CURRENT_USER | Out-File C:\Users\$whoami\Desktop\registrysizelog.txt
            ./ru.exe HKEY_LOCAL_MACHINE | Out-File C:\Users\$whoami\Desktop\registrysizelog.txt
            ./ru.exe HKEY_USERS | Out-File C:\Users\$whoami\Desktop\registrysizelog.txt
            ./ru.exe HKEY_CURRENT_CONFIG | Out-File C:\Users\$whoami\Desktop\registrysizelog.txt
            Write-Host("You can now find the output in a log called registrysizelog.txt on your desktop.")
            Start-Sleep -Seconds 4
        } else {
            return
        }
        Set-Location $homepath
    } else {
        sysintmenu
    }
}

function handle {
    Clear-Host
    Write-Host("")
    Write-Host("What it does: This handy command-line utility will show you what files are open by which processes, and much more.")
    Write-Host("")
    $handyn = Read-Host -Prompt "Would you like to use the command Handle from Microsoft's System Internals Suite?  [y/n]  "
    if ($handyn -eq 'y'){
        $homepath = Get-Location
        $whoami = $env:USERNAME
        Set-Location C:\Users\$whoami\Desktop\SysinternalsSuite
        Write-Host("Starting Handle...")
        ./handle.exe
        Write-Host("")
        Write-Host("")
        Write-Host("")
        $output = Read-Host -Prompt 'Would you like to have this sent to a file on your desktop? [y/n] '
        if ($output -eq 'y'){
            ./handle.exe | Out-File C:\Users\$whoami\Desktop\handlelog.txt
            Write-Host("You can now find the output in a log called handlelog.txt on your desktop.")
            Start-Sleep -Seconds 4
        } else {
            return
        }
        Set-Location $homepath
    } else {
        sysintmenu
    }
}
