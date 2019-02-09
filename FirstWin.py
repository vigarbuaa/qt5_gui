# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMenu,QMainWindow, qApp, QAction
from PyQt5.QtGui import QIcon

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
        
        self.setGeometry(300,300,800,150)
        self.setWindowTitle('simple file menu')
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