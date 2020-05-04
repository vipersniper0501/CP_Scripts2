######################### To-Do's ########################
#Possibly make command to compare current system to my checklist at https://michael.iansweb.org/win10harden.php


#Option to use Sysinternals Suite
#The programs will come with the initial download of the CP_Scripts from GitHub
#


#########################################################################################################
#######IMPORTS############

. ".\mmfunctions.ps1"
. ".\ugmfunctions.ps1"
. ".\sysintfunct.ps1"

##########################
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
    Write-Host("(5)Services*                           (6)User and Group Settings")
    Write-Host("")
    Write-Host("(85)Run all commands now")
    Write-Host("(99)Exit                              (100)Reboot")
    Write-Host("")

    $com = Read-Host -Prompt 'Which command would you like to use? '
    if ($com -eq '1'){
        srchmdia
        Read-Host -Prompt 'Press Enter to exit... '
    } elseif ($com -eq '2'){
        winupd
        Read-Host -Prompt 'Press Enter to exit... '
    } elseif ($com -eq '3'){
        enblbit
        Read-Host -Prompt 'Press Enter to continue... '
    } elseif ($com -eq '4'){
        sysintmenu
    } elseif ($com -eq '5'){

    } elseif ($com -eq '6'){
        usr_grumnu
    } elseif ($com -eq '85'){
        rall
    } elseif ($com -eq '99'){
        Read-Host -Prompt 'Press Enter to exit... '
        Clear-Host
        break
    } elseif ($com -eq '100'){
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
    } else {
        return
    }

}

#sysinternals command Menu
function sysintmenu {
    Clear-Host
    Write-Host("")
    Write-Host("This is the menu for use of the Microsoft SysInternals Suite of commands and applications...")
    Write-Host("These commands are currently under contstruction, they will be ready in a future update.")
    Write-Host("")
    Write-Host("1.)Handle               2.)Registry Size Usage Reporter")
    Write-Host("3.)TCP Viewer")
    Write-Host("")
    Write-Host("99.) Back")

    $com = Read-Host -Prompt 'Which command would you like to use? '
    if ($com -eq 1){
        handle
    } elseif ($com -eq 2) {
        rotkit
    } elseif ($com -eq 3) {
        tcpview
    } elseif ($com -eq 99) {
        main_menu
    } else {
      sysintmenu
    }
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
    Write-Host("")
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


