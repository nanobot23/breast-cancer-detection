from __future__ import division

import sys
from time import time

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

import math 
import fit 

from sklearn.svm import SVC
import random 

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
           
        val =b[len(b)-1] 
        
        
        labels.append(val)
        features.append(v)
    
    features.pop()
    labels.pop()
    
    return features,labels


def predict(dataset="70-30",go=1,bet=0.02,itr=128):

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



    fitness_matrix=[]

    for i in range(0,9):

        result=fit.fitness(i,labels_train,labels_test,features_train ,features_test)

        fitness_matrix.append(result)


       
    best=max(fitness_matrix)
    worst=min(fitness_matrix)


    G0=go
    beta=bet
    e=1

    t0=time()

    a0=0

    random_matrix=[]


    for i in range(0,9):
        random_matrix.append(random.random())


    mass_matrix=[0,0,0,0,0,0,0,0,0]

    q_matrix=[0,0,0,0,0,0,0,0,0]

    pos_matrix=[1,1,1,0,1,1,0,1,0]

    force_matrix=[0,0,0,0,0,0,0,0,0]

    acc_matrix=[0,0,0,0,0,0,0,0,0]

    velocity_matrix=[0,0,0,0,0,0,0,0,0]

    S=[0,0,0,0,0,0,0,0,0]

    feature_subset=[]


    for t in range(0,itr):


        chng=(t0/time())
        G=G0 *(chng**beta)

        for i in range(0,9):

            q=(fitness_matrix[i]-worst)/(best-worst)
            q_matrix[i]=q


        s=sum(q_matrix)

        for i in range(0,9):
            

            m=q_matrix[i]/s
            mass_matrix[i]=m

      
        for i in range(0,9):
            
        
            f=0
            mass=1
            dis1=1
            dis=1
            for j in range(0,9):
                
            
                if (j!=i):
                
                    dis1=abs(pos_matrix[j]-pos_matrix[i])
                         
                    mass = mass_matrix[i] * mass_matrix[j]
                         
                    dis2=pos_matrix[i]**2+pos_matrix[j]**2-2*pos_matrix[i]*pos_matrix[j]


                    if dis2 >0:
                    
                          
                        dis3=0

                    else:
                        
                         
                         dis3=math.sqrt(dis2)        

                         dis=dis3+e         
                         
                f+= G*(random.random())*( mass * dis1 )/dis
                         


            force_matrix[i]=f      

        for i in range(0,9):


            a=0

            if (mass_matrix[i]!=0):
                a=force_matrix[i]/mass_matrix[i]

            acc_matrix[i]=a


        for i in range(0,9):

            v=random_matrix[i]*velocity_matrix[i]+acc_matrix[i]

            velocity_matrix[i]=v
        

        for i in range(0,9):

            s=abs(math.tanh(velocity_matrix[i]))
            

            S[i]=s
            
        

        for i in range(0,9):

            if(random_matrix[i]< S[i]):

                if pos_matrix[i]==0:
                    pos_matrix[i]=1
                else:
                    pos_matrix[i]=0
                

        
        #print pos_matrix

        ft=[]
        tt=[]
        
        for r in features_train:
            v=[]
           
            for i in range(0,9):

                if(pos_matrix[i]==1):
                
                    v.append(r[i])
                   

            ft.append(v)

        for r in features_test:
            v=[]
           
            for i in range(0,9):

                if(pos_matrix[i]==1):
                
                    v.append(r[i])
                   

            tt.append(v)
        
        clf = SVC(kernel='rbf', C=2**15,gamma=2**-19)
        clf.fit(ft, labels_train)

        pred=clf.predict(tt)

        from sklearn.metrics import accuracy_score

        acc=accuracy_score(pred,labels_test)

       # print acc
        
        print sum(pos_matrix)

        if sum(pos_matrix)<9 :
        
            if a0 < acc :
            
                a0=acc
                feature_subset=pos_matrix[:]
                print "I am not 9"
        
        

       # print pos_matrix    
       
    print "Max= " ,a0   
    print "Feature Subset:"
    print feature_subset

    return a0,feature_subset


    
