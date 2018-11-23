import sys
import omdb
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

app = QtGui.QApplication(sys.argv)

window = GtGui.QWidget()
window.setGeometry(0,0,500,300)
window.setWindowTitle("Film search")

window.show()