import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import encode
import main_window
import rsa_master


class myencodeWindow(QtWidgets.QWidget, encode.Ui_hashSum):
    flag = 0

    def __init__(self):
        super(myencodeWindow, self).__init__()
        self.setupUi(self)
        self.selectFile.clicked.connect(self.openFile)
        self.selectpublicKey.clicked.connect(self.openPub)
        self.fire.clicked.connect(self.run)

    def openFile(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择文件")
        self.inputFile.setText(dir)
        myencodeWindow.flag = 1
        if dir == '':
            myencodeWindow.flag = 0

    def openPub(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择公钥")
        self.publicKey_dir.setText(dir)

    def run(self):
        try:
            fileName, ok = QFileDialog.getSaveFileName(self, "文件保存")
            myrsa = rsa_master.RsaUtil(pub_key_dir=self.publicKey_dir.text(), pri_key_dir='')
            if myencodeWindow.flag == 1:
                if os.path.splitext(fileName)[1] == '':
                    fileType = os.path.splitext(self.inputFile.text())[1]
                else:
                    fileType = os.path.splitext(fileName)[1]
                fullname = os.path.splitext(fileName)[0] + fileType
                output = open(fullname, 'wb')
                source = open(self.inputFile.text(), 'rb').read()
                output.write(myrsa.encrypt_by_public_key(source))
                output.close()
                myencodeWindow.flag = 0

            elif myencodeWindow.flag == 0:
                output = open(fileName, 'wb')
                output.write(myrsa.encrypt_by_public_key(self.inputFile.text().encode(main_window.charset)))
                output.close()
        except:
            pass


def showMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = myencodeWindow()
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    showMainWindow()
