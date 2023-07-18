# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:40:38 2023

@author: Legion
"""

def displayParsedData(p):
    for i,d in enumerate(p):
        print("-----------")
        print(f"Object {i}:")
        print("-----------")
        for key, value in d.items():
            print("KEY:",key,"\t","VALUE:",value)
        print("\n")
    
# part 1) Reading the file:
    
with open(r"C:\Users\Legion\Desktop\assignment_03\JSON_file.json", 'r') as file:
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
#print(objects_list)




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
print(parsed_data)  

      


# part 5) Printing the objects:

displayParsedData(parsed_data)


