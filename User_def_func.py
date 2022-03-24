#!/usr/bin/env python
# coding: utf-8

# # User Defined Functions

# In[29]:

"""1.addAllNumerics \n 2.isnumeric \n 3.prime \n 4.rotateStr"""
def addAllNumerics(*args):
    """sum of all numbers passed"""
    s = 0
    for x in args:
        s+=x
    return s
def checkIfNotNumeric(*args):    
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True
def isnumeric(*args):
    for i in args:
        if(isinstance(i,(float,int))):
            print (i,"is real no.")
        else:
            print(i,"is any other")
def prime(n):
    """Checking prime or not"""
    flag=True
    for i in range(2,n//2):
        if n%i==0:
            flag=False
    if(flag):
        return ("prime")
    else:
        return ("not")
def rotateStr():
    """rotating pattern of str"""
    n="string"
    for i in range(len(n)):
        print(n[i:len(n)]+n[-len(n):-len(n)+i])       
myName = '1.addAllNumerics \n 2.isnumeric \n 3.prime \n 4.rotateStr'

