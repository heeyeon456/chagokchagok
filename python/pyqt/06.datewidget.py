from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import sys

class MyDlg:
    def __init__(self):
        self.dlg = loadUi('c.ui')
        self._initDate()
        self._initEvent()
        self.dlg.show()

    def _initDate(self):
        dt = QDate.currentDate()
        self.dlg.dateEdit.setDate(dt)
    def _initEvent(self):
        self.dlg.pushButton.clicked.connect( self.fn )
    def fn(self):
        #self.dlg.dateEdit.setDate(QDate(2020,11,12))
        dt = self.dlg.dateEdit.date()
        print( dt.year(), dt.month(), dt.day() )

app = QApplication(sys.argv)
my = MyDlg()
app.exec()
