# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中单元格添加图片例子
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *


########################################################################
class GridFormExample(QWidget):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,parent=None):
        super(GridFormExample, self).__init__(parent)
        self.initUI()

    def initUI(self):            
        titleLabel = QLabel('标题')  
        authorLabel = QLabel('提交人')  
        contentLabel = QLabel('申告内容')  
 
        titleEdit = QLineEdit()  
        authorEdit = QLineEdit()  
        contentEdit = QTextEdit()  
 
        grid = QGridLayout()  
        grid.setSpacing(10)  
 
        grid.addWidget(titleLabel, 1, 0)  
        grid.addWidget(titleEdit, 1, 1)  
  
        grid.addWidget(authorLabel, 2, 0)  
        grid.addWidget(authorEdit, 2, 1)  
  
        grid.addWidget(contentLabel, 3, 0)  
        grid.addWidget(contentEdit, 3, 1, 5, 1)  
          
        self.setLayout(grid)   
        self.setGeometry(300, 300, 350, 300)  
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = TableBasic()  
	example.show()   
	sys.exit(app.exec_())
