import configparser
import shutil
import subprocess as sub
import logging as log
from scripFunc.AppleCIDR_Util import NewThread, Check_Password, Timer
from functools import lru_cache
from PyQt5 import QtGui
from PyQt5.QtWidgets import QListWidgetItem, QDialog, QMessageBox,\
    QTreeWidgetItem
from PyUIs.add_groupUI import Ui_Add_Group_UIClass
from PyUIs.addusrUI import Ui_addUSR
from PyUIs.changepass import Ui_chngpass
from PyUIs.enblebit import Ui_bitlockerGUI
from PyUIs.rmvUSRoGRU import Ui_rmvusrogru
from PyUIs.user_group_modifyUI import Ui_user_group_list_modifiers

config = configparser.ConfigParser()
config.read('config.ini')


# This function is not really needed, but nice to have if needed.
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS # pylint: disable=no-member
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)


@lru_cache
def Find_Names():
    def find_names():
        # Local users are added to a list of names
        output = sub.run("powershell net localgroup users".split(),
                         stdout=sub.PIPE, text=True, check=True)
        output = output.stdout.split("\n")
        names = []
        for i0 in range(6, len(output) - 3):
            w = output[i0].split('\r')
            x = w[0]
            names.append(x)

        # Local Administrators are added to list of names
        stdout, _ = sub.Popen("powershell net localgroup administrators",
                              stdout=sub.PIPE).communicate()
        output = stdout.decode("utf-8").split("\n")

        stdout, _ = sub.Popen("powershell $env:UserName",
                              stdout=sub.PIPE).communicate()
        current_user = stdout.decode("utf-8").split("\r\n")
        for i4 in range(6, len(output) - 3):
            w = output[i4].split('\r')
            if w[0] == current_user[0]:
                w[0] = current_user[0] + '   (Current User)'
            names.append(x)
        names.insert(0, '\n')
        log.info(names)
        return names
    return NewThread(find_names, True, "Finding Names")


@lru_cache
def Find_Groups(users_n_groups: bool):
    """
    This is to find local groups and users on the windows 10
    operating system

    :param users_n_groups: True/False  Do you need the users in
    each group also.
    :return: Returns a list of local groups and if users_n_groups is True,
    also returns a dictionary of users in each group
    """
    def find_groups(users_n_groups: bool):
        stdout, _ = sub.Popen(["powershell", "& {net localgroup}"], stdout=sub.PIPE).communicate()
        output = stdout.decode("utf-8").split("\n")
        groups = []
        for i in range(4, len(output) - 3):
            w = output[i].split('\r')[0].split('*')[1]
            groups.append(w)

        users_in_groups = {}
        # TODO: SPEED THIS UP
        if users_n_groups:
            for _, group in enumerate(groups):
                stdout2, _ = sub.Popen(["powershell", f"net localgroup '{group}'"], stdout=sub.PIPE).communicate()
                try:
                    output = stdout2.decode("utf-8").split("\n")
                    user_names = []
                    for i3 in range(6, len(output) - 3):
                        y = output[i3].split('\r')[0]
                        user_names.append(y)
                    if len(user_names) == 0:
                        users_in_groups[group] = ['No Users']
                    elif len(user_names) == 1:
                        users_in_groups[group] = [user_names[0]]
                    else:
                        for i4 in range(0, len(user_names)):
                            users_in_groups[group] = user_names
                except Exception as e:
                    log.debug('\n\nException occurred: ' + str(e))

        log.info(groups)
        log.info(users_in_groups)
        return users_in_groups, groups
    return NewThread(find_groups, True, "Finding Groups", users_n_groups)


def BITLOCKER():
    class bitRUN(QDialog, Ui_bitlockerGUI):
        def __init__(self, parent=None):
            super(bitRUN, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(483, 323)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            # Executes encryption command
            def ENCRYPT(drive):
                # Only works if 'Allow BitLocker without compatible TPM' is
                # enabled in the Group Policy
                # Also does not encrypt right away. If you type
                # 'Get-BitlockerVolume' in powershell, it will tell you
                # how much has been encrypted so far.

                if Check_Password(self.encrypPASS.text(), self.encrypPASS_2.text()):
                    command = f"$pass = ConvertTo-SecureString {self.encrypPASS.text()} -AsPlainText -Force " \
                          f"\nEnable-BitLocker {drive} -PasswordProtector $pass"
                    sub.Popen(['powershell', f'& {command}'])

                    def restart():
                        sub.Popen("powershell Restart-Computer")

                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        'You must restart the computer for encryption to begin on the drive. '
                    '\nWould you like to restart now?')
                    COMPLETE.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                    x_restart = COMPLETE.exec_()
                    if x_restart == QMessageBox.Yes:
                        log.info('Restarting...')
                        restart()
                    elif x_restart == QMessageBox.No:
                        log.info('Closing...')
                        self.close()

            # Gets list of drives and encryption status'
            decryptSTATUS = [] # Note: This should be a dictionary
            command = 'Get-BitLockerVolume'
            output = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE).communicate()[0].decode("utf-8").split("\n")
            log.info(f"Output: {output}")
            i = 7
            while True:
                try:
                    output3 = output[i].split()
                    decryptSTATUS.append(output3[1])
                    decryptSTATUS.append(output3[3])
                    i += 1
                except Exception:
                    break
            log.info(decryptSTATUS)
            buttons = [self.radioButton, self.radioButton_2,
                       self.radioButton_3, self.radioButton_4,
                       self.radioButton_5, self.radioButton_6,
                       self.radioButton_7]

            self.selectedDRIVE = ''

            # Displays the encryption status of a drive
            def STATUSCHECK(i):
                self.selectedDRIVE = i
                index = decryptSTATUS.index(i)
                status = index + 1
                if decryptSTATUS[status] == 'FullyDecrypted':
                    self.label_4.setText('FullyDecrypted')
                    self.label_4.setStyleSheet('Color: red')
                else:
                    self.label_4.setText('Encrypted')
                    self.label_4.setStyleSheet('Color: green')

            driveLETTER = []

            def cancel_button():
                self.close()

            # Assigns buttons to commands
            self.radioButton.toggled.connect(lambda:
                                             STATUSCHECK(driveLETTER[0]))
            self.radioButton_2.toggled.connect(lambda:
                                               STATUSCHECK(driveLETTER[1]))
            self.radioButton_3.toggled.connect(lambda:
                                               STATUSCHECK(driveLETTER[2]))
            self.radioButton_4.toggled.connect(lambda:
                                               STATUSCHECK(driveLETTER[3]))
            self.radioButton_5.toggled.connect(lambda:
                                               STATUSCHECK(driveLETTER[4]))
            self.radioButton_6.toggled.connect(lambda:
                                               STATUSCHECK(driveLETTER[5]))
            self.enblBIT.clicked.connect(lambda: NewThread(ENCRYPT, False, "Encrypting Drive", self.selectedDRIVE))
            self.cancelbutton.clicked.connect(cancel_button)

            # NOTE: This will provide an error saying "C: drive cannot be 
            # found in index" if not run as Administrator
            # Sets default status check to the C: Drive
            try:
                STATUSCHECK("C:")
            except Exception:
                STATUSCHECK("c:")

            # adds the drive letters to the available radio buttons
            i = 0
            x = 0
            while True:
                try:
                    buttons[i].setText(decryptSTATUS[x])
                    driveLETTER.append(decryptSTATUS[x])
                    x += 2
                    i += 1
                    if x == len(decryptSTATUS):
                        while i != len(buttons):
                            buttons[i].setText('<No Drive Found>')
                            buttons[i].setEnabled(False)
                            i += 1
                    else:
                        continue
                except Exception:
                    break

            # Sets the C: Drive as the default choice
            i = 0
            while i < len(buttons):
                if buttons[i].text() == "C:":
                    buttons[i].setChecked(True)
                i += 1

        def begin(self):
            super(bitRUN, self).exec_()

    b = bitRUN()
    NewThread(b.begin, False, "Bitlocker Drive Encryption")


def Configure_Browsers():
    def browserCONF():
        log.info('Configuring browser...')
        # def cptree(src, dst, symlinks=False, ignore=None):
        #    for item in os.listdir(src):
        #        s = os.path.join(src, item)
        #        d = os.path.join(dst, item)
        #    if os.path.isdir(s):
        #        shutil.copytree(s, d, symlinks, ignore)
        #    else:
        #        shutil.copy2(s, d)
        try:
            stdout, _ = sub.Popen(["powershell", "& {$env:UserName}"], stdout=sub.PIPE).communicate()
            output = stdout.decode("utf-8").split("\r\n")
            # shutil.rmtree(r'%appdata%\Mozilla\Extensions')
            rmv_folder = 'C:\\Users\\' + str(output[0]) + '\\AppData\\Roaming\\Mozilla\\Firefox'
            shutil.rmtree(rmv_folder)
            # shutil.rmtree(r'%appdata%\Mozilla\SystemExtensionsDev')
        except Exception as e:
            log.debug('Error caught: ' + str(e))
        # copy_tree('../configurations/Win_Mozilla/Extensions', 'C:/')
        # copy_tree('../configurations/Win_Mozilla/Firefox', 'C:/')
        # copy_tree('../configurations/Win_Mozilla/SystemExtensionsDev', 'C:/')
        shutil.copytree('../configurations/Win_Mozilla/Extensions',
                        r'%appdata%\Mozilla\Extensions')
        shutil.copytree('../configurations/Win_Mozilla/Firefox',
                        r'%appdata%\Mozilla\Firefox')
        shutil.copytree('../configurations/Win_Mozilla/SystemExtensionsDev',
                        r'%appdata%\Mozilla\SystemExtensionsDev')
        log.info('Firefox has been configured')
    NewThread(browserCONF, False, "Configuring Browsers")


def addusr():
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
                    log.info('This user will be an admin')
                    self.adminyn = 'y'

            def adminn(selected):
                if selected:
                    log.info('This user will NOT be an admin')
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
                        f"User {username} has been successfully "
                        "added to system.")
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.close()

                if self.adminyn == 'y':
                    log.info('This user will be an admin')
                    if Check_Password(self.Password1_input.text(),
                                       self.Password2_input.text()):
                        command = f"$nusnm = '{username}'" \
                              f"\n$nuspss = ConvertTo-SecureString '{passwd}' -AsPlainText -Force" \
                              "\nNew-LocalUser -Name $nusnm -Password $nuspss"\
                              "\nAdd-LocalGroupMember -Group 'Administrators' -Member $nusnm"
                        sub.Popen(f"powershell {command}")
                        log.info(f"User {username} has been successfully added!")
                        completedPOP()
                elif self.adminyn == 'n':
                    log.info('This user will not be an admin')
                    if Check_Password(self.Password1_input.text(),
                                      self.Password2_input.text()):
                        command = f"$nusnm = '{username}'" \
                              f"\n$nuspss = ConvertTo-SecureString '{passwd}' -AsPlainText -Force" \
                              "\nNew-LocalUser -Name $nusnm -Password $nuspss"
                        sub.Popen(f"powershell {command}")
                        log.info(f"User {username} has been successfully added!")
                        completedPOP()

            def cancel_button():
                self.close()

            self.Confirm_button.clicked.connect(lambda: NewThread(CONFIRM, False, "Adding User"))
            self.Cancel_button.clicked.connect(cancel_button)

        def begin(self):
            super(add_user_to_system, self).exec_()

    auts = add_user_to_system()
    NewThread(auts.begin, False, "Add User To System")


def remusr():
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

            listo_names = Find_Names()

            for _, name in enumerate(listo_names):
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
                    log.info('no username entered')
                    ERROR_NO_USER = QMessageBox()
                    ERROR_NO_USER.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER.setText(
                        'No username was entered. No user was removed.')
                    ERROR_NO_USER.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER.exec_()
                elif username not in listo_names:
                    log.info('User not found')
                    ERROR_NO_USER_FOUND = QMessageBox()
                    ERROR_NO_USER_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER_FOUND.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER_FOUND.setText(
                        'User was not found on system. No user was removed.')
                    ERROR_NO_USER_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER_FOUND.exec_()
                else:
                    sub.Popen(["powershell", f"net user {username} /DELETE"])
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
                    log.info('Removing user...')
                    removal()
                elif x == QMessageBox.No:
                    log.info('Cancelling...')

            def cancel_button():
                self.close()

            self.Cancel_button.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())

        def begin(self):
            super(remove_user_from_system, self).exec_()

    rufg = remove_user_from_system()
    NewThread(rufg.begin, False, "Remove User From System")


def addgrutosys():
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
                    HEY.setText("Hey! Your passwords do not match!")
                    HEY.setIcon(QMessageBox.Critical)
                    HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    HEY.exec_()
                else:
                    sub.Popen(f"net localgroup {self.group_name_input.text()} /add")

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


def remgrufrosys():
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
                        f"Group {group_name} has successfully been removed from the system.")
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
                    log.info('Group not found')
                    ERROR_GROUP_NOT_FOUND = QMessageBox()
                    ERROR_GROUP_NOT_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_GROUP_NOT_FOUND.setWindowTitle('Hey! Listen!')
                    ERROR_GROUP_NOT_FOUND.setText(
                        'Group was not found on system. No group was removed.')
                    ERROR_GROUP_NOT_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_GROUP_NOT_FOUND.exec_()
                else:
                    # Executes command.
                    sub.Popen(f"powershell net localgroup {group_name} /DELETE")
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


def addusrtogru():
    class add_user_to_group(QDialog, Ui_user_group_list_modifiers):
        def __init__(self, parent=None):
            super(add_user_to_group, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(790, 419)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('Add User to Group')
            self.Title_label.setText('Add User to Group')
            self.Name_Input_Label1.setText('User to add to group:')
            self.Name_Input_Label2.setText('Group to add User to:')
            self.list_label1.setText('Current Users:')
            self.list_label2.setText('Current Groups w/ Users:')

            def completedPOP(username, group_name):
                COMPLETE = QMessageBox()
                COMPLETE.setIcon(QMessageBox.Question)
                COMPLETE.setWindowTitle('Hey! Listen!')
                COMPLETE.setText(f"User {username} has been successfully "
                                 "added to group {group_name}")
                COMPLETE.setStandardButtons(QMessageBox.Close)
                COMPLETE.exec_()
                self.__init__()

            t = Timer()
            t.start()
            list_of_names = Find_Names()
            group_accounts, list_of_groups = Find_Groups(True)
            t.stop()

            for _, name in enumerate(list_of_names):
                QListWidgetItem(name, self.listWidget)

            group_tree = self.treeWidget

            for _, group in enumerate(list_of_groups):
                c1 = QTreeWidgetItem(group_tree, [str(group)])
                e = group_accounts.get(group)
                for _, i3 in enumerate(e):
                    QTreeWidgetItem(c1, [str(i3)])

            def run_add_user_to_group():
                user_to_add = self.Name_Input.text()
                group_to_add_user_to = self.Name_Input_2.text()
                log.debug(user_to_add)
                log.debug(group_to_add_user_to)
                if " " in user_to_add:
                    Hey = QMessageBox()
                    Hey.setWindowTitle('Hey! Listen!')
                    Hey.setText('Hey! You cant have spaces in the Username!')
                    Hey.setIcon(QMessageBox.Critical)
                    Hey.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    Hey.exec_()
                else:
                    command = f"net localgroup {group_to_add_user_to} {user_to_add} /add"
                    sub.Popen(f"powershell {command}")
                    completedPOP(user_to_add, group_to_add_user_to)

            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    log.info('Adding User to Group...')
                    run_add_user_to_group()
                elif x == QMessageBox.No:
                    log.info('Cancelling...')

            def cancel_button():
                self.close()

            self.Cancel_button_2.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())

        def begin(self):
            super(add_user_to_group, self).exec_()

    autg = add_user_to_group()
    NewThread(autg.begin, False, "Add User To Group")


def remusrfrogru():
    class remove_user_from_group(QDialog, Ui_user_group_list_modifiers):
        def __init__(self, parent=None):
            super(remove_user_from_group, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cups2.png'))
            self.setFixedSize(790, 419)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('Remove User from Group')
            self.Title_label.setText('Remove User from Group')
            self.Name_Input_Label1.setText('User to remove from a group:')
            self.Name_Input_Label2.setText('Group to remove User from:')
            self.list_label1.setText('Current Users:')
            self.list_label2.setText('Current Groups w/ Users:')

            def completedPOP(username, group_name):
                COMPLETE = QMessageBox()
                COMPLETE.setIcon(QMessageBox.Question)
                COMPLETE.setWindowTitle('Hey! Listen!')
                COMPLETE.setText(f"User {username} has been successfully "
                                 "removed from group {group_name}")
                COMPLETE.setStandardButtons(QMessageBox.Close)
                COMPLETE.exec_()
                self.__init__()

            def run_remove_user_from_group():
                user_to_remove = self.Name_Input.text()
                group_to_remove_user_from = self.Name_Input_2.text()
                if " " in user_to_remove:
                    Hey = QMessageBox()
                    Hey.setWindowTitle('Hey! Listen!')
                    Hey.setText('Hey! You cant have spaces in the Username!')
                    Hey.setIcon(QMessageBox.Critical)
                    Hey.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    Hey.exec_()
                else:
                    command = f"net localgroup {group_to_remove_user_from} {user_to_remove} /delete"
                    sub.Popen('powershell', f"& {command}")
                    completedPOP(user_to_remove, group_to_remove_user_from)

            list_of_names = Find_Names()
            group_accounts, list_of_groups = Find_Groups(True)

            for i in range(0, len(list_of_names)):
                QListWidgetItem(list_of_names[i], self.listWidget)

            group_tree = self.treeWidget

            for i2 in range(0, len(list_of_groups)):
                c1 = QTreeWidgetItem(group_tree, [str(list_of_groups[i2])])
                log = list_of_groups[i2]
                e = group_accounts.get(log)
                for i3 in range(0, len(e)):
                    QTreeWidgetItem(c1, [str(e[i3])])

            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    log.info('Removing User from Group...')
                    run_remove_user_from_group()
                elif x == QMessageBox.No:
                    log.info('Cancelling...')

            def cancel_button():
                self.close()

        def begin(self):
            super(remove_user_from_group, self).exec_()

    rufg = remove_user_from_group()
    NewThread(rufg.begin, False, "Remove User From Group")


def lslocausrs():
    # TODO: make it so that it splits between normal users and Administrators
    class list_local_users(QDialog, Ui_rmvusrogru):
        def __init__(self, parent=None):
            super(list_local_users, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(302, 389)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('List Of Current Users On System')

            def cancel_button():
                self.close()

            self.Cancel_button.setGeometry(200, 349, 91, 31)
            self.Cancel_button.setText('Close')
            self.Cancel_button.clicked.connect(cancel_button)
            self.Name_Input.hide()
            self.Confirm_button.hide()
            t = Timer()
            t.start()
            list_of_names = Find_Names()
            t.stop()
            for _, name in enumerate(list_of_names):
                QListWidgetItem(name, self.listOFnames)

        def begin(self):
            super(list_local_users, self).exec_()

    llu = list_local_users()
    NewThread(llu.begin, False, "List Local Users")


def lslocagrus():
    class list_local_groups(QDialog, Ui_rmvusrogru):
        def __init__(self, parent=None):
            super(list_local_groups, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(302, 389)
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            self.setWindowTitle('List Of Current Groups On System')

            _, list_of_groups = Find_Groups(False)

            for _, group in enumerate(list_of_groups):
                QListWidgetItem(group, self.listOFnames)

            def cancel_button():
                self.close()

            self.Cancel_button.setGeometry(200, 349, 91, 31)
            self.Cancel_button.setText('Close')
            self.Cancel_button.clicked.connect(cancel_button)
            self.Name_Input.hide()
            self.Confirm_button.hide()
        def begin(self):
            super(list_local_groups, self).exec_()

    llg = list_local_groups()
    NewThread(llg.begin, False, "List Local Groups")


def lsmemofgru():
    pass


def lsgrusanusrin():
    pass


def chngpasswdofall():
    class change_password_for_all(QDialog, Ui_chngpass):
        def __init__(self, parent=None):
            super(change_password_for_all, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setupUi(self)
            self.EXECUTE()

        def EXECUTE(self):
            def findnames():
                names = []
                try:
                    log.info('Detecting Users On System...')
                    # Local users are added to a list of names
                    output = sub.run("powershell net localgroup users".split(),
                                     stdout=sub.PIPE, check=True, text=True)
                    output = output.stdout.split("\n")
                    n = []
                    for i in range(6, len(output) - 3):
                        n.append(output[i])
                    a = []
                    for _, i in enumerate(n):
                        x = i.split('\r')
                        a.append(x)
                    for _, i in enumerate(a):
                        x = i[0]
                        names.append(x)
                    # Local Administrators are added to list of names
                    output = sub.run("powershell net localgroup "
                                     "administrators".split(), stdout=sub.PIPE,
                                     text=True, check=True)
                    output = output.stdout.split("\n")
                    n2 = []
                    for i in range(6, len(output) - 3):
                        n2.append(output[i])
                    a2 = []
                    for _, i in enumerate(n2):
                        x = i.split("\r")
                        a2.append(x)
                    for _, i in enumerate(a2):
                        x = i[0]
                        names.append(x)

                    # Removal of current user from list of names (This is so
                    # the current user does not get it's password changed.
                    stdout, _ = sub.Popen(["powershell", "& {$env:UserName}"], stdout=sub.PIPE).communicate()
                    output = stdout.decode("utf-8").split("\r\n")
                    for n, i in enumerate(names):
                        if output[0] == i:
                            names.pop(i)
                        if n == len(names):
                            break
                    log.info('The following list are all current users and admins on this system')
                    log.info(names)
                    return names
                except Exception as e:
                    log.debug(f"Index error has occured. exception was "
                              "caught: {str(e))}")
                    log.debug(names)
                    return names

            x = Find_Names()

            def completedPOP():
                COMPLETE = QMessageBox()
                COMPLETE.setIcon(QMessageBox.Question)
                COMPLETE.setWindowTitle('Hey! Listen!')
                COMPLETE.setText("Passwords for all users have been "
                                 "successfully changed.")
                COMPLETE.setStandardButtons(QMessageBox.Close)
                COMPLETE.exec_()
                self.close()

            def RUN(names):
                if Check_Password(self.passwd.text(), self.pass_verify.text()):
                    for _, name in enumerate(names):
                        command = f"$Password = ConvertTo-SecureString"
                        f" '{self.passwd.text()}' -AsPlainText -Force"
                        f"$Username = Get-LocalUser -Name '{name}'"
                        "$Username | Set-LocalUser -Password $Password"
                        sub.Popen(f"powershell {command}", stdout=sub.PIPE)
                        log.info(f"User {name}'s password has been"
                                 " successfully changed.")
                    completedPOP()

            self.chngpass_button.clicked.connect(lambda:
                                                 NewThread(
                                                     RUN,
                                                     False,
                                                     "Changing_User_Passwords",
                                                     x))

        def begin(self):
            super(change_password_for_all, self).exec_()

    c = change_password_for_all()
    NewThread(c.begin, False, "Change_Password_Dialog")
