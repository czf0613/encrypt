# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.lineEdit = QtWidgets.QLineEdit(hashSum)
        self.lineEdit.setGeometry(QtCore.QRect(10, 150, 511, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.selectFile = QtWidgets.QPushButton(hashSum)
        self.selectFile.setGeometry(QtCore.QRect(550, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.selectFile.setFont(font)
        self.selectFile.setObjectName("selectFile")
        self.fire = QtWidgets.QPushButton(hashSum)
        self.fire.setGeometry(QtCore.QRect(300, 260, 161, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.fire.setFont(font)
        self.fire.setObjectName("fire")
        self.label_2 = QtWidgets.QLabel(hashSum)
        self.label_2.setGeometry(QtCore.QRect(20, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.MD5_result = QtWidgets.QLabel(hashSum)
        self.MD5_result.setGeometry(QtCore.QRect(20, 358, 751, 61))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        self.MD5_result.setFont(font)
        self.MD5_result.setObjectName("MD5_result")
        self.label_3 = QtWidgets.QLabel(hashSum)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 121, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.SHA256_result = QtWidgets.QLabel(hashSum)
        self.SHA256_result.setGeometry(QtCore.QRect(20, 480, 751, 61))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        self.SHA256_result.setFont(font)
        self.SHA256_result.setObjectName("SHA256_result")

        self.retranslateUi(hashSum)
        QtCore.QMetaObject.connectSlotsByName(hashSum)

    def retranslateUi(self, hashSum):
        _translate = QtCore.QCoreApplication.translate
        hashSum.setWindowTitle(_translate("hashSum", "求和校验"))
        self.label.setText(_translate("hashSum", "您可以操作一串文本(直接输入即可)，也可以直接操作整个文件"))
        self.selectFile.setText(_translate("hashSum", "打开"))
        self.fire.setText(_translate("hashSum", "确定"))
        self.label_2.setText(_translate("hashSum", "MD5："))
        self.MD5_result.setText(_translate("hashSum", "0"))
        self.label_3.setText(_translate("hashSum", "SHA256："))
        self.SHA256_result.setText(_translate("hashSum", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hashSum = QtWidgets.QWidget()
    ui = Ui_hashSum()
    ui.setupUi(hashSum)
    hashSum.show()
    sys.exit(app.exec_())