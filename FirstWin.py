# -*- coding: utf-8 -*-

import sys
#from PyQt5.QtWidgets import  QDesktopWidget,QTreeWidgetItem,QTreeWidget,QFormLayout,QFontDialog,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QApplication,QWidget,QMenu,QMainWindow, qApp, QAction,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from TableBasicCls import TableBasic 
from lineEditCls import lineEditDemo 
from TreeWidgetDemoCls import TreeWidgetDemo 
from GridFormExampleCls import GridFormExample 
# 1. [done] add menu bar ,add several actions
# 2. [done]add lineedit dialog (qt04_lineEdit01.py)
# 2. [done]add openfile dialog (qt04_QFileDialog.py)
# 3. add table monitor, open excel/csv file--> show data in table view --> export file
# 4. [done]plot in table view (pyecharts)
# 5. split ui and logic (engine / UI / frame)
# 6. 用qtdesigner改写
# 7. 用element ui 改写

class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontButton  = QPushButton("choose font")
        self.fontButton.clicked.connect(self.getFont)
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
        
        central = QWidget()
        self.setCentralWidget(central)
        #main_layout= QGridLayout()
        h_layout=QHBoxLayout()
        treeElem=TreeWidgetDemo()
        tableElem= TableBasic()
        gridFormElem=GridFormExample()
        lineEditElem= lineEditDemo()
        h_layout.addWidget(treeElem)
        h_layout.addWidget(tableElem)
        h2_layout=QHBoxLayout()
        h2_layout.addWidget(gridFormElem)
        h2_layout.addWidget(lineEditElem)
        v_layout=QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h2_layout)
        self.centralWidget().setLayout(v_layout)
        
#        positions = [(i,j) for i in range(2) for j in range(2)] 
#        for position in positions:
#            aa=TreeWidgetDemo()
#            main_layout.addWidget(aa,*position)
        self.initMenu()
        self.show()
        #self.center()
    
    def initMenu(self):
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

        self.lineEditDemo=lineEditDemo()
        lineAct=QAction(QIcon("exit.png"),'&LineEdit',self)
        lineAct.setShortcut('Ctrl+E')
        lineAct.setStatusTip("line edit demo")
        dialogMenu.addAction(lineAct)
        lineAct.triggered.connect(self.lineEditDemo.show)

        toolMenu=menubar.addMenu("Tool")
        toolMenu.addAction('spider')
        toolMenu.addAction('stock')
        toolMenu.addAction('qihuo')
        toolMenu.addAction('futu')

        #self.setGeometry(50,50,800,550)
        self.setWindowTitle('vigar QT 框架')
        #self.resize(800,600)
        
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
            
    def center(self):  
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()        
        self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)  

if __name__ == '__main__':
    app= QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
