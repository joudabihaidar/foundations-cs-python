# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:50:40 2023

@author: Legion
"""
############
# Choice 1 #
############

def count(n):
    if n==0 or n==-1:
        return 0
    else:
        return 1+count(n//10)
n=int(input("enter a negative or positive number:"))
print(count(n))

############
# Choice 2 #
############

def maximum(l):
    if len(l)==1:
        return l[0]
    elif len(l)==0:
        return 0
    elif l[0]>l[1]:
        #return maximum(l[0:1]+l[2::])
        del l[1]
        return maximum(l)
    else:
        del l[0]
        return maximum(l)
        #return maximum(l[1::])
l=[-1,-3,-5,-4,10,90,80]
print(maximum(l))