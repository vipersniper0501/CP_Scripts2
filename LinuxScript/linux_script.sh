#!/bin/bash

######## Global Variables ##############
UserName = $(whoami)
thedate = $(date)
dist = distro

########################################
############ Functions #################
function linUbunut {
    echo ""
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "                                                                                       "
    echo "            ||    ||  ||||||\   ||    ||  ||     ||  ||||||||||  ||    ||              "
    echo "            ||    ||  ||    ||  ||    ||  |||    ||      ||      ||    ||              "
    echo "            ||    ||  ||    ||  ||    ||  ||||   ||      ||      ||    ||              "
    echo "            ||    ||  |||||||   ||    ||  || ||  ||      ||      ||    ||              "
    echo "            ||    ||  ||    ||  ||    ||  ||  || ||      ||      ||    ||              "
    echo "            ||    ||  ||    ||  ||    ||  ||   ||||      ||      ||    ||              "
    echo "             \||||/   ||||||/    \||||/   ||    |||      ||       \||||/               "
    echo "                                                                                       "
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Created by Apple Cidr~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Log Created $thedate" > Script_logUbu.txt
}

function linDebian {
    echo ""
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "                                                                                       "
    echo "            ||||||\   |||||||  ||||||\   ||||||||    ||||||    ||     ||               "
    echo "            ||    ||  ||       ||    ||     ||      ||    ||   |||    ||               "
    echo "            ||    ||  ||       ||    ||     ||     ||      ||  ||||   ||               "
    echo "            ||    ||  |||||||  |||||||      ||     ||||||||||  || ||  ||               "
    echo "            ||    ||  ||       ||    ||     ||     ||      ||  ||  || ||               "
    echo "            ||    ||  ||       ||    ||     ||     ||      ||  ||   ||||               "
    echo "            ||||||/   |||||||  ||||||/   ||||||||  ||      ||  ||    |||               "
    echo "                                                                                       "
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Created by Apple Cidr~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo ""
    echo "Log Created $thedate" > Script_logDeb.txt
}

function updt {
    if [ $dist = "Ubuntu" ]; then
        echo "Updates starting... | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Updates starting... | $thedate" >> Script_logDeb.txt
    else
        return 
    fi;
    
    sudo apt update && apt upgrade -y
    
    if [ $dist = "Ubuntu" ]; then
        echo "Updates completed | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Updates completed | $thedate" >> Script_logDeb.txt
    else
        return 
    fi;
}

function ubuntu_start {
    clear
    sleep 1s
    main_menu
}

function debian_start {
    clear
    sleep 1s
    main_menu
}

function alyn {
    if [ $dist = "Ubuntu" ]; then
        echo "Started install of Lynis | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Started install of Lynis | $thedate" >> Script_logDeb.txt
    else
        return 
    fi;    
    clear
    sudo apt install lynis -y 
    if [ $dist = "Ubuntu" ]; then
        echo "Install of Lynis completed | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Install of Lynis completed | $thedate" >> Script_logDeb.txt
    else
        return 
    fi;  
    sleep 1s
        if [ $dist = "Ubuntu" ]; then
        echo "Started lynis security audit. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Started lynis security audit. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_logDeb.txt
    else
        return 
    fi; 
    
    #cd /home/$UserName
    #cd Desktop
    #touch LynisLog.txt 
    sudo lynis audit system > LynisLog.txt
        if [ $dist = "Ubuntu" ]; then
        echo "Lynis security audit has been completed. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_logUbu.txt
    elif [ $dist = "Debian" ]; then
        echo "Lynis security audit has been completed. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_logDeb.txt
    else
        return 
    fi;  

}

########################################
############## MENU's ##################
function main_menu {
    
    #for determining which title to show
    if [ $dist = "Ubuntu" ]; then
        linUbunut
    elif [ $dist = "Debian" ]; then
        linDebian
    else
        return 
    fi;
    

    echo ""
    echo "Main Menu"
    echo ""
    echo "Commands:"
    echo "1.) Updates                       2.) User Settings* "
    echo "3.) Firewall Settings*             4.) Services Settings*"
    echo "5.) Remove Prohibited Software*    6.) Malware Removal*"
    echo "7.) Audit using Lynis"
    echo ""
    echo "85.) Run all at once"
    echo "99.) Quit                         100.) Restart"
    echo ""
    echo ""

    read -p 'Which command would you like to use? : ' com
    
    if [ $com = 1 ]; then
        updt
        echo ""
        echo "Please restart for full update to complete..."
        read -p 'Press any key to continue: '
        clear
        main_menu
    elif [ $com = 2 ]; then
	usr_gru    
    elif [ $com = 7 ]; then
	alyn
	read -p 'Press any key to continue: '
	main_menu
    elif [ $com = 99 ]; then
	exit
    elif [ $com = 100 ]; then
	sudo reboot
    else 
	echo ""
    fi

}

function usr_gru {
    
    #for determining which title to show
    if [ $dist = "Ubuntu" ]; then 
	linUbuntu
    elif [ $dist = "Debian" ]; then
	linDebian
    else
	return
    fi;

    echo ""
    echo "User and Group settings"
    echo ""
    echo "Commands:"
    echo "1.) Add User              2.) Remove User"
    echo "3.) Add Group             4.) Remove Group"
    echo "5.) Add user to Group     6.) Remove user from Group"
    echo "7.) List local users      8.) List Local Groups "
    echo ""
    echo "99.) Back to Main Menu"

    read -p 'Which command would you like to use? : ' com
    
    if [ $com = 1 ]; then
	echo ""
    elif [ $com = 99 ]; then
	main_menu
    else
	echo ""
    fi
}



########################################
############### Start Script ###########
function start_scrpt {
    clear
    echo ""
    echo "Are you running with root? [y/n] : "
    read rut
 
    if [ $rut = y ]; then
        echo "Starting Script..."
        sleep 3s
        clear
    else
        echo "Must run the script as root for most commands to work..."
        sleep 5s
        clear
        exit
    fi;

    echo ""
    echo "Have you completed all of the Forensics Questions? [y/n] "
    read fqs

    if [ $fqs = y ]; then
	echo ""

    else
	echo "Please complete the Forensics Questions first before you use this script."
	sleep 3s
	exit
    fi;


    clear
    echo ""
    echo "What linux distro are you using? [Ex: Ubuntu]  : "; 
    read dist
    if [ $dist = 'Ubuntu' ]; then
        ubuntu_start

    elif [ $dist = 'Debian' ]; then
        debian_start
    
    else 
        echo 'That is not an available distro for this script...'
        sleep 2s
        exit
    fi;

    read -p 'Press any key to continue: '

}

########################################
start_scrpt  
########################################