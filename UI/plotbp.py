
from __future__ import division

import sys
from time import time

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler



def extract_data(text):
    x= text.split('\n')

    features=[]
    labels=[]

    
    for a in x:
        b=a.split(',')
        v=[]
        lbl=''
        for i in range(1,len(b)-1):
            if(b[i] == '?'):
                v.append(-9999)
            else:
                v.append(float(b[i]))
           
        val = b[len(b)-1]
        
        
        labels.append(val)
        features.append(v)
    
    features.pop()
    labels.pop()
    
    return features,labels


def predict(sol="sgd",act="tanh",dataset="70-30",hid_size=[100],lrate=0.0001 ):


    print hid_size
    
    train=""
    test=""

    if dataset=="70-30":
        train= "set7030train"
        test= "set7030test"

    elif dataset=="80-20":
        train="set8020train"
        test="set8020test"

    elif dataset=="50-50":
        train="set5050train"
        test="set5050test"

        
    # Import Training Dataset

    file1=open(train,'r')
    text1=file1.read()
    file1.close()


    # Import Testing Dataset

    file2=open(test,'r')
    text2=file2.read()
    file2.close()

    features_train,labels_train=extract_data(text1)

    features_test,labels_test=extract_data(text2)



    print "Training Set :", len(features_train)
    print "Testing Set :", len(features_test)    
        



    abc=[]
    pqr=[]
    a=0

    for r in features_train:
        v=[]
        v.append(r[0])
        v.append(r[1])

        abc.append(v)

       
        pqr.append(float(labels_train[a]))
        
       

        a+=1


        

    scaler = StandardScaler()

    scaler.fit(features_train)

    features_train = scaler.transform(features_train)
    ft1=features_test
    features_test = scaler.transform(features_test)



            

    print "Training Set :", len(abc)    

    from sklearn.svm import SVC

    X = features_train    # we only take the first two features. We could
                          # avoid this ugly slicing by using a two-dim dataset
    y = labels_train

    clf = MLPClassifier(solver='sgd',activation='logistic', hidden_layer_sizes=(100,),random_state=1, shuffle=False)

    t0=time()

    clf.fit(abc,pqr) 

    print "Training Time:" ,round(time()-t0),"s"
    '''
    t1=time()
    pred=clf.predict(features_test)
    print "Predicition Time:" ,round(time()-t1),"s"

    from sklearn.metrics import accuracy_score

    acc=accuracy_score(pred,labels_test)

    print "Accuracy:" ,acc
    '''
    benignx=[]
    benigny=[]
    maligx=[]
    maligy=[]


    for i in range(0,len(features_test)):
        if labels_test[i]=='2':
            benignx.append(ft1[i][0])
            benigny.append(ft1[i][7])
        else:
            maligx.append(ft1[i][0])
            maligy.append(ft1[i][7])

















    plt.xlabel("Clump Thickness")
    plt.ylabel("Normal Nucleoli")

    plt.title("Scatter Plot" )

    plt.legend()


    x_min, x_max = 0.5,11
    y_min, y_max = 0.5,11

       
    h = 0.08 # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot

    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.seismic, alpha=1.0)


    plt.scatter(benignx,benigny,label="Benign",color="green",marker="o",s=10)



            
    plt.scatter(maligx,maligy,label="Malignant",color="red",marker="x",s=10)
    plt.legend()

    plt.show()






