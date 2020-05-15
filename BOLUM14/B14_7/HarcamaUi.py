import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QMessageBox
from PyQt5 import QtWidgets,uic
from HarcamaDB import DBTool

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DBTool()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi("Harcama.ui")
        self.win.lblID.setText("")
        self.HarcamaKalemDoldur()
        self.HarcamaAyDoldur()
        self.HarcamaTabloDoldur()
        self.win.btYeni.clicked.connect(self.Temizle)
        self.win.btKaydet.clicked.connect(self.Kaydet)
        self.win.btSil.clicked.connect(self.Sil)
        self.win.tblHarcama.doubleClicked.connect(self.kayitSec)
        self.win.show()

    def Doldur(self):
        print(self.db.select(Tablo="V_HARCAMA_BILGI"))

    def HarcamaKalemDoldur(self):
        liste = self.db.select(Tablo="HRC_KALEM")
        self.win.cmbKalem.addItem("Seçiniz")
        for kid,kad in liste:
            self.win.cmbKalem.addItem(kad)

    def HarcamaAyDoldur(self):
        liste = self.db.select(Tablo="V_SOZLUK_AY")
        self.win.cmbAY.addItem("Seçiniz")
        for ayid,ayad in liste:
            self.win.cmbAY.addItem(ayad)

    def HarcamaTabloDoldur(self):
        self.Kayitliste = self.db.select(Tablo="V_HARCAMA_TABLO")
        self.win.tblHarcama.clear()
        self.win.tblHarcama.setRowCount(len(self.Kayitliste))
        self.win.tblHarcama.setColumnCount(5)
        for i in range(len(self.Kayitliste)):
            for j in range(len(self.Kayitliste[i])):
                self.win.tblHarcama.setItem(i,j,QTableWidgetItem(str(self.Kayitliste[i][j])))


    def kayitSec(self):
        liste = self.Kayitliste[self.win.tblHarcama.currentItem().row()]
        self.win.cmbKalem.setCurrentText(liste[1])
        self.win.cmbAY.setCurrentText(liste[3])
        self.win.txtTutar.setText(str(liste[2]))
        print(liste[4])
        if liste[4] == "Gider":
            self.win.rdbGider.setChecked(1)
        else:
            self.win.rdbGelir.setChecked(1)
        self.win.lblID.setText(str(liste[0]))

    def Temizle(self):
        self.win.cmbKalem.setCurrentIndex(0)
        self.win.cmbAY.setCurrentIndex(0)
        self.win.txtTutar.setText("")
        self.win.rdbGider.setChecked(0)
        self.win.rdbGelir.setChecked(0)
        self.win.lblID.setText("")

    def Kaydet(self):
        hrcKalem = self.win.cmbKalem.currentIndex()
        hrcAy = self.win.cmbAY.currentIndex()
        hrcTutar = self.win.txtTutar.text()
        if self.win.rdbGider.isChecked():
            hrcTip = 2
        if self.win.rdbGelir.isChecked():
            hrcTip = 1
        hrcID = self.win.lblID.text()
        if hrcID != "":
            sonuc = self.db.update(hrcKalem,hrcTip,hrcAy,hrcTutar,hrcID)
        else:
            sonuc = self.db.insert(hrcKalem,hrcTip,hrcAy,hrcTutar)
        if sonuc == "1":
            QMessageBox.information(self,"Bilgi","Kayıt İşlemi Başarılı")
            self.HarcamaTabloDoldur()
        else:
            QMessageBox.warning(self,"Hata",sonuc)

    def Sil(self):
        hrcID = self.win.lblID.text()
        if hrcID:
            cevap = QMessageBox.question(self,"Silme İşlemi","Emin Misiniz?",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if cevap == QMessageBox.Yes:
                sonuc = self.db.delete(hrcID)
                if sonuc == "1":
                    QMessageBox.information(self, "Bilgi", "Silme İşlemi Başarılı")
                    self.HarcamaTabloDoldur()
                else:
                    QMessageBox.warning(self, "Hata", sonuc)
        else:
            QMessageBox.warning(self, "Kayıt", "Kayıt Seçilmeli")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = App()
    sys.exit(app.exec_())