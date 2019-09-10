
from sklearn.svm import SVC




def extract_col(col,ft):
    
    f=[]

    for a in ft:
        v=[]
        v.append(a[col-1])
        f.append(v)
    

    return f


def fitness(col,labels_train,labels_test,features_train ,features_test):

    f=extract_col(col,features_train)
    t=extract_col(col,features_test)
    

    clf = SVC(kernel='rbf', C=2**15,gamma=2**-19)
    clf.fit(f, labels_train)

    pred=clf.predict(t)

    from sklearn.metrics import accuracy_score

    acc=accuracy_score(pred,labels_test)

    #print acc
    


    a=0
    D=0.0
    X=len(pred)
    E=0.0
    Y=0.0

  

    for  a in range(0,len(pred)):
        
        if (pred[a] == labels_test[a]):
            num=0
            D+=1
            

        if (pred[a]=='4' and  labels_test[a]=='2'):
            E+=1
           

        if (labels_test[a]=='2'):
            Y+=1
            
    
        

        

    fit=(D/X)-(E/Y)
    return fit
