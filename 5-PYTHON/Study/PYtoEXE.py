# Transformar arquivos .py em .exe
#pyinstaller *archieve_name.py* --onefile

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        super(my_window,self).__init__()
        self.setGeometry(800, 300, 500, 500)
        self.setWindowTitle("Application test")
        self.setWindowIcon(QIcon("Image_for_test.jpg"))
        self.initUI()

    def initUI(self):

        self.lbl_fullvalue = QtWidgets.QLabel(self)
        self.lbl_fullvalue.setText("Digite o Valor inteiro: ")
        self.lbl_fullvalue.move(50,50)

        self.txt_fullvalue = QtWidgets.QLineEdit(self)
        self.txt_fullvalue.move(200,50)

        self.lbl_lack = QtWidgets.QLabel(self)
        self.lbl_lack.setText("Digite o tempo de carencia: ")
        self.lbl_lack.move(50,90)

        self.txt_lack = QtWidgets.QLineEdit(self)
        self.txt_lack.move(200,90)

        # def clicked(self):
        #     print("button clicked")
        #     print(f"Preco cheio: {self.txt_fullvalue.text()}")
        #     print(f"Tempo carencia: {self.txt_lack.text()}")

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Salvar")
        self.btn_save.move(200,130)
        # btn_save.clicked.connect(clicked)

def window():
    
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())

window()