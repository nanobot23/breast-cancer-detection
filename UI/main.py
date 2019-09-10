# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import svm_breast

from time import time

import os

import time

import svm_breastdev
import bp_breastdev
import gsadev
import plot
from time import sleep
import plotbp

import matplotlib.pyplot as plt




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.resize(920, 636)
        mainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet(_fromUtf8(""))
        mainWindow.setAnimated(True)
        mainWindow.setWindowIcon(QtGui.QIcon('logo_icon.png'))
        mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
        mainWindow.setGeometry(240, 0, mainWindow.width(), mainWindow.height())
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 10, 61, 71))
        self.label_4.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/logo_icon.png\");\n"
"background-repeat:no-repeat;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 811, 431))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 331, 311))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/ic1.png\");\n"
"background-repeat: no-repeat;\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"margin-right: 10px;\n"
"margin-left: 10px;"))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setLineWidth(1)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 360, 151, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(440, 50, 351, 311))
        self.label_2.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/ic3.png\");\n"
"background-repeat: no-repeat;\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"margin-right: 10px;\n"
"margin-left: 10px;"))
        self.label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(140, 360, 161, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuCredits = QtGui.QMenu(self.menubar)
        self.menuCredits.setObjectName(_fromUtf8("menuCredits"))
        mainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNew = QtGui.QAction(mainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionDatabase_Sources = QtGui.QAction(mainWindow)
        self.actionDatabase_Sources.setObjectName(_fromUtf8("actionDatabase_Sources"))
        self.actionDevelopers = QtGui.QAction(mainWindow)
        self.actionDevelopers.setObjectName(_fromUtf8("actionDevelopers"))
        self.actionDeveloper = QtGui.QAction(mainWindow)
        self.actionDeveloper.setObjectName(_fromUtf8("actionDeveloper"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionDeveloper)
        self.menuFile.addAction(self.actionExit)
        self.menuCredits.addAction(self.actionDatabase_Sources)
        self.menuCredits.addAction(self.actionDevelopers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())

        self.retranslateUi(mainWindow)
        self.btn1Action()
        self.btn2Action()


        
        


        
        
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Breast Cancer Management System ", None))
        self.label_3.setText(_translate("mainWindow", "   Breast Cancer Detection System ", None))
        self.groupBox.setToolTip(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.groupBox.setTitle(_translate("mainWindow", "Choose An Option :", None))
        self.label.setToolTip(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("mainWindow", "Developer ", None))
        self.pushButton.setText(_translate("mainWindow", "Radiologist", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.menuCredits.setTitle(_translate("mainWindow", "Credits", None))
        self.actionExit.setText(_translate("mainWindow", "Exit ", None))
        self.actionExit.setShortcut(_translate("mainWindow", "Ctrl+X", None))
        self.actionNew.setText(_translate("mainWindow", "Radiologist ", None))
        self.actionDatabase_Sources.setText(_translate("mainWindow", "Database Sources", None))
        self.actionDevelopers.setText(_translate("mainWindow", "Developers", None))
        self.actionDeveloper.setText(_translate("mainWindow", "Developer", None))


    
    def btn1Action(self):
        self.pushButton.clicked.connect(self.abc)
        

    def abc(self):
        
        Form.show()
            
    def btn2Action(self):
        self.pushButton_2.clicked.connect(self.pqr)


    def pqr(self):
        Form1.show()
    

class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(975, 771)
        Form.setWindowIcon(QtGui.QIcon('logo_icon.png'))
        Form.setFixedSize(Form.width(), Form.height())
        Form.setGeometry(370, 0, Form.width(), Form.height())

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.label.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/med.png\");\n"
"background-repeat:no-repeat;"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(900, 0, 71, 71))
        self.label_2.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/ic2.png\");\n"
"background-repeat:no-repeat;"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 341, 41))
        self.label_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(40, 150, 891, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(420, 30, 67, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.le2 = QtGui.QLineEdit(self.tab)
        self.le2.setGeometry(QtCore.QRect(90, 30, 261, 25))
        self.le2.setObjectName(_fromUtf8("le2"))
        self.le3 = QtGui.QLineEdit(self.tab)
        self.le3.setGeometry(QtCore.QRect(500, 30, 71, 25))
        self.le3.setObjectName(_fromUtf8("le3"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 121, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(310, 100, 141, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 161, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 171, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(600, 170, 121, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(306, 170, 171, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(600, 100, 131, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(310, 240, 121, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(600, 240, 67, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.le4 = QtGui.QLineEdit(self.tab)
        self.le4.setGeometry(QtCore.QRect(190, 100, 61, 25))
        self.le4.setObjectName(_fromUtf8("le4"))
        self.le5 = QtGui.QLineEdit(self.tab)
        self.le5.setGeometry(QtCore.QRect(190, 160, 61, 25))
        self.le5.setObjectName(_fromUtf8("le5"))
        self.le6 = QtGui.QLineEdit(self.tab)
        self.le6.setGeometry(QtCore.QRect(190, 230, 61, 25))
        self.le6.setObjectName(_fromUtf8("le6"))
        self.le7 = QtGui.QLineEdit(self.tab)
        self.le7.setGeometry(QtCore.QRect(490, 100, 61, 25))
        self.le7.setObjectName(_fromUtf8("le7"))
        self.le8 = QtGui.QLineEdit(self.tab)
        self.le8.setGeometry(QtCore.QRect(490, 160, 61, 25))
        self.le8.setObjectName(_fromUtf8("le8"))
        self.le9 = QtGui.QLineEdit(self.tab)
        self.le9.setGeometry(QtCore.QRect(490, 230, 61, 25))
        self.le9.setObjectName(_fromUtf8("le9"))
        self.le10 = QtGui.QLineEdit(self.tab)
        self.le10.setGeometry(QtCore.QRect(750, 100, 61, 25))
        self.le10.setObjectName(_fromUtf8("le10"))
        self.le11 = QtGui.QLineEdit(self.tab)
        self.le11.setGeometry(QtCore.QRect(750, 160, 61, 25))
        self.le11.setObjectName(_fromUtf8("le11"))
        self.le12 = QtGui.QLineEdit(self.tab)
        self.le12.setGeometry(QtCore.QRect(750, 230, 61, 25))
        self.le12.setObjectName(_fromUtf8("le12"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(10, 290, 301, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.diagbtn = QtGui.QPushButton(self.tab)
        self.diagbtn.setGeometry(QtCore.QRect(360, 300, 181, 31))
        self.diagbtn.setObjectName(_fromUtf8("diagbtn"))
        self.resbtn = QtGui.QPushButton(self.tab)
        self.resbtn.setGeometry(QtCore.QRect(560, 300, 131, 31))
        self.resbtn.setObjectName(_fromUtf8("resbtn"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 130, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(40, 70, 511, 41))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.le_url = QtGui.QLineEdit(self.tab_2)
        self.le_url.setEnabled(False)
        self.le_url.setGeometry(QtCore.QRect(40, 130, 351, 31))
        self.le_url.setObjectName(_fromUtf8("le_url"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(40, 210, 51, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.le_url1 = QtGui.QLineEdit(self.tab_2)
        self.le_url1.setGeometry(QtCore.QRect(90, 200, 301, 31))
        self.le_url1.setObjectName(_fromUtf8("le_url1"))
        self.diagbtn2 = QtGui.QPushButton(self.tab_2)
        self.diagbtn2.setGeometry(QtCore.QRect(250, 270, 131, 41))
        self.diagbtn2.setObjectName(_fromUtf8("diagbtn2"))
        self.resbtn2 = QtGui.QPushButton(self.tab_2)
        self.resbtn2.setGeometry(QtCore.QRect(410, 270, 151, 41))
        self.resbtn2.setObjectName(_fromUtf8("resbtn2"))
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(820, 0, 67, 71))
        self.label_20.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/file.png\");\n"
"background-repeat:no-repeat;"))
        self.label_20.setText(_fromUtf8(""))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 171, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.le1 = QtGui.QLineEdit(Form)
        self.le1.setGeometry(QtCore.QRect(210, 110, 241, 31))
        self.le1.setObjectName(_fromUtf8("le1"))
        self.restb = QtGui.QTextBrowser(Form)
        self.restb.setGeometry(QtCore.QRect(280, 580, 481, 141))
        self.restb.setObjectName(_fromUtf8("restb"))
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(280, 550, 91, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pb = QtGui.QProgressBar(Form)
        self.pb.setGeometry(QtCore.QRect(280, 530, 481, 23))
        self.pb.setProperty("value", 24)
        self.pb.setObjectName(_fromUtf8("pb"))
        self.pb.hide()
        
        self.logbtn = QtGui.QPushButton(Form)
        self.logbtn.setGeometry(QtCore.QRect(280, 530, 481, 25))
        self.logbtn.setObjectName(_fromUtf8("logbtn"))
        self.logbtn.hide()      
	


        self.logurl=""

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)



        self.diagbtn_act()

        self.filedialog_act()

        self.diagbtn2_act()

        self.logbtn_act()

        self.resbtn_act()

        self.resbtn2_act()
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "BCMS : Radiologist", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:26pt;\">DIAGNOSIS CENTER </span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "Name", None))
        self.label_6.setText(_translate("Form", "Age", None))
        self.label_7.setText(_translate("Form", "Clump Thickness", None))
        self.label_8.setText(_translate("Form", "Marginal Adhesion", None))
        self.label_9.setText(_translate("Form", "Uniformity of Cell Size", None))
        self.label_10.setText(_translate("Form", "Uniformity of Cell Shape", None))
        self.label_11.setText(_translate("Form", "Normal Nucleoli", None))
        self.label_12.setText(_translate("Form", "Single Epithelial Cell Size", None))
        self.label_13.setText(_translate("Form", "Bland Chromatin", None))
        self.label_14.setText(_translate("Form", "Bare Nuclei", None))
        self.label_15.setText(_translate("Form", "Mitoses", None))
        self.label_16.setText(_translate("Form", "Note : All Diagonstic Value are in range 1-10", None))
        self.diagbtn.setText(_translate("Form", "Diagnose", None))
        self.resbtn.setText(_translate("Form", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Enter Patient Details", None))
        self.pushButton.setText(_translate("Form", "Choose File", None))
        self.label_18.setText(_translate("Form", "If you want to diagnose multiple patients ,You can choose an Input File :", None))
        self.le_url.setText(_translate("Form", "Enter URL or choose file ", None))
        self.label_19.setText(_translate("Form", "<html><head/><body><p>URL:</p></body></html>", None))
        self.diagbtn2.setText(_translate("Form", "Diagnose", None))
        self.resbtn2.setText(_translate("Form", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Choose a File", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Radiologist Name :</span></p></body></html>", None))
        self.restb.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Results:</span></p></body></html>", None))
        self.logbtn.setText(_translate("Form", "For a detailed Log Click here", None))


    def diagbtn_act(self):
        self.diagbtn.clicked.connect(self.diagbtn_fun)

    def diagbtn_fun(self):
        

        rad_name=self.le1.text()

        pname=self.le2.text()
        page=self.le3.text()
        

        diag_array=[]

        diag_vector=[]


        diag_vector.append( int(self.le4.text()) )
        diag_vector.append( int(self.le5.text()) )
        diag_vector.append( int(self.le6.text()) )
        diag_vector.append( int(self.le7.text()) )
        diag_vector.append( int(self.le8.text()) )
        diag_vector.append( int(self.le9.text()) )
        diag_vector.append( int(self.le10.text()) )
        diag_vector.append( int(self.le11.text()) )
        diag_vector.append( int(self.le12.text()) )
       
        diag_array.append(diag_vector)


        self.pb.show()
        self.pb.setValue(0)

        self.completed=0

        #t0=time()
        res=svm_breast.predict(diag_array)
        

        

        
        while self.completed<=100:      
            self.completed+=0.0075
            self.pb.setValue(self.completed)



            
        self.pb.hide()

        


        r1=""
        if res[0][0]=='4':
            r1="Malignant \nResult Positive"
        else:
            r1="Benign \nResult Negative"
        
 

        self.restb.append("Name:   "+pname+"\t\t Age:  "+page)
       
        self.restb.append("Result:   "+r1)
        self.restb.append("\nDiagnosed By : Dr. "+rad_name)


        print res[0][0]
    
        url="logs/"+pname+page+".txt"
        
        file1=open(url,'w+')
        file1.write("Name:"+pname)
        file1.write("\nAge:"+page)
        file1.write("\nClump Thickness: "+str(diag_vector[0]))
        file1.write("\nUniformity of Cell Size: " + str(diag_vector[1]))
        file1.write("\nUniformity of Cell Shape: "+str(diag_vector[2]))
        file1.write("\nMarginal Adhesion: "+str(diag_vector[3]))
        file1.write("\nSingle Epithelial Cell Size: "+str(diag_vector[4]))
        file1.write("\nBare Nuclei: "+str(diag_vector[5]))
        file1.write("\nBland Chromatin: "+str(diag_vector[6]))
        file1.write("\nNormal Nucleoli: "+str(diag_vector[7]))
        file1.write("\nMitoses: "+str(diag_vector[8]))
        file1.write("\nResult: "+r1)
        file1.write("\nDiagnosed By: Dr. "+rad_name)

        self.logbtn.show()

        url1=" '//home//karan//Desktop//Breast Cancer Detection Project//UI//logs//"

        self.logurl=url1+pname+page+".txt' "

        

        

        
        
        
        

    def filedialog_act(self):

        self.pushButton.clicked.connect(self.filedialog_fun)


    def filedialog_fun(self):
        ur=QtGui.QFileDialog.getOpenFileName(self.pushButton,"Choose File")
        self.le_url.setText(ur)


    def  extract_data(self,text):

        
        x= text.split('\n')

        features=[]
        labels=[]

        
        for a in x:
            b=a.split(',')
            v=[]
            lbl=''
            for i in range(1,len(b)):
                if(b[i] == '?'):
                    v.append(-999999)
                else:
                    v.append(float(b[i]))
               

            
            features.append(v)
        
        features.pop()
        
        
        return features

        


    def diagbtn2_act(self):
        self.diagbtn2.clicked.connect(self.diagbtn2_fun)
        

    def diagbtn2_fun(self):

        file1=open(self.le_url.text(),'r')
        text1=file1.read()
        file1.close()


        features=self.extract_data(text1)

        self.pb.show()
        self.pb.setValue(0)

        self.completed=0

        res=svm_breast.predict(features)

        while self.completed<=100:
            
            self.completed+=0.0075
            self.pb.setValue(self.completed)



            
        self.pb.hide()


        self.restb.setText("")

        localtime = time.asctime( time.localtime(time.time()) )


        url="logs/"+self.le1.text()+localtime+".txt"
        
        file1=open(url,'w+')

        file1.write("---------Diagnosed By :Dr."+self.le1.text()+" On "+localtime+"----------------\n")

        

        

        x=1

        for ans in res:

            file1.write("\nId:"+str(x))
            file1.write("\nClump Thickness: "+str(features[x-1][0]))
            file1.write("\nUniformity of Cell Size: " + str(features[x-1][1]))
            file1.write("\nUniformity of Cell Shape: "+str(features[x-1][2]))
            file1.write("\nMarginal Adhesion: "+str(features[x-1][3]))
            file1.write("\nSingle Epithelial Cell Size: "+str(features[x-1][4]))
            file1.write("\nBare Nuclei: "+str(features[x-1][5]))
            file1.write("\nBland Chromatin: "+str(features[x-1][6]))
            file1.write("\nNormal Nucleoli: "+str(features[x-1][7]))
            file1.write("\nMitoses: "+str(features[x-1][8]))
            
            


            if ans=='4':
                self.restb.append("Id:   "+str(x)+"\t\t Result: Malignant ")
                file1.write("\nResult: Malignant\n")
            
            
            else:

                self.restb.append("Id:   "+str(x)+"\t\t Result: Benign ")
                file1.write("\nResult: Benign\n")                

               
            x+=1
       


        self.restb.append("-----------------------------------------------------------------------------------------------------")
        self.restb.append("Diagnosed By: Dr. "+self.le1.text())



       
        
        
        

        

        

        url1=" '//home//karan//Desktop//Breast Cancer Detection Project//UI//logs//"

        self.logurl=url1+self.le1.text()+localtime+".txt' "
            
        self.logbtn.show()  


    def logbtn_act(self):
        
        
        self.logbtn.clicked.connect(self.logbtn_fun)
        

    def logbtn_fun(self):

        
        com="gedit "+self.logurl
        os.system(str(com))




    def resbtn_act(self):
         self.resbtn.clicked.connect(self.resbtn_fun)
        

    def resbtn_fun(self):

        self.le1.setText("")
        self.le2.setText("")
        self.le3.setText("")
        self.le4.setText("")
        self.le5.setText("")
        self.le6.setText("")
        self.le7.setText("")
        self.le8.setText("")
        self.le9.setText("")
        self.le10.setText("")
        self.le11.setText("")
        self.le12.setText("")
        self.restb.setText("")
        self.logbtn.hide()



    def resbtn2_act(self):
         self.resbtn2.clicked.connect(self.resbtn2_fun)
        

    def resbtn2_fun(self):

        self.le_url.setText("")
        self.le_url1.setText("")
        self.restb.setText("")
        self.logbtn.hide()   


class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName(_fromUtf8("Form1"))
        Form1.resize(963, 719)
        Form1.setWindowIcon(QtGui.QIcon('logo_icon.png'))
        Form1.setFixedSize(Form1.width(), Form1.height())
        Form1.setGeometry(370, 0, Form1.width(), Form1.height())

        
        self.reset3 = QtGui.QTabWidget(Form1)
        self.reset3.setGeometry(QtCore.QRect(40, 120, 881, 511))
        self.reset3.setObjectName(_fromUtf8("reset3"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(810, 0, 67, 71))
        self.label_2.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/svm.png\");\n"
"background-repeat:no-repeat;"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cb1 = QtGui.QComboBox(self.tab)
        self.cb1.setGeometry(QtCore.QRect(160, 80, 151, 25))
        self.cb1.setObjectName(_fromUtf8("cb1"))
        self.cb1.addItem(_fromUtf8(""))
        self.cb1.addItem(_fromUtf8(""))
        self.cb1.addItem(_fromUtf8(""))
        #self.cb1.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(380, 76, 121, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.cb2 = QtGui.QComboBox(self.tab)
        self.cb2.setGeometry(QtCore.QRect(520, 80, 151, 25))
        self.cb2.setObjectName(_fromUtf8("cb2"))
        self.cb2.addItem(_fromUtf8(""))
        self.cb2.addItem(_fromUtf8(""))
        self.cb2.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 140, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.le_c = QtGui.QLineEdit(self.tab)
        self.le_c.setGeometry(QtCore.QRect(160, 140, 81, 31))
        self.le_c.setObjectName(_fromUtf8("le_c"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(380, 140, 71, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.le_gamma = QtGui.QLineEdit(self.tab)
        self.le_gamma.setGeometry(QtCore.QRect(520, 140, 81, 31))
        self.le_gamma.setObjectName(_fromUtf8("le_gamma"))
        self.res1 = QtGui.QTextBrowser(self.tab)
        self.res1.setGeometry(QtCore.QRect(30, 230, 641, 171))
        self.res1.setObjectName(_fromUtf8("res1"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 67, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.crbtn1 = QtGui.QPushButton(self.tab)
        self.crbtn1.setGeometry(QtCore.QRect(80, 420, 151, 41))
        self.crbtn1.setObjectName(_fromUtf8("crbtn1"))
        self.combtn1 = QtGui.QPushButton(self.tab)
        self.combtn1.setGeometry(QtCore.QRect(260, 420, 171, 41))
        self.combtn1.setObjectName(_fromUtf8("combtn1"))
        self.reset1 = QtGui.QPushButton(self.tab)
        self.reset1.setGeometry(QtCore.QRect(460, 420, 121, 41))
        self.reset1.setObjectName(_fromUtf8("reset1"))
        self.reset3.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(800, 0, 81, 71))
        self.label_3.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/nn.png\");\n"
"background-repeat:no-repeat;"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 50, 141, 41))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.cb3 = QtGui.QComboBox(self.tab_2)
        self.cb3.setGeometry(QtCore.QRect(190, 54, 141, 31))
        self.cb3.setObjectName(_fromUtf8("cb3"))
        self.cb3.addItem(_fromUtf8(""))
        self.cb3.addItem(_fromUtf8(""))
        self.cb3.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(410, 60, 91, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.cb4 = QtGui.QComboBox(self.tab_2)
        self.cb4.setGeometry(QtCore.QRect(570, 60, 121, 31))
        self.cb4.setObjectName(_fromUtf8("cb4"))
        self.cb4.addItem(_fromUtf8(""))
        self.cb4.addItem(_fromUtf8(""))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 120, 67, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.cb5 = QtGui.QComboBox(self.tab_2)
        self.cb5.setGeometry(QtCore.QRect(190, 110, 141, 31))
        self.cb5.setObjectName(_fromUtf8("cb5"))
        self.cb5.addItem(_fromUtf8(""))
        self.cb5.addItem(_fromUtf8(""))
        self.cb5.addItem(_fromUtf8(""))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(410, 120, 101, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.le_lr = QtGui.QLineEdit(self.tab_2)
        self.le_lr.setGeometry(QtCore.QRect(570, 110, 121, 31))
        self.le_lr.setObjectName(_fromUtf8("le_lr"))
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 160, 151, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.le_hid = QtGui.QLineEdit(self.tab_2)
        self.le_hid.setGeometry(QtCore.QRect(190, 160, 141, 31))
        self.le_hid.setObjectName(_fromUtf8("le_hid"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 230, 67, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.res2 = QtGui.QTextBrowser(self.tab_2)
        self.res2.setGeometry(QtCore.QRect(30, 250, 661, 151))
        self.res2.setObjectName(_fromUtf8("res2"))
        self.crbtn2 = QtGui.QPushButton(self.tab_2)
        self.crbtn2.setGeometry(QtCore.QRect(60, 420, 171, 41))
        self.crbtn2.setObjectName(_fromUtf8("crbtn2"))
        self.combtn2 = QtGui.QPushButton(self.tab_2)
        self.combtn2.setGeometry(QtCore.QRect(260, 420, 231, 41))
        self.combtn2.setObjectName(_fromUtf8("combtn2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 420, 141, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.reset3.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(800, 0, 81, 71))
        self.label_4.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/gravit.png\");\n"
"background-repeat:no-repeat;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(40, 40, 111, 31))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.cb6 = QtGui.QComboBox(self.tab_3)
        self.cb6.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.cb6.setObjectName(_fromUtf8("cb6"))
        self.cb6.addItem(_fromUtf8(""))
        self.cb6.addItem(_fromUtf8(""))
        self.cb6.addItem(_fromUtf8(""))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(400, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.le_g0 = QtGui.QLineEdit(self.tab_3)
        self.le_g0.setGeometry(QtCore.QRect(610, 40, 91, 31))
        self.le_g0.setObjectName(_fromUtf8("le_g0"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(40, 100, 71, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.le_alpha = QtGui.QLineEdit(self.tab_3)
        self.le_alpha.setGeometry(QtCore.QRect(160, 100, 101, 31))
        self.le_alpha.setObjectName(_fromUtf8("le_alpha"))
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(400, 90, 151, 41))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.cb7 = QtGui.QComboBox(self.tab_3)
        self.cb7.setGeometry(QtCore.QRect(610, 90, 91, 31))
        self.cb7.setObjectName(_fromUtf8("cb7"))
        self.cb7.addItem(_fromUtf8(""))
        self.cb7.addItem(_fromUtf8(""))
        self.cb7.addItem(_fromUtf8(""))
        self.cb7.addItem(_fromUtf8(""))
        self.cb7.addItem(_fromUtf8(""))
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(40, 180, 67, 17))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.res3 = QtGui.QTextBrowser(self.tab_3)
        self.res3.setGeometry(QtCore.QRect(40, 210, 671, 161))
        self.res3.setObjectName(_fromUtf8("res3"))
        self.combtn3 = QtGui.QPushButton(self.tab_3)
        self.combtn3.setGeometry(QtCore.QRect(180, 400, 221, 41))
        self.combtn3.setObjectName(_fromUtf8("combtn3"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 400, 151, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.reset3.addTab(self.tab_3, _fromUtf8(""))
        self.label = QtGui.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(830, 0, 131, 111))
        self.label.setStyleSheet(_fromUtf8("background: url(\"/home/karan/Desktop/Breast Cancer Detection Project/UI/ic4.png\");\n"
"background-repeat:no-repeat;"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(Form1)
        self.label_5.setGeometry(QtCore.QRect(270, 20, 421, 71))
        self.label_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Form1)
        self.pushButton.setGeometry(QtCore.QRect(360, 670, 201, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
    

        self.crbtn1_act()
        self.crbtn2_act()
        self.crbtn3_act()
        self.combtn1_act()
        self.combtn2_act()
        self.combtn_act()
        self.reset1_act()
        self.reset2_act()
        self.reset3_act()

        self.retranslateUi(Form1)
        self.reset3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(_translate("Form1", "BCMS:Developer", None))
        #self.cb1.setCurrentText(_translate("Form1", "RBF", None))
        self.cb1.setItemText(0, _translate("Form1", "rbf", None))
        #self.cb1.setItemText(1, _translate("Form1", "linear", None))
        self.cb1.setItemText(1, _translate("Form1", "poly", None))
        self.cb1.setItemText(2, _translate("Form1", "sigmoid", None))
        self.label_6.setText(_translate("Form1", "Select Kernel", None))
        self.label_7.setText(_translate("Form1", " Dataset", None))
        self.cb2.setItemText(0, _translate("Form1", "70-30", None))
        self.cb2.setItemText(1, _translate("Form1", "80-20", None))
        self.cb2.setItemText(2, _translate("Form1", "50-50", None))
        self.label_8.setText(_translate("Form1", "C", None))
        self.label_9.setText(_translate("Form1", "Gamma", None))
        self.label_10.setText(_translate("Form1", "Results:", None))
        self.crbtn1.setText(_translate("Form1", "Compute Results", None))
        self.combtn1.setText(_translate("Form1", "Compare Kernel(s)", None))
        self.reset1.setText(_translate("Form1", "Reset", None))
        self.reset3.setTabText(self.reset3.indexOf(self.tab), _translate("Form1", "SVM (Support Vector Machine)", None))
        self.label_11.setText(_translate("Form1", "Activation Function", None))
        self.cb3.setItemText(0, _translate("Form1", "logistic", None))
        self.cb3.setItemText(1, _translate("Form1", "tanh", None))
        self.cb3.setItemText(2, _translate("Form1", "relu", None))
        self.label_12.setText(_translate("Form1", "Solver", None))
        self.cb4.setItemText(0, _translate("Form1", "sgd", None))
        self.cb4.setItemText(1, _translate("Form1", "adam", None))
        self.label_13.setText(_translate("Form1", "Dataset", None))
        self.cb5.setItemText(0, _translate("Form1", "70-30", None))
        self.cb5.setItemText(1, _translate("Form1", "80-20", None))
        self.cb5.setItemText(2, _translate("Form1", "50-50", None))
        self.label_14.setText(_translate("Form1", "Learning Rate", None))
        self.label_15.setText(_translate("Form1", "Hidden Layers Size", None))
        self.label_17.setText(_translate("Form1", "Results:", None))
        self.crbtn2.setText(_translate("Form1", "Compute Results", None))
        self.combtn2.setText(_translate("Form1", "Compare Activation Function(s)", None))
        self.pushButton_2.setText(_translate("Form1", "Reset", None))
        self.reset3.setTabText(self.reset3.indexOf(self.tab_2), _translate("Form1", "Back Propagation Neural Network", None))
        self.label_18.setText(_translate("Form1", "Dataset", None))
        self.cb6.setItemText(0, _translate("Form1", "70-30", None))
        self.cb6.setItemText(1, _translate("Form1", "80-20", None))
        self.cb6.setItemText(2, _translate("Form1", "50-50", None))
        self.label_19.setText(_translate("Form1", "G0", None))
        self.label_20.setText(_translate("Form1", "alpha", None))
        self.label_21.setText(_translate("Form1", "Number of Iterations", None))
        self.cb7.setItemText(0, _translate("Form1", "512", None))
        self.cb7.setItemText(1, _translate("Form1", "256", None))
        self.cb7.setItemText(2, _translate("Form1", "128", None))
        self.cb7.setItemText(3, _translate("Form1", "64", None))
        self.cb7.setItemText(4, _translate("Form1", "32", None))
        self.label_22.setText(_translate("Form1", "Results:", None))
        self.combtn3.setText(_translate("Form1", "Compute Results", None))
        self.pushButton_3.setText(_translate("Form1", "Reset", None))
        self.reset3.setTabText(self.reset3.indexOf(self.tab_3), _translate("Form1", "SVM with GSA (Gravitational Search Algo.)", None))
        self.label_5.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:26pt;\">       Experiments And Results</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form1", "Compare All", None))

    def crbtn1_act(self):
        self.crbtn1.clicked.connect(self.crbtn1_fun)

        

    def crbtn1_fun(self):

        kernel= str(self.cb1.currentText())
        print "kernel ", kernel

        dataset=str(self.cb2.currentText())
        print "dataset ", dataset

        C=str(self.le_c.text())
        print "C ",C

        gamma=str(self.le_gamma.text())
        print "gamma ",gamma


        c_float=eval(C)
        
        gamma_float=eval(gamma)

        print c_float,gamma_float
        
        acc,sens,cm=svm_breastdev.predict(kernel,dataset,c_float,gamma_float)

        

        self.res1.append("Confusion Matrix:")

        self.res1.append("\t\tBenign\tMalignant")

        self.res1.append("Benign\t\t"+str(cm[0][0])+"\t"+str(cm[0][1]))

        self.res1.append("Malignant\t\t"+str(cm[1][0])+"\t"+str(cm[1][1]))
        

        self.res1.append("\nAccuracy : "+str(round(acc*100,2))+"%")

        self.res1.append("\nSenstivity :\n"+"Benign: "+str(round(sens[0]*100,2))+"%")

        self.res1.append("Malignant: "+str(round(sens[1]*100,2))+"%\n")

        
        plot.predict(kernel,dataset,c_float,gamma_float) 
           

    def crbtn2_act(self):
        
        self.crbtn2.clicked.connect(self.crbtn2_fun)

    def crbtn2_fun(self):

        act= str(self.cb3.currentText())
        #print "kernel ", kernel

        sol=str(self.cb4.currentText())
        #print "dataset ", dataset

        dataset=str(self.cb5.currentText())
        #print "C ",C

        lrate=str(self.le_lr.text())
        #print "gamma ",gamma

        hid=str(self.le_hid.text())

        x= hid.split(',')
        print x
        
        hid_size=[]

        
        for s in x:

            hid_size.append(int(s))
            

        

        acc,sens,cm=bp_breastdev.predict(sol,act,dataset,hid_size,float(lrate))

        self.res2.append("Confusion Matrix:")

        self.res2.append("\t\tBenign\tMalignant")

        self.res2.append("Benign\t\t"+str(cm[0][0])+"\t"+str(cm[0][1]))

        self.res2.append("Malignant\t\t"+str(cm[1][0])+"\t"+str(cm[1][1]))
        

        self.res2.append("\nAccuracy : "+str(round(acc*100,2))+"%")

        self.res2.append("\nSenstivity :\n"+"Benign: "+str(round(sens[0]*100,2))+"%")

        self.res2.append("Malignant: "+str(round(sens[1]*100,2))+"%\n")


        plotbp.predict(sol,act,dataset,hid_size,float(lrate))

        

    def crbtn3_act(self):
        
        self.combtn3.clicked.connect(self.crbtn3_fun)

    def crbtn3_fun(self):

        dataset=str(self.cb6.currentText())

        go=float(str(self.le_g0.text()))

        alpha=float(str(self.le_alpha.text()))

        itr=int(str(self.cb7.currentText()))


        acc,fet_sub=gsadev.predict(dataset,go,alpha,itr)

        st="["


        self.res3.append("Optimum Feature Subset :")

        for f in fet_sub:

            st+=str(f)+","

        st+="]"    

        self.res3.append(st)

        self.res3.append("Accuracy: "+str(round(acc*100,2))+"\n")


    def combtn1_act(self):
        
        self.combtn1.clicked.connect(self.combtn1_fun)

        

    def combtn1_fun(self):

        ker=["rbf","poly","sigmoid"]

        dataset=["50-50","70-30","80-20"]

        C=str(self.le_c.text())
        

        gamma=str(self.le_gamma.text())

        c_float=eval(C)
        
        gamma_float=eval(gamma)


        plot=[]
        x=[50,70,80]

        for i in ker:
            v=[]
            
            for j in dataset:
                
                acc,sens,cm=svm_breastdev.predict(i,j,c_float,gamma_float)
                v.append(acc)

            plot.append(v)


        a=0

        #print plot

        for i in plot:

            plt.plot(x,i,label=ker[a])
            
            a+=1

            
        plt.xlabel("Training Set (%)")
        plt.ylabel("Accuracy")
        plt.title("Kernel Comparision")
        plt.legend()
        
        plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
       
        plt.show()


    def combtn2_act(self):
        
         
        self.combtn2.clicked.connect(self.combtn2_fun)

        

    def combtn2_fun(self):
        
        act=["logistic","tanh","relu"]

        dataset=["50-50","70-30","80-20"]

        sol=str(self.cb4.currentText())

        lrate=float(str(self.le_lr.text()))
        

        hid=str(self.le_hid.text())

        x= hid.split(',')
        print x
        
        hid_size=[]

        
        for s in x:
             

            hid_size.append(int(s))

        


        plot=[]
        x=[50,70,80]

        for i in act:
            v=[]
            
            for j in dataset:

                acc,sens,cm=bp_breastdev.predict(sol,i,j,hid_size,lrate)
                
                
                v.append(acc)

            plot.append(v)


        a=0

        #print plot

        for i in plot:

            plt.plot(x,i,label=act[a])
            
            a+=1

            
        plt.xlabel("Training Set (%)")
        plt.ylabel("Accuracy")
        plt.title("Activation Function Comparision")
        plt.legend()
         
        plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
        
        plt.show()


    def combtn_act(self):
        
         
        self.pushButton.clicked.connect(self.combtn_fun)

        

    def combtn_fun(self):
        
        
        

        dataset=["50-50","70-30","80-20"]

        svm=[]
        bp=[]
        gsa=[]


            
        
        
        
        

       


        plot=[]
        x=[50,70,80]

        for i in dataset:
            
               acc1,sens1,cm1=svm_breastdev.predict(dataset=i) 
               acc2,sens2,cm2=bp_breastdev.predict(dataset=i)
               acc,fet_sub=gsadev.predict(dataset=i)

               svm.append(acc1)
               bp.append(acc2)
               gsa.append(acc)
                
                


        


        plt.plot(x,svm,label="SVM")
        plt.plot(x,bp,label="BP")
        plt.plot(x,gsa,label="GSA")
            
            

            
        plt.xlabel("Training Set (%)")
        plt.ylabel("Accuracy")
        plt.title("Algorithm Comparision")
        plt.legend()
         
        plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
        
        plt.show()


    def reset1_act(self):
        
        self.reset1.clicked.connect(self.reset1_fun)

        

    def reset1_fun(self):
        self.le_c.setText("")
        self.le_gamma.setText("")
        self.res1.setText("")


    def reset2_act(self):
        
        
        self.pushButton_2.clicked.connect(self.reset2_fun)

        

    def reset2_fun(self):
        self.le_lr.setText("")
        self.le_hid.setText("")
        self.res2.setText("")


    def reset3_act(self):
        
        
        self.pushButton_3.clicked.connect(self.reset3_fun)

        

    def reset3_fun(self):
        self.le_alpha.setText("")
        self.le_g0.setText("")
        self.res3.setText("")        

        
             




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    Form = QtGui.QWidget()
    ui1 = Ui_Form()
    ui1.setupUi(Form)

    Form1 = QtGui.QWidget()
    ui2 = Ui_Form1()
    ui2.setupUi(Form1)
        
    sys.exit(app.exec_())

