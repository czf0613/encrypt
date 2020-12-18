import win32api
from PyQt5.QtWidgets import QFileDialog

import verify
import rsa_master
from PyQt5 import QtWidgets


class myVerify(QtWidgets.QWidget, verify.Ui_hashSum):
    def __init__(self):
        super(myVerify, self).__init__()
        self.setupUi(self)
        self.selectFile.clicked.connect(self.openFile)
        self.selectpublicKey.clicked.connect(self.openPublicKey)
        self.selectprivateKey.clicked.connect(self.openPrivateKey)
        self.signing.clicked.connect(self.signFile)
        self.verifying.clicked.connect(self.verifyKey)

    def openFile(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择文件")
        self.inputFile.setText(dir)

    def openPublicKey(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择公钥")
        self.publicKey_dir.setText(dir)

    def openPrivateKey(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择私钥")
        self.privateKey_dir.setText(dir)

    def verifyKey(self):
        if len(self.publicKey_dir.text()) == 0 or len(self.privateKey_dir.text()) == 0:
            win32api.MessageBox(0, "密钥无效", "错误", 0)
            return
        else:
            self.rsaKit = rsa_master.RsaUtil(pub_key_dir=self.publicKey_dir.text(),
                                             pri_key_dir=self.privateKey_dir.text())
            try:
                self.result.setText(
                    self.rsaKit.verify_by_public_key(open(self.inputFile.text(), 'rb').read(), self.fingerPrint.text()))
            except:
                win32api.MessageBox(0, "签名验证失败", "错误", 0)

    def signFile(self):
        if len(self.publicKey_dir.text()) == 0 or len(self.privateKey_dir.text()) == 0:
            win32api.MessageBox(0, "密钥无效", "错误", 0)
            return
        else:
            self.rsaKit = rsa_master.RsaUtil(pub_key_dir=self.publicKey_dir.text(),
                                             pri_key_dir=self.privateKey_dir.text())

            self.result.setText(
                self.rsaKit.sign_by_private_key(open(self.inputFile.text(), 'rb').read()).decode('utf-8'))
