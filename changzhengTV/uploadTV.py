# -*- coding: utf-8 -*- 

'''
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
#from engine import EventEngine
# add file selector
########################################################################
class TvInfoItem(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def  initUI(self):
        """"""
        self.layout=QHBoxLayout()
        
        self.file_select_btn=QPushButton("select file")
        self.file_select_btn.setFixedWidth(230)
        self.file_select_btn.clicked.connect(self.getfile)
        self.topicEdit=QLineEdit()
        self.subjectEdit=QLineEdit()
        self.locationEdit=QLineEdit()
        self.keywordsEdit=QLineEdit()
        self.personEdit=QLineEdit()
        self.topicEdit.setPlaceholderText("输入主题")
        self.subjectEdit.setPlaceholderText("输入标题")
        self.locationEdit.setPlaceholderText("输入地点")
        self.keywordsEdit.setPlaceholderText("输入关键词")
        self.personEdit.setPlaceholderText("输入人物")
        
        self.topicClassComBox=QComboBox()
        self.topicClassComBox.addItem("社会新闻")
        self.topicClassComBox.addItem("离退休事务")
        self.topicClassComBox.addItem("职工活动")
        self.topicClassComBox.addItem("国内外展会")
        self.topicClassComBox.setStyleSheet("QComboBox{margin:3px};")
        self.layout.addWidget(self.file_select_btn)
        self.layout.addWidget(self.topicEdit)
        self.layout.addWidget(self.subjectEdit)
        self.layout.addWidget(self.locationEdit)
        self.layout.addWidget(self.keywordsEdit)
        self.layout.addWidget(self.personEdit)
        self.layout.addWidget(self.topicClassComBox)
        self.setLayout(self.layout)
        #self.show()
    def getfile(self):
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
    #self.le.setPixmap(QPixmap(fname))
        self.file_select_btn.setText(fname)
        
class TableBasic( QWidget ):
         
    def __init__(self):
        super().__init__()
        #self.event_engine = EventEngine()
        self.initData()
        self.initUI()
    #----------------------------------------------------------------------
    def initData(self):
        """"""
        #config= load_json("mail.json")
        #self.server = EmailEngine(config['mail'],config['passwd'],self.event_engine)
        #self.mailHeaders=self.server.getMailHeader(1100,1120)
        #self.event_engine.register('forward_mail', self.processForward)
        pass
    #----------------------------------------------------------------------
    def addItem(self):
        item = TvInfoItem()
        self.layout.addWidget(item)
    
    def initUI(self):
        self.setWindowTitle("长征电视台视频上传Demo")
        #self.resize(500,300)
        submit_add_layout= QHBoxLayout()
    
        self.submit_btn=QPushButton("提交申请并上传文件")
        self.add_item_btn=QPushButton("新增文件")
        self.add_item_btn.clicked.connect(self.addItem)
        submit_add_layout.addWidget(self.submit_btn)
        submit_add_layout.addWidget(self.add_item_btn)
        item = TvInfoItem()
        self.layout= QVBoxLayout()
        self.layout.addLayout(submit_add_layout)
        self.layout.addWidget(item)
        self.setLayout(self.layout)
    
        '''
        conLayout = QHBoxLayout()
        self.tableWidget= QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        conLayout.addWidget(self.tableWidget)
                 
        self.tableWidget.setHorizontalHeaderLabels(['文件','主题','标题','地点','关键词','人物','分类','增加文件'])  
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        '''
        
        """
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
            #send_button.clicked.connect(lambda: self.put_for_mail_event(mail.mail_id))
            i=i+1
        """
#        self.setLayout(conLayout)
    def put_for_mail_event(self,mail_id):
        print('aaa'+str(mail_id))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableBasic()  
    example.show()   
    sys.exit(app.exec_())