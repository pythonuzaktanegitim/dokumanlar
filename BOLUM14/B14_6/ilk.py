# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonScreen\EGITIM\BOLUM14\B14_6\ilk.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 183)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 581, 76))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt1.setMaxLength(50)
        self.txt1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt1.setObjectName("txt1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmb1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmb1.setObjectName("cmb1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmb1)
        self.lblSecim = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSecim.setText("")
        self.lblSecim.setObjectName("lblSecim")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblSecim)
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(30, 90, 93, 28))
        self.bt1.setObjectName("bt1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.bt1.clicked.connect(self.tiklandi)
        self.cmb1.currentIndexChanged.connect(self.secim)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kalem:"))
        self.label_2.setText(_translate("MainWindow", "Tür:"))
        self.bt1.setText(_translate("MainWindow", "Ekle"))

    def tiklandi(self):
        metin = self.txt1.text()
        self.cmb1.addItem(metin)
        self.cmb1.setCurrentText(metin)

    def secim(self):
        self.lblSecim.setText(self.cmb1.currentText())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

