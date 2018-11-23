# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import omdb
import urllib
import json
import pprint
from PIL import Image
from io import BytesIO
import os##
#import Image##

apiKey = '582f52b9'
searchTerm = "Sharknado"
#omdb.set_default('apikey',apiKey)
baseurl = "http://www.omdbapi.com/?apikey="+apiKey+"&t="+searchTerm#&t=Sharknado&y=2013&plot=short&r=xml"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.dbSelector = QtWidgets.QComboBox(self.centralwidget)
        self.dbSelector.setObjectName("dbSelector")
        self.dbSelector.addItem("")
        self.dbSelector.addItem("")
        self.gridLayout.addWidget(self.dbSelector, 0, 2, 1, 1)
        self.addWishlist = QtWidgets.QPushButton(self.centralwidget)
        self.addWishlist.setObjectName("addWishlist")
        self.gridLayout.addWidget(self.addWishlist, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoBox = QtWidgets.QListWidget(self.centralwidget)
        self.infoBox.setObjectName("infoBox")
        self.verticalLayout.addWidget(self.infoBox)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.searchBox = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBox.setObjectName("searchBox")
        self.gridLayout.addWidget(self.searchBox, 0, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.viewWishlist = QtWidgets.QPushButton(self.centralwidget)
        self.viewWishlist.setObjectName("viewWishlist")
        self.gridLayout.addWidget(self.viewWishlist, 3, 1, 1, 1)
        self.randomSearch = QtWidgets.QPushButton(self.centralwidget)
        self.randomSearch.setObjectName("randomSearch")
        self.gridLayout.addWidget(self.randomSearch, 1, 0, 1, 1)
        self.pictureFrame = QtWidgets.QFrame(self.centralwidget)
        self.pictureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pictureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pictureFrame.setObjectName("pictureFrame")
        self.gridLayout.addWidget(self.pictureFrame, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        self.menuMovie_Information_Client = QtWidgets.QMenu(self.menubar)
        self.menuMovie_Information_Client.setObjectName("menuMovie_Information_Client")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMovie_Information_Client.menuAction())


        self.searchButton.clicked.connect(self.displaySearch)
        #self.show()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dbSelector.setItemText(0, _translate("MainWindow", "OMDB"))
        self.dbSelector.setItemText(1, _translate("MainWindow", "TMDB"))
        self.addWishlist.setText(_translate("MainWindow", "Add to Wishlist"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.viewWishlist.setText(_translate("MainWindow", "View Wishlist"))
        self.randomSearch.setText(_translate("MainWindow", "I\'m Feeling Lucky"))
        self.menuMovie_Information_Client.setTitle(_translate("MainWindow", "Movie Information Client"))

    # @pyqtSlot()
    def displaySearch(self):
        searchBoxValue = self.searchBox.text()
        self.searchBox.setText("")
        self.infoBox.clear()
        data = urllib.request.urlopen(baseurl).read()
        myJson = json.loads(data)
        #myJson = data.decode('utf-8').replace("'",'"')
        #myJson = json.load(data)
        #print_json(myJson)
        print('- ' * 20)
        #data = json.loads(myJson)
        s = json.dumps(myJson, indent=4, sort_keys=True)
        print(s)
        self.infoBox.addItem(myJson["Title"])
        posterURL = myJson["Poster"]
        response = urllib.request.urlopen(posterURL)
        img = Image.open(BytesIO(response.read()))

        #image = Image.open(img)
        img.show()

        #self.pictureFrame.addItem(myJson[img])


        #self.infoBox.addItem(convertSearch(searchBoxValue))
        # res = omdb.search(searchBoxValue)
        # self.infoBox.clear();
        # for r in res:
        #     self.infoBox.addItem(r["title"])

     
def convertSearch(text):
    return text + " bob "

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

