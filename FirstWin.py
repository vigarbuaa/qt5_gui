# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QFontDialog,QLabel,QPushButton,QVBoxLayout, QApplication,QWidget,QMenu,QMainWindow, qApp, QAction
from PyQt5.QtGui import QIcon

# 1. [done] add menu bar ,add several actions
# 2. add openfile dialog (qt04_QFileDialog.py)
# 3. add table monitor, open excel/csv file--> show data in table view --> export file
# 4. plot in table view(pyecharts)
# 5. plot in table view(pyecharts)

class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontButton  = QPushButton("choose font")
        self.fontButton .clicked.connect(self.getFont)
        layout.addWidget(self.fontButton )
        self.fontLineEdit  = QLabel("Hello,测试字体例子")
        layout.addWidget(self.fontLineEdit )
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog 例子")
        
    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(font)
            
########################################################################
class lineEditDemo(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,parent=None):
        """Constructor"""
        super(lineEditDemo,self).__init__(parent)
    
    def initUI(self):
        self.setwindowtitle("QLineEdit example")
        flo=QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit( )
        pPasswordEchoOnEditLineEdit = QLineEdit()

        flo.addRow("Normal", pNormalLineEdit)
        flo.addRow("NoEcho", pNoEchoLineEdit)
        flo.addRow("Password", pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)
        
        pNormalLineEdit.setPlaceholderText("Normal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

    # 设置显示效果
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
                            
        self.setLayout(flo)
   
########################################################################
class Example(QMainWindow):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def printImportLog(self):
        """"""
        print("import mail logic runing")
   
    #----------------------------------------------------------------------
    def newActionFunc(self):
        """"""
        print("new Action pressed")
     
    #----------------------------------------------------------------------
    def toggleMenu(self,state):
        """"""
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
        
    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")
        
        exitAct=QAction(QIcon("exit.png"),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Exit Application")
        exitAct.triggered.connect(qApp.quit)
        
        menubar = self.menuBar()
        
        impMenu=QMenu("Import",self)
        impAct= QAction('import mail',self)
        impAct.triggered.connect(self.printImportLog)
        impMenu.addAction(impAct)
        
        newAct=QAction("New",self)
        newAct.triggered.connect(self.newActionFunc)

        viewStatAct=QAction("view statusBar",self,checkable=True)
        viewStatAct.setStatusTip("view status bar ...")
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        fileMenu=menubar.addMenu("File")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(viewStatAct)
        fileMenu.addAction(exitAct)
        
        dialogMenu=menubar.addMenu("Dialog")
        dialogMenu.addAction("file")
        dialogMenu.addAction("color")
        
        self.fontSelectDemo=FontDialogDemo()
        fontAct=QAction(QIcon("exit.png"),'&Font',self)
        fontAct.setShortcut('Ctrl+D')
        fontAct.setStatusTip("font dialog demo")
        dialogMenu.addAction(fontAct)
        fontAct.triggered.connect(self.fontSelectDemo.show)

        toolMenu=menubar.addMenu("Tool")
        toolMenu.addAction('spider')
        toolMenu.addAction('stock')
        toolMenu.addAction('qihuo')
        toolMenu.addAction('futu')

        self.setGeometry(300,300,800,150)
        self.setWindowTitle('vigar QT 框架')
        self.show()
        
    #---------------pop up menu definition-------------------------------------------------------
    def contextMenuEvent(self,event):
        """"""
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app= QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
