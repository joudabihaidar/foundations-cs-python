# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:05:32 2023

@author: Legion
"""

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
