# -*- coding: utf-8 -*- 

'''
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from emailEngine import *

# add button in this item

class TableBasic( QWidget ):
         
	def __init__(self):
		super().__init__()
		self.initData()
		self.initUI()
	#----------------------------------------------------------------------
	def initData(self):
		""""""
		config= load_json("mail.json")
		self.server = EmailEngine(config['mail'],config['passwd'])
		self.mailHeaders=self.server.getMailHeader()
		
	def initUI(self):
		self.setWindowTitle("QTableWidget 例子")
		self.resize(500,300)
		conLayout = QHBoxLayout()
		self.tableWidget= QTableWidget()
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(4)
		conLayout.addWidget(self.tableWidget)
				 
		self.tableWidget.setHorizontalHeaderLabels(['时间','发件人','标题','--'])  
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		i=0
		for mail in self.mailHeaders:
			print(mail)
			print(mail.__dict__)
			newItem = QTableWidgetItem(mail.time_str)    
			self.tableWidget.setItem(i, 0, newItem)  
		  
			newItem = QTableWidgetItem(mail.sender)  
			self.tableWidget.setItem(i, 1, newItem)  
		  
			newItem = QTableWidgetItem(mail.subject)  
			self.tableWidget.setItem(i, 2, newItem)   
			
			send_button= QPushButton("转发")
			#newItem = QTableWidgetItem(send_button)  
			self.tableWidget.setCellWidget(i,3,send_button)
			#self.tableWidget.setItem(i, 3, newItem)   
			
			i=i+1
		
		#newItem = QTableWidgetItem(QIcon("./images/bao1.png"), "背包")
		#self.tableWidget.setItem(0, 3, newItem ) 
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = TableBasic()  
	example.show()   
	sys.exit(app.exec_())