import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import decode
import rsa_master


class mydecodeWindow(QtWidgets.QWidget, decode.Ui_hashSum):

    def __init__(self):
        super(mydecodeWindow, self).__init__()
        self.setupUi(self)
        self.selectFile.clicked.connect(self.openFile)
        self.selectpvk.clicked.connect(self.openPvk)
        self.fire.clicked.connect(self.run)

    def openFile(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择文件")
        self.file_dir.setText(dir)

    def openPvk(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择私钥")
        self.privateKey_dir.setText(dir)

    def run(self):
        try:
            fileName, ok = QFileDialog.getSaveFileName(self, "文件保存")
            myrsa = rsa_master.RsaUtil(pub_key_dir='', pri_key_dir=self.privateKey_dir.text())
            fileType = os.path.splitext(self.file_dir.text())[1]
            input = open(self.file_dir.text(), 'rb').read()
            if os.path.splitext(fileName)[1] == '':
                fullname = fileName + fileType
            else:
                fullname = fileName
            output = open(fullname, 'wb')
            output.write(myrsa.decrypt_by_private_key(message=input))
            output.close()
        except:
            pass


def showMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = mydecodeWindow()
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    showMainWindow()
