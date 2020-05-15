import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi("ilk.ui")
        self.win.bt1.clicked.connect(self.tiklandi)
        self.win.cmb1.currentIndexChanged.connect(self.secim)
        self.win.show()
    def tiklandi(self):
        metin = self.win.txt1.text()
        self.win.cmb1.addItem(metin)
        self.win.cmb1.setCurrentText(metin)

    def secim(self):
        self.win.lblSecim.setText(self.win.cmb1.currentText())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = App()
    sys.exit(app.exec_())