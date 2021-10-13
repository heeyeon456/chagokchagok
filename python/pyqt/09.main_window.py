from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class OtherDlg:
    def __init__(self):
        self.dlg = loadUi('mydlg.ui')
        self.dlg.pushButton.clicked.connect( self.closeFn )
        self.dlg.exec() #모달다이라로그... show():모달리스
    def closeFn(self):
        self.dlg.close()

class MyDlg:
    def __init__(self):
        self.dlg = loadUi('main.ui')
        # self.dlg.pushButton.clicked1d.connect( self.fn )
        self.dlg.actiontest1.triggered.connect( self.fn )

        self.dlg.show()
    def fn(self):
        o = OtherDlg() # hold
        s = o.dlg.lineEditChild.text()
        self.dlg.lineEditMain.setText( s )
        print("end....")
app = QApplication(sys.argv)
my = MyDlg()
app.exec()
