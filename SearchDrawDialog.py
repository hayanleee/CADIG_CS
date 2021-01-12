# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchDraw_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_SearchDraw(object):
    def setupUi(self, Dialog_SearchDraw, get_caroid, get_dno, get_dver, get_pno, get_pver, svurl):
        Dialog_SearchDraw.setObjectName("Dialog_SearchDraw")
        Dialog_SearchDraw.setFixedSize(1020, 312)
        self.groupBox_20 = QtWidgets.QGroupBox(Dialog_SearchDraw)
        self.groupBox_20.setGeometry(QtCore.QRect(10, 10, 1001, 291))
        self.groupBox_20.setObjectName("groupBox_20")
        self.tableWidget_20 = QtWidgets.QTableWidget(self.groupBox_20)
        self.tableWidget_20.setTabKeyNavigation(False)
        self.tableWidget_20.setGeometry(QtCore.QRect(10, 20, 741, 261))
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(10)
        self.tableWidget_20.setRowCount(0)
        self.tableWidget_20.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_20.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_20.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_20.itemSelectionChanged.connect(self.thumbView)
        self.label_20 = QtWidgets.QLabel(self.groupBox_20)
        self.label_20.setGeometry(QtCore.QRect(760, 20, 231, 221))
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_20.setLineWidth(1)
        self.label_20.setObjectName("label_20")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_20.setGeometry(QtCore.QRect(880, 250, 111, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setEnabled(False)

        # 컬럼 헤더를 click 시에만 정렬
        hheader = self.tableWidget_20.horizontalHeader()
        hheader.sectionClicked.connect(self._horizontal_header_clicked)

        self.retranslateUi(Dialog_SearchDraw)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SearchDraw)

        self.data = {}
        self.svurl = svurl

        # 검색 쿼리 - 파트번호
        if len(get_pno) != 0:
            if len(get_caroid) != 0:
                self.data['get_caroid'] = get_caroid
            if len(get_pno) != 0:
                self.data['get_pno'] = get_pno
            if len(get_pver) != 0:
                self.data['get_pver'] = get_pver.zfill(1)
            self.URL = self.svurl + "/cad/draw/insert/selectSearchDraw.do"
        # 검색 쿼리 - 도면번호
        else:
            if len(get_caroid) != 0:
                self.data['get_caroid'] = get_caroid
            if len(get_dno) != 0:
                self.data['get_dno'] = get_dno
            if len(get_dver) != 0:
                self.data['get_dver'] = get_dver.zfill(1)
            self.URL = self.svurl + "/cad/draw/insert/selectSearchDraw2.do"

        self.init_tableHeader()
        self.init_searchDraw()


    def retranslateUi(self, Dialog_SearchDraw):
        _translate = QtCore.QCoreApplication.translate
        Dialog_SearchDraw.setWindowTitle(_translate("Dialog_SearchDraw", "nyPLM CAD IG"))
        Dialog_SearchDraw.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_20.setTitle(_translate("Dialog_SearchDraw", "[ 도면 선택 ]"))
        self.pushButton_20.setText(_translate("Dialog_SearchDraw", "확인"))


    # 테이블 헤더
    def init_tableHeader(self):
        column_headers = ['구분', '도면개정', '도면번호', '차종정보', '파트개정', '파트번호', '등록자', '등록일', '상태', '차종oid']
        self.tableWidget_20.setHorizontalHeaderLabels(column_headers)
        self.tableWidget_20.setColumnWidth(0, 60)
        self.tableWidget_20.setColumnWidth(1, 60)
        self.tableWidget_20.setColumnWidth(2, 100)
        self.tableWidget_20.setColumnWidth(3, 100)
        self.tableWidget_20.setColumnWidth(4, 60)
        self.tableWidget_20.setColumnWidth(5, 100)
        self.tableWidget_20.setColumnWidth(6, 70)
        self.tableWidget_20.setColumnWidth(7, 80)
        self.tableWidget_20.setColumnWidth(8, 70)
        self.tableWidget_20.setColumnWidth(9, 70)


    def init_searchDraw(self):
        try:
            response = requests.post(url=self.URL, data=self.data)
            json_response = response.json()
            res2 = json_response['data']
            self.searchDraw = []
            for val in res2:
                self.searchDraw.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-SR1025 , " + str(e))
            return 0

        self.init_tableData()


    def init_tableData(self):
        for i in range(len(self.searchDraw)):
            self.tableWidget_20.setRowCount(i + 1)
            dickey = [key for key, values in self.dic1.items() if values == self.searchDraw[i][0]]
            PRTTYPEOID = dickey[0]
            MVERSION = self.searchDraw[i][1]
            DNO = self.searchDraw[i][2]
            NAME = self.searchDraw[i][3]
            PNO = self.searchDraw[i][4]
            REGHUMID = self.searchDraw[i][5]
            date = self.searchDraw[i][6]
            REGDATE = date.replace('-','/')[:10]
            CAROID = self.searchDraw[i][7]
            STAOID = self.searchDraw[i][8]
            PVER = self.searchDraw[i][9]

            item1 = QtWidgets.QTableWidgetItem(PRTTYPEOID)
            # item2 = QtWidgets.QTableWidgetItem(int(MVERSION))
            item3 = QtWidgets.QTableWidgetItem(DNO)
            item4 = QtWidgets.QTableWidgetItem(NAME)
            item5 = QtWidgets.QTableWidgetItem(PNO)
            item6 = QtWidgets.QTableWidgetItem(REGHUMID)
            item7 = QtWidgets.QTableWidgetItem(REGDATE)
            item8 = QtWidgets.QTableWidgetItem(STAOID)
            # item9 = QtWidgets.QTableWidgetItem(int(PVER))
            item10 = QtWidgets.QTableWidgetItem(CAROID)

            item1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            # item2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item6.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item7.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item8.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            # item9.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item10.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            self.tableWidget_20.setItem(i, 0, item1)
            # self.tableWidget_20.setItem(i, 1, item2)
            # 숫자를 기준으로 정렬하기 위함 -- default는 문자임
            idx_item1 = QtWidgets.QTableWidgetItem()
            idx_item1.setData(QtCore.Qt.DisplayRole, int(MVERSION))
            idx_item1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget_20.setItem(i, 1, idx_item1)
            self.tableWidget_20.setItem(i, 2, item3)
            self.tableWidget_20.setItem(i, 3, item4)
            self.tableWidget_20.setItem(i, 5, item5)
            self.tableWidget_20.setItem(i, 6, item6)
            self.tableWidget_20.setItem(i, 7, item7)
            self.tableWidget_20.setItem(i, 8, item8)
            # self.tableWidget_20.setItem(i, 4, item9)
            # 숫자를 기준으로 정렬하기 위함 -- default는 문자임
            idx_item2 = QtWidgets.QTableWidgetItem()
            idx_item2.setData(QtCore.Qt.DisplayRole, int(PVER))
            idx_item2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget_20.setItem(i, 4, idx_item2)
            self.tableWidget_20.setItem(i, 9, item10)

        self.tableWidget_20.setSortingEnabled(False)    # 정렬기능
        self.tableWidget_20.setAlternatingRowColors(True)
        self.tableWidget_20.setColumnHidden(9, True)


    def thumbView(self):
        import urllib.request
        import urllib.parse
        from PySide2.QtGui import QPixmap
        self.pushButton_20.setEnabled(True)

        set1 = set(idx.row() for idx in self.tableWidget_20.selectedIndexes())
        rowindex = list(set1)
        self.sel_Caroid = self.tableWidget_20.item(rowindex[0], 9)
        self.sel_Dno = self.tableWidget_20.item(rowindex[0], 2)
        self.sel_Version = self.tableWidget_20.item(rowindex[0], 1)
        self.sel_CarName = self.tableWidget_20.item(rowindex[0], 3)
        self.sel_Pno = self.tableWidget_20.item(rowindex[0], 5)
        self.sel_Pver = self.tableWidget_20.item(rowindex[0], 4)
        self.sel_Stay = self.tableWidget_20.item(rowindex[0], 8)

        URL2 =  self.svurl + "/cad/draw/insert/selectSearchDrawThumb.do"
        data2 = {
            'sel_Caroid': self.sel_Caroid.text(),
            'sel_Version': self.sel_Version.text(),
            'sel_Dno': self.sel_Dno.text()
        }

        try:
            response = requests.post(url=URL2, data=data2)
            json_response = response.json()
            self.res2 = json_response['data']
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-SR1019 , " + str(e))
            return 0

        url3 =  self.svurl + "/cad/draw/insert/getThumbImage.do"
        if len(self.res2) != 0:
            fpath = self.res2[0].get('filepath')
            fname = self.res2[0].get('filename')
        else:
            self.label_20.clear()
            return 0

        data3 = urllib.parse.urlencode({'filepath': fpath[1:], 'filename': fname}).encode()
        try:
            image = urllib.request.urlopen(url3, data3).read()
        except urllib.request.URLError as e:
            self.errorLog("ERROR-SR1 , " + str(e.reason))
            return 0

        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(230, 220)
        # pixmap = pixmap.scaledToHeight(240)  # 사이즈가 조정
        self.label_20.setPixmap(pixmap)


    def _horizontal_header_clicked(self, idx):
        """
        컬럼 헤더 click 시에만, 정렬하고, 다시 정렬기능 off 시킴
         -- 정렬기능 on 시켜놓으면, 값 바뀌면 바로 자동으로 data 순서 정렬되어 바뀌어 헷갈린다..
        :param idx -->  horizontalheader index; 0, 1, 2,...
        :return:
        """
        self.tableWidget_20.setSortingEnabled(True)  # 정렬기능 on
        self.tableWidget_20.setSortingEnabled(False)  # 정렬기능 off


    # 에러메세지 txt 파일에 떨구기
    def errorLog(self, msg):
        import datetime
        now = datetime.datetime.now()
        today = now.strftime('%Y%m%d')
        realtime = now.strftime('[%Y-%m-%d %H:%M:%S] ')
        mkfile = 'message_' + today + '.txt'
        f = open('log/' + mkfile, 'a')
        f.write(realtime + msg + '\n')
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_SearchDraw = QtWidgets.QDialog()
    ui = Ui_Dialog_SearchDraw()
    ui.setupUi(Dialog_SearchDraw)
    Dialog_SearchDraw.show()
    sys.exit(app.exec_())

