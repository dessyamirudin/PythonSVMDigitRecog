'''
Created on 18 Feb 2014

@author: Dessy Amirudin
'''
#import pandas as pd

from sklearn import svm
import csv

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
    
    print('learning')   
    #training
    clf=svm.SVC(gamma=0.001,C=100.)
    clf.fit(train, target)
    
    #reading test file
    with open('test.csv','r') as testfile:
        if has_header:testfile.readline()
        testdata=[]
        for line in testfile:
            line=line.strip().split(",")
            testdata.append([float(x) for x in line])
    
    print('testing')
    #check the test
    result=clf.predict(testdata)
    
    #write the file
    print('writing')
    with open('submission.csv','w') as filesubmit:
        for line in result:filesubmit.write(",".join(line)+"\n")
    
    print('end')
        
if __name__ == "__main__":
    main()
