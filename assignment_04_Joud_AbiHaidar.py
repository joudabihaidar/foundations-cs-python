# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:05:32 2023

@author: Legion
"""
#first of all i need to create a list or a dictionary of all users (and keep track of their position)
# next i need to create a 2d list for the adjacency matrix of size nxn and n will be the number of users/vertices
adj_matrix=[]
list_users=[]

class Socials:
  def __init__(self, adj_matrix,list_users):
    self.adj_matrix = adj_matrix
    self.list_users=list_users
    
  #################################
  # 1. add a user to the platform #
  #################################

  # to add a user to the platform, it will be a new user with no connections, so im gonna add an empty row and column to the matrix contaning 0's
  # and i also need to check if it already exits
  
  def AddUser(self,user):
      
    # validating the users username
    while user in self.list_users:
        print("this username already exists")
        user=input("enter another username")
        
    #adding a new row in the AM
    self.adj_matrix.append([0]*len(list_users))
              
    # adding the user to the users list
    self.list_users.append(user)
    
    #adding a new column in the AM to have a NxN matrix
    for vertice in self.adj_matrix:
        vertice.append(0) #adding an extra element in each list

  ######################################
  # 2. Remove a user from the platform #
  ######################################

  # i should check if it exists, if not, there's nothing to remove
  #that means i need to remove its column and row completely out of the AM
  # and i should not forget to remove it from the list of users
  
  def RemoveUser(self,user):
      
      if user not in self.list_users:
          print("the user does not exist")
      else:
          for i in range(len(self.list_users)):
              if list_users[i]==user:
                  
                  #removing the user from the list of users
                  list_users.pop(i)
                  
                  #removing its row from AM
                  self.adj_matrix.pop(i)
                  
                  #removing the column to have NxN matrix
                  for vertice in self.adj_matrix:
                      vertice.pop(i)
    
  ############################################
  # 3. Send a friend request to another user #
  ############################################

  # i should add a connection between two people which means im gonna update their connection in the AM to 1                 
    
  def AddConnection(self,user1,user2):
      for user in range(len(self.list_users)):
          #getting the index of user 1 so we can use it AM
          if self.list_users[user]==user1:
              index_user1=user
             
          #getting the index of user 2 so we can use it AM      
          if self.list_users[user]==user2:
              index_user2=user
              
      #changing the values of the edges in AM to indecate that there's a connection
      self.adj_matrix[index_user1][index_user2]=1
      self.adj_matrix[index_user2][index_user1]=1
    
  #####################################
  # 4. Remove a friend from your list #
  #####################################

  # i should remove a connection between two people which means im gonna update their connection in the AM to 0    
    
  def disconnet(self,user1,user2):
      #here its the same process as adding a friend
      # the only diffrence is that we're setting the edges to 0 since theres no more connection
      for user in range(len(self.list_users)):
          if self.list_users[user]==user1:
              index_user1=user
          if self.list_users[user]==user2:
              index_user2=user
      self.adj_matrix[index_user1][index_user2]=0
      self.adj_matrix[index_user2][index_user1]=0
    
 ################################
 # 5. View your list of friends #
 ################################

 # that means im gonna display all the connections of a certain user
 # i can do that by checking the AM matrix and where there's 1, ill display the username  
    
  def friends(self,user):
      for users in range(len(self.list_users)):
          if self.list_users[users]==user:
              
              #navigating in the list of connections of the user that we want
              for edge in range(len(self.adj_matrix[users])):
                  if self.adj_matrix[users][edge]==1:
                      print(self.list_users[edge])
  def displayUsers(self):
      for users in self.list_users:
          print(users)

                  
a=Socials(adj_matrix,list_users)
a.AddUser('joud')
a.AddUser('lala')
a.AddUser('nana')
a.AddConnection('joud', 'lala')
a.AddConnection('nana', 'lala')
a.friends('joud')
a.friends('lala')
a.friends('nana')
a.displayUsers()