
 ##############
 # exercise 1 #
 ##############
 
 
def fact(n):
    f=1 
    for i in range(1,n+1): 
        #we started from 1 cz we can't multiply with 0 and ended with n+1 since we didn't start from 0
        f=f*i
    return f
n=input("enter a positive number:")
while ( not n.isnumeric()): 
    # we don't have to check for neg nb since .isnumeric() doesn't consider them as numbers
    n=input("enter a positive number:")
print(fact(int(n)))


 ##############
 # exercise 2 #
 ##############
 
 
def div(n):
    d=[]
    for i in range(1,n+1):
        if i!=0:
            if (n%i==0):
                d.append(i)
    return d
n=input("enter a number:")
while ( not n.isnumeric()): 
    # we don't have to check for neg nb since .isnumeric() doesn't consider them as numbers
    n=input("enter a positive number:")
print(div(int(n)))


 ##############
 # exercise 3 #
 ##############
 
 
def reverseString(s):
    rev=""
    for i in s:
        rev=i+rev #if the string was joud, rev=d+u+o+j+" " 
    return rev
word=input("enter a string:")
print(reverseString(word))


 ##############
 # exercise 4 #
 ##############


def even(l):
    ev=[]
    for i in l:
        if (i%2==0):
            ev.append(i)
    return ev
n=int(input("enter the size of the list:"))
while(n<0):
    n=int(input("enter the size of the list:"))
l=[]
for i in range(n):
    v=int(input(f"enter value {i}:")) # f string
    l.append(v)
print(even(l))


 ##############
 # exercise 5 #
 ##############


def isStrongPass(p):
    #to check if we have at least 1 upper character:
    upp=False
    #to check if we have at least 1 lower character:
    low=False
    #to check if we have at least one digit
    digit=False
    for i in p:
        if (i.isupper()):
            upp=True
        if (i.islower()):
            low=True
        if (i.isdigit()):
            digit=True
    #to check if we have a special character
    special=False
    if ('#' in p) or ('?' in p) or ('!' in p) or ('$' in p):
        special=True
    if (len(p)>=8 and upp==True and low==True and digit==True and special==True):
        print("Strong password")
    else:
        print("Weak password")
s=input("enter a password:")
isStrongPass(s)


 ##############
 # exercise 6 #
 ##############


def IPv4(s):
    nb=True #if number >0 and <255
    zero=True #if the number doesn't have a leading 0 like '06'
    period=True  #if we don't have consecutive periods
    l=s.split('.')  #so we can track our numbers better 
    c=0 #to count the accurate number of octets
    for i in l:
        if i=="": 
            #if the input was: 255.255.255..2 the list will be: [255,255,255,'',1]
            #theres a space where the dot is
            period=False
            print("consecutive periods")
        else:
            c+=1 #thats why we created a counter c because we don't wanna count any extra spaces
            if i[0]=="-": #(i != "") so it won't give us an error message (IndexError:string index out of range)
                nb=False
                print(f"{i} is out of interval [0;255]")
        if i.isdigit() and int(i)>255: #we need to make sure that i is a digit and not a space or something else
            nb=False
            print(f"{i} is out of interval [0;255]")
        if len(i)>1 and i[0]=='0': #if the number starts with 0 and its length is >1 --> leading 0 
            zero=False
            print(f"{i} is {i[1::]} but with a leading 0")

    if c!=4:
        print("the length of this address is not 4")
    if c==4 and nb==True and zero==True and period==True:
        print("valid IPv4 address")
    else:
        print("Invalid IPv4")

address=input("enter an IPv4 address:")
IPv4(address)
#if we don't want to display the messages we can simply return so the program
#can skip the rest of the conditions