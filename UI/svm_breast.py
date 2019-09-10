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



# Import Training Dataset

file1=open('winco_orig','r')
text1=file1.read()
file1.close()

features_train,labels_train=extract_data(text1)



def predict(test_set):

    from sklearn.svm import SVC

    clf = SVC(kernel='rbf', C=2**15 , gamma=2**-19)  #optimized values 

    clf.fit(features_train, labels_train) 

    pred=clf.predict(test_set)
    
        
    return pred






    

