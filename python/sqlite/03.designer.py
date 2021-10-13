from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyDlg:
    def __init__(self):
        # xml 정보를 통해 객체 생성
        # dialog 객체 참조
        self.dlg = loadUi('a.ui')
        self.dlg.pushButton.clicked.connect( self.fn )
        self.dlg.show()
    def fn(self):
        #self.dlg.lineEdit.setText("코리아")
        #print('click...')
        s = self.dlg.lineEdit.text()
        print(s)
app = QApplication(sys.argv)
my = MyDlg()
app.exec()
print('hello')
