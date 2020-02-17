#!/bin/bash

thedate=$(date)

################### Functions #####################
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
}

function distro_select {
  clear
  echo ""
  echo 'What linux distro are you using? [Ex: Ubuntu]  : '
  read dist
  if [ $dist = 'Ubuntu' ] || [ $dist = 'ubuntu' ]; then
    start_menu
  elif [ $dist = 'Debian' ] || [ $dist = 'debian' ]; then
    start_menu
  else
    echo 'That is not an available distro for this script...'
    sleep 2s
    distro_select
  fi
}

function start_menu {
  clear
  sleep 1s
  if [ -s ScriptSettings.sh ]; then
    echo
  else
    echo ''
    echo "This script requires a little bit of information about your system's required services and programs..."
    echo ''
    read -p 'Does this system require SSH functionality? [y/n] : ' ssh
    read -p 'Does this system require FTP functionality? [y/n] : ' ftp
    if [ $ftp = 'y' ]; then
      read -p 'Does this system use Proftpd? [y/n] : ' proftp
      read -p 'Does this system use Vsftpd? [y/n] : ' vsftpd
    fi
    read -p 'Does this system require Webserver functionality? Does it need to host a website? [y/n] : ' web
    if [ $web = 'y' ]; then
      read -p 'Does this system use Apache2 webserver for hosting? [y/n] : ' apaweb
      read -p 'Does this system use Nginx webserver for hosting? [y/n] : ' nginweb
      read -p 'Does the Webserver require SSL or HTTPS? [y/n] : ' https
    fi
    read -p 'Does this system require Samba (smb) functionality? [y/n] : ' smb
    read -p 'Does this system require SQL functionality? [y/n] : ' sql
    read -p 'Does this system require Rsync functionality? [y/n] : ' rsnc
    echo -e "!#/bin/bash \n. linux_Script.sh \n. linux_basicfunctions.sh \n. linux_mmfunctions.sh \n. linux_ugmfunctions.sh \n\UserName=$(whoami) \ndist=distro \nssh=${ssh} \nftp=${ftp} \nproftp=${proftp} \nvsftpd=${vsftpd} \nweb=${web} \napaweb=${apaweb} \nnginweb=${nginweb} \nsmb=${smb} \nsql=${sql} \nrsnc=${rsnc}" > ScriptSettings.sh
  fi
  main_menu
}
