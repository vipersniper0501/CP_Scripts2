import configparser
import subprocess as sub
import distro
import logging as log
from functools import lru_cache
from Commands.AppleCIDR_Util import NewThread, Check_Password
from PyQt5 import QtGui
from PyQt5.QtWidgets import QListWidgetItem, QDialog, QMessageBox  # ,\
# QTreeWidgetItem
from PyUIs.add_groupUI import Ui_Add_Group_UIClass
from PyUIs.addusrUI import Ui_addUSR
# from PyUIs.changepass import Ui_chngpass
from PyUIs.rmvUSRoGRU import Ui_rmvusrogru
# from PyUIs.user_group_modifyUI import Ui_user_group_list_modifiers


OS = distro.linux_distribution()[0]

config = configparser.ConfigParser()
config.read('config.ini')


@lru_cache
def Linux_Find_Names():
    """
    This function seaerches for local usernames on the current system.

    :return: Returns three lists, Standard Users, Admins, and all users.
    """
    # convert these to python function. Get rid of shell script.
    # Honestly, there is no reason to use 'ls /home' in a shell script
    # when I can do it in python -_-
    def find_names():
        # Local users are added to a list of standardUsers
        output = sub.run("ls /home".split(), stdout=sub.PIPE, check=True,
                         text=True)
        output = output.stdout.split("\n")
        allUsers = []
        standardUsers = []
        admins = []
        for _, i in enumerate(output):
            standardUsers.append(i)

        # Local Administrators are added to list of admins
        process_catGroup = sub.run("cat /etc/group".split(), stdout=sub.PIPE,
                                   check=True, text=True)
        # NOTE: This is not working for some reason.    :s
        output = sub.run("grep 'root'".split(), input=process_catGroup.stdout,
                         stdout=sub.PIPE, check=True, text=True)
        output = output.stdout.split("\n")
        output[0] = output[0][9:]
        for _, i in enumerate(output):
            admins.append(i)
        log.debug(standardUsers)
        for _, i in enumerate(standardUsers):
            if i not in allUsers:
                allUsers.append(i)
        for _, i in enumerate(admins):
            if i not in allUsers:
                allUsers.append(i)
        return standardUsers, admins, allUsers
    return NewThread(find_names, True, "Finding Names")


# Need to be configured for linux
@lru_cache
def Find_Groups(users_n_groups: bool):
    """
    This is to find local groups and users on the windows 10 operating system

    :param users_n_groups: True/False  Do you need the users in each group also
    :return: Returns a list of local groups
    if users_n_groups is True, also returns a dictionary of users in each group
    """
    def find_groups(users_n_groups: bool):
        f = open("/etc/group", "r")
        output = f.read().split("\n")
        groups = []
        users_in_groups = {}
        for _, i in enumerate(output):
            group_name = i.split(":")[1]
            group_users = i.split(":")[3]
            groups.append(group_name)
            if len(group_users) == 0:
                users_in_groups[group_name] = "No Users"
            else:
                users_in_groups[group_name] = group_users

        return users_in_groups, groups
    return NewThread(find_groups, True, "Finding Groups", users_n_groups)


def malRem():
    def malrem():
        if OS == 'Manjaro Linux':
            sub.run("sudo pacman -S clamav -y".split())
        else:
            sub.run("sudo apt install clamav -y".split())
        command = ['sudo freshclam', 'sudo touch CLAMresults.txt',
                   'sudo clamscan -r --remove / | tee CLAMresults.txt']
        for _, i in enumerate(command):
            sub.run(command[i].split())
    NewThread(malrem, False, "Malware Removal")


def alyn():
    def audit_w_lynis():
        if OS in ('Ubuntu', 'debian'):
            if sub.run("sudo lynis".split(), check=True,
                       text=True).returncode == 1:
                sub.run("sudo apt install lynis -y".split())
            sub.run("sudo lynis audit system | "
                    "tee ~/Desktop/audit_results.txt".split())
        elif OS == 'Manjaro Linux':
            command = 'sudo pacman -S lynis --noconfirm'
            sub.run(command.split())
            command = 'sudo touch audit_results.txt'
            sub.run(command.split())
            command2 = 'sudo lynis audit system | tee audit_results.txt'
            sub.run(command2.split())
    NewThread(audit_w_lynis, False, "Auditing with lynis")


def Linux_addusr():
    class add_user_to_system(QDialog, Ui_addUSR):
        def __init__(self, parent=None):
            super(add_user_to_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(345, 187)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.adminyn = 'n'

            def adminy(selected):
                if selected:
                    print("This user will be an admin and"
                          "have root permissions")
                    self.adminyn = 'y'

            def adminn(selected):
                if selected:
                    print("This user will NOT be an admin and not have "
                          "root permissions")
                    self.adminyn = 'n'

            self.admin_y.toggled.connect(adminy)
            self.admin_n.toggled.connect(adminn)

            def CONFIRM():
                username = self.username_input.text()
                passwd = self.Password1_input.text()

                def completedPOP():
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        f"User {username} has been successfully"
                        "added to system.")
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.close()

                # Need to make error message if could not add user. Currently
                # popup will still activate announcing success even if the
                # command failed. Possible way is to use sub.run as it gives
                # back a return code that can be used to check if
                # the command succeeded.
                if self.adminyn == 'y':
                    print('This user will be an admin')
                    if Check_Password(self.Password1_input.text(),
                                      self.Password2_input.text()):
                        sub.run("sudo useradd -G users,admin,sudo -m -d"
                                f" /home/{username} -p $(echo {passwd} | "
                                "openssl passwd -1 "
                                f"-stdin) {username}".split())
                        sub.run("sudo echo '%/# User privelage specfication"
                                f"\na\n{username}    ALL=(ALL:ALL) ALL\n.\nwq'"
                                " | ed /etc/sudoers".split())
                        log.info(f"User {username} has been "
                                 "successfully added!")
                        completedPOP()
                elif self.adminyn == 'n':
                    log.info('This user will not be an admin')
                    if Check_Password(self.Password1_input.text(),
                                      self.Password2_input.text()):
                        output = sub.run(f"echo '{passwd}' | openssl passwd -1"
                                         " -stdin".split(), stdout=sub.PIPE,
                                         check=True, text=True)
                        sub.run(f"useradd -g users -m -d /home/{username} -p "
                                f"'{output.stdout}' {username}".split())
                        log.info(f"User {username} has been "
                                 "successfully added!")
                        completedPOP()

            def cancel_button():
                self.close()

            self.Confirm_button.clicked.connect(lambda: NewThread(CONFIRM,
                                                                  False,
                                                                  "Adding User"
                                                                  ))
            self.Cancel_button.clicked.connect(cancel_button)

        def begin(self):
            super(add_user_to_system, self).exec_()

    auts = add_user_to_system()
    NewThread(auts.begin, False, "Add User To System")


def Linux_remusr():
    class remove_user_from_system(QDialog, Ui_rmvusrogru):
        def __init__(self, parent=None):
            super(remove_user_from_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(302, 410)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('Remove User From System')
            self.label.setText('Current Users:')
            self.label2.setText('Username: ')

            listo_names = Linux_Find_Names()

            for _, name in enumerate(listo_names[2]):
                QListWidgetItem(name, self.listOFnames)

            def removal():
                username = self.Name_Input.text()

                def completedPOP(username):
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        f"User {username} has been successfully "
                        "removed from the system.")
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.listOFnames.clear()
                    self.Name_Input.clear()
                    for _, name in enumerate(listo_names):
                        QListWidgetItem(name, self.listOFnames)

                if len(username) == 0:
                    print('no username entered')
                    ERROR_NO_USER = QMessageBox()
                    ERROR_NO_USER.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER.setText(
                        'No username was entered. No user was removed.')
                    ERROR_NO_USER.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER.exec_()
                elif username not in listo_names:
                    print('User not found')
                    ERROR_NO_USER_FOUND = QMessageBox()
                    ERROR_NO_USER_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER_FOUND.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER_FOUND.setText(
                        'User was not found on system. No user was removed.')
                    ERROR_NO_USER_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER_FOUND.exec_()
                else:
                    sub.run(f"sudo killall -u {username}".split())
                    sub.run(f"sudo userdel -f -r {username}".split())
                    completedPOP(username)

            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    print('Removing user...')
                    removal()
                elif x == QMessageBox.No:
                    print('Cancelling...')

            def cancel_button():
                self.close()

            self.Cancel_button.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())

        def begin(self):
            super(remove_user_from_system, self).exec_()

    rufg = remove_user_from_system()
    NewThread(rufg.begin, False, "Remove User From System")


def Linux_add_group_to_system():
    class add_group_to_system(QDialog, Ui_Add_Group_UIClass):
        def __init__(self, parent=None):
            super(add_group_to_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(292, 94)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            def add_group():
                # Add ability to check to make sure group does
                # not already exist
                _, groups = Find_Groups(False)
                if self.group_name_input.text() in groups:
                    HEY = QMessageBox()
                    HEY.setWindowTitle('Hey! Listen!')
                    HEY.setText("Hey! This group already exists!")
                    HEY.setIcon(QMessageBox.Critical)
                    HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    HEY.exec_()
                else:
                    sub.run("sudo groupadd "
                            f"{self.group_name_input.text()}".split())

            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    log.info('Adding Group...')
                    add_group()
                elif x == QMessageBox.No:
                    log.info('Cancelling...')

            def cancel_button():
                self.close()

            self.Cancel_button.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())

        def begin(self):
            super(add_group_to_system, self).exec_()

    agts = add_group_to_system()
    NewThread(agts.begin, False, "Add Group To System")


def Linux_remgrufrosys():
    class remove_group_from_system(QDialog, Ui_rmvusrogru):
        def __init__(self, parent=None):
            super(remove_group_from_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(302, 410)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('Remove Group From System')
            self.label.setText('Current Groups:')
            self.label2.setText('Group Name: ')

            _, list_of_groups = Find_Groups(False)

            for _, group in enumerate(list_of_groups):
                QListWidgetItem(group, self.listOFnames)

            def remove_group():
                group_name = self.Name_Input.text()

                def completedPOP(group_name):
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        f"Group {group_name} has successfully been removed "
                        "from the system.")
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.listOFnames.clear()
                    self.Name_Input.clear()
                    for i in range(0, len(list_of_groups)):
                        QListWidgetItem(list_of_groups[i], self.listOFnames)

                if len(group_name) == 0:
                    log.info('no group entered')
                    ERROR_NO_GROUP_ENTERED = QMessageBox()
                    ERROR_NO_GROUP_ENTERED.setIcon(QMessageBox.Warning)
                    ERROR_NO_GROUP_ENTERED.setWindowTitle('Hey! Listen!')
                    ERROR_NO_GROUP_ENTERED.setText(
                        "No group name was entered. No group was removed.")
                    ERROR_NO_GROUP_ENTERED.setStandardButtons(
                        QMessageBox.Close)
                    ERROR_NO_GROUP_ENTERED.exec_()
                elif group_name not in list_of_groups:
                    log.info("Group not found")
                    ERROR_GROUP_NOT_FOUND = QMessageBox()
                    ERROR_GROUP_NOT_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_GROUP_NOT_FOUND.setWindowTitle("Hey! Listen!")
                    ERROR_GROUP_NOT_FOUND.setText(
                        "Group was not found on system. No group was removed.")
                    ERROR_GROUP_NOT_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_GROUP_NOT_FOUND.exec_()
                else:
                    # Executes command.
                    sub.run(f"sudo groupdel {group_name}".split())
                    completedPOP(group_name)

            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    log.info('Removing group...')
                    remove_group()
                elif x == QMessageBox.No:
                    log.info('Cancelling...')

            def cancel_button():
                self.close()

            self.Cancel_button.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())

        def begin(self):
            super(remove_group_from_system, self).exec_()

    rgfs = remove_group_from_system()
    NewThread(rgfs.begin, False, "Remove Group From System")
