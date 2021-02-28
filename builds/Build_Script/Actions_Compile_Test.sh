#!/bin/bash

git checkout dev

if [ "$@" = 'osx' ]; then
    ~/.local/bin/pyinstaller -y -F -c -i "./src/images/cup2.ico" --name "AppleCIDR_MacOS_x64"  --add-data "./src/configurations":"configurations/" --add-data "./src/images":"images/" --add-data "./src/PyUIs":"PyUIs/" --add-data "./src/Commands":"Commands/" --add-data "./src/requirements.txt":"." --add-data "./src/resources_rc.py":"." --add-data "./src/resources.qrc":"."  "./src/ScriptGUIrunner.py"
elif [ "$@" = 'windows' ]; then
    ~/.local/bin/pyinstaller --noconfirm --onefile --console --icon "./src/images/cup2.ico" --name "AppleCIDR_Windows_x64" --debug "bootloader" --version-file "./src/VERSION" --uac-admin --add-data "./src/resources.qrc;." --add-data "./src/resources_rc.py;." --add-data "./src/Commands;Commands/" --add-data "./src/PyUIs;PyUIs/" --add-data "./src/images;images/" --add-data "./src/configurations;configurations/"  "./src/ScriptGUIrunner.py"
elif [ "$@" = 'linux' ]; then
    export LD_LIBRARY_PATH=/usr/local/bin/
    # Install some custom requirements on Linux
    ~/.local/bin/pyinstaller -y -F -c -i "./src/images/cup2.ico" --name "AppleCIDR_Linux_x64" --add-data "./src/configurations":"configurations/" --add-data "./src/images":"images/" --add-data "./src/PyUIs":"PyUIs/" --add-data "./src/Commands":"Commands/" --add-data "./src/requirements.txt":"." --add-data "./src/resources_rc.py":"." --add-data "./src/resources.qrc":"."  "./src/ScriptGUIrunner.py"
fi
