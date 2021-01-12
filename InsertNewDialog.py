# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertNew_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from ftplib import FTP_TLS
import ftplib
import requests
import hashlib
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_InsertNew(object):
    def setupUi(self, Dialog_InsertNew, files, fpath, rootFile, id, pw):
        Dialog_InsertNew.setObjectName("Dialog_InsertNew")
        Dialog_InsertNew.setFixedSize(1032, 602)
        # Dialog_InsertNew.setFixedSize(1032, 625)          # for progress bar
        self.groupBox_40 = QtWidgets.QGroupBox(Dialog_InsertNew)
        self.groupBox_40.setGeometry(QtCore.QRect(10, 10, 231, 581))
        self.groupBox_40.setObjectName("groupBox_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_40)
        self.pushButton_41.setGeometry(QtCore.QRect(10, 500, 211, 31))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_41.clicked.connect(self.tableDataClear_2)
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_40)
        self.pushButton_42.setGeometry(QtCore.QRect(10, 540, 211, 31))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_40)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 460, 211, 31))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_40.clicked.connect(self.copyTableCell_2)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_40.setGeometry(QtCore.QRect(80, 32, 111, 20))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_40.textChanged.connect(self.changeData_n)
        self.lineEdit_40.setEnabled(False)
        self.label_40 = QtWidgets.QLabel(self.groupBox_40)
        self.label_40.setGeometry(QtCore.QRect(13, 33, 57, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_40)
        self.label_41.setGeometry(QtCore.QRect(13, 64, 57, 16))
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_40)
        self.label_42.setGeometry(QtCore.QRect(13, 95, 57, 16))
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_40)
        self.label_43.setGeometry(QtCore.QRect(13, 126, 57, 16))
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_40)
        self.label_44.setGeometry(QtCore.QRect(13, 157, 57, 16))
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_40)
        self.label_45.setGeometry(QtCore.QRect(13, 188, 57, 16))
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_40)
        self.label_46.setGeometry(QtCore.QRect(13, 219, 57, 16))
        # self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_40)
        self.label_47.setGeometry(QtCore.QRect(13, 250, 57, 16))
        # self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_40)
        self.label_48.setGeometry(QtCore.QRect(13, 281, 57, 16))
        # self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_40)
        self.label_49.setGeometry(QtCore.QRect(13, 312, 57, 16))
        # self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_401 = QtWidgets.QLabel(self.groupBox_40)
        self.label_401.setGeometry(QtCore.QRect(13, 343, 57, 16))
        self.label_401.setFont(font)
        self.label_401.setObjectName("label_401")
        self.label_402 = QtWidgets.QLabel(self.groupBox_40)
        self.label_402.setGeometry(QtCore.QRect(13, 374, 57, 16))
        self.label_402.setFont(font)
        self.label_402.setObjectName("label_402")
        self.comboBox_40 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_40.setObjectName("comboBox_40")
        self.comboBox_40.setGeometry(QtCore.QRect(81, 63, 139, 20))
        self.lineEdit_41 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_41.setGeometry(QtCore.QRect(81, 94, 139, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_41.setEnabled(False)
        self.lineEdit_41.textChanged.connect(self.changeData_n2)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_42.setGeometry(QtCore.QRect(81, 125, 139, 20))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_42.textChanged.connect(self.changeData_n3)
        self.lineEdit_42.setValidator(QtGui.QIntValidator(0, 99))
        self.lineEdit_42.setMaxLength(2)
        self.lineEdit_42.setEnabled(False)
        self.comboBox_41 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_41.setGeometry(QtCore.QRect(81, 156, 139, 20))
        self.comboBox_41.setObjectName("comboBox_41")
        self.comboBox_42 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_42.setGeometry(QtCore.QRect(81, 187, 139, 20))
        self.comboBox_42.setObjectName("comboBox_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_43.setGeometry(QtCore.QRect(81, 218, 139, 20))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_43.textChanged.connect(self.changeData_n4)
        self.comboBox_43 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_43.setGeometry(QtCore.QRect(81, 249, 139, 20))
        self.comboBox_43.setObjectName("comboBox_43")
        self.comboBox_44 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_44.setGeometry(QtCore.QRect(81, 280, 139, 20))
        self.comboBox_44.setObjectName("comboBox_44")
        self.comboBox_45 = QtWidgets.QComboBox(self.groupBox_40)
        self.comboBox_45.setGeometry(QtCore.QRect(81, 311, 139, 20))
        self.comboBox_45.setObjectName("comboBox_45")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_45.setGeometry(QtCore.QRect(81, 342, 139, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_45.textChanged.connect(self.changeData_n12)
        self.lineEdit_46 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_46.setGeometry(QtCore.QRect(81, 373, 139, 20))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_46.textChanged.connect(self.changeData_n13)
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_40)
        self.pushButton_43.setGeometry(QtCore.QRect(194, 31, 27, 22))
        self.pushButton_43.setObjectName("pushButton_43")
        self.tableWidget_40 = QtWidgets.QTableWidget(Dialog_InsertNew)
        self.tableWidget_40.setGeometry(QtCore.QRect(250, 16, 771, 574))
        self.tableWidget_40.setObjectName("tableWidget_40")
        self.tableWidget_40.setColumnCount(14)
        self.tableWidget_40.setRowCount(len(files))
        self.tableWidget_40.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_40.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_40.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_40.clicked.connect(self.selectRowData_2)
        # self.tableWidget_40.setStyleSheet(
        #     '''
        #     QTableWidget:item { padding-left: 10px; }
        #     '''
        # )
        self.lineEdit_44 = QtWidgets.QLineEdit(self.groupBox_40)
        self.lineEdit_44.setGeometry(QtCore.QRect(80, 380, 111, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_44.textChanged.connect(self.changeData_n11)
        self.lineEdit_44.hide()

        # self.progressBar = QtWidgets.QProgressBar(Dialog_InsertNew)
        # self.progressBar.setGeometry(QtCore.QRect(10, 599, 1011, 19))
        # self.progressBar.setObjectName("progressBar")
        # self.progressBar.setRange(0, 100)
        # self.progressBar.setStyleSheet(
        #     '''
        #     QProgressBar {
        #         text-align: center;
        #         height: 10px;
        #     }
        #     QProgressBar:chunk{
        #         background-color: #3073ad;
        #         width: 10px;
        #         margin: 1px;
        #     }
        #     '''
        # )

        self.comboBox_40.addItem("")
        # self.dic11 = {"완제품": "CCN11671", "반제품": "CCN11672", "부품": "CCN11683"}
        for i in self.dic11.keys():
            self.comboBox_40.addItem(i)
        self.comboBox_41.addItem("")
        # self.dic12 = {"일반도면": "CCN00056", "프로젝트": "CCN00057"}
        for i in self.dic12.keys():
            self.comboBox_41.addItem(i)
        self.comboBox_42.addItem("")
        # self.dic13 = {"견적도 [DT01]": "CCN00059", "요구사양도 [DT02]": "CCN00060", "승인요청도 [DT03]": "CCN00061",
        #               "승인도 [DT04]": "CCN00062",
        #               "부품도 [DT05]": "CCN11715", "임시도 [DT06]": "CCN11716", "휴면도 [DT07]": "CCN11717",
        #               "참고도 [DT08]": "CCN11718",
        #               "외래도 [DT09]": "CCN11719", "JIG도면 [DT10]": "CCN11720", "FIXTURE도면 [DT11]": "CCN11721"}
        for i in self.dic13.keys():
            self.comboBox_42.addItem(i)
        self.comboBox_43.addItem("")
        # self.dic14 = {"현대자동차 [DF01]": "CCN00077", "기아자동차 [DF02]": "CCN00078", "위아 [DF03]": "CCN00079",
        #               "지엠대우 [DF04]": "CCN00080",
        #               "르노삼성 [DF05]": "CCN00179", "쌍용자동차 [DF06]": "CCN11708", "남양넥스모 [DF07]": "CCN11709",
        #               "현대모비스 [DF08]": "CCN11710",
        #               "TRW [DF21]": "CCN11711", "BMW [DF22]": "CCN11712", "VW [DF23]": "CCN11713",
        #               "협력사 [DF09]": "CCN11714"}
        for i in self.dic14.keys():
            self.comboBox_43.addItem(i)
        self.comboBox_44.addItem("")
        # self.dic15 = {"A0": "CCN00068", "A1": "CCN00069", "A2": "CCN00070", "A3": "CCN00071", "A4": "CCN00072",
        #               "B4": "CCN00073",
        #               "B5": "CCN00074", "기타": "CCN00075"}
        for i in self.dic15.keys():
            self.comboBox_44.addItem(i)
        self.comboBox_45.addItem("")
        # self.dic16 = {"선행": "CCN11960", "T-CAR": "CCN11961", "PROTO": "CCN11678", "PILOT1": "CCN11679",
        #               "PILOT2": "CCN1180", "M": "CCN11962", "SOP": "CCN11681"}
        for i in self.dic16.keys():
            self.comboBox_45.addItem(i)

        self.retranslateUi(Dialog_InsertNew)
        QtCore.QMetaObject.connectSlotsByName(Dialog_InsertNew)

        self.col_2 = self.tableWidget_40.columnCount()
        self.row_2 = self.tableWidget_40.rowCount()
        self.regid = id
        self.regpw = pw
        self.fpath = fpath
        self.new_files = files      # new_files_2
        self.rootFile = rootFile

        idx = self.comboBox_41.findText('일반도면', QtCore.Qt.MatchFixedString)
        self.comboBox_41.setCurrentIndex(idx)

        self.setInitTableWidget_2()
        self.comboBox_40.currentIndexChanged.connect(self.changeData_n5)
        self.comboBox_41.currentIndexChanged.connect(self.changeData_n6)
        self.comboBox_42.currentIndexChanged.connect(self.changeData_n7)
        self.comboBox_43.currentIndexChanged.connect(self.changeData_n8)
        self.comboBox_44.currentIndexChanged.connect(self.changeData_n9)
        self.comboBox_45.currentIndexChanged.connect(self.changeData_n10)


    def retranslateUi(self, Dialog_InsertNew):
        _translate = QtCore.QCoreApplication.translate
        Dialog_InsertNew.setWindowTitle(_translate("Dialog_InsertNew", "nyPLM CAD IG"))
        Dialog_InsertNew.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_40.setTitle(_translate("Dialog_InsertNew", "[ 신규 등록 ]"))
        self.pushButton_41.setText(_translate("Dialog_InsertNew", "초  기  화"))
        self.pushButton_42.setText(_translate("Dialog_InsertNew", "등       록"))
        self.pushButton_40.setText(_translate("Dialog_InsertNew", "공통 적용"))
        self.label_40.setText(_translate("Dialog_InsertNew", "차종정보:"))
        self.label_41.setText(_translate("Dialog_InsertNew", "제품구분:"))
        self.label_42.setText(_translate("Dialog_InsertNew", "도면번호:"))
        self.label_43.setText(_translate("Dialog_InsertNew", "도면개정:"))
        self.label_44.setText(_translate("Dialog_InsertNew", "도면구분:"))
        self.label_45.setText(_translate("Dialog_InsertNew", "도면종류:"))
        self.label_46.setText(_translate("Dialog_InsertNew", "EONO:"))
        self.label_47.setText(_translate("Dialog_InsertNew", "도면출처:"))
        self.label_48.setText(_translate("Dialog_InsertNew", "도면크기:"))
        self.label_49.setText(_translate("Dialog_InsertNew", "개발단계:"))
        self.label_401.setText(_translate("Dialog_InsertNew", "파트번호:"))
        self.label_402.setText(_translate("Dialog_InsertNew", "도면명:"))
        self.pushButton_43.setText(_translate("Dialog_InsertNew", "..."))


    # 테이블 초기 셋팅
    def setInitTableWidget_2(self):
        self.selectFlag_2 = True
        self.checkBoxList = [QtWidgets.QCheckBox() for i in range(self.row_2)]

        column_headers = ['파일명', '파트번호', '도면번호', '차종정보', '제품구분', '도면개정', '도면구분',
                          '도면종류', 'EONO', '도면출처', '도면크기', '개발단계', '차종넘버', '도면명']
        self.tableWidget_40.setHorizontalHeaderLabels(column_headers)
        for i in range(self.row_2):
            self.tableWidget_40.setCellWidget(i, 0, self.checkBoxList[i])
            self.tableWidget_40.setItem(i, 0, QtWidgets.QTableWidgetItem("    " + self.new_files[i]))
            self.checkBoxList[i].setCheckState(QtCore.Qt.Checked)
            # 최상위 파일은 체크박스 선택 디폴트
            if self.new_files[i] == self.rootFile:
                self.checkBoxList[i].setEnabled(False)

        self.tableWidget_40.setAlternatingRowColors(True)
        self.pushButton_41.setEnabled(False)
        self.pushButton_42.setEnabled(False)

        # 좋은거있어서노트.. (C++ 만인듯?)
        # 마지막 열의 크기가 안맞을 경우 보기 안좋을 수 있는데
        # 마지막 컬럼 사이즈를 테이블 width에 맞추는 방법.
        # ui -> QTableWidget -> horizontalHeader() -> setStretchLastSection(true);


    # 공통 적용
    def copyTableCell_2(self):
        self.pushButton_41.setEnabled(True)
        self.pushButton_42.setEnabled(True)
        letext_1 = self.lineEdit_40.text()              # 차종정보
        # letext_2 = self.lineEdit_41.text()              # 도면번호
        letext_3 = self.lineEdit_42.text().zfill(1)     # 도면개정
        letext_4 = self.lineEdit_43.text()              # EONO
        # cbtext_1 = self.comboBox_40.currentText()       # 제품구분
        cbtext_2 = self.comboBox_41.currentText()       # 도면구분
        cbtext_3 = self.comboBox_42.currentText()       # 도면종류
        cbtext_4 = self.comboBox_43.currentText()       # 도면출처
        cbtext_5 = self.comboBox_44.currentText()       # 도면크기
        cbtext_6 = self.comboBox_45.currentText()       # 개발단계
        letext_6 = self.lineEdit_45.text()              # 파트번호
        letext_5 = self.lineEdit_44.text()              # 차종넘버
        letext_7 = self.lineEdit_46.text()              # 도면명

        try:
            # 채번 가져오기 - 도면번호
            URL1 = self.svurl + "/cad/draw/select/selectComtecopseq2.do"
            data1 = {
                'id': 'CAV_ID',
                'seq': self.row_2
            }
            response1 = requests.post(url=URL1, data=data1)
            json_response1 = response1.json()
            res1 = json_response1['data']
            self.dno_seq = []
            for val in res1:
                self.dno_seq.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.qMessageBox("도면번호 채번을 가져오지 못했습니다.")
            self.errorLog("ERROR-IR2123 , " + str(e))
            return 0

        for i in range(self.row_2):
            fname = self.tableWidget_40.item(i, 0).text().lstrip()
            ind = 0
            if '.CATProduct' in fname:
                if fname != self.rootFile:
                    ind = self.comboBox_40.findText('반제품', QtCore.Qt.MatchFixedString)
                else:
                    ind = self.comboBox_40.findText('완제품', QtCore.Qt.MatchFixedString)
            # elif '.CATPart' in fname or '.CATDrawing':
            elif '.CATPart' in fname:
                ind = self.comboBox_40.findText('부품', QtCore.Qt.MatchFixedString)
            self.comboBox_40.setCurrentIndex(ind)
            cbtext_1 = self.comboBox_40.currentText()

            seq = int(self.dno_seq[0][1]) + i
            dno = 'CAV' + str(seq).zfill(6)
            self.tableWidget_40.setItem(i, 3, QtWidgets.QTableWidgetItem(letext_1))
            self.tableWidget_40.setItem(i, 4, QtWidgets.QTableWidgetItem(cbtext_1))
            self.tableWidget_40.setItem(i, 2, QtWidgets.QTableWidgetItem(dno))
            self.tableWidget_40.setItem(i, 5, QtWidgets.QTableWidgetItem(letext_3))
            self.tableWidget_40.setItem(i, 6, QtWidgets.QTableWidgetItem(cbtext_2))
            self.tableWidget_40.setItem(i, 7, QtWidgets.QTableWidgetItem(cbtext_3))
            self.tableWidget_40.setItem(i, 8, QtWidgets.QTableWidgetItem(letext_4))
            self.tableWidget_40.setItem(i, 9, QtWidgets.QTableWidgetItem(cbtext_4))
            self.tableWidget_40.setItem(i, 10, QtWidgets.QTableWidgetItem(cbtext_5))
            self.tableWidget_40.setItem(i, 11, QtWidgets.QTableWidgetItem(cbtext_6))
            self.tableWidget_40.setItem(i, 1, QtWidgets.QTableWidgetItem(letext_6.upper()))
            self.tableWidget_40.setItem(i, 12, QtWidgets.QTableWidgetItem(letext_5))
            self.tableWidget_40.setItem(i, 13, QtWidgets.QTableWidgetItem(fname))


    # 테이블 row 단위 선택
    def selectRowData_2(self, item):
        self.selectFlag_2 = False

        self.clickRow_2 = item.row()
        txt = []
        for i in range(self.col_2):
            tmp = self.tableWidget_40.item(self.clickRow_2, i)
            if tmp is None:
                return 0
            txt.append(tmp.text())

        self.lineEdit_40.setText(txt[3])  # 차종정보
        self.lineEdit_41.setText(txt[2])  # 도면번호
        self.lineEdit_42.setText(txt[5])  # 도면개정
        self.lineEdit_43.setText(txt[8])  # EONO
        self.lineEdit_45.setText(txt[1])  # 파트번호
        self.lineEdit_44.setText(txt[12])  # 차종넘버
        self.lineEdit_46.setText(txt[13])  # 도면명

        index_1 = self.comboBox_40.findText(txt[4], QtCore.Qt.MatchFixedString)
        index_2 = self.comboBox_41.findText(txt[6], QtCore.Qt.MatchFixedString)
        index_3 = self.comboBox_42.findText(txt[7], QtCore.Qt.MatchFixedString)
        index_4 = self.comboBox_43.findText(txt[9], QtCore.Qt.MatchFixedString)
        index_5 = self.comboBox_44.findText(txt[10], QtCore.Qt.MatchFixedString)
        index_6 = self.comboBox_45.findText(txt[11], QtCore.Qt.MatchFixedString)

        self.comboBox_40.setCurrentIndex(index_1)  # 제품구분
        self.comboBox_41.setCurrentIndex(index_2)  # 도면구분
        self.comboBox_42.setCurrentIndex(index_3)  # 도면종류
        self.comboBox_43.setCurrentIndex(index_4)  # 도면출처
        self.comboBox_44.setCurrentIndex(index_5)  # 도면크기
        self.comboBox_45.setCurrentIndex(index_6)  # 개발단계


    # 신규등록 에러잡기
    def registNew_CatchError(self):
        for row in range(self.row_2):
            # 미등록 도면은 체크안함 - 2020.12.09
            if self.checkBoxList[row].isChecked():
                for col in range(self.col_2):
                    # EONO, 도면출처, 도면크기, 개발단계는 필수값 제외함 - 2020.12.03
                    if col == 8 or col == 9 or col == 10 or col == 11:
                        continue

                    cell = self.tableWidget_40.item(row, col)
                    if len(cell.text()) == 0:
                        self.qMessageBox("비어있는칸이 있습니다.")
                        return 'no'

        tmp_pno = []
        for tmprow in range(self.row_2):
            if self.checkBoxList[tmprow].isChecked():
                temp = self.tableWidget_40.item(tmprow, 1)
                tmp_pno.append(temp.text())
        if len(tmp_pno) != len(set(tmp_pno)):
            self.qMessageBox("중복된 파트번호를 작성했습니다. 중복을 제거해주세요.")
            return 'no'

        put_pno = ''
        for i in range(self.row_2):
            pno = self.tableWidget_40.item(i, 1).text()
            put_pno += pno + ";"

        try:
            URL = self.svurl + "/cad/draw/select/selectRegCatchError3.do"
            data = {
                'put_pno': put_pno
            }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            self.prtInfo = []
            db_pno = []
            for val in res:
                self.prtInfo.append(list(val.values()))
                db_pno.append(list(val.values())[1])
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR1556 , " + str(e))
            return 'no'

        noPrt = list(set(tmp_pno) - set(db_pno))
        if len(noPrt) != 0:
            self.qMessageBox("일치하는 파트번호 정보가 없습니다. \n (" + str(noPrt[0]) + ")")
            return 'no'

        for idx in range(len(self.prtInfo)):
            if self.prtInfo[idx][2] == "CCN00196":
                self.qMessageBox("승인 상태인 파트번호입니다. \n (" + self.prtInfo[idx][1] + ")")
                return 'no'


    ############################ ▽ 부품만 신규등록 ############################

    # .wrl 파일 생성
    def onlypart_CATPtoWrl(self):
        import subprocess
        try:
            self.op_CATPtoWrl = []
            for fname in self.new_files:
                cmd = "CATPtoWrl.exe \"" + self.fpath + "\" \"" + fname + "\""
                return_code = subprocess.call(cmd, shell=True)

                # return_code = 0 is success
                if not return_code:
                    print("- success : " + fname)
                    notype = fname[:fname.rfind('.')]
                    self.op_CATPtoWrl.append(notype + ".wrl")
                else:
                    self.errorLog("ERROR-op-CATPtoWrl() , cmd return_code is not 0 : " + fname)
                    continue
        except Exception as e:
            self.errorLog("ERROR-IR1620 , " + str(e))
            raise Exception('< Exception func > onlypart_CATPtoWrl')


    # CATDrawing 파일 존재시 PDF 변환
    def onlypart_CATDrawing_PDF(self):
        import subprocess
        import os, fnmatch

        try:
            self.op_CATDrawing_and_Pdf = []
            for fn in self.fnameNoType:
                fname = fn + ".CATDrawing"
                if os.path.isfile(self.fpath + "\\" + fname):
                    cmd = "CATDrawingToPdf.exe \"" + self.fpath + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)
                    self.op_CATDrawing_and_Pdf.append(fn + ".CATDrawing")

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fn)
                    else:
                        self.errorLog("ERROR-IS12 , cmd return_code is not 0 : " + fname)
                        self.noConvertFile.append(fname)
                        continue

                    file_list = fnmatch.filter(os.listdir(self.fpath), fn + "*")
                    pdf_dic = {}
                    for tmpfname in file_list:
                        if '.pdf' in tmpfname:
                            fsize = os.path.getsize(self.fpath + "\\" + tmpfname)
                            pdf_dic[tmpfname] = fsize

                    if len(pdf_dic) > 0:
                        pdf_rfilename = max(pdf_dic.keys(), key=(lambda k: pdf_dic[k]))
                        if len(pdf_rfilename) != 0:
                            os.rename(self.fpath + "\\" + pdf_rfilename, self.fpath + "\\" + fn + ".pdf")
                            self.op_CATDrawing_and_Pdf.append(fn + ".pdf")
        except Exception as e:
            self.errorLog("ERROR-IR1621 , " + str(e))
            raise Exception('< Exception func > onlypart_CATDrawing_PDF')


    # 파일 업로드
    def onlypart_FileUpload(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        mkdirFlag = True
        self.makedir = "\\viz\\ebom\\" + self.regid + nowTime
        alluploadFile = self.new_files + self.op_CATDrawing_and_Pdf + self.op_CATPtoWrl

        for upFile in alluploadFile:
            if os.path.isfile(self.fpath + "\\" + upFile):
                try:
                    Output_Directory = self.makedir
                    ftps = FTP_TLS(self.ftphost)
                    ftps.login(self.ftpid, self.ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    if mkdirFlag:
                        ftps.mkd(self.makedir)
                        mkdirFlag = False
                    ftps.cwd(Output_Directory)
                    with open(self.fpath + '\\' + upFile, 'rb') as ftpup:
                        ftps.storbinary('STOR %s' % upFile, ftpup)
                    ftps.quit()
                    ftpup.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-IF312 , " + str(err))
                    raise Exception('< Exception func > onlypart upload')


    def onlyPart_makeData(self):
        try:
            self.onlyPart_ModData = ""
            for i in range(self.row_2):
                if self.checkBoxList[i].isChecked():
                    filename = self.tableWidget_40.item(i, 0).text().lstrip()
                    caroid = self.tableWidget_40.item(i, 12).text()
                    prttypeoid = self.dic11[self.tableWidget_40.item(i, 4).text()]
                    dno = self.tableWidget_40.item(i, 2).text()
                    mversion = self.tableWidget_40.item(i, 5).text()
                    moduletype = self.dic12[self.tableWidget_40.item(i, 6).text()]
                    modtypeoid = self.dic13[self.tableWidget_40.item(i, 7).text()]
                    eono = ''
                    if len(self.tableWidget_40.item(i, 8).text()) == 0:
                        eono = '-'
                    else:
                        eono = self.tableWidget_40.item(i, 8).text()
                    dscoid = ''
                    if len(self.tableWidget_40.item(i, 9).text()) == 0:
                        dscoid = '-'
                    else:
                        dscoid = self.dic14[self.tableWidget_40.item(i, 9).text()]
                    modsizeoid = ''
                    if len(self.tableWidget_40.item(i, 10).text()) == 0:
                        modsizeoid = '-'
                    else:
                        modsizeoid = self.dic15[self.tableWidget_40.item(i, 10).text()]
                    devstep = ''
                    if len(self.tableWidget_40.item(i, 11).text()) == 0:
                        devstep = '-'
                    else:
                        devstep = self.dic16[self.tableWidget_40.item(i, 11).text()]
                    pno = self.tableWidget_40.item(i, 1).text()
                    dnam = self.tableWidget_40.item(i, 13).text()

                    self.onlyPart_ModData += filename + ";"
                    self.onlyPart_ModData += caroid + ";"
                    self.onlyPart_ModData += prttypeoid + ";"
                    self.onlyPart_ModData += dno + ";"
                    self.onlyPart_ModData += mversion + ";"
                    self.onlyPart_ModData += moduletype + ";"
                    self.onlyPart_ModData += modtypeoid + ";"
                    self.onlyPart_ModData += eono + ";"
                    self.onlyPart_ModData += dscoid + ";"
                    self.onlyPart_ModData += modsizeoid + ";"
                    self.onlyPart_ModData += devstep + ";"
                    self.onlyPart_ModData += pno + ";"
                    self.onlyPart_ModData += dnam + "|"
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR2654 , " + str(e))
            raise Exception('< Exception func > onlyPart_makeData')


    def requestOnlyPart(self):
        print("------------- onlyPart server start --------------")
        string_notypeFname = ''
        for txt in self.fnameNoType:
            string_notypeFname += txt + ";"

        thumb_dir = self.svdraw + self.makedir
        cmd_thumb = "VIZCoreTrans.exe -i \"" + thumb_dir + "\\"
        cmd_thumb2 = "\" -o \"" + thumb_dir + "\" -mode i -iw 400 -ih 300 -subimg t -info t -path path -log 2"
        URL = self.svurl + "/cad/draw/insert/insertNewOnlyPart.do"

        data = {
            'id': self.regid,
            'pwd': self.regpw,
            'thumb_dir': thumb_dir,
            'notypeFname': string_notypeFname,
            'moddata': self.onlyPart_ModData,
            'cmd_thumb': cmd_thumb,
            'cmd_thumb2': cmd_thumb2
        }

        try:
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            print('-' * 10 + " resultMsg " + '-' * 10)
            print(json_response['resultMsg'])
            self.resp_result = json_response['resultMsg']
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR2257 , " + str(e))
            raise Exception('< Exception func > requestOnlyPart')


    ############################ ▽ 전체 신규등록 ############################

    # .wrl 파일 생성
    def insert_CATPtoWrl(self):
        import subprocess
        try:
            self.CATPtoWrl = []
            for fname in self.new_files:
                cmd = "CATPtoWrl.exe \"" + self.fpath + "\" \"" + fname + "\""
                return_code = subprocess.call(cmd, shell=True)

                # return_code = 0 is success
                if not return_code:
                    print("- success : " + fname)
                    notype = fname[:fname.rfind('.')]
                    self.CATPtoWrl.append(notype + ".wrl")
                else:
                    self.errorLog("ERROR-new-CATPtoWrl() , cmd return_code is not 0 : " + fname)
                    continue
        except Exception as e:
            self.errorLog("ERROR-IE1623 , " + str(e))
            raise Exception('< Exception func > insert_CATPtoWrl')


    # CATDrawing, PDF 파일 insert
    def insert_CATDrawing_PDF(self):
        import subprocess
        import os, fnmatch

        try:
            fn_noExtension = list(set(list([item[:item.rfind('.')] for item in self.new_files])))

            self.CATDrawing_and_Pdf = []
            for fn in fn_noExtension:
                fname = fn + ".CATDrawing"
                if os.path.isfile(self.fpath + "\\" + fname):
                    cmd = "CATDrawingToPdf.exe \"" + self.fpath + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)
                    self.CATDrawing_and_Pdf.append(fname)

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fn)
                    else:
                        self.errorLog("ERROR-IS1 , cmd return_code is not 0 : " + fname)
                        self.noConvertFile.append(fname)
                        continue

                    file_list = fnmatch.filter(os.listdir(self.fpath), fn + "*")
                    pdf_dic = {}
                    for tmpfname in file_list:
                        if '.pdf' in tmpfname:
                            fsize = os.path.getsize(self.fpath + "\\" + tmpfname)
                            pdf_dic[tmpfname] = fsize

                    if len(pdf_dic) > 0:
                        new_pdfName = max(pdf_dic.keys(), key=(lambda k: pdf_dic[k]))
                        if len(new_pdfName) != 0:
                            os.rename(self.fpath + "\\" + new_pdfName, self.fpath + "\\" + fn + ".pdf")
                            self.CATDrawing_and_Pdf.append(fn + ".pdf")
        except Exception as e:
            self.errorLog("ERROR-IE1624 , " + str(e))
            raise Exception('< Exception func > insert_CATDrawing_PDF')


    # 파일 업로드
    def uploadNewData(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        mkdirFlag = True
        self.makedir = "\\viz\\ebom\\" + self.regid + nowTime
        alluploadFile = self.new_files + self.CATDrawing_and_Pdf + self.CATPtoWrl

        for upFile in alluploadFile:
            if os.path.isfile(self.fpath + "\\" + upFile):
                try:
                    Output_Directory = self.makedir
                    ftps = FTP_TLS(self.ftphost)
                    ftps.login(self.ftpid, self.ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    if mkdirFlag:
                        ftps.mkd(self.makedir)
                        mkdirFlag = False
                    ftps.cwd(Output_Directory)
                    with open(self.fpath + '\\' + upFile, 'rb') as ftpup:
                        ftps.storbinary('STOR %s' % upFile, ftpup)
                    ftps.quit()
                    ftpup.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-IF31 , " + str(err))
                    raise Exception('< Exception func > uploadNewData')


    # DB data 만들기
    def newRegMakeData(self):
        try:
            self.new_ModData = ""
            for i in range(self.row_2):
                if self.checkBoxList[i].isChecked():
                    filename = self.tableWidget_40.item(i, 0).text().lstrip()
                    caroid = self.tableWidget_40.item(i, 12).text()
                    prttypeoid = self.dic11[self.tableWidget_40.item(i, 4).text()]
                    dno = self.tableWidget_40.item(i, 2).text()
                    mversion = self.tableWidget_40.item(i, 5).text()
                    moduletype = self.dic12[self.tableWidget_40.item(i, 6).text()]
                    modtypeoid = self.dic13[self.tableWidget_40.item(i, 7).text()]
                    eono = ''
                    if len(self.tableWidget_40.item(i, 8).text()) == 0:
                        eono = '-'
                    else:
                        eono = self.tableWidget_40.item(i, 8).text()
                    dscoid = ''
                    if len(self.tableWidget_40.item(i, 9).text()) == 0:
                        dscoid = '-'
                    else:
                        dscoid = self.dic14[self.tableWidget_40.item(i, 9).text()]
                    modsizeoid = ''
                    if len(self.tableWidget_40.item(i, 10).text()) == 0:
                        modsizeoid = '-'
                    else:
                        modsizeoid = self.dic15[self.tableWidget_40.item(i, 10).text()]
                    devstep = ''
                    if len(self.tableWidget_40.item(i, 11).text()) == 0:
                        devstep = '-'
                    else:
                        devstep = self.dic16[self.tableWidget_40.item(i, 11).text()]
                    pno = self.tableWidget_40.item(i, 1).text()
                    dnam = self.tableWidget_40.item(i, 13).text()

                    self.new_ModData += filename + ";"
                    self.new_ModData += caroid + ";"
                    self.new_ModData += prttypeoid + ";"
                    self.new_ModData += dno + ";"
                    self.new_ModData += mversion + ";"
                    self.new_ModData += moduletype + ";"
                    self.new_ModData += modtypeoid + ";"
                    self.new_ModData += eono + ";"
                    self.new_ModData += dscoid + ";"
                    self.new_ModData += modsizeoid + ";"
                    self.new_ModData += devstep + ";"
                    self.new_ModData += pno + ";"
                    self.new_ModData += dnam + "|"
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR0409 , " + str(e))
            raise Exception('< Exception func > newRegMakeData')


    # request to server
    def requestNewData(self):
        print("------------- new server start --------------")
        thumb_dir = self.svdraw + self.makedir
        path_1 = self.svdraw + self.makedir + "\\" + self.rootFile
        path_2 = self.svdraw + self.makedir + "\\" + self.rootFile + "_result.xml"
        cmd_xml = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + path_2 + "\" -mode xml -fs t -att t -info t -path path -log 2"
        cmd_thumb = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + thumb_dir + "\" -mode i -iw 400 -ih 300 -subimg t -info t -log 2"
        # cmd_thumb = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + thumb_dir + "\" -mode i -iq 100 -iw 2048 -ih 2048 -subimg t -info t -log 2"

        # Creo 는 -path 옵션 안붙어
        # cmd_xml = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + path_2 + "\" -mode xml -fs t -att t -info t -log 2"
        # cmd_thumb = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + thumb_dir + "\" -mode i -iw 400 -ih 300 -subimg t -info t -log 2"

        URL = self.svurl + "/cad/draw/insert/insertNewRegistEBOM.do"

        data = {
            'id': self.regid,
            'pwd': self.regpw,
            'thumb_dir': thumb_dir,
            'path_1': path_1,
            'path_2': path_2,
            'cmd_xml': cmd_xml,
            'cmd_thumb': cmd_thumb,
            'put_staoid': self.selectStaoid,
            'moddata': self.new_ModData
        }

        try:
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            print('-' * 10 + " resultMsg " + '-' * 10)
            print(json_response['resultMsg'])
            self.resp_result = json_response['resultMsg']
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR33 , " + str(e))
            raise Exception('< Exception func > requestNewData')


    # 만들어진 서버 폴더 삭제
    def delete_mkdir(self):
        try:
            ftps = FTP_TLS(self.ftphost)
            ftps.login(self.ftpid, self.ftppw)
            ftps.encoding = 'utf-8'
            ftps.prot_p()
            ftps.cwd(self.makedir)
            for something in ftps.nlst():
                ftps.delete(something)
            ftps.rmd(".." + self.makedir[self.makedir.rfind("\\"):])
            ftps.quit()
        except ftplib.all_errors as err:
            self.errorLog("ERROR-IF234 , " + str(err))
            raise Exception('< Exception func > delete_mkdir')


    # 데이터 실시간 변경
    def changeData_n(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 3, QtWidgets.QTableWidgetItem(text))

    def changeData_n2(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 2, QtWidgets.QTableWidgetItem(text))

    def changeData_n3(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 5, QtWidgets.QTableWidgetItem(text))

    def changeData_n4(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 8, QtWidgets.QTableWidgetItem(text))

    def changeData_n5(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_40.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 4, QtWidgets.QTableWidgetItem(text))

    def changeData_n6(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_41.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 6, QtWidgets.QTableWidgetItem(text))

    def changeData_n7(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_42.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 7, QtWidgets.QTableWidgetItem(text))

    def changeData_n8(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_43.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 9, QtWidgets.QTableWidgetItem(text))

    def changeData_n9(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_44.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 10, QtWidgets.QTableWidgetItem(text))

    def changeData_n10(self):
        if self.selectFlag_2:
            return 0
        text = self.comboBox_45.currentText()
        self.tableWidget_40.setItem(self.clickRow_2, 11, QtWidgets.QTableWidgetItem(text))

    def changeData_n11(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 12, QtWidgets.QTableWidgetItem(text))

    def changeData_n12(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 1, QtWidgets.QTableWidgetItem(text.upper()))

    def changeData_n13(self, text):
        if self.selectFlag_2:
            return 0
        self.tableWidget_40.setItem(self.clickRow_2, 13, QtWidgets.QTableWidgetItem(text.upper()))


    # 초기화
    def tableDataClear_2(self):
        self.tableWidget_40.clear()
        self.setInitTableWidget_2()


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


    # 메세지박스 (선택)
    def qMessageBox_Select(self, msg):
        buttonReply = QtWidgets.QMessageBox.question(self, 'Message', msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            return 'yes'
        else:
            return 'no'


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
    Dialog_InsertNew = QtWidgets.QDialog()
    ui = Ui_Dialog_InsertNew()
    ui.setupUi(Dialog_InsertNew)
    Dialog_InsertNew.show()
    sys.exit(app.exec_())

