import subprocess as sub


command = pyinstaller -y -F -i "./GUIs/ScriptRunnerPyQt5_GUI/images/cup2.ico" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/configurations":"configurations/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/images":"images/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/PyUIs":"PyUIs/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/scripFunc":"scripFunc/" --add-data "./GUIs/ScriptRunnerPyQt5_GUI/requirements.txt":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py":"." --add-data "./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc":"."  "./GUIs/ScriptRunnerPyQt5_GUI/ScriptGUIrunner.py"

sub.Popen(command.split())
