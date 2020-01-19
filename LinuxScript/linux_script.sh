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
    #echo "Log Created $thedate" > Script_log.txt
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
    #echo "Log Created $thedate" > Script_log.txt
}

function updt {
    echo "Updates starting... | $thedate" >> Script_log.txt
    sudo apt update && apt upgrade -y
    echo "Updates completed | $thedate" >> Script_log.txt
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

function fwset {
	clear
	read -p 'Does this system require SSH functionality? [y/n] : ' ssh
        read -p 'Does this system require FTP functionality? [y/n] : ' ftp
	read -p 'Does this system require Webserver functionality? Does it need to host a website? [y/n] : ' web
	read -p 'Does this system require SMB file sharing? (Ex: School shared drive) Does the system need this? [y/n] : ' smb
	echo "Started install of UFW if not installed already | $thedate" >> Script_log.txt
	sudo apt install ufw -y	
	echo "Completed install of UFW on system | $thedate" >> Script_log.txt
	sudo ufw enable
	echo "UFW has been enabled on the system | $thedate" >> Script_log.txt
	if [ $ssh = 'y' ]; then 
		sudo ufw allow 22
		echo "Port 22 has been opened for SSH networking | $thedate" >> Script_log.txt
	elif [ $ssh = 'n' ]; then
		sudo ufw deny 22
		echo "Port 22 has been closed to stop SSH networking | $thedate" >> Script_log.txt
	elif [ $ftp = 'y' ]; then
		sudo ufw allow 21
		echo "Port 21 has been opened for FTP networking | $thedate" >> Script_log.txt
	elif [ $web = 'y' ]; then
		sudo ufw allow 80
		echo "Port 80 has been opened for basic Webserver hosting | $thedate" >> Script_log.txt
		read -p 'Does the Webserver require ssl or HTTPS? [y/n] : ' https
		if [ $https -eq 'y' ]; then
			sudo ufw allow 443
			echo "Port 443 has been opened for HTTPS or ssl | $thedate" >> Script_log.txt 
		fi
	elif [ $smb = 'y' ]; then 
		sudo ufw allow 139
		echo "Port 139 has been opened for SMB file sharing | $thedate" >> Script_log.txt
	else
		return
	fi;

}

function alyn {
    echo "Started install of Lynis | $thedate" >> Script_log.txt
    clear
    sudo apt install lynis -y 
    echo "Install of Lynis completed | $thedate" >> Script_log.txt
    sleep 1s
    echo "Started lynis security audit. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_log.txt

    #cd /home/$UserName
    #cd Desktop
    #touch LynisLog.txt 
    sudo lynis audit system > LynisLog.txt
    echo "Lynis security audit has been completed. For audit results find file LynisLog.txt near where you launched the script | $thedate" >> Script_log.txt

}

########################################
############## MENU's ##################
function main_menu {
    clear

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
    echo "3.) Firewall Settings             4.) Services Settings*"
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
    elif [ $com = 3 ]; then
	    clear
	    fwset
	    main_menu
    elif [ $com = 7 ]; then
	    alyn
	read -p 'Press any key to continue: '
	    main_menu
    elif [ $com = 99 ]; then
	    clear
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
	  return
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
	echo "Log Created | $thedate" > Script_log.txt
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
