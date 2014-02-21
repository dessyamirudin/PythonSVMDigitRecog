'''
Created on 21 Feb 2014

@author: Dessy Amirudin
'''

from svmutil import *
import csv

def readcsv(namefile,header):
    isidata=[]
    with open(namefile,'r') as file:
        if header:file.readline()
        for line in file:
            line=line.strip().split(",")
            isidata.append([float(x) for x in line])
    return isidata

def main():
    print('reading file')
    data1=readcsv('submitted_libSVM_lin_c5.csv',header=True)
    data2=readcsv('submitted_libSVM_lin_c10.csv',header=True)
    data3=readcsv('submitted_libSVM_lin_c20.csv',header=True)
    data4=readcsv('rf_benchmark.csv',header=True)
    x1=[x[1] for x in data1]
    x2=[x[1] for x in data2]
    x3=[x[1] for x in data3]
    y=[x[1] for x in data4]
    
    #print(data1)
    print('\n')
    print('Presentase benar dari data 1')
    res1=evaluations(y,x1)
    print(res1)
    
    print('\n')
    print('Presentase benar dari data 2')
    res2=evaluations(y,x2)
    print(res2)

    print('\n')
    print('Presentase benar dari data 3')
    res2=evaluations(y,x3)
    print(res2)
    
    
if __name__=='__main__':
    main()
