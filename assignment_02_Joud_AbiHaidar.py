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

############
# Choice 2 #
############

def maximum(l):
    if len(l)==1:
        return l[0]
    elif len(l)==0:
        return 0
    elif l[0]>l[1]:
        del l[1]
        return maximum(l)
    else:
        del l[0]
        return maximum(l)

########
# Menu #
########

def main():
    choices=['1','2','3','4']
    print("1. Count Digits\n2. Find Max\n3. Count tags\n4. Exit")
    print("- - - - - - - - - - - - - - -")
    choice=input("Enter a choice:")
    while (not choice.isnumeric()) or choice not in choices:
        choice=input("Enter a choice:")
    while choice!='4':
            if choice=='1':
                n=int(input("enter a negative or positive number:"))
                print(count(n))
            elif choice=='2':
                l=[]
                size=input("enter the size of the list:")
                while not size.isnumeric():
                    size=input("enter the size of the list:")
                for i in range(int(size)):
                    value=int(input(f"enter value {i}:"))
                    l.append(value)
                print(maximum(l))
            choice=input("Enter a choice:")
            while (not choice.isnumeric()) or choice not in choices:
                choice=input("Enter a choice:") 
main()