# -*- coding: utf-8 -*-

import sys
#from PyQt5.QtWidgets import  QDesktopWidget,QTreeWidgetItem,QTreeWidget,QFormLayout,QFontDialog,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QApplication,QWidget,QMenu,QMainWindow, qApp, QAction,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# 1. [done] add menu bar ,add several actions
# 2. [done]add lineedit dialog (qt04_lineEdit01.py)
# 2. add openfile dialog (qt04_QFileDialog.py)
# 3. add table monitor, open excel/csv file--> show data in table view --> export file
# 4. plot in table view(pyecharts)
# 5. split ui and logic (engine / UI / frame)
# 6. 用qtdesigner改写
# 7. 用element ui 改写

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
        main_layout= QGridLayout()
        self.centralWidget().setLayout(main_layout)
        positions = [(i,j) for i in range(2) for j in range(2)] 
        for position in positions:
            aa=GridFormExample()
            main_layout.addWidget(aa,*position)
        #self.initMenu()
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
