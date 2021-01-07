#!/bin/bash

git checkout dev

if [ $@ = 'osx' ]; then
    /home/runner/.local/bin/pyinstaller -y -F -c -i "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_MacOS_x64"  --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations":"configurations/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images":"images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs":"PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc":"scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/requirements.txt":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc":"."  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
elif [ $@ = 'windows' ]; then
    /home/runner/.local/bin/pyinstaller --noconfirm --onefile --console --icon "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_Windows_x64" --debug "bootloader" --version-file "./GUIs/ScriptRunnerPyQt5_GUI/VERSION" --uac-admin --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc;." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py;." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc;scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs;PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images;images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations;configurations/"  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
elif [ $@ = 'linux' ]; then
    # Install some custom requirements on Linux
    /home/runner/.local/bin/pyinstaller -y -F -c -i "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_Linux_x64" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations":"configurations/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images":"images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs":"PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc":"scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/requirements.txt":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc":"."  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
fi
