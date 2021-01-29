~/.local/bin/pyinstaller -y -F -c -i "./GUI/images/cup2.ico" --name "AppleCIDR_Linux_x64" --add-data "./GUI/configurations":"configurations/" --add-data "./GUI/images":"images/" --add-data "./GUI/PyUIs":"PyUIs/" --add-data "./GUI/scripFunc":"scripFunc/" --add-data "./GUI/requirements.txt":"." --add-data "./GUI/resources_rc.py":"." --add-data "./GUI/resources.qrc":"."  "./GUI/ScriptGUIrunner.py"

