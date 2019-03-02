# -*- coding: utf-8 -*- 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from emailEngine import *
from engine import EventEngine
from utility import  *

class TableBasic( QWidget ):
         
	def __init__(self):
		super().__init__()
		self.event_engine = EventEngine()
		self.initData()
		self.initUI()
		date_str=todayDateStr()	
		self.backup_dir= "./_backup_attach/"+date_str
		print("[init]: " + self.backup_dir)
		# self.buttonlist=[]
				
	#----------------------------------------------------------------------
	def initData(self):
		""""""
		config= load_json("mail.json")
		self.recv_server = EmailEngine(config['receive_mail'],config['receive_passwd'],self.event_engine)
		#self.fr_server = EmailEngine(config['fr_mail'],config['fr_passwd'],self.event_engine)
		self.fr_server=zmail.server(config['fr_mail'],config['fr_passwd'],smtp_host='192.168.102.207',pop_host='192.168.102.207',smtp_ssl=False)
		self.mailHeaders=self.recv_server.getMailHeader(1100,1120)
#		self.event_engine.register('forward_mail', self.processForward)
		
	#----------------------------------------------------------------------
		
	def initUI(self):
		self.setWindowTitle("邮件转发例子")
		self.resize(500,300)
		conLayout = QHBoxLayout()
		self.tableWidget= QTableWidget()
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(5)
		conLayout.addWidget(self.tableWidget)
				 
		self.tableWidget.setHorizontalHeaderLabels(['ID','时间','发件人','标题','--'])  
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		i=0
		for mail in self.mailHeaders:
			print("mailid: " + str(mail.mail_id))
			newItem = QTableWidgetItem(str(mail.mail_id)) 
			self.tableWidget.setItem(i, 0, newItem)

			newItem = QTableWidgetItem(mail.time_str) 
			self.tableWidget.setItem(i, 1, newItem)
		  
			newItem = QTableWidgetItem(mail.sender)
			self.tableWidget.setItem(i, 2, newItem) 
		  
			newItem = QTableWidgetItem(mail.subject)
			self.tableWidget.setItem(i, 3, newItem)
			
			send_button= QPushButton("转发")
			self.tableWidget.setCellWidget(i,4,send_button)
			send_button.setObjectName("btn_"+str(mail.mail_id))
			print("!!!" + send_button.objectName())
			#self.buttonlist.append(send_button)
			send_button.clicked.connect(self.resend_mail)
			i=i+1
		
		self.setLayout(conLayout)
		
	def resend_mail(self):
		sender=self.sender()
		#print()
		print("[obj_name]:" + sender.objectName())
		mail_id=str( sender.objectName()).split("_")[1]
		elem = self.recv_server.getMailById(mail_id)
		print(elem.__dict__.keys)		
		print(elem['id'],elem['from'], elem['date'], elem['subject'])
		#self.fr_server.sendMail('vigarcheck@bctto.me', elem['subject'], elem['content'])
		#self.fr_server.sendMail('qufw@xczdadao.com', elem['subject'], '做一个测试试一下')
		#self.fr_server.send_mail('baidu@xczdadao.com',{'subject':elem['subject'],'content_text':'aaabbbcc'})
		self.recv_server.sendMail('qufw@htdadao.net', elem['subject'], '做一个测试试一下')
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = TableBasic()
	example.show()
	sys.exit(app.exec_())