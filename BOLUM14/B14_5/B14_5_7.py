import sys
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit,QFileDialog
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
        self.kaydetDialogAc()
        ################################
        self.show()
    def fileDialogAc(self):
        secenekler = QFileDialog.Options()
        secenekler |= QFileDialog.DontUseNativeDialog
        dosyaadi , _ = QFileDialog.getOpenFileName(self,"Dosya Aç", "",
                                                   "Bütün Dosyalar (*);;Python Dosyaları (*.py)",options=secenekler)
        if dosyaadi:
            print(dosyaadi)

    def filesDialogAc(self):
        secenekler = QFileDialog.Options()
        secenekler |= QFileDialog.DontUseNativeDialog
        dosyalar , _ = QFileDialog.getOpenFileNames(self,"Çoklu Dosyalar", "",
                                                   "Bütün Dosyalar (*);;Python Dosyaları (*.py)",options=secenekler)
        if dosyalar:
            print(dosyalar)

    def kaydetDialogAc(self):
        secenekler = QFileDialog.Options()
        secenekler |= QFileDialog.DontUseNativeDialog
        dosyaAdi, _ = QFileDialog.getSaveFileName(self,"Dosya Kaydet","","Bütün Dosyalar (*);;Python Dosyaları (*.py)"
                                                  ,options=secenekler)
        if dosyaAdi:
            print(dosyaAdi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())