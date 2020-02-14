#!/bin/bash

function updt {
  echo "Updates starting... | ${thedate}" >> Script_log.txt
  sudo apt update && apt upgrade -y
  echo "Updates completed | ${thedate}" >> Script_log.txt
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
  echo "------------- Firewall Settings Has Started ----------------  | ${thedate}" >> Script_log.txt
  echo "Started install of UFW if not installed already | ${thedate}" >> Script_log.txt
  sudo apt install ufw -y
  echo "Completed install of UFW on system | ${thedate}" >> Script_log.txt
  sudo ufw reset
  echo "UFW has been reset to factory defaults clearing all settings | ${thedate}" >> Script_log.txt
  sudo ufw enable
  echo "UFW has been enabled on the system | ${thedate}" >> Script_log.txt
#SSH
  if [ $ssh = 'y' ]; then
    sudo ufw allow 22
    echo "Port 22 has been opened for SSH networking | ${thedate}" >> Script_log.txt
    echo "##"
  elif [ $ssh = 'n' ]; then
    sudo ufw deny 22
    echo "Port 22 has been closed to stop SSH networking | ${thedate}" >> Script_log.txt
    echo "##"
  fi
#Ftp
  if [ $ftp = 'y' ]; then
    sudo ufw allow 21
    echo "Port 21 has been opened for FTP networking | ${thedate}" >> Script_log.txt
    echo "####"
  elif [ $ftp = 'n' ]; then
    sudo ufw deny 21
    echo "Port 21 has been closed to stop FTP networking | ${thedate}" >> Script_log.txt
    echo "####"
  fi
#Web
  if [ $web = 'y' ]; then
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
  fi
#Samba
  if [ $smb = 'y' ]; then
    sudo ufw allow 139
    echo "Port 139 has been opened for SMB file sharing | ${thedate}" >> Script_log.txt
    echo "########"
  elif [ $smb = 'n' ]; then
    sudo ufw deny 139
    echo "Port 139 has been closed to stop SMB file sharing | ${thedate}" >> Script_log.txt
    echo "########"
  fi
#SQL
  if [ $sql = 'y' ]; then
    sudo ufw allow 3306
    echo "Port 3306 has been opened to provide SQL database functionality | ${thedate}" >> Script_log.txt
    echo "##########"
  elif [ $sql = 'n' ]; then
    sudo ufw deny 3306
    echo "Port 3306 has been closed to deny SQL database functionality | ${thedate}" >> Script_log.txt
    echo "##########"
  fi
#Rsync
  if [ $rsnc = 'y' ]; then
    sudo ufw allow 873
    echo "Port 873 has been opened to allow rsync service functionality  | ${thedate}" >> Script_log.txt
    echo "############"
  elif [ $rsnc = 'n' ]; then
    sudo ufw deny 873
    echo "Port 873 has been closed to deny rsync service functionality  | ${thedate}" >> Script_log.txt
    echo "############"
  fi

  echo "------------ The following Ports have been closed automatically ---------------  | ${thedate}" >> Script_log.txt
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
  echo "------------- Firewall Settings Has Ended ---------------  | ${thedate}" >> Script_log.txt
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

function clamtime {
  echo "This command will take a long time! Once started you will no longer be able to use this terminal until the command has completed. I recommend that if you need to be able to continue using this script, that you then open a another tab and run the script again from that tab while the scan is running."
  read -p "Are you sure you want to start this now? [y/n]" clams
  if [ $clams = 'y' ]; then
    echo "Starting install of clamav if not installed already on system...  | ${thedate}" >> Script_log.txt
    sudo apt install clamav -y
    sudo freshclam #make sure clamav's virus and malware database is updated
    echo "Installation of clamav is now installed or verified to be installed...  | ${thedate}" >> Script_log.txt
    echo "Starting scan of system...  | ${thedate}" | tee Script_log.txt
    sudo touch clamResult.txt
    sudo clamscan -r --remove / | tee clamResult.txt
    echo "You can find the output of this saved to a text file called clamResult.txt next to where the script is located"
    echo "Clamscan has finished...  | ${thedate}" | tee Script_log.txt
  else
    echo "If you get this message, it is because you did not run this script as sudo su (root)"
    sleep 2s
    main_menu
  fi
}

function srchmedia {
  echo "This output will be also be placed in the Script_log.txt for further review..."
  sleep 2s
  echo "--------------- Prohibited Media Search Started ---------------  | ${thedate}" | tee Script_log.txt
  sleep 1s
  find / -name '*.jpg' -o -name '*.mp4' -o -name '*.flv' -o -name '*.avi' -o -name '*.wmv' -o -name '*.mov' -o -name '*.png' -o -name '*.jpg' -o -name '*.tif' -o -name '*.gif' -o -name '*.mp3' -o -name '*.wmv' -o -name '*.wma' -o -name '*.aif' -o -name '*.jar' | tee Script_log.txt
  echo "----------------- Prohibited Media Search Ended --------------  | ${thedate}"
  sleep 1s
}

function basic_config {
  #edit the current systems policy's and secure them
  #copy the newly secured policy's to where the linux script is
  #Use this as a patch to paste over the policy settings in the competition image
  echo "Starting basic configuration"
  echo "-------------- Starting basic configuration -------------  | ${thedate}" >> Script_log.txt
  sudo apt install libpam-cracklib -y
  echo "Pam module crack lib has been installed... | ${thedate}" | tee Script_log.txt
  sudo apt install fail2ban -y
  echo "Fail2ban has been installed  | ${thedate}" | tee Script_log.txt
  sudo cp ../config_files/pamCommonPass_patch /etc/pam.d/common-password
  sudo cp ../config_files/pamCommonSess_patch /etc/pam.d/common-session
  sudo cp ../config_files/pamLogin_patch /etc/pam.d/login
  sudo cp ../config_files/pamOther_patch /etc/pam.d/other
  echo "Pam.d setting policies have been completed  | ${thedate}" | tee Script_log.txt
  clear

  read -p 'Does this system use SSH? [y/n] : ' sshconf
  read -p 'Does this system use proFTP? [y/n] : ' ftpconf
  read -p 'Does this system use Samba? [y/n] : ' smbconf
  read -p 'Does this system use Apache2 Web Server? [y/n] : ' webconf
  #SSH
  if [ $sshconf = 'y' ]; then
    sudo cp sshConfPatch /etc/ssh/ssh_config  #replacing ssh client configuration files with pre-configured version
    sudo cp sshdConfPatch /etc/ssh/sshd_config  #replacing sshd server configuration files with pre-configured version
    echo "Both ssh client and server settings have been configured  | ${thedate}" | tee Script_log.txt
  fi
  #FTP
  if [ $ftpconf = 'y' ]; then
    sudo cp /etc/proftpd/proftpd.conf ~/Desktop/orig_proftpd.conf
    sudo mkdir /etc/proftpd/ssl
    sudo openssl req -new -x509 -days 365 -nodes -out /etc/proftpd/ssl/proftpd.cert.pem -keyout /etc/proftpd/ssl/proftpd.key.pem
    echo "TLS/SSL keys have been created for ProFTP server  | ${thedate}" | tee Script_log.txt
    sudo cp ftpTls_patch.conf /etc/proftpd/tls.conf #replaces tls configuration files
    sudo cp ftpConf_patch.conf /etc/proftpd/proftpd.conf #replacing proftpd configuration files
    echo "Proftpd server settings have been configured  | ${thedate}" | tee Script_log.txt
  fi
  #Samba
  if [ $smbconf = 'y' ]; then
    sudo cp smbConf_patch.conf /etc/samba/smb.conf #replacing samba configuration files
    echo "Samba server settings have been configured  | ${thedate}" | tee Script_log.txt
  fi
  #Web
  if [ $webocnf = 'y' ]; then
    sudo cp apaConf_patch.conf /etc/apache2/apache2.conf #replacing apache webserver configuration files
    echo "Apache2 web server settings have been configured  | ${thedate}" | tee Script_log.txt
  fi
  echo "Basic configuration has completed"
  echo "------------- Basic configuration completed -------------  | ${thedate}" >> Script_log.txt
  sleep 1s
}
