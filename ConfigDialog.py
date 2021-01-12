# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config_v0.1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import configparser

class Ui_Dialog_config(object):
    def setupUi(self, Dialog_config):
        Dialog_config.setObjectName("Dialog_config")
        Dialog_config.setFixedSize(622, 163)
        self.groupBox_conf = QtWidgets.QGroupBox(Dialog_config)
        self.groupBox_conf.setGeometry(QtCore.QRect(10, 10, 601, 101))
        self.groupBox_conf.setObjectName("groupBox_conf")
        self.label_conf = QtWidgets.QLabel(self.groupBox_conf)
        self.label_conf.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_conf.setObjectName("label_conf")
        self.label_conf2 = QtWidgets.QLabel(self.groupBox_conf)
        self.label_conf2.setGeometry(QtCore.QRect(20, 64, 81, 16))
        self.label_conf2.setObjectName("label_conf2")
        self.lineEdit_conf = QtWidgets.QLineEdit(self.groupBox_conf)
        self.lineEdit_conf.setGeometry(QtCore.QRect(109, 28, 431, 20))
        self.lineEdit_conf.setObjectName("lineEdit_conf")
        self.lineEdit_conf.setEnabled(False)
        self.lineEdit_conf2 = QtWidgets.QLineEdit(self.groupBox_conf)
        self.lineEdit_conf2.setGeometry(QtCore.QRect(109, 62, 431, 20))
        self.lineEdit_conf2.setObjectName("lineEdit_conf2")
        self.lineEdit_conf2.setEnabled(False)
        self.pushButton_conf = QtWidgets.QPushButton(self.groupBox_conf)
        self.pushButton_conf.setGeometry(QtCore.QRect(548, 27, 31, 23))
        self.pushButton_conf.setObjectName("pushButton_conf")
        self.pushButton_conf.clicked.connect(self.setDownloadPath)
        self.pushButton_conf2 = QtWidgets.QPushButton(self.groupBox_conf)
        self.pushButton_conf2.setGeometry(QtCore.QRect(548, 60, 31, 23))
        self.pushButton_conf2.setObjectName("pushButton_conf2")
        self.pushButton_conf2.clicked.connect(self.setNewRegistPath)
        self.pushButton_conf3 = QtWidgets.QPushButton(Dialog_config)
        self.pushButton_conf3.setGeometry(QtCore.QRect(520, 120, 91, 31))
        self.pushButton_conf3.setObjectName("pushButton_conf3")

        self.retranslateUi(Dialog_config)
        QtCore.QMetaObject.connectSlotsByName(Dialog_config)

    def retranslateUi(self, Dialog_config):
        _translate = QtCore.QCoreApplication.translate
        Dialog_config.setWindowTitle(_translate("Dialog_config", "nyPLM CAD IG"))
        Dialog_config.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_conf.setTitle(_translate("Dialog_config", "[ 경로 설정 ]"))
        self.label_conf.setText(_translate("Dialog_config", "다운로드 위치:"))
        self.label_conf2.setText(_translate("Dialog_config", "신규등록 위치:"))
        self.pushButton_conf.setText(_translate("Dialog_config", "..."))
        self.pushButton_conf2.setText(_translate("Dialog_config", "..."))
        self.pushButton_conf3.setText(_translate("Dialog_config", "확인"))

        self.Init()


    # 초기셋팅
    def Init(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        downpath = config.get('PATH_INFO', 'downpath')
        self.lineEdit_conf.setText(downpath)
        newpath = config.get('PATH_INFO', 'newpath')
        self.lineEdit_conf2.setText(newpath)


    # 다운로드 위치
    def setDownloadPath(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        fd = FileDialogWidget()
        if not fd.newPath:
            return 0
        else:
            if fd.newPath.find('/'):
                fd.newPath = fd.newPath.replace('/', '\\')
            self.lineEdit_conf.setText(fd.newPath)
            config.set('PATH_INFO', 'downpath', self.lineEdit_conf.text())
            with open('config.ini', 'w') as configfile:
                config.write(configfile)


    # 신규등록 위치
    def setNewRegistPath(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        fd = FileDialogWidget()
        if not fd.newPath:
            return 0
        else:
            if fd.newPath.find('/'):
                fd.newPath = fd.newPath.replace('/', '\\')
            self.lineEdit_conf2.setText(fd.newPath)
            config.set('PATH_INFO', 'newpath', self.lineEdit_conf2.text())
            with open('config.ini', 'w') as configfile:
                config.write(configfile)


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


# 파일 다이얼로그 클래스
class FileDialogWidget(QtWidgets.QWidget, Ui_Dialog_config):
    def __init__(self):
        super(FileDialogWidget, self).__init__()
        self.newPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_config = QtWidgets.QDialog()
    ui = Ui_Dialog_config()
    ui.setupUi(Dialog_config)
    Dialog_config.show()
    sys.exit(app.exec_())