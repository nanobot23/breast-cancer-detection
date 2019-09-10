# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName(_fromUtf8("Form1"))
        Form1.resize(963, 719)
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
        self.cb1.addItem(_fromUtf8(""))
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
        self.cb1.setItemText(1, _translate("Form1", "linear", None))
        self.cb1.setItemText(2, _translate("Form1", "poly", None))
        self.cb1.setItemText(3, _translate("Form1", "sigmoid", None))
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
    Form1 = QtGui.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())

