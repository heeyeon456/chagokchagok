from PyQt5.QtWidgets import *
import sys

class MyDlg:
    def __init__(self):
        self.dlg = QDialog() # 밥상
        self.dlg.setWindowTitle('Title')
        self.dlg.setGeometry(100, 100, 300, 400)
        # 쟁반
        self.vbox = QVBoxLayout() # 위젯 수직 배치 (layoyt)

        # 재료들
        self.dlg.show() # window 띄워짐
        self.btn = QPushButton('클릭')
        # 버튼을 눌렀을 때의 시그널을 주면됨
        self.btn.clicked.connect(self.fn)
        self.lineEdit = QLineEdit()

        # 쟁반에 올림
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.lineEdit)

        # 밥상에 올림
        self.dlg.setLayout(self.vbox)
        self.dlg.show()

    def fn(self):
        print('click...')


app = QApplication(sys.argv)
dlg = MyDlg()

app.exec() # 무한 루프 큐 메모리 감시
# 저 윈도우가 종료되면 큐 메모리 감시를 끝내고 프린트
print('hello')

# pyinstaller *.py -> *.exe # 배포버전 생성가능!


