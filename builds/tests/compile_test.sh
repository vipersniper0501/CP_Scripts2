#!/bin/bash

git checkout GUI-Updates

if [ $TRAVIS_OS_NAME = 'osx' ]; then
    # Install some custom requirements on macOS
    # e.g. brew install pyenv-virtualenv
    case "${TOXENV}" in
        py38)
            # Install some custom Python 3.2 requirements on macOS
            brew install python@3.8
            ;;
    esac
    pyinstaller -y -F -i "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_MacOS_x64"  --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations":"configurations/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images":"images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs":"PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc":"scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/requirements.txt":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc":"."  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
elif [ $TRAVIS_OS_NAME = 'windows' ]; then
    pyinstaller --noconfirm --onefile --console --icon "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_Windows_x64" --version-file "./GUIs/ScriptRunnerPyQt5_GUI/VERSION" --uac-admin --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc;." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py;." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc;scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs;PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images;images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations;configurations/"  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
elif [ $TRAVIS_OS_NAME = 'linux' ]; then
    # Install some custom requirements on Linux
    pyinstaller -y -F -i "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --name "AppleCIDR_Linux_x64" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations":"configurations/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images":"images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs":"PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc":"scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/requirements.txt":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc":"."  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"
fi

