import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
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
        elCevap = QMessageBox.question(self,"Merhaba","Python Eğitiminde misin?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if elCevap == QMessageBox.Yes:
            QMessageBox.information(self,"Python Eğitimi","Hoşgeldin")
        else:
            QMessageBox.warning(self,"Python Eğitimi","Hoşgeldin")
        self.show()
        ################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())