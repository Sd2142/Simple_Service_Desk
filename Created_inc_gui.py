# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Created_inc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Created_inc(object):
    def setupUi(self, Created_inc):
        Created_inc.setObjectName("Created_inc")
        Created_inc.setEnabled(True)
        Created_inc.resize(465, 310)
        Created_inc.setMinimumSize(QtCore.QSize(465, 310))
        Created_inc.setMaximumSize(QtCore.QSize(465, 310))
        self.centralwidget = QtWidgets.QWidget(Created_inc)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 30, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 0, 20, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 60, 271, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 0, 271, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 90, 271, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 341, 51))
        self.label_3.setObjectName("label_3")
        Created_inc.setCentralWidget(self.centralwidget)

        self.retranslateUi(Created_inc)
        QtCore.QMetaObject.connectSlotsByName(Created_inc)

    def retranslateUi(self, Created_inc):
        _translate = QtCore.QCoreApplication.translate
        Created_inc.setWindowTitle(_translate("Created_inc", "MainWindow"))
        self.label.setText(_translate("Created_inc", "Статус обращения:"))
        self.comboBox.setItemText(0, _translate("Created_inc", "Не работает принтер"))
        self.comboBox.setItemText(1, _translate("Created_inc", "Не работает ПК"))
        self.comboBox.setItemText(2, _translate("Created_inc", "Не работает почта"))
        self.comboBox.setItemText(3, _translate("Created_inc", "Прочее -> См подробное описание"))
        self.label_2.setText(_translate("Created_inc", "Тема обращения:"))
        self.label_4.setText(_translate("Created_inc", "Подробное описание:"))
        self.label_5.setText(_translate("Created_inc", "Клиент:"))
        self.pushButton.setText(_translate("Created_inc", "Создать \n"
"обращение!"))
        self.lineEdit_3.setText(_translate("Created_inc", "Назначено"))
        self.label_3.setText(_translate("Created_inc", ""))
