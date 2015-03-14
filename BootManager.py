#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a bit
more complicated window layout using
the QtGui.QGridLayout manager. 

theme: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
import img

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        name = QtGui.QLabel('NAME')
        theme = QtGui.QLabel('THEME')
   	button = QtGui.QPushButton('SUBMIT')

        self.nameEdit = QtGui.QLineEdit()
        themeEdit = QtGui.QLineEdit()
   
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(theme, 2, 0)
        grid.addWidget(themeEdit, 2, 1)

        grid.addWidget(button, 3, 0,1,2)
      	
        
	button.clicked.connect(self.buttonClicked)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('BootManager')    
        self.show()
        
    def buttonClicked(self):
	text=str(self.nameEdit.text())
	img.runscript(text)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
