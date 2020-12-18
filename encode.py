# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hashSum(object):
    def setupUi(self, hashSum):
        hashSum.setObjectName("hashSum")
        hashSum.resize(800, 600)
        self.label = QtWidgets.QLabel(hashSum)
        self.label.setGeometry(QtCore.QRect(20, 30, 621, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.inputFile = QtWidgets.QLineEdit(hashSum)
        self.inputFile.setGeometry(QtCore.QRect(10, 150, 511, 51))
        self.inputFile.setObjectName("inputFile")
        self.selectFile = QtWidgets.QPushButton(hashSum)
        self.selectFile.setGeometry(QtCore.QRect(550, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.selectFile.setFont(font)
        self.selectFile.setObjectName("selectFile")
        self.fire = QtWidgets.QPushButton(hashSum)
        self.fire.setGeometry(QtCore.QRect(310, 470, 161, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.fire.setFont(font)
        self.fire.setObjectName("fire")
        self.selectpublicKey = QtWidgets.QPushButton(hashSum)
        self.selectpublicKey.setGeometry(QtCore.QRect(300, 270, 161, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.selectpublicKey.setFont(font)
        self.selectpublicKey.setObjectName("selectpublicKey")
        self.label_2 = QtWidgets.QLabel(hashSum)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 231, 121))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.publicKey_dir = QtWidgets.QLineEdit(hashSum)
        self.publicKey_dir.setGeometry(QtCore.QRect(20, 360, 511, 51))
        self.publicKey_dir.setObjectName("publicKey_dir")

        self.retranslateUi(hashSum)
        QtCore.QMetaObject.connectSlotsByName(hashSum)

    def retranslateUi(self, hashSum):
        _translate = QtCore.QCoreApplication.translate
        hashSum.setWindowTitle(_translate("hashSum", "RSA加密"))
        self.label.setText(_translate("hashSum", "您可以加密一串文本(直接输入即可)，也可以直接加密整个文件"))
        self.selectFile.setText(_translate("hashSum", "打开"))
        self.fire.setText(_translate("hashSum", "确定"))
        self.selectpublicKey.setText(_translate("hashSum", "打开"))
        self.label_2.setText(_translate("hashSum", "选择公钥"))
