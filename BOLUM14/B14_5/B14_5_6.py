import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import  QPixmap
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
        etiket = QLabel(self)
        resim = QPixmap(r'resimler\happy_python.png')
        etiket.setPixmap(resim)
        self.resize(resim.width(),resim.height())
        ################################
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())