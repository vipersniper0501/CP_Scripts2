#!/bin/bash

######## Global Variables ##############
UserName = $(whoami)
thedate = $(date)
logU = Script_logUbu.txt
logD = Script_logDeb.txt
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
    echo "             ||||||   ||||||/    ||||||   ||    |||      ||       ||||||               "
    echo "                                                                                       "
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Created by Apple Cidr~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #printf "Log Created $thedate" > $logU
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
    #printf "Log Created $thedate" > $logD
}

function updt {
    sudo apt update && apt upgrade -y
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
    echo "1.) Updates                       2.) User Settings "
    echo "3.) Firewall Settings             4.) Services Settings"
    echo "5.) Remove Prohibited Software    6.) Malware Removal"
    echo "7.) Remove Prohibited Software    8.) Audit using Lynis"
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
