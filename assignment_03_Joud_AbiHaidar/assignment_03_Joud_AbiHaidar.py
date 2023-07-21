# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:40:38 2023

@author: Legion
"""
############
# Choice 1 #
############

def sumTuple(t1,t2):
    SUM=[]
    for i in range(len(t1)):
        s=0
        s=s+t1[i]+t2[i]
        SUM.append(s)
    return tuple(SUM)

#############
# Choice 2: #
############# 

def exportJson(dic,filename):
    #print(employees)
    s='['+'\n'
    for i, c in enumerate(employees):
        s+='\t'+'{'+'\n'+'\t'
        for key, value in c.items():
            if not issubclass(type(value), str):
                s+='\t'+'"'+key+'"'+':'+str(value)+','+'\n'+'\t'
            else:
                s+='\t'+'"'+key+'"'+':'+'"'+value+'"'+','+'\n'+'\t'
        if i==len(employees)-1:
            s+='}'+'\n'+']'
        else:
            s+='},'+'\n'
    print(s)
    
    filename = "data.json"
    with open(filename, "w") as json_file:
        # Step 4: Write the JSON-formatted string to the file
        json_file.write(s)

employees=[{'name': 'John Doe', 'age':20, 'job_title': 'Software Engineer','skills':['sql','python','java','html']}, {'name': 'Jane Smith', 'age': 25, 'job_title': 'Data Analyst','skills':["sql","R language","python","tableau"]}, {'name': 'Michael Johnson', 'age': 28, 'job_title': 'Product Manager','skills':["management","team-work"]}]

############
# Choice 3 #
############

def displayParsedData(p):
    for i,d in enumerate(p):
        print("-----------")
        print(f"Object {i}:")
        print("-----------")
        for key, value in d.items():
            print("KEY:",key,"\t","VALUE:",value)
        print("\n")

def importJson(json_file):
    
    # part 1) Reading the file:
        
    with open(json_file, 'r') as file:
        json_data=file.read()
    #print(json_data)
    json_data=json_data.split()
    
    
    
    #part 2) Cleaning the data:
         
    unwanted_char=['[{',',','}','},',']','[']
    #removing unwanted characters that make the task harder and leaving only "{" to distinguish objects
    # and adding them to the cleaned data list
    cleaned_data=[]
    for i, c in enumerate(json_data):
        if c not in unwanted_char:
            cleaned_data.append(c)
    #print(cleaned_data)
    #joining the cleaned data so we can split it again by "{" and have the objects seperated from each other
    cleaned_data=" ".join(cleaned_data)
    cleaned_data=cleaned_data.split('{')
    #print(cleaned_data)
    
    
    
    
    #part 3) Creating a list of objects:
        
    #objects_list will be a 2d list where each list inside is an object and each elements inside the inner lists
    #is a key value pair
    objects_list=[]
    for obj in cleaned_data:
        objects_list.append(obj.split(','))
    #taking into consideration the spaces at the start and end of the json file
    if objects_list[0]==['']:
        objects_list=objects_list[1:len(objects_list)]
    if objects_list[len(objects_list)-1]==['']:
        objects_list=objects_list[0:len(objects_list)-1]
    print(objects_list)
    
    
    
    
    # part 4) Parsing the data:
    
    #parsed_data is the list that contains dictionaries of each object from the JSON file
    parsed_data=[]
    for i in objects_list:
        dictJson={}
        for j in i:
            j=j.split(":") #seperating the key value pairs so we can add them to the dictionary
            #key is j[0] before ":"
            #value is j[1] after ":"
            dictJson[j[0].strip().strip('"')]=j[1].strip().strip('"') 
            # .strip().strip(' " ') to remove spaces and excess """
        parsed_data.append(dictJson)
    
    
    print (parsed_data)
    
json_file=r"C:\Users\Legion\Desktop\FCS\Assignments\assignment_03_Joud_AbiHaidar\JSON_file1.json"
importJson(json_file)   
    
# part 5) Printing the objects:
    
#displayParsedData(importJson(json_file))



