#!/bin/bash

git checkout dev

if [ $@ = 'osx' ]; then
    ~/.local/bin/pyinstaller -y -F -c -i "./GUI/images/cup2.ico" --name "AppleCIDR_MacOS_x64"  --add-data "./GUI/configurations":"configurations/" --add-data "./GUI/images":"images/" --add-data "./GUI/PyUIs":"PyUIs/" --add-data "./GUI/scripFunc":"scripFunc/" --add-data "./GUI/requirements.txt":"." --add-data "./GUI/resources_rc.py":"." --add-data "./GUI/resources.qrc":"."  "./GUI/ScriptGUIrunner.py"
elif [ $@ = 'windows' ]; then
    ~/.local/bin/pyinstaller --noconfirm --onefile --console --icon "./GUI/images/cup2.ico" --name "AppleCIDR_Windows_x64" --debug "bootloader" --version-file "./GUI/VERSION" --uac-admin --add-data "./GUI/resources.qrc;." --add-data "./GUI/resources_rc.py;." --add-data "./GUI/scripFunc;scripFunc/" --add-data "./GUI/PyUIs;PyUIs/" --add-data "./GUI/images;images/" --add-data "./GUI/configurations;configurations/"  "./GUI/ScriptGUIrunner.py"
elif [ $@ = 'linux' ]; then
    # Install some custom requirements on Linux
    ~/.local/bin/pyinstaller -y -F -c -i "./GUI/images/cup2.ico" --name "AppleCIDR_Linux_x64" --add-data "./GUI/configurations":"configurations/" --add-data "./GUI/images":"images/" --add-data "./GUI/PyUIs":"PyUIs/" --add-data "./GUI/scripFunc":"scripFunc/" --add-data "./GUI/requirements.txt":"." --add-data "./GUI/resources_rc.py":"." --add-data "./GUI/resources.qrc":"."  "./GUI/ScriptGUIrunner.py"
fi
