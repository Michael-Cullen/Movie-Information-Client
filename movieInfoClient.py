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
from PIL import Image, ImageQt
#from PIL.ImageQt import ImageQt
from io import BytesIO
import os##
from random import randint
#import Image##

apiKey = '582f52b9'
#searchTerm = "Sharknado"
#omdb.set_default('apikey',apiKey)
#searchUrl = "http://www.omdbapi.com/?apikey="+apiKey+"&t="+searchTerm#&t=Sharknado&y=2013&plot=short&r=xml"

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

        self.pictureFrame = QtWidgets.QLabel(self.centralwidget)
        # self.pictureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.pictureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
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

        #Search function on click
        self.searchButton.clicked.connect(self.displaySearch)

        #Wishlist function on click
        self.addWishlist.clicked.connect(self.addToWishlist)

        #Display wishlist on click
        self.viewWishlist.clicked.connect(self.displayWishlist)

        #I'm feeling lucky button on click
        self.randomSearch.clicked.connect(self.feelingLucky)


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

    	# Search
        searchTerm = self.searchBox.text()
        searchTerm = searchTerm.replace(" ", "_")
        searchUrl = "http://www.omdbapi.com/?apikey="+apiKey+"&t="+searchTerm
        self.searchBox.setText("")
        self.infoBox.clear()

        # Data Processing
        data = urllib.request.urlopen(searchUrl).read()
        myJson = json.loads(data)
        # s = json.dumps(myJson, indent=4, sort_keys=True)
        # print(s)


        # Data storage
        with open('searchItem.json', 'w') as outfile:
        	json.dump(myJson,outfile)


        # Data output
        self.infoBox.addItem(myJson["Title"])
        self.infoBox.addItem(myJson["Year"])
        for rating in myJson["Ratings"]:
        	self.infoBox.addItem(rating["Source"])
        	self.infoBox.addItem(rating["Value"])
        self.infoBox.addItem(myJson["Runtime"])

        # Poster output
        posterURL = myJson["Poster"]
        data = urllib.request.urlopen(posterURL).read()
        qtimg = QtGui.QImage()
        qtimg.loadFromData(data)
        pixmap = QtGui.QPixmap(qtimg)
        self.pictureFrame.setPixmap(pixmap)


    def addToWishlist(self):

    	#load search term data

    	with open("searchItem.json") as f:
    		data = json.load(f)

    	with open("Wishlist.txt", "a") as wishlistFile:
    		wishlistFile.write(data["Title"])
    		wishlistFile.write("\n")
    	#print(data["Title"])
    	# filmTitle = data["Title"]
    	# print(filmTitle)
    	#wishlistFile.write()
    	#wishlistFile.close()

    def displayWishlist(self):

    	self.infoBox.clear()
    	with open("Wishlist.txt") as f:
    		content = f.readlines()

    	content = [x.strip() for x in content]
    	self.infoBox.addItem("Wishlist:")
    	for line in content:
    		self.infoBox.addItem(line)


    def feelingLucky(self):

    	# Identify Random element
    	with open("randomSearch.txt") as f:
    		content = f.readlines()

    	content = [x.strip() for x in content]

    	
    	randNum = randint(0,9)

    	searchTerm = content[randNum]

    	searchTerm = searchTerm.replace(" ", "_")
    	searchUrl = "http://www.omdbapi.com/?apikey="+apiKey+"&t="+searchTerm
    	self.searchBox.setText("")
    	self.infoBox.clear()

    	data = urllib.request.urlopen(searchUrl).read()
    	myJson = json.loads(data)

    	with open('searchItem.json', 'w') as outfile:
    		json.dump(myJson,outfile)

    	self.infoBox.addItem(myJson["Title"])
    	self.infoBox.addItem(myJson["Year"])
    	for rating in myJson["Ratings"]:
    		self.infoBox.addItem(rating["Source"])
    		self.infoBox.addItem(rating["Value"])

    	self.infoBox.addItem(myJson["Runtime"])

    	posterURL = myJson["Poster"]
    	data = urllib.request.urlopen(posterURL).read()
    	qtimg = QtGui.QImage()
    	qtimg.loadFromData(data)
    	pixmap = QtGui.QPixmap(qtimg)
    	self.pictureFrame.setPixmap(pixmap)

    	




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

