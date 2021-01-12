import sys
import requests
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from pywin.dialogs import login

from LoginForm import Ui_Login
from MainWindow import Ui_MainWindow
# from CancleDialog import Ui_Dialog_Cancle
from SearchDrawDialog import Ui_Dialog_SearchDraw
from HistoryDialog import Ui_Dialog_History
from SelectCar import Ui_Dialog_SelectCar
from InsertAddDialog import Ui_Dialog_InsertAdd
from InsertNewDialog import Ui_Dialog_InsertNew
from ConfigDialog import Ui_Dialog_config
from CreateVerDialog import Ui_CreateVersionDialog
from partSearchDialog import Ui_PartSearchDialog
import os
os.environ['NLS_LANG'] = '.UTF8'


class ConfigDialog(QDialog, Ui_Dialog_config):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_conf3.clicked.connect(self.savePath)


    def savePath(self):
        # self.parent().statusbar.showMessage("경로 적용중..")
        self.parent().label_11.setText(self.lineEdit_conf.text())
        self.parent().lineEdit.setText(self.lineEdit_conf2.text())
        # self.parent().newRegInit()
        # self.parent().statusbar.showMessage("")
        self.close()


class SearchPart(QDialog, Ui_PartSearchDialog):
    def __init__(self, parent=None):
        super(SearchPart, self).__init__(parent)
        svurl = self.parent().svurl
        self.setupUi(self, svurl)
        self.pushButton2.clicked.connect(self.choicePart)


    def choicePart(self):
        set1 = set(idx.row() for idx in self.tableWidget.selectedIndexes())
        rowindex = list(set1)
        addpart_oid = self.tableWidget.item(rowindex[0], 7)
        addpart_pno = self.tableWidget.item(rowindex[0], 2)
        self.parent().addPartRevision(addpart_oid.text(), addpart_pno.text())
        self.close()


class CreateVerDialog(QDialog, Ui_CreateVersionDialog):
    def __init__(self, parent=None):
        super(CreateVerDialog, self).__init__(parent)
        self.dic_cv = self.parent().ccn_dic16
        self.chkMod = self.parent().selectCheckMod
        svurl = self.parent().cfg_svurl
        self.setupUi(self, svurl)
        self.pushButton_cv3.clicked.connect(self.saveCreateVer)
        self.pushButton_cv4.clicked.connect(self.open_SearchPart)


    def open_SearchPart(self):
        if self.selectFlag_3:
            self.qMessageBox("파트를 추가할 라인을 선택하세요.")
            return 0

        self.dialog_searchPart = SearchPart(self)
        self.dialog_searchPart.show()


    def saveCreateVer(self):
        for row in range(self.row_3):
            for col in range(self.col_3):
                # 개발단계, EONO 는 필수값 제외함 - 2020.12.07
                if col == 2 or col == 3:
                    continue

                cell = self.tableWidget_cv.item(row, col)
                if len(cell.text()) == 0:
                    self.qMessageBox("비어있는칸이 있습니다.")
                    return 0

        put_oid = ""
        put_dno = ""
        put_num = ""
        put_step = ""
        put_eono = ""
        put_prtpno = ""
        pnolist = ""

        for i in range(self.row_3):
            oid = self.tableWidget_cv.item(i, 5).text()
            dno = self.tableWidget_cv.item(i, 0).text()
            cv_num = self.tableWidget_cv.item(i, 1).text().zfill(1)
            # cv_step = self.dic_cv[self.tableWidget_cv.item(i, 2).text()]
            # eono = self.tableWidget_cv.item(i, 3).text()
            cv_step = ''
            if len(self.tableWidget_cv.item(i, 2).text()) == 0:
                cv_step = '-'
            else:
                cv_step = self.dic_cv[self.tableWidget_cv.item(i, 2).text()]
            eono = ''
            if len(self.tableWidget_cv.item(i, 3).text()) == 0:
                eono = '-'
            else:
                eono = self.tableWidget_cv.item(i, 3).text()
            prtpno = self.tableWidget_cv.item(i, 4).text()

            put_oid += oid + ";"
            put_dno += dno + ";"
            put_num += cv_num + ";"
            put_step += cv_step + ";"
            put_eono += eono + ";"
            put_prtpno += prtpno + ";"
            pnolist += prtpno + ","

        # 엮인 파트번호 전부 max값 상태확인 기능 추가 (전부 승인상태일때만 개정가능) - 2020.04.21
        try:
            URL = self.svurl + "/cad/draw/select/selectPnoMaxStaoid.do"
            data = {'pnolist': pnolist}
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            pnoStaoid= []
            for val in res:
                pnoStaoid.append(list(val.values()))

            msgPno = ""
            for tmp in pnoStaoid:
                if tmp[2] != "CCN00196":
                    msgPno += tmp[0] + ","

            if len(msgPno) != 0:
                self.qMessageBox("최신파트 상태가 '승인'이 아니어서 개정할 수 없습니다.\n승인상태가 아닌 파트명: " + msgPno)
                return 0
            else:
                self.parent().real_CheckOut_revision(put_oid, put_dno, put_num, put_step, put_prtpno, put_eono)
                self.close()
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-RC4533 , " + str(e))
            return 0


class InsertNewDialog(QDialog, Ui_Dialog_InsertNew):
    def __init__(self, parent=None):
        super(InsertNewDialog, self).__init__(parent)
        self.svurl = self.parent().cfg_svurl
        self.ftpid = self.parent().cfg_ftpid
        self.ftppw = self.parent().cfg_ftppw
        self.ftphost = self.parent().cfg_ftphost
        self.ftpport = self.parent().cfg_ftpport
        self.svdraw = self.parent().cfg_svdraw
        # self.pathcatia = self.parent().cfg_pathcatia
        self.dic11 = self.parent().ccn_dic11
        self.dic12 = self.parent().ccn_dic12
        self.dic13 = self.parent().ccn_dic13
        self.dic14 = self.parent().ccn_dic14
        self.dic15 = self.parent().ccn_dic15
        self.dic16 = self.parent().ccn_dic16

        self.get_draws = self.parent().put_draw_list
        get_fpath = self.parent().put_directoryPath
        get_rootFile = self.parent().label_13.text()
        get_id = self.parent().cfg_userid
        get_pw = self.parent().cfg_userpw

        self.setupUi(self, self.get_draws, get_fpath, get_rootFile, get_id, get_pw)
        self.pushButton_43.clicked.connect(self.open_SelectCar)
        self.pushButton_42.clicked.connect(self.div_registNew)


    def open_SelectCar(self):
        self.dialog_selectCar = SelectCar(self)
        self.dialog_selectCar.show()


    # 신규등록 구분 (Product 유/무)
    def div_registNew(self):
        self.fnameNoType = []
        cnt = 0
        for fname in self.new_files:
            if '.CATPart' in fname:
                cnt += 1
                self.fnameNoType.append(fname[:fname.rfind('.')])

        if cnt == len(self.get_draws):     # 모두 부품일때
            self.onlyPartRegist()
        else:                              # Product 파일 있을때
            self.registNew()


    # 신규등록 (파트만)
    def onlyPartRegist(self):
        catch_res = 'yes'
        catch_res = self.registNew_CatchError()     # DNO 중복, 빈칸 등 각종 에러잡기
        if catch_res == 'no':
            return 0

        self.showMinimized()
        self.parent().showMinimized()

        self.noConvertFile = []
        try:
            self.onlypart_CATPtoWrl()           # .wrl 파일 생성 추가 (2020-04-14)
            self.onlypart_CATDrawing_PDF()      # CATDrawing 파일 존재시 PDF 변환
            self.onlypart_FileUpload()          # 로컬→서버 파일 업로드
            self.onlyPart_makeData()            # DB data 만들기
            self.requestOnlyPart()              # 서버 .do 호출 (썸네일 생성) + DB data insert

            if self.resp_result == 'Success':
                self.delete_mkdir()             # 만들어진 서버 폴더 삭제
                if len(self.noConvertFile) == 0:
                    self.qMessageBox("등록이 완료되었습니다.")
                else:
                    tmp_str = ""
                    for text in self.noConvertFile:
                        tmp_str += text + "\n"
                    self.qMessageBox("도면등록이 완료되었습니다." + "\n\n- pdf변환되지 않은 도면 -\n" + tmp_str)
                self.close()
            else:
                self.errorLog("ERROR-YR4474 , " + str(self.resp_result))
                self.qMessageBox("등록에 실패했습니다.")
                self.showNormal()
        except Exception as e:
            self.errorLog("ERROR-YE2020 , " + str(e))
            self.qMessageBox("등록에 실패했습니다.")

        self.parent().showNormal()


    # 신규등록
    def registNew(self):
        catch_res = 'yes'
        catch_res = self.registNew_CatchError()  # DNO 중복, 빈칸 등 각종 에러잡기
        if catch_res == 'no':
            return 0

        assyFlag = True
        for i in range(self.row_2):
            assy = self.tableWidget_40.item(i, 4).text()
            if assy == '완제품':
                assyFlag = False

        if assyFlag:
            ret = self.qMessageBox_Select("완제품이 없습니다. 진행하시겠습니까?")
            if ret == 'no':
                return 0

        reply = self.qMessageBox_Select("\n도면확정을 하시겠습니까? \n\n(도면확정: Yes / 작업중: No)\n")
        if reply == "yes":
            self.selectStaoid = "CCN00193"
        else:
            self.selectStaoid = "CCN00192"

        self.showMinimized()
        self.parent().showMinimized()

        self.noConvertFile = []
        try:
            self.insert_CATPtoWrl()             # .wrl 파일 생성 추가 (2020-04-14)
            self.insert_CATDrawing_PDF()        # CATDrawing 파일 존재시 PDF 변환
            self.uploadNewData()                # 로컬→서버 파일 업로드
            self.newRegMakeData()               # DB data 만들기
            self.requestNewData()               # 서버 .do 호출 (썸네일 생성) + DB data insert

            if self.resp_result == 'Success':
                self.delete_mkdir()             # 만들어진 서버 폴더 삭제
                if len(self.noConvertFile) == 0:
                    self.qMessageBox("등록이 완료되었습니다.")
                else:
                    tmp_str = ""
                    for text in self.noConvertFile:
                        tmp_str += text + "\n"
                    self.qMessageBox("도면등록이 완료되었습니다." + "\n\n- pdf변환되지 않은 도면 -\n" + tmp_str)
                self.close()
            else:
                self.errorLog("ERROR-YR4474 , " + str(self.resp_result))
                self.qMessageBox("등록에 실패했습니다.")
                self.showNormal()
        except Exception as e:
            self.errorLog("ERROR-YE2001 , " + str(e))
            self.qMessageBox("등록에 실패했습니다.")

        self.parent().statusbar.showMessage("")
        self.parent().showNormal()


class InsertAddDialog(QDialog, Ui_Dialog_InsertAdd):
    def __init__(self, parent=None):
        super(InsertAddDialog, self).__init__(parent)
        self.svurl = self.parent().cfg_svurl
        self.ftpid = self.parent().cfg_ftpid
        self.ftppw = self.parent().cfg_ftppw
        self.ftphost = self.parent().cfg_ftphost
        self.ftpport = self.parent().cfg_ftpport
        self.svdraw = self.parent().cfg_svdraw
        # self.pathcatia = self.parent().cfg_pathcatia
        self.dic1 = self.parent().ccn_dic11
        self.dic2 = self.parent().ccn_dic12
        self.dic3 = self.parent().ccn_dic13
        self.dic4 = self.parent().ccn_dic14
        self.dic5 = self.parent().ccn_dic15
        self.dic6 = self.parent().ccn_dic16

        get_addfile = self.parent().put_addfile
        get_path = self.parent().put_path
        get_rootfile = self.parent().put_rootfile
        get_radioBt = self.parent().put_radioBt
        get_id = self.parent().cfg_userid
        get_pw = self.parent().cfg_userpw
        get_chkout_files = self.parent().checkout_files

        self.setupUi(self, get_addfile, get_path, get_rootfile, get_radioBt, get_id, get_pw, get_chkout_files)
        self.pushButton_53.clicked.connect(self.open_SelectCar)
        self.pushButton_52.clicked.connect(self.registAdd)


    def open_SelectCar(self):
        self.dialog_selectCar = SelectCar(self)
        self.dialog_selectCar.show()


    # 추가 등록
    def registAdd(self):
        catch_res = 'yes'
        catch_res = self.registAdd_CatchError()     # DNO 중복, 빈칸 등 각종 에러잡기
        if catch_res == 'no':
            return 0

        self.showMinimized()
        self.parent().showMinimized()

        self.noConvertFile = []
        try:
            self.add_CATPtoWrl()        # .wrl 파일 생성 추가 (2020-04-14)
            self.drawing_to_pdf()       # CATDrawing → pdf 변환 (체크아웃, 추가등록 파일만)
            self.uploadAddData()        # 로컬→서버 파일 업로드 (전부)
            self.addRegMakeData()       # DB data 만들기
            self.requestAddData()       # 서버 .do 호출 (xml ebom, 썸네일 생성)
            if self.resp_result == 'Success':
                self.delete_mkdir()  # 만들어진 서버 폴더 삭제
                if len(self.noConvertFile) == 0:
                    self.qMessageBox("등록이 완료되었습니다.")
                else:
                    tmp_str = ""
                    for text in self.noConvertFile:
                        tmp_str += text + "\n"
                    self.qMessageBox("추가등록이 완료됬습니다." + "\n\n- pdf변환되지 않은 도면 -\n" + tmp_str)
                self.close()
            else:
                self.errorLog("ERROR-YR563 , " + str(self.resp_result))
                self.qMessageBox("등록에 실패했습니다.")
                self.showNormal()
        except Exception as e:
            self.errorLog("ERROR-YE2002 , " + str(e))
            self.qMessageBox("등록에 실패했습니다.")

        self.parent().statusbar.showMessage("")
        self.parent().showNormal()


# class CancleDialog(QDialog, Ui_Dialog_Cancle):
#     def __init__(self, parent=None):
#         super(CancleDialog, self).__init__(parent)
#         get_id = self.parent().cfg_userid
#         svurl = self.parent().cfg_svurl
#         self.setupUi(self, get_id, svurl)
#         self.pushButton_60.clicked.connect(self.cancleCheckOut)
#
#
#     # 해제 버튼
#     def cancleCheckOut(self):
#         flag = True
#         for i in range(len(self.chkout_Dno_Ver_Oid)):
#             if self.getDnoVerItem[i].checkState(0) > 0:
#                 flag = False
#                 try:
#                     URL = self.svurl + "/cad/draw/insert/updateCancleDraw.do"
#                     data = {
#                         'dno': self.chkout_Dno_Ver_Oid[i][0],
#                         'mversion': self.chkout_Dno_Ver_Oid[i][1]
#                     }
#                     response = requests.post(url=URL, data=data)
#                     json_response = response.json()
#                     self.resMsg = json_response['resultMsg']
#                 except requests.exceptions.RequestException as e:
#                     self.errorLog("ERROR-CR1948 , " + str(e))
#                     return 0
#
#         if flag:
#             self.qMessageBox("도면확정 취소할 도면을 선택해주세요.")
#         else:
#             if self.resMsg == 'Success':
#                 self.qMessageBox("도면확정이 취소되었습니다.")
#                 self.close()
#             else:
#                 self.qMessageBox("ERROR")


class SelectCar(QDialog, Ui_Dialog_SelectCar):
    def __init__(self, parent=None):
        super(SelectCar, self).__init__(parent)
        cLogin = Login()
        svurl = cLogin.cfg_server_url
        self.setupUi(self, svurl)
        self.pushButton_car.clicked.connect(self.choiceCaroid)


    def choiceCaroid(self):
        flag = 0
        for i in range(len(self.engctgView_list)):
            if self.all_Items[i].checkState(0) > 0:
                flag += 1
                choice = self.all_Text[i]

        if flag == 0:
            self.qMessageBox("차종을 선택해 주세요.")
            return 0
        elif flag > 1:
            self.qMessageBox("차종을 하나만 선택해 주세요.")
            return 0

        carName = choice[:choice.find(':')]
        carOID = choice[choice.find(':')+1:]

        # print(self.parent())
        # print(type(self.parent()))
        # print(self.parent().__class__.__name__)

        clsName = self.parent().__class__.__name__
        if clsName == "MainWindow":
            self.parent().lineEdit_3.setText(carName)
            self.parent().lineEdit_6.setText(carOID)
        elif clsName == "InsertNewDialog":
            self.parent().lineEdit_40.setText(carName)
            self.parent().lineEdit_44.setText(carOID)
        elif clsName == "InsertAddDialog":
            self.parent().lineEdit_50.setText(carName)
            self.parent().lineEdit_54.setText(carOID)
        self.close()


class SearchDraw(QDialog, Ui_Dialog_SearchDraw):
    def __init__(self, parent=None):
        super(SearchDraw, self).__init__(parent)
        get_caroid = self.parent().lineEdit_6.text()
        get_dno = self.parent().lineEdit_4.text().strip()
        get_dver = self.parent().lineEdit_5.text()
        get_pno = self.parent().lineEdit_7.text().strip()
        get_pver = self.parent().lineEdit_8.text()
        svurl = self.parent().cfg_svurl
        self.dic1 = self.parent().ccn_dic11
        self.setupUi(self, get_caroid, get_dno, get_dver, get_pno, get_pver, svurl)
        self.pushButton_20.clicked.connect(self.selectRootDraw)


    def selectRootDraw(self):
        self.parent().lineEdit_3.setText(self.sel_CarName.text())
        self.parent().lineEdit_4.setText(self.sel_Dno.text())
        self.parent().lineEdit_5.setText(self.sel_Version.text())
        self.parent().lineEdit_6.setText(self.sel_Caroid.text())
        self.parent().lineEdit_7.setText(self.sel_Pno.text())
        self.parent().lineEdit_8.setText(self.sel_Pver.text())
        self.parent().search_staoid = self.sel_Stay.text()
        self.parent().statusbar.showMessage("검색 중..")
        self.parent().clickSearchModBtn()
        self.parent().statusbar.showMessage("")
        self.close()


class HistoryDialog(QDialog, Ui_Dialog_History):
    def __init__(self, parent=None):
        super(HistoryDialog, self).__init__(parent)
        self.ftpid = self.parent().cfg_ftpid
        self.ftppw = self.parent().cfg_ftppw
        self.ftphost = self.parent().cfg_ftphost
        self.ftpport = self.parent().cfg_ftpport
        self.allmodfilehistory = self.parent().allmodfilehistory
        get_dno = self.parent().selDno
        self.download_path = self.parent().label_11.text()
        self.setupUi(self, get_dno)
        self.down_action_2.triggered.connect(self.rightRowDownloadClick)


    # 파일 히스토리 다운로드
    def rightRowDownloadClick(self):
        import ftplib
        from ftplib import FTP_TLS
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        if not self.tableWidget_30.selectedIndexes():
            self.qMessageBox("파일을 선택해 주세요.")
            return 0

        set1 = set(idx.row() for idx in self.tableWidget_30.selectedIndexes())
        rowindex = list(set1)
        Select_dno = self.tableWidget_30.item(rowindex[0], 0)
        Select_mVer = self.tableWidget_30.item(rowindex[0], 3)
        Select_fVer = self.tableWidget_30.item(rowindex[0], 6)

        localDirPath = self.download_path + "\\_download_History\\" + Select_dno.text() + nowTime
        if not (os.path.isdir(self.download_path + "\\_download_History")):
            os.makedirs(self.download_path + "\\_download_History")
        os.makedirs(localDirPath)
        for i in range(len(self.allmodfilehistory)):
            if Select_dno.text() == self.allmodfilehistory[i][0] and Select_mVer.text() == self.allmodfilehistory[i][3] and Select_fVer.text() == self.allmodfilehistory[i][6]:
                input_Directory = localDirPath + "\\" + self.allmodfilehistory[i][10]
                if self.allmodfilehistory[i][11] is None or len(self.allmodfilehistory[i][11]) == 0:
                    output_Directory = "\\"
                else:
                    output_Directory = self.allmodfilehistory[i][11]
                try:
                    ftps = FTP_TLS(self.ftphost)
                    ftps.login(self.ftpid, self.ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    ftps.cwd(output_Directory)
                    fd = open(input_Directory, 'wb')
                    ftps.retrbinary('RETR %s' % self.allmodfilehistory[i][9], fd.write)
                    ftps.quit()
                    fd.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-YP26 , " + str(err))
                    return 0
        self.qMessageBox("다운로드가 완료되었습니다.")
        self.close()


class Login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.le_ID.returnPressed.connect(self.loginCheck)
        self.le_PW.returnPressed.connect(self.loginCheck)
        self.pb_OK.clicked.connect(self.loginCheck)


    # Oracle DB 로그인, 패스워드 확인
    def loginCheck(self):
        import configparser
        self.__class__.cf_lid = self.le_ID.text()
        self.__class__.cf_lpw = self.le_PW.text()
        if self.cf_lid == "":
            self.qMessageBox("아이디를 입력하세요.")
            self.le_PW.clear()
            self.le_ID.setFocus()
            return 0
        elif self.cf_lpw == "":
            self.qMessageBox("비밀번호를 입력하세요.")
            self.le_PW.setFocus()
            return 0
        userip = self.cf_lid + self.le_PW.text()
        userpw_hash = self.hashSHA(userip)

        try:
            URL = self.cfg_server_url + "/cad/draw/insert/selectHumCheck.do"
            data = {
                'id': self.cf_lid,
                'pw': userpw_hash
            }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            loginCheck = []
            for val in res:
                loginCheck.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-CR2005 , " + str(e))
            return 0

        if len(loginCheck) == 1:
            self.__class__.usrname = loginCheck[0][1]
            config = configparser.ConfigParser()
            config.read('config.ini')
            config.set('LOGIN', 'id', self.le_ID.text())
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            self.window_Main = MainWindow()
            self.window_Main.show()
            self.close()
        else:
            self.qMessageBox("아이디/비밀번호를 확인하세요.")
            self.le_PW.clear()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        cLogin = Login()
        self.cfg_usrname = cLogin.usrname
        self.cfg_userid = cLogin.cf_lid
        self.cfg_userpw = cLogin.cf_lpw
        self.cfg_dbuser = cLogin.cfg_oracle_user
        self.cfg_dbpasswd = cLogin.cfg_oracle_passwd
        self.cfg_dbhost = cLogin.cfg_oracle_host
        self.cfg_dbport = cLogin.cfg_oracle_port
        self.cfg_dbname = cLogin.cfg_oracle_dbname
        self.cfg_ftpid = cLogin.cfg_ftp_id
        self.cfg_ftppw = cLogin.cfg_ftp_pw
        self.cfg_ftphost = cLogin.cfg_ftp_host
        self.cfg_ftpport = cLogin.cfg_ftp_port
        self.cfg_pathdown = cLogin.cfg_path_down
        self.cfg_pathnew = cLogin.cfg_path_new
        # self.cfg_pathcatia = cLogin.cfg_path_catia
        self.cfg_svurl= cLogin.cfg_server_url
        self.cfg_svdraw = cLogin.cfg_server_draw
        self.ccn_dic11 = cLogin.dic11
        self.ccn_dic12 = cLogin.dic12
        self.ccn_dic13 = cLogin.dic13
        self.ccn_dic14 = cLogin.dic14
        self.ccn_dic15 = cLogin.dic15
        self.ccn_dic16 = cLogin.dic16
        self.ccn_dic17 = cLogin.dic17

        self.setupUi(self, self.cfg_userid, self.cfg_userpw, self.cfg_usrname)
        self.pushButton_2.clicked.connect(self.open_SelectCar)
        self.pushButton_3.clicked.connect(self.open_SearchDraw)
        self.lineEdit_4.returnPressed.connect(self.open_SearchDraw)
        self.lineEdit_5.returnPressed.connect(self.open_SearchDraw)
        self.lineEdit_7.returnPressed.connect(self.open_SearchDraw)
        self.lineEdit_8.returnPressed.connect(self.open_SearchDraw)
        # self.pushButton_8.clicked.connect(self.open_CancleStaoid)
        self.pushButton_9.clicked.connect(self.checkInBtnClick)
        self.pushButton_10.clicked.connect(self.open_InsertNewData)
        self.history_action.triggered.connect(self.open_History)
        self.pushButton_c.clicked.connect(self.open_Config)


    def open_Config(self):
        self.dialog_config = ConfigDialog(self)
        self.dialog_config.show()


    def open_SelectCar(self):
        self.dialog_selectCar = SelectCar(self)
        self.dialog_selectCar.show()


    def open_SearchDraw(self):
        if len(self.lineEdit_4.text()) == 0 and len(self.lineEdit_7.text()) == 0:
            self.qMessageBox("파트번호 또는 도면번호를 입력하세요.")
            return 0
        if len(self.lineEdit_4.text()) != 0 and len(self.lineEdit_7.text()) != 0:
            self.qMessageBox("파트번호, 도면번호 중 하나만 입력하세요.")
            return 0

        self.dialog_searchDraw = SearchDraw(self)
        self.dialog_searchDraw.show()


    def open_History(self):
        self.dialog_history = HistoryDialog(self)
        self.dialog_history.show()


    # def open_CancleStaoid(self):
    #     self.dialog_cancle = CancleDialog(self)
    #     self.dialog_cancle.show()


    def open_InsertAddData(self):
        self.dialog_addData = InsertAddDialog(self)
        self.dialog_addData.show()


    # 신규등록
    def open_InsertNewData(self):
        if len(self.label_13.text()) == 0:
            self.qMessageBox("최상위 파일을 선택하세요.")
            return 0

        files = os.listdir(self.lineEdit.text())

        self.put_draw_list = []
        for item in files:
            # if '.CATPart' in item or '.CATProduct' in item or '.CATDrawing' in item:
            if '.CATPart' in item or '.CATProduct' in item:
                self.put_draw_list.append(item)
        self.put_directoryPath = self.lineEdit.text().replace("/", "\\")

        self.dialog_newData = InsertNewDialog(self)
        self.dialog_newData.show()


    # 체크아웃 버튼
    def checkOutBtn(self):
        chkModoid = self.parentoidChkBoxChecking()
        if chkModoid != 'Success':
            self.qMessageBox("체크아웃할 상위 도면도 체크아웃 해야합니다.")
            return 0

        chkflag = self.checkMaxVersion()
        if chkflag != 'Success':
            self.qMessageBox("최신버전이 아니므로 체크아웃 할 수 없습니다.")
            return 0

        if len(self.selectCheckMod) == 0:
            self.qMessageBox("체크아웃 도면을 선택해 주세요.")
            return 0

        for chk in self.selectCheckMod:
            if chk[chk.rfind('|') + 1:] != '-:-':
                self.qMessageBox("이미 체크아웃 되어있습니다. (" + chk[chk.find('|') + 1:chk.rfind('|')] + ")")
                return 0

        staoid_list = []
        for y in range(len(self.selectCheckMod)):
            sel_chkmod = self.selectCheckMod[y][:self.selectCheckMod[y].find('|')]
            for x in range(len(self.allmodlist)):
                if sel_chkmod == self.allmodlist[x][0]:
                    staoid_list.append(self.allmodlist[x][11])
        staoid_set = list(set(staoid_list))

        if len(staoid_set) > 1:
            self.qMessageBox("선택한 도면상태가 서로 달라서 체크아웃할 수 없습니다.")
            return 0
        elif len(staoid_set) == 1:
            if staoid_set[0] == 'CCN00192' or staoid_set[0] == 'CCN00197':         # 등록 (작성중 or 반송)
                self.real_CheckOut('','')
            elif staoid_set[0] == 'CCN00193':       # 도면확정
                self.qMessageBox("도면확정 상태이므로, 체크아웃할 수 없습니다.")
                return 0
            elif staoid_set[0] == 'CCN00196':       # 승인
                ret = self.qMessageBox_Select("개정하시겠습니까?")
                if ret == 'no':
                    return 0

                # 최신버전일때만 개정 가능하도록 기능 추가 # 2020-05-18 (요청자: 김동빈)
                if self.rootStayName == '승인':
                    if self.radioButton_4.isChecked() == True:
                        pass
                    else:
                        self.qMessageBox("EBOM 정보가 최신버전일때만 개정이 가능합니다.")
                        return 0

                self.dialog_createver = CreateVerDialog(self)
                self.dialog_createver.show()
            else:
                self.qMessageBox("! 도면 상태 확인")
                return 0


    # 체크인
    def checkInBtnClick(self):
        if len(self.label_12.text()) == 0:
            self.qMessageBox("최상위 파일을 선택하세요.")
            return 0

        # local file list
        path_dir = self.lineEdit_2.text()
        self.file_list = os.listdir(path_dir)

        # db file list
        self.newPathdir = path_dir.replace("/", "\\")
        try:
            URL = self.cfg_svurl + "/cad/draw/select/selectModCheckIn2.do"
            data = {
                'chkout_path': self.newPathdir
            }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            self.db_file_list = []
            for val in res:
                self.db_file_list.append(list(val.values())[7])

            if len(self.db_file_list) == 0:
                self.qMessageBox("체크아웃 폴더가 아닙니다.")
                return 0

            URL2 = self.cfg_svurl + "/cad/draw/insert/selectModCheckIn.do"
            data2 = {
                'chkout_path': self.newPathdir
            }
            response2 = requests.post(url=URL2, data=data2)
            json_response2 = response2.json()
            res2 = json_response2['data']
            self.checkout_files = []
            for val in res2:
                self.checkout_files.append(list(val.values())[3])
        except Exception as e:
            self.errorLog("ERROR-CE2530 , " + str(e))
            self.qMessageBox("체크인 에러")
            return 0

        # radioButton 선택
        if self.radioButton.isChecked() == True:
            self.put_radioBt = "CCN00192"  # 작업중
        else:
            self.put_radioBt = "CCN00193"  # 도면확정

        # db / local 파일 비교
        db_draw = []
        local_draw = []
        for txt in self.db_file_list:
            if '.CATPart' in txt or '.CATProduct' in txt:
                db_draw.append(txt)
        for txt in self.file_list:
            if '.CATPart' in txt or '.CATProduct' in txt:
                local_draw.append(txt)

        diff_set = list(set(local_draw) - set(db_draw))

        # 체크인시 중요한 가정(?) 하나 있음.
        # 예전 파일은 .CATPart.jpg, .CATPart.wrl, .CATPart.pdf 이렇게 중간에 .CATPart 가 들어가있어
        # 그래서 wrl, pdf 변환할 때 우선 체크아웃 기준 파일명으로 따라갈거야 (체크아웃에 wrl, pdf 파일 없으면 .wrl, .pdf 형식으로)
        # 서버에서 가운데 .CATPart 부분 제거하고 업데이트(또는 인서트) 쳐주는 방향으로 개발할거임.

        # 맘바뀜! 변환할때 체크아웃 기준으로 안따라가, 내스탈대로 .wrl, .pdf 형식으로 간다

        if len(diff_set) != 0:
            print("---- add")
            self.qMessageBox("추가파일이 존재합니다. 추가등록을 해주세요.")
            self.put_addfile = []
            for item in diff_set:
                if '.CATPart' in item or '.CATProduct' in item:
                    self.put_addfile.append(item)
            self.put_path = self.newPathdir
            self.put_rootfile = self.label_12.text()
            self.open_InsertAddData()
        else:
            print("----- not add")
            self.notAddFile()
        self.searchReset()


    def notAddFile(self):
        self.upload_wrl_pdf = []
        self.noConvertFile = []
        self.showMinimized()
        try:
            self.CATPtoWrl()                # .wrl 파일 생성 추가 (2020-04-14)
            self.drawing_to_pdf()           # CATDrawing -> pdf 변환
            self.upload_notAddData()        # 로컬→서버 파일 업로드
            self.request_notAddData()       # 서버 .do 호출 (xml ebom, 썸네일 생성)
            if self.resp_result == 'Success':
                self.delete_mkdir()         # 만들어진 서버 폴더 삭제
                if len(self.noConvertFile) == 0:
                    self.qMessageBox("체크인 완료")
                else:
                    tmp_str = ""
                    for text in self.noConvertFile:
                        tmp_str += text + "\n"
                    self.qMessageBox("체크인 완료" + "\n\n- pdf변환되지 않은 도면 -\n" + tmp_str)
            else:
                self.qMessageBox("체크인 에러")
        except Exception as e:
            self.errorLog("ERROR-YE2000 , " + str(e))
            self.qMessageBox("체크인 에러")
        finally:
            self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("----- start -----")
    print(sys.argv)
    print(sys.argv[1:])
    prog = Login()
    prog.show()
    sys.exit(app.exec_())