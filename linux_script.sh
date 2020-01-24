#!/bin/bash
#use lynis for more things to add to script



######## Global Variables ##############
UserName=$(whoami)
thedate=$(date)
dist=distro

########################################################################################
######################################  Functions ######################################

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
    echo "Log Created ${thedate}" > Script_log.txt
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
    echo "Log Created ${thedate}" > Script_log.txt
}

function distro_select {
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
		distro_select
    fi;
}

function updt {
    echo "Updates starting... | ${thedate}" >> Script_log.txt
    sudo apt update && apt upgrade -y
    echo "Updates completed | ${thedate}" >> Script_log.txt
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

function fwset {	#Function configures firewall settings
	clear
	#move the install of ufw up here and ask user if it is installed already/ or figure out way to check if it is already installed
	read -p 'Does this system require SSH functionality? [y/n] : ' ssh
  read -p 'Does this system require FTP functionality? [y/n] : ' ftp
	read -p 'Does this system require Webserver functionality? Does it need to host a website? [y/n] : ' web
	read -p 'Does this system require SMB file sharing? (Ex: School shared drive) Does the system need this? [y/n] : ' smb
	read -p 'Does this system require MySQL or similar services? [y/n] : ' sql
	read -p 'Does this system require Rsync? [y/n] : ' rsnc

	echo "------------------------- Firewall Settings Has Started -------------------------------  | ${thedate}" >> Script_log.txt
	echo "Started install of UFW if not installed already | ${thedate}" >> Script_log.txt
	sudo apt install ufw -y
	echo "Completed install of UFW on system | ${thedate}" >> Script_log.txt
	sudo ufw reset
	echo "UFW has been reset to factory defaults clearing all settings | ${thedate}" >> Script_log.txt
	sudo ufw enable
	echo "UFW has been enabled on the system | ${thedate}" >> Script_log.txt

	if [ $ssh = 'y' ]; then
		sudo ufw allow 22
		echo "Port 22 has been opened for SSH networking | ${thedate}" >> Script_log.txt
		echo "##"
	elif [ $ssh = 'n' ]; then
		sudo ufw deny 22
		echo "Port 22 has been closed to stop SSH networking | ${thedate}" >> Script_log.txt
		echo "##"
	elif [ $ftp = 'y' ]; then
		sudo ufw allow 21
		echo "Port 21 has been opened for FTP networking | ${thedate}" >> Script_log.txt
		echo "####"
	elif [ $ftp = 'n' ]; then
		sudo ufw deny 21
		echo "Port 21 has been closed to stop FTP networking | ${thedate}" >> Script_log.txt
		echo "####"
	elif [ $web = 'y' ]; then
		sudo ufw allow 80
		echo "######"
		echo "Port 80 has been opened for basic Webserver hosting | ${thedate}" >> Script_log.txt
		read -p 'Does the Webserver require SSL or HTTPS? [y/n] : ' https
		if [ $https = 'y' ]; then
			sudo ufw allow 443
			echo "Port 443 has been opened for HTTPS or SSL | ${thedate}" >> Script_log.txt
			echo "########"
		else
			sudo ufw deny 443
			echo "Port 443 has been closed to stop HTTPS or SSL | ${thedate}" >> Script_log.txt
			echo "########"
		fi
	elif [ $web = 'n' ]; then
		sudo ufw deny 80
		echo "Port 80 has been closed to stop the use of HTTP | ${thedate}" >> Script_log.txt
		echo "######"
	elif [ $smb = 'y' ]; then
		sudo ufw allow 139
		echo "Port 139 has been opened for SMB file sharing | ${thedate}" >> Script_log.txt
		echo "########"
	elif [ $smb = 'n' ]; then
		sudo ufw deny 139
		echo "Port 139 has been closed to stop SMB file sharing | ${thedate}" >> Script_log.txt
		echo "########"
	elif [ $sql = 'y' ]; then
		sudo ufw allow 3306
		echo "Port 3306 has been opened to provide SQL database functionality | ${thedate}" >> Script_log.txt
		echo "##########"
	elif [ $sql = 'n' ]; then
		sudo ufw deny 3306
		echo "Port 3306 has been closed to deny SQL database functionality | ${thedate}" >> Script_log.txt
		echo "##########"
	elif [ $rsnc = 'y' ]; then
		sudo ufw allow 873
		echo "Port 873 has been opened to allow rsync service functionality  | ${thedate}" >> Script_log.txt
		echo "############"
	elif [ $rsnc = 'n' ]; then
		sudo ufw deny 873
		echo "Port 873 has been closed to deny rsync service functionality  | ${thedate}" >> Script_log.txt
		echo "############"
	fi
	echo "----------The following Ports have been closed automatically-----------" >> Script_log.txt

	sudo ufw deny 19
	echo "Port 19 has been closed to stop potential DoS attack | ${thedate}" >> Script_log.txt
	echo "##############"
	sudo ufw deny 123
	echo "Port 123 has been closed to stop potential trojan (NetController) | ${thedate}" >> Script_log.txt
	echo "################"
	sudo ufw deny 161
	echo "Port 161 has been closed to stop SNMP functionality | ${thedate}" >> Script_log.txt
	echo "##################"
	sudo ufw deny 162
	echo "Port 162 has been closed to stop SNMPtrap functionality | ${thedate}" >> Script_log.txt
	echo "####################"
	sudo ufw deny 1434
	echo "Port 1434 has been blocked to stop potential DoS attack | ${thedate}" >> Script_log.txt
	echo "######################"
	sudo ufw deny 23
	echo "Port 23 has been denied due to Telnet functionality is not necessary | ${thedate}" >> Script_log.txt
	echo "########################"
	sudo ufw deny 53
	echo "Port 53 has been closed to stop the use of DNS functionality since this is not a DNS Server | ${thedate}" >> Script_log.txt
	echo "##########################"
	echo "------------------------------------- Firewall Settings Has Ended ------------------------------------  | ${thedate}" >> Script_log.txt
}

function alyn {
    clear
    echo "Started install of Lynis | ${thedate}" >> Script_log.txt
    sudo apt install lynis -y
    echo "Install of Lynis completed | ${thedate}" >> Script_log.txt
    sleep 1s
    echo "Started lynis security audit. For audit results find file LynisLog.txt near where you launched the script | ${thedate}" >> Script_log.txt
    echo $'\nWhile looking at the log, pay close attention to the right side for FOUND, OK, DIFFERENT, SUGGESTION and more. \n\n\n\n' >> Script_log.txt
    sudo lynis audit system | tee LynisLog.txt
    echo "Lynis security audit has been completed. For audit results find file LynisLog.txt near where you launched the script | ${thedate}" >> Script_log.txt
}

#function isec {
#	read -p 'You are going to install a custom set of security tools and files. Would you like to continue? [y/n] : ' isecinstyn
#	if [ $isecinstyn = 'y' ]; then
#		sudo apt install lynis -y, clamav -y, libpam-cracklib -y, fail2ban -y,
#	fi
#
#}

function clamtime {
	echo "This command will take a long time! Once started you will no longer be able to use this terminal until the command has completed. I recommend that if you need to be able to continue using this script, that you then open a another tab and run the script again from that tab while the scan is running."
	read -p "Are you sure you want to start this now? [y/n]" clams
	if [ clams = 'y' ]; then
		echo "Starting install of clamav if not installed already on system...  | ${thedate}" >> Script_log.txt
		sudo apt install clamav -y
		sudo freshclam #make sure clamtk's virus and malware database is updated
		echo "Installation of clamav is now installed or verified to be installed...  | ${thedate}" >> Script_log.txt
		echo "Starting scan of system..."
		echo "Starting scan of system...  | ${thedate}" >> Script_log.txt
		sudo touch clamResult.txt
		sudo clamscan -r --remove / | tee clamResult.txt
		echo "You can find the output of this saved to a text file called clamResult.txt next to where the script is located"
		echo "Clamscan has finished...  | ${thedate}" >> Script_log.txt
	else
		main_menu
	fi
}

function basic_config {

	#edit the current systems policy's and secure them
	#copy the newly secured policy's to where the linux script is
	#Use this as a patch to paste over the policy settings in the competition image

	echo "Starting basic configuration"
	echo "-----------------------Starting basic configuration-------------------------" >> Script_log.txt
	sudo apt install libpam-cracklib -y
	echo "Pam module crack lib has been installed... | ${thedate}" >> Script_log.txt
	sudo apt install fail2ban -y
	echo "Fail2ban has been installed  | ${thedate}" >> Script_log.txt
	sudo cp -f pamCommonPass_patch.txt /etc/pam.d/common-password.txt
	sudo cp -f pamCommonSess_patch.txt /etc/pam.d/common-session.txt
	echo "Pam.d setting policies have been completed  | ${thedate}" >> Script_log.txt
	read -p 'Does this system use SSH? [y/n] : ' sshconf
	read -p 'Does this system use proFTP? [y/n] : ' ftpconf
	read -p 'Does this system use Samba? [y/n] : ' smbconf
	read -p 'Does this system use Apache2 Web Server? [y/n] : ' webconf
	read -p ''
	if [ $sshconf = 'y' ]; then
		sudo cp -f sshConfPatch.txt /etc/ssh/ssh_config.txt  #replacing ssh client configuration files with pre-configured version
		sudo cp -f sshdConfPatch.txt /etc/ssh/sshd_config.txt  #replacing sshd server configuration files with pre-configured version
		echo "Both ssh client and server settings have been configured  | ${thedate}" >> Script_log.txt
	fi
	#Needs to be completed##########
}

function aduser {
	read -p 'Would you like to add a user? [y/n] : ' aduseryn
	if [ $aduseryn = 'y' ]; then
		aduser=1
		while [ $aduser = 1 ]; do
			read -p 'What would you like to name this new user? : ' name
			read -p 'Is this user an Admin? [y/n] : ' adminyn
			if [ $adminyn = 'y' ]; then
        sudo adduser --force-badname $name
				sudo usermod -a -G sudo $name		#adds user to sudo group
        sudo usermod -a -G adm $name   #adds user to admin group
				echo "User ${name} has been created and has been added to admin and sudo groups"
				echo "User ${name} has been created and has been added to admin and sudo groups  | ${thedate}" >> Script_log.txt
			else
				sudo useradd $name
				echo "User ${name} has been added!"
				echo "User ${name} has been added!  | ${thedate}" >> Script_log.txt
			fi
			read -p 'Would you like to add another user? [y/n] : ' aga
			if [ $aga = 'n' ]; then
				$aduser=0
			fi
		done
		sleep 1s
	else
		usr_gru
	fi
}

function rmuser {
	read -p 'Would you like to remove a user from this system? [y/n] : ' rmuseryn
	if [ $rmuseryn = 'y' ]; then
		rmuser=1
		while [ $rmuser = 1 ]; do
			eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1  #this prints out the users that are able to sign in (not system users that are used by programs)
			read -p 'Which user would you like to remove from the system? : ' name
			userdel -r $name
      echo "User ${name} has been removed from this system!  | ${thedate}" | tee Script_log.txt
      read -p 'Would you like to remove another user from this system? [y/n] : ' aga
      if [ $aga = 'n' ]; then
        $rmuseryn=0
      fi
		done
	else
		usr_gru
	fi
}

function lsusrs {
  eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1 #prints users
  read -p 'Press Enter to continue...'
}

function lsgrus {
  getent group | cut -d: -f1 #prints out groups to screen
  read -p 'Press Enter to continue...'
}

function usrtogru {
  read -p 'Would you like to add a user to a group? [y/n] : ' usrtogruyn
  if [ $usrtogruyn = 'y' ]; then
    usrtogru=1
    while [ $usrtogru = 1 ]; do
      eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1  #this prints out the users that are able to sign in (not system users that are used by programs)
      read -p 'Which user would you like to add to a group? : ' name
      getent group | cut -d: -f1
      read -p 'Which group would you like to add user ${name} to? : ' group
      sudo usermod -a -G $group $name
      echo "User ${name} has been added to group ${group}  | ${thedate}" | tee Script_log.txt  #prints to screen and log file
      read -p 'Would you like to add another user to another group? [y/n] : ' aga
      if [ $aga = 'n' ]; then
        usrtogru=0
      fi
    done
  else
    usr_gru
  fi
}

function crtgru {
  read -p 'Would you like to create a new group? [y/n] : ' crtgruyn
  if [ $crtgruyn = 'y' ]; then
    crtgru=1
    while [ $crtgru = 1 ]; do
      read -p 'What would you like to name the new group? : ' name
      sudo groupadd $name
      echo "The new group called ${name} has been created!  | ${thedate}" | tee Script_log.txt
      echo ""
      read -p 'Would you like to create another group? [y/n] : ' aga
      if [ $aga = 'n' ]; then
        crtgru=0
      fi
    done
  else
    usr_gru
  fi
}

function rmgru {
  read -p 'Would you like to delete a group? [y/n] : ' rmgruyn
  if [ $rmgruyn = 'y' ]; then
    rmgru=1
    while [ $rmgru = 1 ]; do
      getent group | cut -d: -f1 #prints out groups to screen
      read -p 'What group would you like to remove from the system? : ' name
      sudo groupdel $name
      echo "The group called ${name} has been removed from the system!  | ${thedate}" | tee Script_log.txt
      echo ""
      read -p 'Would you like to remove another user from the system? [y/n] : ' aga
      if [ $aga = 'n' ]; then
        rmgru=0
      fi
    done
  else
    usr_gru
  fi
}

function rmfrogru {
  read -p 'Would you like to remove a user from a group? [y/n] : ' rmfrogruyn
  if [ $rmfrogruyn = 'y' ]; then
    rmfrogru=1
    while [ $rmfrogru = 1 ]; do
      eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1
      read -p 'Which user would you like to remove from a group? : ' name
      getent group | cut -d: -f1
      read -p 'Which group would you like to remove the user from? : ' gruname
      gpasswd -d $name $gruname
      echo "User ${name} has been removed from group ${gruname}!  | ${thedate}" | tee Script_log.txt
      read -p 'Would you like to remove another user from another group? [y/n] : ' aga
      if [ $aga = 'n' ]; then
        rmfrogru=0
      fi
    done
  else
    usr_gru
  fi
}

function usrgrumem {
  read -p 'Would you like to see what groups a specific user is in? [y/n] : ' usrgrumemyn
  if [ $usrgrumemyn = 'y' ]; then
    read -p 'What is the name of the user that you want to know the groups of? : ' name
    groups $name
  else
    usr_gru
  fi
}

function grumem {
  read -p 'Would you like to see what members are in a specific group? [y/n] : ' grumemyn
  if [ $grumemyn = 'y' ]; then
    getent group | cut -d: -f1
    read -p 'What group would you like to see the members of? : ' gruname
    grep -i --color $gruname /etc/group
  else
    usr_gru
  fi
}

####################################################################################
###################################### MENU's ######################################
function main_menu {
    clear

    #for determining which title to show
    if [ $dist = "Ubuntu" ]; then
        linUbunut
    elif [ $dist = "Debian" ]; then
        linDebian
    else
        return
    fi

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
    echo "1.) Add User                   2.) Remove User"
    echo "3.) Add Group                  4.) Remove Group"
    echo "5.) Add user to Group          6.) Remove user from Group"
    echo "7.) List local users           8.) List Local Groups"
    echo "9.) List members of group      10.) List the groups an user is in*"
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
	    echo ""
	    sleep 1s
	    exit
    fi
    echo ""
    read -p 'Have you completed all of the Forensics Questions? [y/n] : ' fqs
    if [ $fqs = y ]; then
		echo "" #since yes, the script continues.
    else
		echo "Please complete the Forensics Questions first before you use this script."
		sleep 3s
		exit
    fi
    distro_select #asks users what distro they are using, then open main menu for that 'distro'
    read -p 'Press any key to continue: '

}

########################################
start_scrpt
########################################
