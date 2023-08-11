# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:05:32 2023

@author: Legion
"""
adj_matrix=[]
list_users=[]
class Graph:
  def __init__(self, adj_matrix,list_users):
    self.adj_matrix = adj_matrix
    self.list_users=list_users
  def AddUser(self,user):
      
    # validating the users username
    while user in list_users:
        print("this username already exists")
        user=input("enter another username")
    #adding a new column in the AM
    
    self.adj_matrix.append([0]*len(list_users))
              
    # adding the user to the users list
    self.list_users.append(user)
    
    #adding a new row in the AM to have a NxN matrix
    for vertice in self.adj_matrix:
        vertice.append(0) #adding an extra element in each list

  def RemoveUser(self,user):
      if user not in self.list_users:
          print("the user does not exist")
      else:
          for i,c in enumerate(self.list_users):
              # i stands for index
              # c stands for the element itself
              if c==user:
                  self.list_users.remove(c)
                  self.adj_matrix.remove(self.adj_matrix[i])

          #removing a row in the AM to have a NxN matrix
          for vertice in self.adj_matrix:
              vertice.pop() #removing an element in each list
        
    
#first of all i need to create a list or a dictionary of all users (and keep track of their position)
# next i need to create a 2d list for the adjacency matrix of size nxn and n will be the number of users/vertices

#################################
# 1. add a user to the platform #
#################################

# to add a user to the platform, it will be a new user with no connections, so im gonna add an empty row and column to the matrix contaning 0's
# and i also need to check if it already exits

######################################
# 2. Remove a user from the platform #
######################################

# i should check if it exists, if not, there's nothing to remove
#that means i need to remove its column and row completely out of the AM
# and i should not forget to remove it from the list of users

############################################
# 3. Send a friend request to another user #
############################################

# i should add a connection between two people which means im gonna update their connection in the AM to 1

#####################################
# 4. Remove a friend from your list #
#####################################

# i should remove a connection between two people which means im gonna update their connection in the AM to 0

################################
# 5. View your list of friends #
################################

# that means im gonna display all the connections of a certain user
# i can do that by checking the AM matrix and where there's 1, ill display the username

###########################################
# 6. View a list of users on the platform #
###########################################

#here, to traverse the graph, i can use bfs or dfs
