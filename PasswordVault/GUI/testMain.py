'''
Created on Jul 26, 2015

@author: Daniel Bruce
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
import PyQt5
import pintDog_ui
from pintDog_ui import Ui_MainWindow

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Ui_MainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
	pass