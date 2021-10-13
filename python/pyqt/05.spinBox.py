from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyDlg:
    def __init__(self):
        self.dlg = loadUi('b.ui')
        self.dlg.pushButton.clicked.connect( self.fn )
        self.dlg.show()
    def fn(self):
        s1 = self.dlg.spinBox.value()
        s2 = self.dlg.spinBox_2.value()
        self.dlg.lineEdit.setText(f"합: {s1+s2}")


app = QApplication(sys.argv)
my = MyDlg()
app.exec()
