import sys
import urllib.request
import json
import sqlite3

import tmdbConnect

from PyQt5 import QtWidgets, uic, QtGui, QtCore
# from PyQt5.QtWidgets import QWidget, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap

from SqlHelperM import *
movie = SqlHelperM('movie.db')
movie.create_table()
from SqlHelperS import *
serie = SqlHelperS('serie.db')
serie.create_table()



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.conn = None
        self.cursor = None

    # ---------------------
    # Buttons TAB Recherche
    # ---------------------

        self.lineEdit_Search_T3.returnPressed.connect(self.loadData)
        self.pushButton_movie_T3.clicked.connect(self.loadData)
        self.tableWidget_T3.itemSelectionChanged.connect(self.selectionChanged)
        self.pushButton_After_T3.clicked.connect(self.later)
        self.pushButton_Collection_T3.clicked.connect(self.later)

    # ------------------------
    # Buttons TAB Films a voir
    # ------------------------
        self.Viewed()

        self.pushButton_movie_Remove.clicked.connect(self.removeViewed)
        self.tableWidget_M.itemSelectionChanged.connect(self.selectionChangedViewed)
        
    # -------------------------

        self.show()

    # ---------------------
    # TAB Recherche
    # ---------------------

    def loadData(self):
        txt = self.lineEdit_Search_T3.text()
        data = tmdbConnect.movie(txt)

        for idx, d in enumerate(data):
            self.tableWidget_T3.insertRow(idx)
            for column_number, dt in enumerate(d):
                cell = QtWidgets.QTableWidgetItem(str(dt))
                self.tableWidget_T3.setItem(idx, column_number, cell)

        self.header = self.tableWidget_T3.horizontalHeader()
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def later(self):
        row = self.tableWidget_T3.currentRow()
        g = self.tableWidget_T3.item(row, 2).text()
        # g = self.getSelectedMovieId()
        d = tmdbConnect.movieDescription(g)
        title = d[0]
        img = d[3]

        movie.edit(g, title, img)

    def selectionChanged(self):
        row = self.tableWidget_T3.currentRow()
        g = self.tableWidget_T3.item(row, 2).text()
        d = tmdbConnect.movieDescription(g)
        self.label_Title_T3.setText(d[0])
        self.label_Year_T3.setText(d[1])

        if self.label_Description_T3.setText(d[2]) == '':
            print('Pas de description') 
        else:
            self.label_Description_T3.setText(d[2])

        if d[3] == None:
            self.label_Poster_T3.clear()
            self.label_Poster_T3.setText("Pas d'image")
        else:
            url = 'https://image.tmdb.org/t/p/w185/' + d[3]
            data = urllib.request.urlopen(url).read()

            image = QtGui.QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.label_Poster_T3.setPixmap(pixmap)
            self.label_Poster_T3.resize(pixmap.width(),pixmap.height())

    # ------------------------
    # TAB Films a voir
    # ------------------------

    def clearData(self):
        while (self.tableWidget_M.rowCount()>0):
            self.tableWidget_M.removeRow(0)
        self.Viewed()

    def Viewed(self):
        self.conn = sqlite3.connect('movie.db')
        self.cursor = self.conn.cursor()
        g = self.cursor.execute('''SELECT id_tmdb, title, vu FROM movie''')

        self.tableWidget_M.setRowCount(self.cursor.rowcount)

        for idx, d in enumerate(g):
            self.tableWidget_M.insertRow(idx)
            for column_number, vu in enumerate(d):
                cell = QtWidgets.QTableWidgetItem(str(vu))
                self.tableWidget_M.setItem(idx, column_number, cell)

        self.header = self.tableWidget_M.horizontalHeader()
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    
    def selectionChangedViewed(self):
        row = self.tableWidget_M.currentRow()
        g = self.tableWidget_M.item(row, 0).text()


        d = tmdbConnect.movieDescription(g)
        self.label_Title_T2.setText(d[0])
        self.label_Year_T2.setText(d[1])

        

        if self.label_Description_T2.setText(d[2]) == '':
            print('Pas de description') 
        else:
            self.label_Description_T2.setText(d[2])

        if d[3] == None:
            self.label_Poster_T2.clear()
            self.label_Poster_T2.setText("Pas d'image")
        else:
            url = 'https://image.tmdb.org/t/p/w185/' + d[3]
            data = urllib.request.urlopen(url).read()

            image = QtGui.QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.label_Poster_T2.setPixmap(pixmap)
            self.label_Poster_T2.resize(pixmap.width(),pixmap.height())

    def removeViewed(self):
        self.conn = sqlite3.connect('movie.db')
        self.c = self.conn.cursor()

        r = self.tableWidget_M.currentRow()
        row = self.tableWidget_M.item(r, 1).text()
        print(row)
        self.c.execute('''DELETE FROM movie WHERE title = "%s"''' % row)
        # query = "DELETE FROM movie WHERE title = '%s';" % row
        # c.execute(query)
        print('ok')
        self.conn.commit()

        self.clearData()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
