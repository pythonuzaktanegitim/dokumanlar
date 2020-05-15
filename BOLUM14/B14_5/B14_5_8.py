import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFontDialog,QLineEdit,QColorDialog,QStyle
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
class Uygulama(QWidget):
    def __init__(self):
        super().__init__()
        self.baslik = "Örnek 1"
        self.sol = 100
        self.ust = 100
        self.width = 640
        self.height = 480
        self.Goster()

    def Goster(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol,self.ust,self.width,self.height)
        ################################
        dugme = QPushButton("Font Seçim",self)
        dugme.move(50,50)
        dugme.clicked.connect(self.tiklandi)
        self.textBox = QLineEdit(self)
        self.textBox.setText("Python")
        self.textBox.resize(100,50)
        self.textBox.move(50,80)

        ################################
        self.show()
    @pyqtSlot()
    def tiklandi(self):
        self.fontDialogAc()
        self.renkDialogAc()

    def fontDialogAc(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.font = font
            self.textBox.setFont(self.font)

    def renkDialogAc(self):
        renk = QColorDialog.getColor()
        if renk.isValid():
            print(renk,renk.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())