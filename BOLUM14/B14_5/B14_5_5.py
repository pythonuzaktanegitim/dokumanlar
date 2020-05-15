import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMessageBox,QInputDialog,QLineEdit
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
        mainMenu = self.menuBar()
        dosyaMenu = mainMenu.addMenu("Dosya")
        duzenleMenu = mainMenu.addMenu("Düzenle")
        #-------------------------------
        girisYap1 = QAction("Giriş Yap Double",self)
        girisYap1.triggered.connect(self.gYap1)
        duzenleMenu.addAction(girisYap1)
        girisYap2 = QAction("Giriş Yap Int",self)
        girisYap2.triggered.connect(self.gYap2)
        duzenleMenu.addAction(girisYap2)
        girisYap3 = QAction("Giriş Yap Text",self)
        girisYap3.triggered.connect(self.gYap3)
        duzenleMenu.addAction(girisYap3)
        #------------------------------
        hakkindaMenu = mainMenu.addMenu("Hakkında")
        hakkinda = QAction("Hakkında",self)
        hakkinda.triggered.connect(self.Hakkinda)
        hakkindaMenu.addAction(hakkinda)

        ################################
        self.statusBar().showMessage("Çalışıyor")
        self.show()

    def Hakkinda(self):
        QMessageBox.information(self,"Python","Python Eğitimi Örnek")

    def gYap1(self):
        d,okBasildi = QInputDialog.getDouble(self,"Değer Al","Değer",15,1,100,5)
        if okBasildi:
            print(d)

    def gYap2(self):
        d,okBasildi = QInputDialog.getInt(self,"Değer Al Integer","Değer",20,0,50,5)
        if okBasildi:
            print(d)

    def gYap3(self):
        d,okBasildi = QInputDialog.getText(self,"Değer Al Text","Değer",echo=QLineEdit.Password,text="Değer")
        if okBasildi:
            print(d)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())