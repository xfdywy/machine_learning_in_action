# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 22:11:31 2016

@author: Administrator
"""
from numpy import *
import operator
from os import listdir

def img2vector(filename):
    res = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            res[0,32*i+j] = int(linestr[j])
    return res


def classify0(test,dataset,label,k):
    datasetsize = dataset.shape[0]
    diffmat = tile(test,(datasetsize,1))-dataset
    sqdiffmat = diffmat**2
    sqdis = sqdiffmat.sum(axis = 1)    
    dis = sqdis**0.5
    
    sorteddis = dis.argsort()
    
    classcount={}
    
    for ii in range(k):
        votelabel = label[sorteddis[ii],0]
        classcount[votelabel] = classcount.get(votelabel,0)+1
    sortedclasscount = sorted(classcount.iteritems(),key = operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]
    
    
    
    
    

def handwriteclass():

    trainingfile = listdir('trainingDigits')
    m = len(trainingfile)
    trainingdata = zeros((m,1024))
    traininglabel = zeros((m,1))
    for ii in range(m):
        thissample = trainingfile[ii]
        traininglabel[ii] = int(thissample.split('_')[0])
        trainingdata[ii,:] = img2vector('./trainingDigits/'+thissample)
    
    testfile = listdir('testDigits')
    n = len(testfile)
    err = 0.0
    for jj in range(n):
        thistest = testfile[jj]
        thislabel =  int(thistest.split('_')[0])
        testdata = img2vector('./testDigits/'+thistest)
        classifierres = classify0(testdata,trainingdata,traininglabel,3)
        print "the classifier came back with: %d, the real answer is: %d , the picture is %d" % (classifierres, thislabel,jj)
        if (classifierres != thislabel): err += 1.0
    print "\nthe total number of errors is: %d" % err
    print "\nthe total error rate is: %f" % (err/float(n))
        
        
    