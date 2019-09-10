from __future__ import division    
import sys
from time import time

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
                v.append(-999999)
            else:
                v.append(float(b[i]))
           

        labels.append(b[len(b)-1])
        features.append(v)
    
    features.pop()
    labels.pop()
    
    return features,labels







def predict(ker="rbf",dataset="70-30",c=2**15,gam=2**-19):

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
        

    from sklearn.svm import SVC



    clf = SVC(kernel=ker, C=c , gamma=gam)  #optimized values 

    t0=time()

    clf.fit(features_train, labels_train) 

    print "Training Time:" ,round(time()-t0),"s"

    t1=time()
    pred=clf.predict(features_test)
    print "Predicition Time:" ,round(time()-t1),"s"


    from sklearn.metrics import confusion_matrix

    cm=confusion_matrix(labels_test, pred,labels=["2","4"])

    print cm    

    from sklearn.metrics import recall_score

    sens=recall_score(labels_test, pred, average=None) 
    
    print "Senstivity:" ,sens

    from sklearn.metrics import accuracy_score

    acc=accuracy_score(pred,labels_test)

    print "Accuracy:" ,acc

    return acc,sens,cm




