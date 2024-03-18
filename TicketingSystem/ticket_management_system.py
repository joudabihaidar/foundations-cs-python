# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:11:31 2023

@author: Legion
"""
################################################################
# normal merge sort when there are no dictionaries in the list #
#                 (used it in function 3)                      #
################################################################

#https://youtu.be/cVZMah9kEjI
def mergeSortNormal(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2] #left array is from the start till the middle
        right_arr=arr[len(arr)//2:] # start from the middle till the end
        
        #recursion
        mergeSortNormal(left_arr) #to split again
        mergeSortNormal(right_arr) #to split again
        
        #merge
        i=0 # left_arr index
        j=0 # right_arr index
        k=0 #merged array index
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

##################################################
# Merge Sort when we have a list of dictionaries #
# (sorting by ticket, date, event, priority...)  #
##################################################

def mergeSortDict(arr,key_name):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2] #left array is from the start till the middle
        right_arr=arr[len(arr)//2:] # start from the middle till the end
        
        #recursion
        mergeSortDict(left_arr,key_name) #to split again
        mergeSortDict(right_arr,key_name) #to split again
        
        #merge
        i=0 # left_arr index
        j=0 # right_arr index
        k=0 #merged array index
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i][key_name]<right_arr[j][key_name]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
            
            
#################
# Binary Search #
#################

def binarySearch(ticket,tik_id):
  #binary search is used to search in sorted lists, and since we want to search a ticket,
  # we will merge sort it by ticket:
  mergeSortDict(ticket,'ticket_id')
  
  low = 0
  high = len(ticket) - 1

  while low <= high:

    mid = (low + high) // 2

    if (tik_id==ticket[mid]['ticket_id']):
      return ticket[mid]
    elif (tik_id> ticket[mid]['ticket_id']): 
      low = mid + 1
    else:
      high = mid - 1

  return -1

##################
# Date Validator #
##################
def dateValidator(year,month,day):
    
    #https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
    from datetime import datetime
    
    currentDay = str(datetime.now().day)
    currentMonth =str( datetime.now().month)
    currentYear = str(datetime.now().year)
    
    # the year shoudn't be less than the current year:
    while int(year)<int(currentYear):
        print('Invalid year')
        year=input('enter the year:')
        
    # The month can't be a smaller than the current month if we are in the current year:
    # also validating the interval of months between [1;12]
    while (int(year)==int(currentYear) and int(month)<int(currentMonth)) or (int(month)<1 or int(month)>12):
        print("Invalid month:")
        month=input('enter the month:')
        
    # The day can't be a smaller than the current day if we are in the current year and month:
    # also validating the interval of days between [1;31]
    while (int(year)==int(currentYear) and int(month)==int(currentMonth) and int(day)<int(currentDay)) or ( int(day) <1 or int(day)>31): 
        print("Invalid day:")
        day=input('enter the day:')
        
    #validating the digits:
    #if its < 1 digit we should add 0 for correct date string:
    if len(month)<2: 
        month='0'+month
        
    #same here:
    if len(day)<2: 
        day='0'+day
        
    #concatinating the date in the form that we want:
    Date=year+month+day 
    return Date

###########################
# Saving the updated file #
###########################

# it is more optimized to create a new file with all the updated data rather than appending it to the existing file
# because if we want to directly append to the existing txt file, the data would be unorderd and messy
 
def saveFile(tickets):
    saved_txt_file=''
    # Converting the list of tickets to a string so we can save them as a txt file
    for dictt in tickets:
        saved_txt_file+=dictt['ticket_id']+','+dictt['event_id']+','+dictt['username']+','+dictt['date']+','+str(dictt['priority'])+'\n'
        # Writing the txt file
        with open('updated_tickets.txt', "w") as txt_file:
            txt_file.write(saved_txt_file)
    print("the updated file  is saved")

###################
# display Tickets #
###################
def displayTickets(tickets):
    for i in tickets:
        print(i)


################################
# Menu options for admin users #
################################

#########################
# 1. Display Statistics #
#########################

def DisplayStatistics(tickets):
    maxi=0 #to know the maximum
    events={} #this dictttionary will be of this form : {ev003:1,ev004:3,....} where the key is the event_id and the value is its occurence
    for dictt in tickets:
        event_id=dictt['event_id'] 
        if event_id in events:
            events[event_id]+=1 
        else:
            events[event_id]=1 
    for key , value in events.items():
        if value > maxi:
            maxi=value
    #if we have more than one event that has the same number of tickets:
    print("The event(s) with most tickets is/are:")
    for key, value in events.items():
        if events[key]==maxi:
            print(key)
    
####################
# 2. Book a Ticket #
####################

def BookATicket(ev_id,user_name,Date,Priority,tickets):
    # since the list is sorted by priority, we have to get the the ticket_id that has the biggest id
    maxi=0
    for dictt in tickets:
        if int(dictt['ticket_id'][4:])>maxi:  #[4:] is used to only take the numbers after 'tick'
            maxi=int(dictt['ticket_id'][4:])
    tik_id='tick'+str(maxi+1)
    dictt={'ticket_id':tik_id,'event_id':ev_id,'username':user_name,'date':Date,'priority':Priority} #the new ticket
    tickets.append(dictt)
    mergeSortDict(tickets,'priority') #since it will be appended at the end regardless the priority we will merge sort it again


##########################
# 3. Display all tickets #
##########################



def displayAllTickets(tickets):
# step 1: getting the current date so we can know which tickets needs to be displayed
# step 2: creating a list called present_dates that contains all the dictionaries with the dates that we want
# step 3: sorting the list that we created 'present_date' by dates so we won't modify our original list
# step 4: creating a list called unique_dates that will hold only the dates that we want but without duplicates so the program won't compare the same date another time
# step 5: sorting the list 'unique_dates'
# step 6: comparing the dates in present_dates to the dates in unique_dates,
        # and if we have similar dates , we will append them to a new list called similar dates and sort them by event_id and display them on the screen  
      
    #https://www.programiz.com/python-programming/datetime
    import datetime
        
    # step 1:
    current_date = str(datetime.date.today())
    current_date=current_date.split('-')
    current_date=''.join(current_date)
    print(current_date)
    
    # step 2:
    present_dates=[]
    for dictt in tickets:
        
        if dictt['date']>=current_date:
            present_dates.append(dictt)
    print("--------------------------")
    
    #step 3:
    mergeSortDict(present_dates,'date')
    
    
    #step 4:
    unique_dates=[]
    for dictt in present_dates:
        unique_dates.append(dictt['date'])
        # to remove duplicates from unique_dates so we wont process the same date again:
        # we can simply convert the list into a set and the from a set to a list again :
    unique_dates=set(unique_dates)
    unique_dates=list(unique_dates)
    
    #step 5:
    #sorting again since the set does't respect order
    mergeSortNormal(unique_dates) #using merge sort normal since its not a dictionary
    
    #step 6:
    for date in unique_dates:
        similar_dates = []
        for dictt in present_dates:
            if dictt['date'] == date:
                similar_dates.append(dictt)
        # sorting the similar dates by tickets:
        mergeSortDict(similar_dates,'event_id')
        
        for i in similar_dates:
            print(i['ticket_id'], ' ', i['event_id'],' ',i['date'])


    
###############################
# 4. Change Ticket's Priority #
###############################
def changePriority(ticket,tik_id,p):
    if binarySearch(ticket,tik_id) == -1:
        print("Ticket not found")
    else:
        binarySearch(ticket,tik_id)['priority']=p
    # we will merge sort it by priority again because in the binarysearch function, we are merge sorting them by ticket to be able to find a ticket
    mergeSortDict(ticket,'priority')  

#####################
# 5. Disable Ticket #
#####################

def disbaleTicket(ticket,tik_id):
    if binarySearch(ticket, tik_id)==-1:
        print("ticket not found")
    else:
        binarySearch(ticket,tik_id)
        #since the binarySearch function return the value not the index, i used .remove
        #https://note.nkmk.me/en/python-list-clear-pop-remove-del/#:~:text=In%20Python%2C%20use%20list%20methods,with%20an%20index%20or%20slice.
        ticket.remove(binarySearch(ticket,tik_id))
        # we will merge sort it by priority again because in the binarysearch function, we are merge sorting them by ticket to be able to find a ticket
        mergeSortDict(ticket,'priority')
        
#################
# 6. Run Events #
#################     
        
def runEvents(ticket):
    
    #https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
    from datetime import datetime
    
    #getting the current date:
    currentDay = str(datetime.now().day)
    currentMonth = str(datetime.now().month)
    currentYear = str(datetime.now().year)
    if len(currentMonth)<2: #if its < 1 digit ww should add 0 for correct date string
        currentMonth='0'+currentMonth
    if len(currentDay)<2: #same here
        currentDay='0'+currentDay
    currentDate=currentYear+currentMonth+currentDay #concatinating the date in the form that we want
    
    # using sequential search for the events with the current date,
    #because we can't use binary search here since it stops as soon as it finds the first occurence
    counter=0
    for dictt in ticket:
        if dictt['date']==currentDate:
            # it will be displayed by priority since its already sorted
            print("this event is today :", dictt['event_id']," with priority :", dictt['priority'])
            ticket.remove(dictt)
            counter+=1 #to test if there are events today or not
    if counter==0:
        print('no events for today')
        
        
#################################
# Menu options for normal users #
#################################

####################
# 1. Book a ticket #
####################

def bookATicket(ev_id,username,Date,ticket):
    # since the list is sorted by priority, we have to get the the ticket_id that has the biggest id
    maxi=0
    for dictt in ticket:
        if int(dictt['ticket_id'][4:])>maxi:  #[4:] is used to only take the numbers after 'tick'
            maxi=int(dictt['ticket_id'][4:])
    tik_id='tick'+str(maxi+1)
    dictt={'ticket_id':tik_id,'event_id':ev_id,'username':username,'date':Date,'priority':0} #the new ticket
    ticket.append(dictt)
    mergeSortDict(ticket,'priority') #since it will be appended at the end regardless the priority we will merge sort it again
        
    
########
# Main #       
########
def main():

    ########################################################################################
    # Importing tickets from the text file into the special list without user intervention #
    ########################################################################################
    
    ####################
    # reading the file #
    ####################
    with open("tickets.txt", 'r') as file:
        text_file=file.read()
    #####################
    # Creating the list #
    #####################
    # tickets is the list of dictttionaries which will be of this form:
        # tickets=[{ticket_id:value, event_id:value, username:value, date:value, priority:value},{...},{...}]
    tickets=[]             
    #assuming that the structure of the text file is always: ticket_id, event_id, username, date, priority  
    #for iterating throught each line in a multiline string:
        #https://stackoverflow.com/questions/3054604/iterate-over-the-lines-of-a-string
    lines=text_file.splitlines() #this will return a list containing each line as an element
    for i in range(len(lines)):
        tik={}  # tik is the dictttionary of each ticket
        lines[i]=lines[i].split(',') #splitting each line by ','
        tik['ticket_id']=lines[i][0].strip()
        tik['event_id']=lines[i][1].strip()
        tik['username']=lines[i][2].strip()
        tik['date']=lines[i][3].strip()
        tik['priority']=int(lines[i][4].strip())
        tickets.append(tik)
    #sorting the tickets list by priority:
    mergeSortDict(tickets,'priority')
    displayTickets(tickets)
    
    
    
    ################################################################
    # Greeting the user and asking for their username and password #
    ################################################################
    
    #all posibilities:
        #for admins:
    	  #-he might enter a wrong username that contain the word 'admin' which means he is an admin but entered the wrong username
    	  #-the admin might input an empty password but that doesn't mean that hes a normal user
        #for users:
    	  #-the user might input a normal username and fill the password, he shouldn't input a password cz hes a user
    
    print("Login form")
    print("------------")
    username=input("username:")
    password=input("password:")
    
    
    ##############
    # Admin User #
    ##############
    
    if 'admin' in username:
        choices=['1','2','3','4','5','6','7']
        #it means that an admin in trying to log in
        c=1 #c is the counter of attempts and it starts by 2 since we already took an input from the user
        while (username!='admin' or password!='admin') and c!=6:
            if username=='admin' and password != 'admin123123':
                #the username is correct but the pass is wrong
                print(f' attempt {c}')
                print("Incorrect password")
                password=input("password:")
            else:
                #the username is wrong cz its != 'admin'
                #checking the password:
                if password != 'admin123123':
                    #username and password are wrong
                    print(f' attempt {c}')
                    print("Incorrect username and password")
                    username=input("username:")
                    password=input("password:")
            c+=1
        if (username == 'admin' and password == 'admin123123'):
            # we display the admins menu
            print("------------")
            print("Menu")
            print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")
            choice=input("Enter your choice:")
            while choice not in choices:
                choice=input("Enter your choice:")
            while choice != '7':
                
                #############
                # choice 1: #
                #############
                if choice=='1':
                    DisplayStatistics(tickets)
                    
                #############
                # choice 2: #
                #############
                elif choice=='2':
                    ev_id=input("enter the event id:")
                    #validating the event_id:
                    while 'ev' not in ev_id:
                        ev_id=input("enter the event id:")
                    user_name=input("enter the username:")
                    
                    # inputing the date and validating it:    
                    year=input('enter the year:')
                    # the year should be numeric:
                    while not year.isnumeric():
                        year=input('enter the year:')
                        
                    month=input('enter the month:')
                    # the month should be numeric:
                    while not month.isnumeric():
                        month=input('enter the month:')
                        
                    day=input('enter the day:')
                    # the day should be numeric:
                    while not day.isnumeric():
                        day=input('enter the day:')
                    # Validating the date, this fucntion will return the correct date form with the correct year, month and day:
                    date=dateValidator(year, month, day)    
                        
                    Priority=input("enter the priority:")
                    #validating the priority to be an integer:
                    while not Priority.isnumeric(): 
                        Priority=input("enter the priority:")
                    #priority should always be an int:
                    Priority=int(Priority)
                    
                    BookATicket(ev_id,user_name,date,Priority,tickets)
                    displayTickets(tickets)
                    
                #############
                # choice 3: #
                #############
                elif choice=='3':
                    displayAllTickets(tickets)
                    
                #############
                # choice 4: #
                #############
                elif choice=='4':
                    tik_id=input("enter the ticket_id:")
                    #validating the ticket's input:
                    while 'tick'not in tik_id:
                        print("invalid id")
                        tik_id=input("enter the ticket_id:")
                    p=input("enter the priority:")
                    #validatin the priority to be an int:
                    while not p.isnumeric():
                        p=input("enter the priority:")
                    p=int(p) #priority always int
                    changePriority(tickets,tik_id,p)
                    displayTickets(tickets)
     
                #############
                # choice 5: #
                #############
                elif choice=='5':
                    tik_id=input("enter the ticket_id:")
                    #validating the ticket's input:
                    while 'tick'not in tik_id:
                        print("invalid id")
                        tik_id=input("enter the ticket_id:")
                    disbaleTicket(tickets,tik_id)
                    displayTickets(tickets)
                 
                #############    
                # choice 6: #
                #############
                elif choice=='6':
                    runEvents(tickets)
                    displayTickets(tickets)
                print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")
                choice=input("Enter your choice:")
                while choice not in choices:
                    choice=input("Enter your choice:")
            # Asking the admin if he wants to save the updated file:
            IsSave=input(f"do you wanna save choice {choice}?") 
            IsSave=IsSave.lower()
            # Validating his answer:
            while IsSave!='yes' and IsSave!='no':
                IsSave=input(f"do you wanna save choice {choice}?") 
                IsSave=IsSave.lower() 
            if IsSave=='yes':
                saveFile(tickets)
                
        else:
            #if the username and password are still incorrect, we cant display the menu
            print("since there's no correct username or password after 5 attempts, we can't display the menu")
            
            
    ###############
    # Normal User #        
    ###############
    else:
        #its a normal user
        #but what if the normal user entered a password:
        if password != '':
            print("as a user, your password should be empty")
            password=''
        print("------------")
        
        ########
        # Menu #
        ########
        choices=['1','2']
        print("Menu")
        print("1. Book a ticket\n2. EXit")
        choice=input("enter your choice:")
        while choice not in choices:
            choice=input("enter your choice:")
        while choice!='2':
            
            #############
            # choice 1: #
            #############
            
            if choice=='1':
                ev_id=input("enter the event id:")
                #validating the event_id:
                while 'ev' not in ev_id:
                    ev_id=input("enter the event id:")
                # inputing the date and validating it:    
                year=input('enter the year:')
                # the year should be numeric:
                while not year.isnumeric():
                    year=input('enter the year:')
                    
                month=input('enter the month:')
                # the month should be numeric:
                while not month.isnumeric():
                    month=input('enter the month:')
                    
                day=input('enter the day:')
                # the day should be numeric:
                while not day.isnumeric():
                    day=input('enter the day:')
                # Validating the date, this fucntion will return the correct date form with the correct year, month and day:
                date=dateValidator(year, month, day)
                bookATicket(ev_id,username,date,tickets) 
            
            print("1. Book a ticket\n2. EXit")
            choice=input("enter your choice:")
            while choice not in choices:
                choice=input("enter your choice:")
        saveFile(tickets)
main()
        





    

 
    

    


    