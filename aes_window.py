from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import aes
import base64
from Crypto.Cipher import AES
import os


class myAES(QtWidgets.QWidget, aes.Ui_hashSum):
    flag = 0

    def __init__(self):
        super(myAES, self).__init__()
        self.setupUi(self)
        self.selectFile.clicked.connect(self.selectFileFromDisk)
        self.encode.clicked.connect(self.encoder)
        self.decode.clicked.connect(self.decoder)

    def selectFileFromDisk(self):
        directory, fileType = QFileDialog.getOpenFileName(self, "选择文件")
        self.file_dir.setText(directory)
        if directory == '':
            myAES.flag = 0
        else:
            myAES.flag = 1

    def encoder(self):
        if myAES.flag == 1:
            file = open(self.file_dir.text(), 'rb')
            self.encrypt(file.read())
            file.close()
        else:
            self.encrypt(self.file_dir.text().encode('utf-8'))

    def encrypt(self, byteStream):
        base64text = base64.b64encode(byteStream).decode("utf-8")
        actualKey = self.key.text()
        while len(actualKey) % 16 != 0:
            actualKey += '\0'
        while len(base64text) % 16 != 0:
            base64text += '='

        crypt = AES.new(actualKey.encode('utf-8'), AES.MODE_ECB)
        cipher_text = crypt.encrypt(base64text.encode('utf-8'))

        fileName, ok = QFileDialog.getSaveFileName(self, "文件保存")
        if os.path.splitext(fileName)[1] == '':
            fileType = os.path.splitext(self.file_dir.text())[1]
        else:
            fileType = os.path.splitext(fileName)[1]
        fullname = os.path.splitext(fileName)[0] + fileType

        output = open(fullname, 'wb')
        output.write(cipher_text)
        output.close()

    def decoder(self):
        file = open(self.file_dir.text(), 'rb')
        actualKey = self.key.text()
        while len(actualKey) % 16 != 0:
            actualKey += '\0'
        crypt = AES.new(actualKey.encode('utf-8'), AES.MODE_ECB)

        plain_text = crypt.decrypt(file.read())
        outputStream = base64.b64decode(plain_text)
        fileName, ok = QFileDialog.getSaveFileName(self, "文件保存")
        if os.path.splitext(fileName)[1] == '':
            fileType = os.path.splitext(self.file_dir.text())[1]
        else:
            fileType = os.path.splitext(fileName)[1]
        fullname = os.path.splitext(fileName)[0] + fileType
        output = open(fullname, 'wb')
        output.write(outputStream)
        output.close()
        file.close()
