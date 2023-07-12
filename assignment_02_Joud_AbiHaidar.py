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

