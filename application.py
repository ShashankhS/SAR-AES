import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
from controller import crypter

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.show()
        self.browse.clicked.connect(self.browsefiles)
        self.encrypt.clicked.connect(self.encryption)
        self.decrypt.clicked.connect(self.decryption)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Shashankh S\\Desktop')
        self.filename.setText(fname[0])
        print(fname)

    def encryption(self):
        path = self.filename.text()
        key = self.inputkey.text()
        print(path, key)
        crypter(path, key, '1')
        output_path = os.path.dirname(path) + '/encrypted_' + os.path.basename(path)
        self.output_label.setText('File encrypted and stored in: ' + output_path)

    def decryption(self):
        path = self.filename.text()
        key = self.inputkey.text()
        print(path, key)
        crypter(path, key, '2')
        output_path = os.path.dirname(path) + '/decrypted_' + os.path.basename(path)
        self.output_label.setText('File decrypted and stored in: ' + output_path)
        print(output_path)

app = QApplication(sys.argv)
mainwindow = MainWindow()
sys.exit(app.exec_())
