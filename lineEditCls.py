# -*- coding: utf-8 -*- 

'''
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *

class lineEditDemo(QWidget):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,parent=None):
        """Constructor"""
        super(lineEditDemo,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLineEdit example")
        self.flo=QFormLayout()
        self.pNormalLineEdit = QLineEdit()
        self.pNoEchoLineEdit = QLineEdit()
        self.pPasswordLineEdit = QLineEdit( )
        self.pPasswordEchoOnEditLineEdit = QLineEdit()
        self.flo.addRow("Normal", self.pNormalLineEdit)
        self.flo.addRow("NoEcho", self.pNoEchoLineEdit)
        self.flo.addRow("Password", self.pPasswordLineEdit)
        self.flo.addRow("PasswordEchoOnEdit", self.pPasswordEchoOnEditLineEdit)
        self.pNormalLineEdit.setPlaceholderText("Normal")
        self.pNoEchoLineEdit.setPlaceholderText("NoEcho")
        self.pPasswordLineEdit.setPlaceholderText("Password")
        self.pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

    # 设置显示效果
        self.pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        self.pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        self.pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.setLayout(self.flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = lineEditDemo()  
    example.show()   
    sys.exit(app.exec_())