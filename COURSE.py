#!/urs/bin/python3
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from Encoding import *
from main import *


# Класс отвечающий за стартовое окно
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("qt_login.ui", self)
        self.login()

    def login(self):
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_btn.clicked.connect(lambda: self.personal_ac())
        self.registr_btn.clicked.connect(lambda: self.registr())

    def personal_ac(self):
        username = self.line_username.text().strip()
        password = self.line_password.text()
        if check_login(username, password):
            self.line_username.setText('')
            self.line_password.setText('')
            widget.close()
            main()


        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка\t\t\t\t\t")
            error.setText("Введен неверный логин или пароль.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def registr(self):
        self.line_username.setText('')
        self.line_password.setText('')
        widget.setCurrentWidget(new_ac_window)

# Класс отвечающий за окно регистрации
class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        loadUi("qt_registration.ui", self)
        self.registration()

    def registration(self):
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.replay_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_create.clicked.connect(lambda: self.login_window(True))
        self.back_btn.clicked.connect(lambda: self.login_window(False))


    def login_window(self, flag):
        if flag:
            username = self.new_username.text().strip()
            password = self.new_password.text()
            replay_password = self.replay_password.text()
            if password != replay_password:
                error = QMessageBox()
                error.setWindowTitle("Ошибка\t\t\t\t\t")
                error.setText("Пароли не совпадают!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                return False
            registr = check_registr(username, password)
            if registr ==True:
                flag = False
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка\t\t\t\t\t")
                error.setText("Введены неверный данные!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.setDetailedText(" Требования к паролю:\n"
                                      "1) Пароль может состоять из: \n"
                                      "- Латинского алфавита (a-z; A-Z)\n"
                                      "- знаков препинания ('.', '!', '?', ',', '_')\n"
                                      "- цифр (0-9)\n"
                                      "2) Длина пароля должна быть не менее 8 и не более 30\n"
                                      "Требования к логину: \n"
                                      " Длина логина должна быть не менее 2 и не более 50\n\n"
                                      "Примечание: Если все требования выполняются, но программа выдает ошибку. Это значит,"
                                      " что пользователь с таким логином или паролем уже существует.")
                error.exec_()
        if not flag:
            self.new_username.setText('')
            self.new_password.setText('')
            self.replay_password.setText('')
            return widget.setCurrentWidget(login_window)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    new_ac_window = Registration()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login_window)
    widget.addWidget(new_ac_window)
    widget.show()
    sys.exit(app.exec_())