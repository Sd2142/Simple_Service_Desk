# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Auth_Form(object):
    def setupUi(self, Auth_Form):
        Auth_Form.setObjectName("Auth_Form")
        Auth_Form.resize(329, 195)
        self.centralwidget = QtWidgets.QWidget(Auth_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(16)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        Auth_Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Auth_Form)
        self.statusbar.setObjectName("statusbar")
        Auth_Form.setStatusBar(self.statusbar)

        self.retranslateUi(Auth_Form)
        QtCore.QMetaObject.connectSlotsByName(Auth_Form)

    def retranslateUi(self, Auth_Form):
        _translate = QtCore.QCoreApplication.translate
        Auth_Form.setWindowTitle(_translate("Auth_Form", "Auth_Form"))
        self.label.setText(_translate("Auth_Form", "Логин:"))
        self.pushButton.setText(_translate("Auth_Form", "Авторизация"))
        self.label_2.setText(_translate("Auth_Form", "Пароль:"))
