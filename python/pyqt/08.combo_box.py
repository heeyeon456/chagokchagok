from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyDlg:
    def __init__(self):
        self.dlg = loadUi('d.ui')
        self.dlg.pushButton.clicked.connect( self.fn )
        self.dlg.comboBox.currentIndexChanged.connect(self.fn)
        self.dlg.comboBox.addItems(['회사3', '회사4'])
        self.dlg.comboBox.addItem('회사5',)
        self.dlg.show()
    def fn(self):
        s = self.dlg.comboBox.currentText()
        self.dlg.lineEdit.setText(s)

app = QApplication(sys.argv)
my = MyDlg()
app.exec()
