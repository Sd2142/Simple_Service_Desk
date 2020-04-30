import datetime
import sqlite3 as sql
import sys
import os
from PyQt5 import QtWidgets
from Created_inc_gui import Ui_Created_inc

###Получаем Дату и Время для БД
date = datetime.datetime.now().replace(second=0, microsecond=0)
SQL_date = date.strftime("%Y-%m-%d %H:%M:%S")
SQL_deadline = date.strftime("%Y-%m-%d %H:%M:%S")
###Получаем Имя инициатора
cfg = open('config.cfg')
UserName = str(cfg.read())
cfg.close()
###Получаем Адрес инициатора
cfg1 = open("config2.cfg", "r", encoding="utf-8")
AdresS = str(cfg1.read())
cfg.close()
class mywindow(QtWidgets.QMainWindow):
	def __init__(self):#Инициализация всех кнопок
		super(mywindow, self).__init__()
		self.ui = Ui_Created_inc()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.Create_inc)
		self.ui.lineEdit_2.setText(UserName)
		self.ui.comboBox.setObjectName("comboBox")
		self.ui.label_3.text()
	def Create_inc(self):
		#Naznachennoe_lico
		con = sql.connect('DataBaseFolder/Python_bd_for_ayth.db')
		with con:
			cur = con.cursor()
			Description = self.ui.plainTextEdit.toPlainText()
			Status = self.ui.lineEdit_3.text()
			Theme = self.ui.comboBox.currentText()
			Client = self.ui.lineEdit_2.text()
			Adres = str(AdresS)
			Deadline = ('SLA/OLA_Date')
			DataCreated = SQL_date
			Comment = str('')
			Naznachennoe_lico = str("Исполнитель отсутствует")
			cur.execute(f"INSERT INTO `All_inc` VALUES ('{Status}', '{Theme}', '{Client}', '{Naznachennoe_lico}', '{Description}', '{Adres}', '{DataCreated}', '{Deadline}', '{Comment}')")
			#Получаем данные из бд для проверки
			cur.execute("SELECT * FROM `All_inc`")
			rows = cur.fetchall()
			for row in rows:
				print(row[0],'|', row[1],'|', row[2],'|', row[3],'|', row[4],'|', row[5],'|', row[6],'|', row[7],'|', row[8])
			con.commit()
			cur.close()
		self.ui.label_3.setText('Заявка успешно создана')
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.setStyle('Fusion')
sys.exit(app.exec())
