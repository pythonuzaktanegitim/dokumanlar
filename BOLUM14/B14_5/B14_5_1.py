import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon
class Uygulama(QMainWindow):
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
        dugme = QPushButton("Tıkla",self)
        dugme.move(100,70)
        ################################
        self.statusBar().showMessage("Çalışıyor")
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())