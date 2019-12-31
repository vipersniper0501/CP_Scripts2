######################### To-Do's ########################
#(0.)Organize script
#(1.)Make area only for menus
#(2.)Remake user menu actions into functions
#(3.)Add more commands to Script

#(3.a)Possibly make command to compare current system to my checklist at https://michael.iansweb.org/win10harden.php 


#Option to use Microsoft Attack Surface Analyzer
#The program will come with the initial download of the CP_Scripts from GitHub
#


#########################################################################################################
########################### MENUS #######################################################################

#main menu function
function main_menu{
    Clear-Host
    Write-Host("Windows 10 CyberPatriots Script created by Michael Brenner for Team Apple Cidr")
    Write-Host("Commands:")
    Write-Host("")
    Write-Host("(1)Search Media Files                 (2)Windows Update")
    Write-Host("(3)Enable BitLocker                   (4)Microsoft Attack Surface Analyzer")
    Write-Host("(5)                                   (6)User and Group Settings ")
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
        $rstrtcpu = Read-Host -Prompt 'Would you like to restart your computer? [y/n] '
        if ($rstrtcpu -eq 'y'){
            Restart-Computer
        } else {
            return 
        }
    }

}


######user/group menu function#####
function usr_grumnu{
    Clear-Host
    Write-Host("Windows 10 CyberPatriots Script created by Michael Brenner for Team Apple Cidr")
    Write-Host("Commands:")
    Write-Host("")
    Write-Host("(1)Add user to system           (2)Remove User from system")
    Write-Host("(3)Create New User Group        (4)Remove User Group*")
    Write-Host("(5)Add User to User Group*       (6)Remove User from User Group*")
    Write-Host("(7)List Local Users		(8)List Local Groups")
    Write-Host("(99)Back            ")
    Write-Host("")

    $usrcommand = Read-Host -Prompt 'Which command would you like to use? '
    
    if ($usrcommand -eq '1'){
	$aus = Read-Host -Prompt 'Would you like to add a user to this system? [y/n] '
	    if ($aus -eq 'y'){
		    $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
		    $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
		    New-LocalUser $nusnm -Password $nuspss -Confirm 
		    Get-LocalUser 
	    } else {
		    Read-Host -Prompt 'Press any key to continue... '
		    break
	    }
    }
    
    if ($usrcommand -eq '2'){
	$rusyn = Read-Host -Prompt 'Would you like to remove a user from this system? [y/n] '
	    if ($rusyn -eq 'y'){
		    $remvusr = $True
		    while ($remvusr -eq $True){
			    Write-Host(Get-LocalUser)
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
            break
            }
	    }
    }

    if ($usrcommand -eq '3'){
	$crtgruyn = Read-Host -Prompt 'Do you want to create a new local user group? [y/n] '
	    if ($crtgruyn -eq 'y'){
		    $crtgru = $True
		    while ($crtgru -eq $True){
			    $ngrunm = Read-Host -Prompt 'What is the name of the new group? '
			    New-LocalGroup -Name $ngrunm 
			    Write-Host("New group " + $ngrunm + " has been created!")
                
			    $anotgru = Read-Host -Prompt 'Would you like to make another local user group? [y/n] '
		    }
	    } else {
		    Read-Host -Prompt 'Press any key to continue... '
		    break
	    }
    }

    if ($usrcommand -eq '4'){

    }

    if ($usrcommand -eq '5'){

    }

    if ($usrcommand -eq '6'){

    }

    if ($usrcommand -eq '7'){
    Clear-Host
    Get-LocalUser
	Read-Host -Prompt 'Press any key to continue... '	
    	usr_grumnu
    }

    if ($usrcommand -eq '8'){
    Clear-Host
    Get-LocalGroup
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
    Write-Host("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Write-Host("         ||       ||      ||      ||      |||     ||||||      ")
    Write-Host("         ||       ||  ||  |||     ||     ||||    ||    ||     ")
    Write-Host("         ||       ||      ||||    ||    || ||    ||    ||     ")
    Write-Host("         ||       ||  ||  || ||   ||       ||    ||    ||     ")
    Write-Host("         ||       ||  ||  ||  ||  ||       ||    ||    ||     ")
    Write-Host("         ||  |||  ||  ||  ||   || ||       ||    ||    ||     ")
    Write-Host("         || || || ||  ||  ||    ||||       ||    ||    ||     ")
    Write-Host("          ||     ||   ||  ||     |||     ||||||   ||||||      ")
    Write-Host("~~~~~~~~~~~~~~~~~~~~Created by Apple Cidr~~~~~~~~~~~~~~~~~~~~~")
    Write-Host("")
}

function MASA {
    Clear-Host
    Write-Host("")
    Write-Host("This command uses Microsoft's Attack Security Analyzer to audit the system.")
    $asayn = Read-Host -Prompt 'Would you like to use the Microsoft Attack Security Analyzer to audit this system? [y/n] '
    if ($asayn -eq 'y'){
        Write-Host("Starting Microsoft Attack Surface Analyzer...")
        Start-Process -FilePath "AsaLaunchGui.bat" -WorkingDirectory "E:\Cyber Patriots\Asa-win-2.1.50\Asa-win-2.1.50\" -Verb RunAs
    }
}


function srchmdia {
    get-childitem -Path C:\Users\* -Recurse -Force -Include *.flv, *.mp4, *.avi, *.wmv, *.mov, *.png, *.jpg, *.tif, *.gif, *.mp3, *.wmv, *.wma, *.aif
}

function winupd {
    Clear-Host
    Write-Host("Installing module PSWindowsUpdate if not already installed... ")
    Install-Module PSWindowsUpdate
    Get-WindowsUpdate
    Install-WindowsUpdate -Confirm
}

function enblbit {
    Clear-Host
    manage-bde -status
    $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
    manage-bde -protectors -add -pw $drv
    manage-bde -on $drv     
}

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

function auts {
    $aus = Read-Host -Prompt 'Would you like to add a user to this system? [y/n] '
	    if ($aus -eq 'y'){
		    $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
		    $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
		    New-LocalUser $nusnm -Password $nuspss -Confirm 
		    Get-LocalUser 
	    } else {
		    Read-Host -Prompt 'Press any key to continue... '
		    break
	    }
}

#########################################################################################################
######################### Start #########################################################################
start_script
#########################################################################################################
