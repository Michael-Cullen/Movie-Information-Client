import sys
import omdb
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import urllib.request

class App(QMainWindow):
    omdb.set_default('apikey', '582f52b9')
    def __init__(self):
        super().__init__()
        self.title = 'Movie Information Client'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Search', self)
        self.button.move(20,80)
        self.list = QListWidget(self)
        self.list.resize(280,120)
        self.list.move(20,120)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.textbox.setText("")
        combinedRequest = "http://img.omdbapi.com/?apikey=582f52b9&" + textboxValue
        contents = urllib.request.urlopen(combinedRequest).read()
        res = omdb.search(textboxValue)
        self.list.clear();
        for r in res:
            self.list.addItem(r["title"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
