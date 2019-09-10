from __future__ import division    
import sys
from time import time

def extract_data(text):
    x= text.split('\n')

    features=[]
    labels=[]

    print x;
    
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


# Import Testing Dataset

file2=open('winco_test','r')
text2=file2.read()
file2.close()

features_train,labels_train=extract_data(text1)

features_test,labels_test=extract_data(text2)



print "Training Set :", len(features_train)
print "Testing Set :", len(features_test)


from sklearn.svm import SVC



clf = SVC(kernel='rbf', C=2**15 , gamma=2**-19)  #optimized values 

t0=time()

clf.fit(features_train, labels_train) 

print "Training Time:" ,round(time()-t0),"s"

t1=time()
pred=clf.predict(features_test) 
print "Predicition Time:" ,round(time()-t1),"s"

from sklearn.metrics import accuracy_score

acc=accuracy_score(pred,labels_test)

print "Accuracy:" ,acc


