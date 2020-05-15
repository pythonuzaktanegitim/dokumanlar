import sys
from PyQt5.QtWidgets import *
class Dialog(QDialog):
    def slotmetodu(self):
        print("Slot Çağırıldı")
    def __init__(self):
        super(Dialog,self).__init__()
        button = QPushButton("Tıkla")
        button.clicked.connect(self.slotmetodu)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())
