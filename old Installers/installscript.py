import shutil
import errno
import platform
import getpass
import os
import subprocess as sub

def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise

user = getpass.getuser()
cwd = os.getcwd()

print(cwd)
def main():
    if platform == 'win32':
        copy('WindowsScript\\', 'C:\\Users\\' + user + '\\Desktop\\WindowsScript')
        copy('Script Runner GUI\\', 'C:\\User\\' + user + '\\Desktop\\Script Runner GUI')
        command = "pip install distro"
        sub.Popen(command.split())
    else:
        copy('Script Runner GUI/', '/home/' + user + '/Desktop/Script Runner GUI')
        copy('LinuxScript/', '/home/' + user + '/Desktop/LinuxScript')
        command = "sudo pip install distro"
        sub.Popen(command.split())


main()
