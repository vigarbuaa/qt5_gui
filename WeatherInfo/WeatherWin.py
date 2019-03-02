# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from WeatherEngine import queryWeatherEngine

########################################################################
class Example(QWidget):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,parent=None):
        """Constructor"""
        super(Example,self).__init__(parent)
        self.weatherEngine= queryWeatherEngine()
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        self.setWindowTitle("查询城市天气")
        self.flo=QFormLayout()
        #self.pNormalLineEdit=QLineEdit()
        self.weatherComBox=QComboBox()
        self.weatherComBox.addItem("北京")
        self.weatherComBox.addItem("天津")
        self.weatherComBox.addItem("上海")
        self.resultText=QTextEdit()
        
        self.horz=QHBoxLayout()
        self.queryBtn= QPushButton("查询")
        self.clearBtn=QPushButton("清除")
        self.horz.addWidget(self.queryBtn)
        self.horz.addWidget(self.clearBtn)
        #self.flo.addRow("Normal",self.pNormalLineEdit)
        self.flo.addRow("城市",self.weatherComBox)
        self.flo.addRow("结果",self.resultText)
        self.flo.addRow('',self.horz)
        self.clearBtn.clicked.connect(self.resultText.clear)
        self.queryBtn.clicked.connect(self.queryWeather)
        
        
        self.setLayout(self.flo)
        self.show()
    #----------------------------------------------------------------------
    def  queryWeather(self):
        cityName= self.weatherComBox.currentText()
        print("debug:cityName " + cityName)
        info = self.weatherEngine.queryWeather(cityName)
        print("debug: " + info)
        self.resultText.setText(info)
            
if __name__ == '__main__':
    app= QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())