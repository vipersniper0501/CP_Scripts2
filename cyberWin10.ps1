######################### To-Do's ########################
#(0.)Organize script
#(1.)Make area only for menus
#(2.)Remake user menu actions into functions
#(3.)Add more commands to Script

#(3.a)Possibly make command to compare current system to my checklist at https://michael.iansweb.org/win10harden.php 


#Option to use Sysinternals Suite
#The program will come with the initial download of the CP_Scripts from GitHub
#


#########################################################################################################
########################### MENUS #######################################################################

#main menu function
function main_menu{
    Clear-Host
    win10
    Write-Host("Windows 10 CyberPatriots Script created by Michael Brenner for Team Apple Cidr")
    Write-Host("Commands:")
    Write-Host("")
    Write-Host("(1)Search Media Files                 (2)Windows Update")
    Write-Host("(3)Enable BitLocker                   (4)SysInternals Commands*")
    Write-Host("(5)                                   (6)User and Group Settings*")
    Write-Host("(99)Exit                              (100)Reboot")
    Write-Host("")

    $com = Read-Host -Prompt 'Which command would you like to use? '
    if ($com -eq '1'){
        srchmdia
        Read-Host -Prompt 'Press any key to exit... '
    }
    if ($com -eq '2'){
        winupd
        Read-Host -Prompt 'Press any key to exit... '
    }
    if ($com -eq '3'){
        enblbit
        Read-Host -Prompt 'Press any key to continue... '
    }
    if ($com -eq '4'){
        sysintmenu
    }
    if ($com -eq '5'){

    }
    if ($com -eq '6'){
        usr_grumnu
    }
    if ($com -eq '99'){
        Read-Host -Prompt 'Press any key to exit... '
        Clear-Host
        break
    }
    if ($com -eq '100'){
        Write-Host("")
        Write-Host("")
        Write-Host("!WARNING!")
        Write-Host("Make sure to save all your work saved and not have any important processes running on the computer such as windows updates. ")
        Write-Host("")
        $rstrtcpu = Read-Host -Prompt 'Would you like to restart your computer? [y/n] '
        if ($rstrtcpu -eq 'y'){
            Restart-Computer -Confirm
        } else {
            return 
        }
    }

}

#sysinternals command Menu
function sysintmenu {
    Clear-Host
    Write-Host("")
    Write-Host("This is the menu for use of the Microsoft SysInternals Suite of commands and applications...")
    Write-Host("These commands are currently under contstruction, they will be ready in a future update.")
}



###### user/group menu #####
function usr_grumnu{
    Clear-Host
    win10
    Write-Host("Windows 10 CyberPatriots Script created by Michael Brenner for Team Apple Cidr")
    Write-Host("Commands:")
    Write-Host("")
    Write-Host("(1)Add user to system           (2)Remove User from system")
    Write-Host("(3)Create New User Group        (4)Remove User Group")
    Write-Host("(5)Add User to User Group       (6)Remove User from User Group")
    Write-Host("(7)List Local Users		(8)List Local Groups")
    Write-Host("(99)Back            ")
    Write-Host("")

    $usrcommand = Read-Host -Prompt 'Which command would you like to use? '
    
    if ($usrcommand -eq '1'){
        #add user to system 
        auts
    }
    
    if ($usrcommand -eq '2'){
        #remove user from system
        rusr 
    }

    if ($usrcommand -eq '3'){
        #create user groups
        crtgrup
    }

    if ($usrcommand -eq '4'){
        #remove local user group
        rusrgru
    }

    if ($usrcommand -eq '5'){
        #add user to to group
        autgru
    }

    if ($usrcommand -eq '6'){
        #removes user from local user group
        rusrfgru
    }

    if ($usrcommand -eq '7'){
        Clear-Host
        Write-Host("You may have to repeat the command if nothing shows up...")
        Write-Host("")
        Write-Host("")
        Get-LocalUser
        Write-Host("")
	    Read-Host -Prompt 'Press any key to continue... '	
        usr_grumnu
    }

    if ($usrcommand -eq '8'){
        Clear-Host
        Write-Host("You may have to repeat the command if nothing shows up...")
        Write-Host("")
        Write-Host("")
        Get-LocalGroup
        Write-Host("")
	    Read-Host -Prompt 'Press any key to continue... '
	    usr_grumnu
    }
    
    if ($usrcommand -eq '99'){
        main_menu
    }

}
#########################################################################################################
######################## Functions ######################################################################

function win10 {
    Write-Host("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Write-Host("        ||       ||  ||||||  ||      ||         /||      /||||\         ")
    Write-Host("        ||       ||    ||    ||\     ||        //||     ||    ||        ")
    Write-Host("        ||       ||    ||    ||\\    ||       // ||     ||    ||        ")
    Write-Host("        ||       ||    ||    || \\   ||          ||     ||    ||        ")
    Write-Host("        ||       ||    ||    ||  \\  ||          ||     ||    ||        ")
    Write-Host("        ||  /|\  ||    ||    ||   \\ ||          ||     ||    ||        ")
    Write-Host("        || // \\ ||    ||    ||    \\||          ||     ||    ||        ")
    Write-Host("         ||     ||   ||||||  ||     \||       ||||||||   \||||/         ")
    Write-Host("~~~~~~~~~~~~~~~~~~~~~~~~~Created by Apple Cidr~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Write-Host("")
}

#function Sysint {
#    Clear-Host
#    Write-Host("")
#    #Write-Host("This command uses Microsoft's Attack Security Analyzer to audit the system.")
#    $sysyn = Read-Host -Prompt 'Would you like to use the Microsoft Attack Security Analyzer to audit this system? [y/n] '
#    if ($sysyn -eq 'y'){
#        Write-Host("Starting Microsoft Attack Surface Analyzer...")
#        Start-Process -FilePath "AsaLaunchGui.bat" -WorkingDirectory "E:\Cyber Patriots\Asa-win-2.1.50\Asa-win-2.1.50\" -Verb RunAs
#    }
#}


function srchmdia {
    Clear-Host
    get-childitem -Path C:\Users\* -Recurse -Force -Include *.flv, *.mp4, *.avi, *.wmv, *.mov, *.png, *.jpg, *.tif, *.gif, *.mp3, *.wmv, *.wma, *.aif
}

function winupd {
    Clear-Host
    Write-Host("Installing module PSWindowsUpdate if not already installed... ")
    Install-Module PSWindowsUpdate
    Write-Host("PSWindowsUpdate is now installed.")
    Write-Host("")
    Write-Host("Getting Windows Updates...")
    Get-WindowsUpdate
    Install-WindowsUpdate -Confirm
}

function crtgrup {
    Clear-Host
    $crtgruyn = Read-Host -Prompt 'Do you want to create a new local user group? [y/n] '
    if ($crtgruyn -eq 'y'){
        $crtgru = $True
        while ($crtgru -eq $True){
            $ngrunm = Read-Host -Prompt 'What is the name of the new group? '
            New-LocalGroup -Name $ngrunm 
            Write-Host("New group " + $ngrunm + " has been created!")
            
            $anotgru = Read-Host -Prompt 'Would you like to make another local user group? [y/n] '
            if ($anotgru -eq 'y'){
                return $True0
            } else {
                return $crtgru = $False
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function rusrfgru {
    Clear-Host
    Write-Host("")
    Get-LocalGroup
    Write-Host("")
    $rgrusrf = Read-Host -Prompt 'Would you like to remove a user from a group? [y/n] '
    if ($rgrusrf -eq 'y'){
        $agn = $true
        while ($agn -eq $true){
            Clear-Host
            Write-Host("")
            $usrnam = Read-Host -Prompt 'What is the name of the user you would like to remove from a group? '
            $gru = Read-Host -Prompt 'What is the name of the group you would like the user removed from? '
            Remove-LocalGroupMember -Group $gru -Member $usrnam -Confirm
            Write-Host("User " + $usrnam + " has been removed from group " + $gru + "!")
            $agnyn = Read-Host -Prompt 'Would you like to remove another user from another local user group? [y/n] '
            if ($agnyn -eq 'y'){
                return $agn = $true
            } else {
                return $agn = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function auts {
    Clear-Host
    $augruyn = Read-Host -Prompt 'Would you like to add a user to the system? [y/n]'
    if ($augruyn -eq 'y'){
        $augag = $true
        while ($augag -eq $true){
            $admn = Read-Host -Prompt 'Will the user be an admin? [y/n] '
            if ($admn -eq 'y'){
                $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
                $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
                New-LocalUser $nusnm -Password $nuspss -Confirm 
                Add-LocalGroupMember -Group "Administrators" -Member $nusnm
                Get-LocalUser 
            } else {
                $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
                $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
                New-LocalUser $nusnm -Password $nuspss -Confirm 
                Get-LocalUser 
            }
            $augagyn = Read-Host -Prompt 'Would you like to add another user to the system? [y/n] '
            if ($augagyn -eq 'y'){
                return $augag = $true
            } else {
                return $augag = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function rusr {
    Clear-Host
    Write-Host("")
    $rusyn = Read-Host -Prompt 'Would you like to remove a user from this system? [y/n] '
    if ($rusyn -eq 'y'){
	    $remvusr = $True
	    while ($remvusr -eq $True){
		    Get-LocalUser
		    $rus = Read-Host -Prompt 'Which user would you like to remove from the system? '
		    Remove-LocalUser -Name $rus -Confirm
		    Write-Host("User " + $rus + " has been removed!")
		    Write-Host("")
		    $remvanthusr = Read-Host -Prompt 'Would you like to remove another user? [y/n] '
		    if ($remvanthusr -eq 'y'){
			    $remvusr = $True
		    } else {
			    $remvusr = $False
		    }
	    } else {
	    Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
       }
    }
}


function rusrgru {
    Clear-Host
    Write-Host("")
    Get-LocalGroup
    Write-Host("")
    $rusrgruyn = Read-Host -Prompt 'Would you like to remove a Local User Group from this list of groups on the system? [y/n] '
    if ($rusrgruyn -eq 'y'){
        $rgru = $true
        while ($rgru -eq $true){
            Clear-Host
            Get-LocalGroup
            Write-Host("")
            $grunam = Read-Host -Prompt 'Which group would you like to remove from this system?'
            Remove-LocalGroup -Name $grunam -Confirm
            Write-Host("The local group " + $grunam + " has been removed!")
            Write-Host("")
            $end = Read-Host -Prompt 'Would you like to remove another group from the list? [y/n] '
            if ($end -eq 'y'){
                return $rgru = $true
            } else {
                return $rgru = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function autgru {
    Clear-Host
    Write-Host("")
    $autgruyn = Read-Host -Prompt 'Would you like to add a user to a group? [y/n] '
    if ($autgruyn -eq 'y'){
        $autgruag = $true
        while ($autgruag -eq $true){
            Get-LocalUser
            Clear-Host #This is done so it is a gurantee that the list will show
            Get-LocalUser
            $usrnam = Read-Host -Prompt 'What user would you like to add to a group? '
            Get-LocalGroup 
            Clear-Host #This is done so it is a gurantee that the list will show
            Get-LocalGroup
            $usrgruadd = Read-Host -Prompt 'Which local group would you like to add' + $usrnam + ' to? '
            Add-LocalGroupMember -Name $usrnam -Member $usrgruadd
            Write-Host("User " + $usrnam + " has been add to group " + $usrgruadd + "! ")
            $autag = Read-Host -Prompt 'Would you like to add another user to another group? [y/n] '
            if ($autag -eq 'y'){
                return $autgruag = $true
            } else {
                return $autgruag = $false
            }

        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function enblbit {
    Clear-Host
    manage-bde -status
    $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
    manage-bde -protectors -add -pw $drv
    manage-bde -on $drv     
}

#########################################################################################################
######################### Start #########################################################################

function start_script {
    Clear-Host
    #Requires -RunAsAdministrator
    Write-Host("")
    Write-Host("")
    Write-Host("This is the CyberPatriots powershell script created by team Apple Cidr    ")
    win10
    $ynfo = Read-Host -Prompt 'Have you completed all of the Forensics Questions? [y/n] '
    if ($ynfo -eq 'y'){
        $start_sc = $True
        while ($start_sc -eq $True){
            Clear-Host
            main_menu
        }
      
    } else {
        Write-Host("You must complete the Forensics first before you use this script.")
        Write-Host("")
        Read-Host -Prompt 'Press any key to continue...'
        break
    }
}



###################|
start_script      #|
#########################################################################################################