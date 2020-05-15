import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMessageBox,QInputDialog,QLineEdit,QLabel,QFileDialog
from PyQt5.QtGui import QPixmap
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
        #-----------------------------------------
        dosyaDialog = QAction("Aç",self)
        dosyaDialog.triggered.connect(self.dosyaAc)
        dosyaMenu.addAction(dosyaDialog)

        dCikis = QAction("Çıkış",self)
        dCikis.triggered.connect(self.cikis)
        dosyaMenu.addAction(dCikis)
        #-----------------------------------------
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
        self.etiket = QLabel(self)
        self.etiket.setText("Buradayım")
        self.etiket.move(10,20)
        self.show()

    def Hakkinda(self):
        QMessageBox.information(self,"Python","Python Eğitimi Örnek")

    def dosyaAc(self):
        secenek = QFileDialog.Options()
        secenek |= QFileDialog.DontUseNativeDialog
        self.dosyaAdi, _ = QFileDialog.getOpenFileName(self,"Resim Aç","",
                                                       "Bütün Dosyalar (*);;PNG Resim Dosyaları (*.png)",
                                                       options=secenek)
        if self.dosyaAdi:
            self.resimAc()



    def resimAc(self):
        resim = QPixmap(self.dosyaAdi)
        self.etiket.setPixmap(resim)
        self.etiket.resize(resim.width(),resim.height())
        self.resize(resim.width(),resim.height()+30)

    def cikis(self):
        elCevap = QMessageBox.question(self,"Soru","Emin misin?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                       )
        self.close()


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