#exercise 1
def fact(n):
    f=1 
    for i in range(1,n+1): 
        #we started from 1 cz we can't multiply with 0 and ended with n+1 since we didn't start from 0
        f=f*i
    return f
n=input("enter a positive number:")
while (n.isnumeric()==False):
    n=input("enter a positive number:")
while(int(n)<0):
    n=input("enter a positive number:")
print(fact(int(n)))


##############################################


#exercise 2
def div(n):
    d=[]
    for i in range(1,n+1):
        if (n%i==0):
            d.append(i)
    return d
n=input("enter a number:")
while (n.isnumeric()==False):
    n=input("enter a positive number:")
while(int(n)<0):
    n=input("enter a positive number:")
print(div(int(n)))


###############################################


#exercise 3
def reverseString(s):
    rev=""
    for i in s:
        rev=i+rev #if the string was joud, rev=d+u+o+j+" " 
    return rev
word=input("enter a string:")
print(reverseString(word))


################################################


#exercise 4
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


################################################


#exercise 5
def isStrongPass(p):
    #to check if we have at least 1 upper character:
    upp=False
    #to check if we have at least 1 lower character:
    low=False
    #to check if we have at least one digit
    digit=False
    for i in p:
        if (i.isupper()==True):
            upp=True
        if (i.islower()==True):
            low=True
        if (i.isdigit()==True):
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


##################################################


#exercise 6
def IPv4(s):
    #if number <0 or >255
    nb=True
    #if the number has a leading zero in octet
    zero=True
    #if we have consecutive periods
    period=True
    l=s.split('.')
    for i in l:
        if i=="": 
            #if the input was: 255.255.255..2 the list will be: [255,255,255,'',1]
            #theres a space where the dot is
            period=False
        if int(i)<0 or int(i)>255:
            nb=False
        if len(i)==2 and i[0]=='0':
            zero=False
    if len(l)==4 and nb==True and zero==True and period==True:
        print("valid IPv4 address")
    else:
        print("Invalid IPv4")

address=input("enter an IPv4 address:")
IPv4(address)