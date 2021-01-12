# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_History(object):
    def setupUi(self, Dialog_History, getdno):
        Dialog_History.setObjectName("Dialog_History")
        Dialog_History.setFixedSize(862, 373)
        self.groupBox_30 = QtWidgets.QGroupBox(Dialog_History)
        self.groupBox_30.setGeometry(QtCore.QRect(10, 10, 841, 351))
        self.groupBox_30.setObjectName("groupBox_30")
        self.tableWidget_30 = QtWidgets.QTableWidget(self.groupBox_30)
        self.tableWidget_30.setGeometry(QtCore.QRect(10, 20, 821, 321))
        self.tableWidget_30.setObjectName("tableWidget_30")
        self.tableWidget_30.setColumnCount(7)
        self.tableWidget_30.setRowCount(0)
        self.tableWidget_30.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_30.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_30.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_30.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.down_action_2 = QtWidgets.QAction("다운로드", self.tableWidget_30)
        self.tableWidget_30.addAction(self.down_action_2)

        self.retranslateUi(Dialog_History)
        QtCore.QMetaObject.connectSlotsByName(Dialog_History)

        self.init_table()
        self.draw_table(getdno)

    def retranslateUi(self, Dialog_History):
        _translate = QtCore.QCoreApplication.translate
        Dialog_History.setWindowTitle(_translate("Dialog_History", "nyPLM CAD IG"))
        Dialog_History.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_30.setTitle(_translate("Dialog_History", "[ 히스토리 ]"))


    def init_table(self):
        column_headers = ['도면번호', '차종정보', '제품구분', '도면개정', '도면종류', '등록일', '파일버전']
        self.tableWidget_30.setHorizontalHeaderLabels(column_headers)
        self.tableWidget_30.setColumnWidth(0, 120)
        self.tableWidget_30.setColumnWidth(1, 120)
        self.tableWidget_30.setColumnWidth(2, 120)
        self.tableWidget_30.setColumnWidth(3, 85)
        self.tableWidget_30.setColumnWidth(4, 120)
        self.tableWidget_30.setColumnWidth(5, 120)
        self.tableWidget_30.setColumnWidth(6, 85)


    def draw_table(self, getDno):
        tmp_shortHistory = []
        for rows in self.allmodfilehistory:
            tmp_shortHistory.append(tuple(rows[:7]))
        tmp_set = set()
        shortHistory = []
        for rows2 in tmp_shortHistory:
            if rows2 not in tmp_set:
                shortHistory.append(rows2)
                tmp_set.add(rows2)

        currentRow = 0
        for k in range(len(shortHistory)):
            if shortHistory[k][0] == getDno:
                self.tableWidget_30.setRowCount(currentRow + 1)
                DNO = shortHistory[k][0]
                CAROID = shortHistory[k][1]
                PRTTYPEOID = shortHistory[k][2]
                MVERSION = shortHistory[k][3]
                MODTYPEOID = shortHistory[k][4]
                date = shortHistory[k][5]
                REGDATE = date.replace('-', '/')[:10]
                # date = shortHistory[k][5]
                # REGDATE = date.strftime('%Y/%m/%d')
                VERSION = shortHistory[k][6]

                item1 = QtWidgets.QTableWidgetItem(DNO)
                item2 = QtWidgets.QTableWidgetItem(CAROID)
                item3 = QtWidgets.QTableWidgetItem(PRTTYPEOID)
                item4 = QtWidgets.QTableWidgetItem(MVERSION)
                item5 = QtWidgets.QTableWidgetItem(MODTYPEOID)
                item6 = QtWidgets.QTableWidgetItem(REGDATE)
                item7 = QtWidgets.QTableWidgetItem(VERSION)

                item1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item6.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                item7.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

                self.tableWidget_30.setItem(currentRow, 0, item1)
                self.tableWidget_30.setItem(currentRow, 1, item2)
                self.tableWidget_30.setItem(currentRow, 2, item3)
                self.tableWidget_30.setItem(currentRow, 3, item4)
                self.tableWidget_30.setItem(currentRow, 4, item5)
                self.tableWidget_30.setItem(currentRow, 5, item6)
                self.tableWidget_30.setItem(currentRow, 6, item7)
                currentRow = currentRow + 1

        self.tableWidget_30.setAlternatingRowColors(True)


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_History = QtWidgets.QDialog()
    ui = Ui_Dialog_History()
    ui.setupUi(Dialog_History)
    Dialog_History.show()
    sys.exit(app.exec_())

