from PyQt5 import QtWidgets
from auth_gui import Ui_Auth_Form
import sys
import sqlite3 as sql

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_Auth_Form()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.Auth_Connect)

	def Auth_Connect(self):
		file_1 = open("config2.cfg", "w+", encoding="utf-8")# Импортируем имя инициатора из БД в файл конфигурации
		file_2 = open("config.cfg", "w+", encoding="windows-1252")# Импортируем Адрес инициатора из БД в файл конфигурации
		username = self.ui.lineEdit.text()
		password = self.ui.lineEdit_2.text()
		con = sql.connect('DataBaseFolder/Python_bd_for_ayth.db')
		result = con.execute("SELECT * FROM auth_bd WHERE Login = ? AND PWD = ?", (username, password))
		username_for_BD = ("'"+username+"'")
		BD_iz_username = con.execute("SELECT Username FROM auth_bd WHERE Login ="+username_for_BD)
		BD_iz_adress = con.execute("SELECT Adres FROM auth_bd WHERE Login ="+username_for_BD)
		rows = BD_iz_username.fetchall()
		for row in rows:
			UserName = str(row[0])
			file_2.write(str(UserName))
			file_2.close()
		rows_adr = BD_iz_adress.fetchall()
		for row in rows_adr:
			addrgbfsbfdg = str(row[0])
			AddresS = addrgbfsbfdg
			file_1.write(str(AddresS))
			file_1.close()
		if (len(result.fetchall()) > 0):
			from subprocess import call
      call(["python.exe", "Created_inc.py"])
		else:
			self.ui.label_3.setText("Неверный логин или пароль")
		con.close()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.setStyle('Fusion')
sys.exit(app.exec())

exit(0)
