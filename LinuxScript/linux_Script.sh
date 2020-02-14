#!/bin/bash
#use lynis for more things to add to script
################# Imports ##############
. linux_basicfunctions.sh #location of functions used by start script
. linux_mmfunctions.sh #location of functions used for main menu
. linux_ugmfunctions.sh #location of functions used for User and Group Settings menu
. linux_GV.sh
######## Global Variables ##############
#UserName=$(whoami)
#thedate=$(date)
#dist=distro
##Service Variables##
#ssh='' #basic ssh settings
#ftp='' #basic ftp Settings
#proftp='' #proftp specific settings
#vsftpd='' #vsftpd specific settings
#web='' #basic web settings
#apaweb='' #apache2 specific settings
#nginweb='' #nginx specific settings
#smb='' #basic samba settings
#sql='' #basic sql settings
#rsnc='' #basic rsync settings
########################################################################################
###################################### MENU's ######################################
function main_menu {
  clear
  #if statement for determining which title to show
  if [ $dist = "Ubuntu" ] || [ $dist = "ubuntu" ]; then
    linUbunut
  elif [ $dist = "Debian" ] || [ $dist = "debian" ]; then
    linDebian
  fi
  #Main Menu for most functions
  echo "If there is a * after the command, then the command has either not been made yet or is not finished."
  echo ""
  echo "Main Menu"
  echo ""
  echo "Commands:"
  echo "1.) Updates                            2.) User Settings "
  echo "3.) Firewall Settings                  4.) Services Settings*"
  echo "5.) Remove Prohibited Software*        6.) Malware Removal"
  echo "7.) Audit using Lynis                  8.) Basic Configurations*"
  echo "9.) Search for Prohibited Media*"
  echo ""
  echo "85.) Run all at once*"
  echo "99.) Quit                         100.) Restart"
  echo ""
  echo ""
  read -p 'Which command would you like to use? : ' com
  if [ $com = 1 ]; then
    clear
    updt
    echo ""
    echo "Please restart for full update to complete..."
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 2 ]; then
    clear
	  usr_gru
  elif [ $com = 3 ]; then
    clear
    fwset
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 6 ]; then
    clear
    clamtime
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 7 ]; then
    clear
    alyn
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 8 ]; then
    clear
    basic_config
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 9 ]; then
    clear
    srchmedia
    read -p 'Press Enter key to continue: '
    clear
    main_menu
  elif [ $com = 99 ]; then
    clear
    exit
  elif [ $com = 100 ]; then
    sudo reboot
  fi
}

function usr_gru {
  clear
  #for determining which title to show
  if [ $dist = "Ubuntu" ] || [ $dist = "ubuntu" ]; then
	  linUbunut
  elif [ $dist = "Debian" ] || [ $dist = "debian" ]; then
	  linDebian
  else
	  return
  fi

  #Menu for user and Group settings
  echo ""
  echo "User and Group settings"
  echo ""
  echo "Commands:"
  echo "1.) Add User                                 2.) Remove User"
  echo "3.) Add Group                                4.) Remove Group"
  echo "5.) Add user to Group                        6.) Remove user from Group"
  echo "7.) List local users                         8.) List Local Groups"
  echo "9.) List members of group                    10.) List the groups an user is in*"
  echo "11.) Change all users passwords at once      "
  echo ""
  echo "99.) Back to Main Menu"
  read -p 'Which command would you like to use? : ' com
  if [ $com = 1 ]; then
    clear
    aduser
    usr_gru
  elif [ $com = 2 ]; then
    clear
    rmuser
    usr_gru
  elif [ $com = 3 ]; then
    clear
    crtgru
    usr_gru
  elif [ $com = 4 ]; then
    clear
    rmgru
    usr_gru
  elif [ $com = 5 ]; then
    clear
    usrtogru
    usr_gru
  elif [ $com = 6 ]; then
    clear
    rmfrogru
    usr_gru
  elif [ $com = 7 ]; then
    clear
    lsusrs
    usr_gru
  elif [ $com = 8 ]; then
    clear
    lsgrus
    usr_gru
  elif [ $com = 9 ]; then
    clear
    grumem
    usr_gru
  elif [ $com = 10 ]; then
    clear
    usrgrumem
    usr_gru
  elif [ $com = 11 ]; then
    clear
    chpaswdall
    usr_gru
  elif [ $com = 99 ]; then
	  main_menu
  fi
}

########################################
############### Start Script ###########
function start_scrpt {
  clear
  echo ""
  if [[ $(/usr/bin/id -u) -ne 0 ]]; then	#this statement checks for if you are running as superuser (sudo)
	  echo "You are not root. You must be running as root to use this script"
	  sleep 1s
	  exit
  fi
  echo "Log Created ${thedate}" > Script_log.txt
  sudo chmod 777 Script_log.txt
  read -p 'Have you completed all of the Forensics Questions? [y/n] : ' fqs
  if [ $fqs = y ]; then
	  echo
  else
	  echo "Please complete the Forensics Questions first before you use this script."
	  sleep 3s
	  exit
  fi
  distro_select #asks users what distro they are using, then open main menu for that 'distro'
}

########################################
start_scrpt
########################################
