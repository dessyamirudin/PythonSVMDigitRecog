'''
Created on 18 Feb 2014

@author: Dessy Amirudin
'''

#from sklearn import svm
#from libsvm import *
from svmutil import *
#import csv

def main():
    # create the training & test sets
    print('reading file')
    has_header=True
    with open('train.csv','r') as csvfile:
        if has_header:csvfile.readline()
        data=[]
        for line in csvfile:
            line=line.strip().split(",")
            data.append([float(x) for x in line])
    
    target=[x[0] for x in data]
    train=[x[1:] for x in data]
    
    training=svm_problem(target,train)
    setparameter=svm_parameter('-t 0 -c 10')
    print('learning')   
    
    mod=svm_train(training,setparameter)
    #reading test file
    with open('test.csv','r') as testfile:
        if has_header:testfile.readline()
        testdata=[]
        for line in testfile:
            line=line.strip().split(",")
            testdata.append([float(x) for x in line])
    
    print('testing')
    #check the test
    y=[0]*len(testdata)
    #result=svm_predict(y,testdata,mod)
    p_label, p_acc, p_val = svm_predict(y, testdata, mod)
    
        #write the file
    print('writing')
    filesubmit=open('submission.csv','w')
    filesubmit.write("\n".join(str(x) for x in p_label))
    filesubmit.close
        
    print('end')
    
if __name__ == "__main__":
    main()