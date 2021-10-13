from PyQt5.QtWidgets import *
import sys

def fn():
    print('click...')


app = QApplication(sys.argv)

# 밥상
dlg = QDialog()
dlg.setWindowTitle('Title')
dlg.setGeometry(100, 100, 300, 400)
# 쟁반
vbox = QVBoxLayout() # 위젯 수직 배치 (layoyt)

# 재료들
dlg.show() # window 띄워짐
btn = QPushButton('클릭')
# 버튼을 눌렀을 때의 시그널을 주면됨
btn.clicked.connect(fn)
lineEdit = QLineEdit()

# 쟁반에 올림
vbox.addWidget(btn)
vbox.addWidget(lineEdit)

# 밥상에 올림
dlg.setLayout(vbox)
dlg.show()

app.exec() # 무한 루프 큐 메모리 감시
# 저 윈도우가 종료되면 큐 메모리 감시를 끝내고 프린트
print('hello')


