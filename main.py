# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuperEncoder(object):
    def setupUi(self, SuperEncoder):
        SuperEncoder.setObjectName("SuperEncoder")
        SuperEncoder.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperEncoder.sizePolicy().hasHeightForWidth())
        SuperEncoder.setSizePolicy(sizePolicy)
        self.genkey = QtWidgets.QPushButton(SuperEncoder)
        self.genkey.setGeometry(QtCore.QRect(270, 30, 165, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genkey.sizePolicy().hasHeightForWidth())
        self.genkey.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.genkey.setFont(font)
        self.genkey.setObjectName("genkey")
        self.instruction = QtWidgets.QPushButton(SuperEncoder)
        self.instruction.setGeometry(QtCore.QRect(520, 30, 165, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instruction.sizePolicy().hasHeightForWidth())
        self.instruction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.instruction.setFont(font)
        self.instruction.setObjectName("instruction")
        self.label = QtWidgets.QLabel(SuperEncoder)
        self.label.setGeometry(QtCore.QRect(130, 180, 512, 512))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("image: url(:/newPrefix/1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.RSA_encode = QtWidgets.QPushButton(SuperEncoder)
        self.RSA_encode.setGeometry(QtCore.QRect(820, 140, 400, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RSA_encode.sizePolicy().hasHeightForWidth())
        self.RSA_encode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.RSA_encode.setFont(font)
        self.RSA_encode.setObjectName("RSA_encode")
        self.RSA_decode = QtWidgets.QPushButton(SuperEncoder)
        self.RSA_decode.setGeometry(QtCore.QRect(820, 260, 400, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RSA_decode.sizePolicy().hasHeightForWidth())
        self.RSA_decode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.RSA_decode.setFont(font)
        self.RSA_decode.setObjectName("RSA_decode")
        self.sumup = QtWidgets.QPushButton(SuperEncoder)
        self.sumup.setGeometry(QtCore.QRect(770, 480, 500, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumup.sizePolicy().hasHeightForWidth())
        self.sumup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.sumup.setFont(font)
        self.sumup.setObjectName("sumup")
        self.aes = QtWidgets.QPushButton(SuperEncoder)
        self.aes.setGeometry(QtCore.QRect(830, 610, 401, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aes.sizePolicy().hasHeightForWidth())
        self.aes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.aes.setFont(font)
        self.aes.setObjectName("aes")
        self.RSA_verification = QtWidgets.QPushButton(SuperEncoder)
        self.RSA_verification.setGeometry(QtCore.QRect(820, 370, 400, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RSA_verification.sizePolicy().hasHeightForWidth())
        self.RSA_verification.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.RSA_verification.setFont(font)
        self.RSA_verification.setObjectName("RSA_verification")

        self.retranslateUi(SuperEncoder)
        QtCore.QMetaObject.connectSlotsByName(SuperEncoder)

    def retranslateUi(self, SuperEncoder):
        _translate = QtCore.QCoreApplication.translate
        SuperEncoder.setWindowTitle(_translate("SuperEncoder", "SuperEncoder"))
        self.genkey.setText(_translate("SuperEncoder", "生成密钥对"))
        self.instruction.setText(_translate("SuperEncoder", "使用说明"))
        self.RSA_encode.setText(_translate("SuperEncoder", "RSA加密"))
        self.RSA_decode.setText(_translate("SuperEncoder", "RSA解密"))
        self.sumup.setText(_translate("SuperEncoder", "MD5/SHA256求和校验"))
        self.aes.setText(_translate("SuperEncoder", "AES加密/解密"))
        self.RSA_verification.setText(_translate("SuperEncoder", "RSA签名/验签"))


import picture1_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SuperEncoder = QtWidgets.QWidget()
    ui = Ui_SuperEncoder()
    ui.setupUi(SuperEncoder)
    SuperEncoder.show()
    sys.exit(app.exec_())
