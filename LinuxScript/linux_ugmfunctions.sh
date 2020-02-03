#!/bin/bash

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
			#eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1  #this prints out the users that are able to sign in (not system users that are used by programs)
			cat /etc/passwd | grep "/home" | cut -d":" -f1
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
  #eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1 #prints users
  cat /etc/passwd | grep "/home" | cut -d":" -f1
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
      #eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1  #this prints out the users that are able to sign in (not system users that are used by programs)
      cat /etc/passwd | grep "/home" | cut -d":" -f1
      
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
      #eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1
      cat /etc/passwd | grep "/home" | cut -d":" -f1
      
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

function chpaswdall {
  read -p 'Would you like to change all of the passwords for the users? [y/n] : ' chpaswdallyn
  if [ $chpaswdallyn = 'y' ]; then
    userlist = ()
    mapfile -t $userlist < <( cat /etc/passwd | grep "/home" | cut -d":" -f1 )  #shows users in home directory
    
    usersleft = ${#userlist[@]}  #this variable is equivelent to the number of users in list $userlist
    read -p 'What would you like the new passwords to be?' newpasswd
    while [ $usersleft != 0 ]; do
      
      
    done
  else
    usr_gru
  fi
}