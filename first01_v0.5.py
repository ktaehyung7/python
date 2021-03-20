## Ex 5-20. QTextEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QProgressBar
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QDate, Qt
import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.expand_frame_repr', False)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
  
        self.lbl1 = QLabel('Data Location...')
        
        btn01 = QPushButton('&Open Data', self)
        btn02 = QPushButton('주가예측', self)

        btn01.clicked.connect(self.showFileDialog)
        btn02.clicked.connect(self.stock_lv3)
        
        self.lbl_logo = QLabel('logo')
        self.lbl_logo.setPixmap(QPixmap('삼성전자logo.PNG'))
  
        today = QDate.currentDate()
        today = today.addDays(1)
        self.lbl_tomorrow = QLabel(today.toString(Qt.DefaultLocaleLongDate))
        self.lbl_tomorrow.setFont(QFont("맑은고딕", 20))
        self.lbl_result = QLabel("분석결과")
        self.lbl_result.setFont(QFont("맑은고딕", 30))
        self.lbl_result.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
 
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        
        self.lbl21 = QLabel('종가 유사패턴수: 0')
        self.lbl22 = QLabel('종가 상승패턴수: 0')
        self.lbl23 = QLabel('종가 보합패턴수: 0')
        self.lbl24 = QLabel('종가 하락패턴수: 0')
        self.lbl25 = QLabel('-----------------')
        self.lbl26 = QLabel('거래량 유사패턴수: 0')
        self.lbl27 = QLabel('거래량 상승패턴수: 0')
        self.lbl28 = QLabel('거래량 보합패턴수: 0')
        self.lbl29 = QLabel('거래량 하락패턴수: 0')
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lbl1)
        vbox1.addWidget(btn01)
        vbox1.addWidget(btn02)
        vbox1.addWidget(self.lbl_logo)
        vbox1.addWidget(self.lbl_tomorrow)
        #vbox1.addStretch(1)
        vbox1.addWidget(self.lbl_result)
        vbox1.addStretch()
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.te)
        vbox2.addWidget(self.lbl21)
        vbox2.addWidget(self.lbl22)
        vbox2.addWidget(self.lbl23)
        vbox2.addWidget(self.lbl24)
        vbox2.addWidget(self.lbl25)
        vbox2.addWidget(self.lbl26)
        vbox2.addWidget(self.lbl27)
        vbox2.addWidget(self.lbl28)
        vbox2.addWidget(self.lbl29)
        vbox2.addWidget(self.pbar)
        vbox2.addStretch()
        
        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        #hbox.addStretch(4)

        self.setLayout(hbox)

        self.setWindowTitle('주가예측')
        self.setWindowIcon(QIcon('주가예측_logo.PNG'))
        self.setGeometry(300, 300, 900, 700)
        self.show()

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            self.lbl1.setText(fname[0])
            s=fname[0].rsplit('/', 1)
            s1=s[1].rsplit('.')
            code = str(s1[0])
            code_img = {'005930' : '삼성전자logo.PNG', '035420' : '네이버logo.PNG', '095700' : '제넥신logo.PNG'}
            #self.lbl_tomorrow.setText(code_img[code])
            
            pixmap = QPixmap()
            pixmap = pixmap.scaledToWidth(200)
            pixmap.load(code_img[code])
            self.lbl_logo.setPixmap(pixmap)
            self.lbl_result.setText("")
            self.lbl_result.setStyleSheet("color: black;"
                               "background-color: #808080;")
            self.te.setText('')
            

    def stock_lv3(self):
        # read csv file
        df8 = pd.read_csv(self.lbl1.text(), sep=',', encoding='EUC-KR', index_col='일자')
        
        # adjustment value
        adjust_amt = 0.10
        adjust_diff = 0.50
        
        # prediction duration
        prediction_duration = 8
        
        # list for sorting
        a =[0]
        
        # count variables
        cnt=0
        cnt_d0=0
        cnt_up=0
        cnt_dn=0
        cnt_eq=0
        cnt_up_i=0
        cnt_dn_i=0
        cnt_eq_i=0
        cnt_up_5_i=0
        cnt_dn_5_i=0
        cnt_eq_5_i=0
  
        # 오름차순 정렬 및 '대비'항목 추가
        df8 = df8.sort_index(axis=0, ascending=True)
        
        for value in range(len(df8)):
            if value == 0:
                continue
            fin_val_cur = df8.iloc[value].종가
            fin_val_pre = df8.iloc[value-1].종가
            a_dif = int(fin_val_cur.replace(",","")) - int(fin_val_pre.replace(",",""))
            a.append(a_dif)
        
        df8['대비'] = a
     
        #numbers=[6,5,3,8,4,2,5,4,11]
        numbers0=[0,1,2]
        df8_r = df8[-3:]
        
        거래량_opp0 = float(df8_r.iloc[1].거래량.replace(",","")) / float(df8_r.iloc[0].거래량.replace(",",""))
        거래량_opp1 = float(df8_r.iloc[2].거래량.replace(",","")) / float(df8_r.iloc[1].거래량.replace(",",""))
        
        diff = int(df8_r.iloc[2].종가.replace(",","")) - int(df8_r.iloc[0].종가.replace(",",""))
        diff0 = df8_r.iloc[0].대비
   
        #df8_t = df8[0:4]
  
        for value in range(len(df8)-3):
            self.pbar.setValue(int(value/len(df8)*100))
            df8_t = df8[value:value+prediction_duration]
            
            if float(df8_t.iloc[0].거래량.replace(",","")) == 0 or float(df8_t.iloc[1].거래량.replace(",","")) == 0 :
                거래량_n_opp0 = 1;
                거래량_n_opp1 = 1;
            else :
                거래량_n_opp0 = float(df8_t.iloc[1].거래량.replace(",","")) / float(df8_t.iloc[0].거래량.replace(",",""))
                거래량_n_opp1 = float(df8_t.iloc[2].거래량.replace(",","")) / float(df8_t.iloc[1].거래량.replace(",",""))
            
            diff_n = int(df8_t.iloc[2].종가.replace(",","")) - int(df8_t.iloc[0].종가.replace(",",""))
            diff_n_0 = df8_t.iloc[0].대비
            
            if diff0 * diff_n_0 < 0:
                continue
            
            if 거래량_n_opp0 >= 거래량_opp0 *(1-adjust_amt) and 거래량_n_opp0 <= 거래량_opp0*(1+adjust_amt) :
                if 거래량_n_opp1 >= 거래량_opp1*(1-adjust_amt) and 거래량_n_opp1 <= 거래량_opp1*(1+adjust_amt) :
                    if diff >= 0:
                        if diff_n >= diff*(1-adjust_diff) and diff_n <= diff*(1+adjust_diff) :
                            self.te.append("lv3 success!!!")
                            #print("lv3 success!!!")
                            self.te.append(str(df8_t))
                            #print(df8_t)
                            self.te.append("3일간 종가 차이: {0}".format(diff_n))
                            #print("3일간 종가 차이: ", diff_n)
                            self.te.append("시작일 대비: {0}".format(diff_n_0))
                            #print("시작일 대비: ", diff_n_0)
                            cnt=cnt+1
                            self.te.append("내일 대비: {0}".format(df8_t.iloc[3].대비))
                            #print("내일 대비: ", df8_t.iloc[3].대비)
                            diff_5 = int(df8_t.iloc[len(df8_t)-1].종가.replace(",",""))-int(df8_t.iloc[2].종가.replace(",",""))
                            self.te.append("{0} 일후 대비: {1}".format(len(df8_t)-3, diff_5))
                            #print("%02d 일후 대비: %d" %(len(df8_t)-3, diff_5))
                            # 상승/하락 종목수 count
                            if df8_t.iloc[3].대비 > 0:
                                cnt_up_i=cnt_up_i+1
                            elif df8_t.iloc[3].대비 < 0:
                                cnt_dn_i=cnt_dn_i+1
                            else:
                                cnt_eq_i=cnt_eq_i+1
                                
                            # 5일 후 상승/하락 종목수 count
                            if diff_5 > 0:
                                cnt_up_5_i=cnt_up_5_i+1
                            elif diff_5 < 0:
                                cnt_dn_5_i=cnt_dn_5_i+1
                            else:
                                cnt_eq_5_i=cnt_eq_5_i+1
                        else: cnt_d0=cnt_d0+1
                    else:
                        if diff_n >= diff*(1+adjust_diff) and diff_n <= diff*(1-adjust_diff) :
                            self.te.append("lv3 success!!!")
                            #print("lv3 success!!!")
                            self.te.append(str(df8_t))
                            #print(df8_t)
                            self.te.append("3일간 종가 차이: {0}".format(diff_n))
                            #print("3일간 종가 차이: ", diff_n)
                            self.te.append("시작일 대비: {0}".format(diff_n_0))
                            #print("시작일 대비: ", diff_n_0)
                            cnt=cnt+1
                            self.te.append("내일 대비: {0}".format(df8_t.iloc[3].대비))
                            #print("내일 대비: ", df8_t.iloc[3].대비)
                            diff_5 = int(df8_t.iloc[len(df8_t)-1].종가.replace(",",""))-int(df8_t.iloc[2].종가.replace(",",""))
                            self.te.append("{0} 일후 대비: {1}".format(len(df8_t)-3, diff_5))
                            #print("%02d 일후 대비: %d" %(len(df8_t)-3, diff_5))
                            # 상승/하락 종목수 count
                            if df8_t.iloc[3].대비 > 0:
                                cnt_up_i=cnt_up_i+1
                            elif df8_t.iloc[3].대비 < 0:
                                cnt_dn_i=cnt_dn_i+1
                            else:
                                cnt_eq_i=cnt_eq_i+1
                                
                            # 5일 후 상승/하락 종목수 count
                            if diff_5 > 0:
                                cnt_up_5_i=cnt_up_5_i+1
                            elif diff_5 < 0:
                                cnt_dn_5_i=cnt_dn_5_i+1
                            else:
                                cnt_eq_5_i=cnt_eq_5_i+1
                        else: cnt_d0=cnt_d0+1
                        
                    if df8_t.iloc[3].대비 > 0:
                        cnt_up=cnt_up+1
                    elif df8_t.iloc[3].대비 < 0:
                        cnt_dn=cnt_dn+1
                    else:
                        cnt_eq=cnt_eq+1
 
        self.te.append('===================================================================')
        self.te.append(str(df8_r))
        self.te.append('===================================================================')
        self.te.append("3일간(현재) 종가의 증감은 {0}".format(diff))
        self.te.append("종가 흐름 유사 패턴 검출수: {0}".format(cnt))
        self.te.append("종가 흐름 패턴중 상승 검출수: {0}".format(cnt_up_i))
        self.te.append("종가 흐름 패턴중 보합 검출수: {0}".format(cnt_eq_i))
        self.te.append("종가 흐름 패턴중 하락 검출수: {0}".format(cnt_dn_i))
        self.te.append("----------------------------------------------------")
        self.te.append("거래량 흐름 패턴 검출수(나머지): {0}".format(cnt_d0))
        self.te.append("거래량 흐름 패턴중 상승 검출수: {0}".format(cnt_up))
        self.te.append("거래량 흐름 패턴중 보합 검출수: {0}".format(cnt_eq))
        self.te.append("거래량 흐름 패턴중 하락 검출수: {0}".format(cnt_dn))
        self.te.append("----------------------------------------------------")
        self.te.append("5일후 종가 흐름 패턴중 상승 검출수: {0}".format(cnt_up_5_i))
        self.te.append("5일후 종가 흐름 패턴중 보합 검출수: {0}".format(cnt_eq_5_i))
        self.te.append("5일후 종가 흐름 패턴중 하락 검출수: {0}".format(cnt_dn_5_i))
        
        self.lbl21.setText('종가 유사패턴수: {0}'.format(cnt))
        self.lbl22.setText('종가 상승패턴수: {0}'.format(cnt_up_i))
        self.lbl23.setText('종가 보합패턴수: {0}'.format(cnt_eq_i))
        self.lbl24.setText('종가 하락패턴수: {0}'.format(cnt_dn_i))
        self.lbl25.setText('-----------------')
        self.lbl26.setText('거래량 유사패턴수: {0}'.format(cnt_d0))
        self.lbl27.setText('거래량 상승패턴수: {0}'.format(cnt_up))
        self.lbl28.setText('거래량 보합패턴수: {0}'.format(cnt_eq))
        self.lbl29.setText('거래량 하락패턴수: {0}'.format(cnt_dn))
        
        self.pbar.setValue(100)
        
        if (cnt_up_i > cnt_dn_i) or (cnt_up_i == cnt_dn_i and cnt_up > cnt_dn):
            #상승
            self.lbl_result.setText("상승")
            self.lbl_result.setStyleSheet("color: red;"
                               "background-color: #FA7CD7;")
        elif (cnt_up_i < cnt_dn_i) or (cnt_up_i == cnt_dn_i and cnt_up < cnt_dn):
            #하락
            self.lbl_result.setText("하락")
            self.lbl_result.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;")
        else:
            #보합
            self.lbl_result.setText("보합권")
            self.lbl_result.setStyleSheet("color: black;"
                               "background-color: #808080;")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())