
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rad.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import svm_breast

from time import time

import os

import time




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

class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(975, 771)
        Form.setWindowIcon(QtGui.QIcon('logo_icon.png'))
        Form.setFixedSize(Form.width(), Form.height())
        Form.setGeometry(310, 0, Form.width(), Form.height())

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
        self.restb.append("\nDiagnosed By : Dr."+rad_name)


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
        self.restb.append("Diagnosed By: Dr."+self.le1.text())



       
        
        
        

        

        

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
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


