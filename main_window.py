import os
import sys
import webbrowser as web

import win32api
from PyQt5 import QtWidgets

import decode_window
import encode_window
import genkey
import main
import sumup_window
import aes_window
import verify_window


class myMainWindow(QtWidgets.QWidget, main.Ui_SuperEncoder):

    def __init__(self):
        super(myMainWindow, self).__init__()
        self.setupUi(self)
        self.genkey.clicked.connect(self.keygen)
        self.instruction.clicked.connect(self.showInstruction)
        self.RSA_encode.clicked.connect(self.rsa_encode)
        self.RSA_decode.clicked.connect(self.rsa_decode)
        self.RSA_verification.clicked.connect(self.rsa_sign)
        self.sumup.clicked.connect(self.MD5SHA256)
        self.aes.clicked.connect(self.aesEncrption)

    def keygen(self):
        try:
            genkey.keygen()
            local = os.path.expanduser("~")
            win32api.MessageBox(0, r"密钥已经生成，位于%s\.ssh中" % local, "提示", 0)
        except:
            win32api.MessageBox(0, "未知错误，请联系管理员", "错误", 0)

    def showInstruction(self):
        try:
            web.open(r"resources\软件使用说明.pdf")
        except:
            win32api.MessageBox(0, "无法打开指定目标", "错误", 0)

    def rsa_encode(self):
        self.encode = encode_window.myencodeWindow()
        self.encode.show()

    def rsa_decode(self):
        self.decode = decode_window.mydecodeWindow()
        self.decode.show()

    def rsa_sign(self):
        self.rsaSign = verify_window.myVerify()
        self.rsaSign.show()

    def MD5SHA256(self):
        self.sum = sumup_window.mySumUp()
        self.sum.show()

    def aesEncrption(self):
        self.aes = aes_window.myAES()
        self.aes.show()


def showMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = myMainWindow()
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    showMainWindow()
