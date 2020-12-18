import hashlib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import main_window
import sumup


class mySumUp(QtWidgets.QWidget, sumup.Ui_hashSum):
    # if it is file,it will be 1, or it will be 0
    flag = 0

    def __init__(self):
        super(mySumUp, self).__init__()
        self.setupUi(self)
        self.selectFile.clicked.connect(self.choose)
        self.fire.clicked.connect(self.run)

    def choose(self):
        dir, fileType = QFileDialog.getOpenFileName(self, "选择文件")
        self.lineEdit.setText(dir)
        mySumUp.flag = 1

    def run(self):
        try:
            if mySumUp.flag == 0:
                MD5 = hashlib.md5(self.lineEdit.text().encode(encoding=main_window.charset)).hexdigest()
                SHA256 = hashlib.sha256(self.lineEdit.text().encode(encoding=main_window.charset)).hexdigest()
                self.MD5_result.setText(MD5)
                self.SHA256_result.setText(SHA256)
            elif mySumUp.flag == 1:
                mySumUp.flag = 0
                f = open(self.lineEdit.text(), 'rb')
                md5_obj = hashlib.md5()
                sha256_obj = hashlib.sha256()
                while True:
                    d = f.read(8096)
                    if not d:
                        break
                    md5_obj.update(d)
                    sha256_obj.update(d)
                hashcode1 = md5_obj.hexdigest()
                hashcode2 = sha256_obj.hexdigest()
                f.close()
                md5 = str(hashcode1).lower()
                sha256 = str(hashcode2).lower()
                self.MD5_result.setText(md5)
                self.SHA256_result.setText(sha256)
        except:
            pass


def showMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = mySumUp()
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    showMainWindow()
