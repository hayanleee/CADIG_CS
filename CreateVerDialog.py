# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateVer_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests

class Ui_CreateVersionDialog(object):
    def setupUi(self, CreateVersionDialog, svurl):
        CreateVersionDialog.setObjectName("CreateVersionDialog")
        CreateVersionDialog.setFixedSize(954, 409)
        self.groupBox_cv = QtWidgets.QGroupBox(CreateVersionDialog)
        self.groupBox_cv.setGeometry(QtCore.QRect(10, 10, 231, 390))
        self.groupBox_cv.setObjectName("groupBox_cv")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_cv = QtWidgets.QLabel(self.groupBox_cv)
        self.label_cv.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_cv.setObjectName("label_cv")
        self.label_cv.setFont(font)
        self.label_cv2 = QtWidgets.QLabel(self.groupBox_cv)
        self.label_cv2.setGeometry(QtCore.QRect(20, 62, 71, 16))
        self.label_cv2.setObjectName("label_cv2")
        self.label_cv3 = QtWidgets.QLabel(self.groupBox_cv)
        self.label_cv3.setGeometry(QtCore.QRect(20, 126, 71, 16))
        self.label_cv3.setObjectName("label_cv3")
        self.label_cv3.setFont(font)
        self.label_cv4 = QtWidgets.QLabel(self.groupBox_cv)
        self.label_cv4.setGeometry(QtCore.QRect(20, 94, 71, 16))
        self.label_cv4.setObjectName("label_cv4")
        self.lineEdit_cv = QtWidgets.QLineEdit(self.groupBox_cv)
        self.lineEdit_cv.setGeometry(QtCore.QRect(90, 28, 131, 20))
        self.lineEdit_cv.setObjectName("lineEdit_cv")
        self.lineEdit_cv.setValidator(QtGui.QIntValidator(0, 99))
        self.lineEdit_cv.setMaxLength(2)
        self.lineEdit_cv.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_cv.textChanged.connect(self.changeData_cv1)
        self.lineEdit_cv.setEnabled(False)
        self.lineEdit_cv2 = QtWidgets.QLineEdit(self.groupBox_cv)
        self.lineEdit_cv2.setGeometry(QtCore.QRect(90, 92, 131, 20))
        self.lineEdit_cv2.setObjectName("lineEdit_cv2")
        self.lineEdit_cv2.textChanged.connect(self.changeData_cv3)
        self.listWidget_cv = QtWidgets.QListWidget(self.groupBox_cv)
        self.listWidget_cv.setGeometry(QtCore.QRect(90, 152, 131, 111))
        self.listWidget_cv.setObjectName("listWidget_cv")
        self.pushButton_cv = QtWidgets.QPushButton(self.groupBox_cv)
        self.pushButton_cv.setGeometry(QtCore.QRect(10, 280, 211, 29))
        self.pushButton_cv.setObjectName("pushButton_cv")
        self.pushButton_cv.clicked.connect(self.copyTableCell_3)
        self.pushButton_cv2 = QtWidgets.QPushButton(self.groupBox_cv)
        self.pushButton_cv2.setGeometry(QtCore.QRect(10, 315, 211, 29))
        self.pushButton_cv2.setObjectName("pushButton_cv2")
        self.pushButton_cv2.clicked.connect(self.resetBtn)
        self.pushButton_cv3 = QtWidgets.QPushButton(self.groupBox_cv)
        self.pushButton_cv3.setGeometry(QtCore.QRect(10, 350, 211, 29))
        self.pushButton_cv3.setObjectName("pushButton_cv3")
        self.pushButton_cv4 = QtWidgets.QPushButton(self.groupBox_cv)
        self.pushButton_cv4.setGeometry(QtCore.QRect(89, 125, 41, 22))
        self.pushButton_cv4.setObjectName("pushButton_cv4")
        self.pushButton_cv5 = QtWidgets.QPushButton(self.groupBox_cv)
        self.pushButton_cv5.setGeometry(QtCore.QRect(135, 125, 41, 22))
        self.pushButton_cv5.setObjectName("pushButton_cv5")
        self.pushButton_cv5.clicked.connect(self.deleteDrawrel)
        self.comboBox_cv = QtWidgets.QComboBox(self.groupBox_cv)
        self.comboBox_cv.setGeometry(QtCore.QRect(90, 60, 131, 21))
        self.comboBox_cv.setObjectName("comboBox_cv")
        self.comboBox_cv.addItem("")
        # self.dic_cv = {"PILOT": "CCN11678", "P1": "CCN11679", "P2": "CCN11680", "SOP": "CCN11681"}
        for k in self.dic_cv.keys():
            self.comboBox_cv.addItem(k)
        self.comboBox_cv.currentIndexChanged.connect(self.changeData_cv2)
        self.tableWidget_cv = QtWidgets.QTableWidget(CreateVersionDialog)
        self.tableWidget_cv.setGeometry(QtCore.QRect(250, 16, 691, 383))
        self.tableWidget_cv.setObjectName("tableWidget_cv")
        self.tableWidget_cv.setColumnCount(6)
        self.tableWidget_cv.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_cv.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_cv.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_cv.clicked.connect(self.selectRowData_3)

        self.retranslateUi(CreateVersionDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateVersionDialog)

        self.svurl = svurl
        self.chkMod = list(set(self.chkMod))

        self.tmp_chkDnoList = []
        for i in range(len(self.chkMod)):
            self.tmp_chkDnoList.append(self.chkMod[i][:self.chkMod[i].rfind('|')])
            # self.tmp_chkDnoList.append(self.chkMod[i][self.chkMod[i].find('|')+1:self.chkMod[i].rfind('|')])

        self.chkDnoList = []
        self.chkOidList = []
        for txt in self.tmp_chkDnoList:
            self.chkDnoList.append(txt[txt.find('|')+1:])
            self.chkOidList.append(txt[:txt.find('|')])
        self.tableWidget_cv.setRowCount(len(self.chkDnoList))

        self.col_3 = self.tableWidget_cv.columnCount()
        self.row_3 = self.tableWidget_cv.rowCount()

        self.setInitTableHeader()
        self.drawAutoRevision()


    def retranslateUi(self, CreateVersionDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateVersionDialog.setWindowTitle(_translate("CreateVersionDialog", "nyPLM CAD IG"))
        CreateVersionDialog.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_cv.setTitle(_translate("CreateVersionDialog", "[ 개정 생성 ]"))
        self.label_cv.setText(_translate("CreateVersionDialog", "개정 번호 :"))
        self.label_cv2.setText(_translate("CreateVersionDialog", "개발 단계 :"))
        self.label_cv3.setText(_translate("CreateVersionDialog", "파트 개정 :"))
        self.label_cv4.setText(_translate("CreateVersionDialog", "EONO     :"))
        self.pushButton_cv.setText(_translate("CreateVersionDialog", "공통 적용"))
        self.pushButton_cv2.setText(_translate("CreateVersionDialog", "초  기  화"))
        self.pushButton_cv3.setText(_translate("CreateVersionDialog", "확       인"))
        self.pushButton_cv4.setText(_translate("CreateVersionDialog", "추가"))
        self.pushButton_cv5.setText(_translate("CreateVersionDialog", "삭제"))


    # 테이블 초기 셋팅
    def setInitTableHeader(self):
        self.selectFlag_3 = True
        column_headers = ['도면번호', '개정번호', '개발단계', 'EONO', '파트개정', 'modoid']
        self.tableWidget_cv.setHorizontalHeaderLabels(column_headers)
        for i in range(self.row_3):
            self.tableWidget_cv.setItem(i, 0, QtWidgets.QTableWidgetItem(self.chkDnoList[i]))
            self.tableWidget_cv.setItem(i, 5, QtWidgets.QTableWidgetItem(self.chkOidList[i]))
        self.tableWidget_cv.setAlternatingRowColors(True)
        self.tableWidget_cv.setColumnHidden(5, True)
        header = self.tableWidget_cv.horizontalHeader()
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.pushButton_cv2.setEnabled(False)
        self.pushButton_cv3.setEnabled(False)
        self.pushButton_cv4.setEnabled(False)
        self.pushButton_cv5.setEnabled(False)


    # 도면 개정번호 자동 생성 (+ oid 추가)
    def drawAutoRevision(self):
        try:
            # 개정
            string_dnoList = ''
            for txt in self.chkDnoList:
                string_dnoList += txt + ";"
            URL = self.svurl + "/cad/draw/select/selectModMaxVersion.do"
            data = {'dnolist': string_dnoList}
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            self.ver_dic = {}
            for i in range(len(res)):
                self.ver_dic[res[i]['dno']] = res[i]['mver']

            # drawrel oid -> pno로 변경 (중복있다해서) 2020-03-19
            string_oidList = ''
            for txt in self.chkOidList:
                string_oidList += txt + ";"
            URL2 = self.svurl + "/cad/draw/select/selectModDrawrel.do"
            data2 = {'oidlist': string_oidList}
            print(string_oidList)
            response2 = requests.post(url=URL2, data=data2)
            json_response2 = response2.json()
            res2 = json_response2['data']
            self.drawrelInfo = []
            for val in res2:
                self.drawrelInfo.append(list(val.values()))
            print(self.drawrelInfo)
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-RC4533 , " + str(e))
            return 0

        for k in range(self.row_3):
            tableModoid = self.tableWidget_cv.item(k, 5)
            tableDno = self.tableWidget_cv.item(k, 0)
            next_ver = self.ver_dic[tableDno.text()]
            self.tableWidget_cv.setItem(k, 1, QtWidgets.QTableWidgetItem(next_ver))
            for i in range(len(self.drawrelInfo)):
                if tableModoid.text() == self.drawrelInfo[i][1]:
                    self.tableWidget_cv.setItem(k, 4, QtWidgets.QTableWidgetItem(self.drawrelInfo[i][0]))


    # 공통적용
    def copyTableCell_3(self):
        self.pushButton_cv2.setEnabled(True)
        self.pushButton_cv3.setEnabled(True)
        self.pushButton_cv4.setEnabled(True)
        self.pushButton_cv5.setEnabled(True)
        # letext = self.lineEdit_cv.text().zfill(1)   # 개정 번호
        cbtext = self.comboBox_cv.currentText()     # 개발 단계
        letext2 = self.lineEdit_cv2.text()          # EONO

        for i in range(self.row_3):
            # self.tableWidget_cv.setItem(i, 1, QtWidgets.QTableWidgetItem(letext))
            self.tableWidget_cv.setItem(i, 2, QtWidgets.QTableWidgetItem(cbtext))
            self.tableWidget_cv.setItem(i, 3, QtWidgets.QTableWidgetItem(letext2))


    # 테이블 row 단위 선택
    def selectRowData_3(self, item):
        self.selectFlag_3 = False
        self.listWidget_cv.clear()

        self.clickRow_3 = item.row()
        txt = []
        for i in range(self.col_3):
            tmp = self.tableWidget_cv.item(self.clickRow_3, i)
            if tmp is None:
                return 0
            txt.append(tmp.text())

        self.lineEdit_cv.setText(txt[1].zfill(1))            # 개정 번호
        idx = self.comboBox_cv.findText(txt[2], QtCore.Qt.MatchFixedString)
        self.comboBox_cv.setCurrentIndex(idx)                # 개발 단계
        self.lineEdit_cv2.setText(txt[3])                    # EONO
        revPart = txt[4].split(",")
        self.listWidget_cv.addItems(revPart)                 # 개정할 파트


    # 개정할 파트 삭제
    def deleteDrawrel(self):
        items = self.listWidget_cv.currentItem()
        row = self.listWidget_cv.currentRow()
        if items:
            self.listWidget_cv.takeItem(row)
            ori_pno = self.tableWidget_cv.item(self.clickRow_3, 4).text()
            del_pno = items.text()
            strIndex = ori_pno.find(del_pno)
            if strIndex == 0:           # 맨 앞 파트 삭제할때
                tmp_pno = del_pno + ","
            else:
                tmp_pno = "," + del_pno
            res_pno = ori_pno.replace(tmp_pno, "")

            if ori_pno == del_pno:      # 하나남은파트 삭제할때
                self.tableWidget_cv.setItem(self.clickRow_3, 4, QtWidgets.QTableWidgetItem(""))
            else:
                self.tableWidget_cv.setItem(self.clickRow_3, 4, QtWidgets.QTableWidgetItem(res_pno))
        else:
            self.qMessageBox("삭제할 파트를 선택하세요.")


    # 개정할 파트 추가
    def addPartRevision(self, prtoid, pno):
        ori_pno = self.tableWidget_cv.item(self.clickRow_3, 4)
        if pno in ori_pno.text():
            self.qMessageBox("이미 선택되어있는 파트번호입니다.")
        else:
            if len(ori_pno.text()) == 0:
                self.listWidget_cv.clear()
                put_pno = pno
            else:
                put_pno = ori_pno.text() + "," + pno
            self.tableWidget_cv.setItem(self.clickRow_3, 4, QtWidgets.QTableWidgetItem(put_pno))
            self.listWidget_cv.addItem(pno)


    # 데이터 실시간 변경
    def changeData_cv1(self, text):
        if self.selectFlag_3:
            return 0
        self.tableWidget_cv.setItem(self.clickRow_3, 1, QtWidgets.QTableWidgetItem(text))

    def changeData_cv2(self):
        if self.selectFlag_3:
            return 0
        text = self.comboBox_cv.currentText()
        self.tableWidget_cv.setItem(self.clickRow_3, 2, QtWidgets.QTableWidgetItem(text))

    def changeData_cv3(self, text):
        if self.selectFlag_3:
            return 0
        self.tableWidget_cv.setItem(self.clickRow_3, 3, QtWidgets.QTableWidgetItem(text))


    # 초기화
    def resetBtn(self):
        self.tableWidget_cv.clear()
        self.setInitTableHeader()
        self.drawAutoRevision()


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


    # 에러메세지 txt 파일에 떨구기
    def errorLog(self, msg):
        import datetime
        now = datetime.datetime.now()
        today = now.strftime('%Y%m%d')
        realtime = now.strftime('[%Y-%m-%d %H:%M:%S] ')
        mkfile = 'message_' + today + '.txt'
        try:
            f = open('log/' + mkfile, 'a')
            f.write(realtime + msg + '\n')
            f.close()
        except:
            raise Exception


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateVersionDialog = QtWidgets.QDialog()
    ui = Ui_CreateVersionDialog()
    ui.setupUi(CreateVersionDialog)
    CreateVersionDialog.show()
    sys.exit(app.exec_())

