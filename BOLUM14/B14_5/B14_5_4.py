import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLineEdit,QMessageBox,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
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
        self.textBox = QLineEdit(self)
        self.textBox.move(30,30)
        self.textBox.resize(240,40)
        dugme = QPushButton("Tıkla",self)
        dugme.clicked.connect(self.tiklandi)
        dugme.move(100,70)
        self.secim = QCheckBox("Güzeeel",self)
        self.secim.stateChanged.connect(self.secildi)
        self.secim.move(120,100)
        ################################
        self.statusBar().showMessage("Çalışıyor")
        self.show()

    @pyqtSlot()
    def tiklandi(self):
        textboxValue = self.textBox.text()
        elCevap = QMessageBox.question(self,"Python","Doğrulama:"+textboxValue,
                                       QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Ok)
        if elCevap == QMessageBox.Ok:
            self.textBox.setText("değiştirildi")
            self.secim.setChecked(False)



    def secildi(self,state):
        if state == QtCore.Qt.Checked:
            print("İşaretlendi")
        else:
            print("İşaretlenmedi")
        self.textBox.setText("Seçim Yapıldı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())