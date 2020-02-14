#!/bin/bash


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
  echo "What linux distro are you using? [Ex: Ubuntu]  : "
  read dist
  if [ $dist = 'Ubuntu' ]; then
    ubuntu_start
  elif [ $dist = 'Debian' ]; then
    debian_start
  else
    echo 'That is not an available distro for this script...'
    sleep 2s
	distro_select
  fi
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