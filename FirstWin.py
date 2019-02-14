# -*- coding: utf-8 -*-

import sys
#from PyQt5.QtWidgets import  QDesktopWidget,QTreeWidgetItem,QTreeWidget,QFormLayout,QFontDialog,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QApplication,QWidget,QMenu,QMainWindow, qApp, QAction,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
# 1. [done] add menu bar ,add several actions
# 2. [done]add lineedit dialog (qt04_lineEdit01.py)
# 2. add openfile dialog (qt04_QFileDialog.py)
# 3. add table monitor, open excel/csv file--> show data in table view --> export file
# 4. plot in table view(pyecharts)
# 5. split ui and logic (engine / UI / frame)
# 6. 用qtdesigner改写
# 7. 用element ui 改写

class TreeWidgetDemo(QMainWindow):   
    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')
        self.tree = QTreeWidget()
    # 设置列数
        self.tree.setColumnCount(2)
    # 设置头的标题
        self.tree.setHeaderLabels(['Key','Value'])
        # 设置根节点
        root= QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setIcon(0,QIcon("./images/root.png"))
        # 设置列宽
        self.tree.setColumnWidth(0, 160)

        ### 设置节点的背景颜色
        #brush_red = QBrush(Qt.red)
        #root.setBackground(0, brush_red) 
        #brush_green = QBrush(Qt.green)
        #root.setBackground(1, brush_green) 

        # 设置子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'ios')
        child1.setIcon(0,QIcon("./images/IOS.png"))
        child1.setCheckState(0, Qt.Checked)

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'')
        child2.setIcon(0,QIcon("./images/android.png"))

        # 设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'android')
        child3.setIcon(0,QIcon("./images/music.png"))

        self.tree.addTopLevelItem(root)
        # 结点全部展开
        self.tree.expandAll()

        self.setCentralWidget(self.tree)  

class TableBasic( QWidget ):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget Basic 例子")
        self.resize(500,300);
        conLayout = QHBoxLayout()
        self.tableWidget= QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        conLayout.addWidget(self.tableWidget )

        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重', '显示图片'])  
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        newItem = QTableWidgetItem("张三")    
        self.tableWidget.setItem(0, 0, newItem)  

        newItem = QTableWidgetItem("男")  
        self.tableWidget.setItem(0, 1, newItem)  

        newItem = QTableWidgetItem("160")  
        self.tableWidget.setItem(0, 2, newItem)   

        newItem = QTableWidgetItem(QIcon("./images/bao1.png"), "背包")
        self.tableWidget.setItem(0, 3, newItem ) 
        self.setLayout(conLayout)

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