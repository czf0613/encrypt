# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decode.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 30, 621, 91))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.file_dir = QtWidgets.QLineEdit(hashSum)
        self.file_dir.setGeometry(QtCore.QRect(10, 150, 511, 51))
        self.file_dir.setObjectName("file_dir")
        self.selectFile = QtWidgets.QPushButton(hashSum)
        self.selectFile.setGeometry(QtCore.QRect(550, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.selectFile.setFont(font)
        self.selectFile.setObjectName("selectFile")
        self.fire = QtWidgets.QPushButton(hashSum)
        self.fire.setGeometry(QtCore.QRect(320, 490, 161, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.fire.setFont(font)
        self.fire.setObjectName("fire")
        self.privateKey_dir = QtWidgets.QLineEdit(hashSum)
        self.privateKey_dir.setGeometry(QtCore.QRect(10, 370, 511, 51))
        self.privateKey_dir.setObjectName("privateKey_dir")
        self.selectpvk = QtWidgets.QPushButton(hashSum)
        self.selectpvk.setGeometry(QtCore.QRect(550, 370, 161, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.selectpvk.setFont(font)
        self.selectpvk.setObjectName("selectpvk")
        self.label_2 = QtWidgets.QLabel(hashSum)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 251, 101))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(hashSum)
        QtCore.QMetaObject.connectSlotsByName(hashSum)

    def retranslateUi(self, hashSum):
        _translate = QtCore.QCoreApplication.translate
        hashSum.setWindowTitle(_translate("hashSum", "RSA解密"))
        self.label.setText(_translate("hashSum", "选择需要解密的文件"))
        self.selectFile.setText(_translate("hashSum", "打开"))
        self.fire.setText(_translate("hashSum", "确定"))
        self.selectpvk.setText(_translate("hashSum", "打开"))
        self.label_2.setText(_translate("hashSum", "选择私钥"))
