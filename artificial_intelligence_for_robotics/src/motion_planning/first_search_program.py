'''
Created on 13/05/2015

@author: Arturo Escobedo
'''
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------
from _imaging import path
from egginst.macho.util import move

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],    # go up
         [ 0, -1],    # go left
         [ 1, 0],    # go down
         [ 0, 1]]    # go right

delta_name = ['^', '<', 'v', '>']


    

def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    gcost = 0    #Initial gvalue is zero.
    path = [gcost, init[0], init[1]]    #[gcost, row, column]
    open_list = []    #Items that have to be checked
    gcosts = []    #Corresponding gcosts for each item in open_list
    closed_list = []    #Items that were already checked
    #Add the start point to the open list
    open_list.append(init)
    gcosts.append(gcost)    #initial cell will have zero cost.
    cell = open_list[0]
    while True :
        #Check if cell is the goal
        if cell == goal:
            path = [gcost, cell[0], cell[1]]
            print path
            return path    #If we find the goal we finish the programm
        else:
            #Add it to the closed list
            closed_list.append(cell)
            #Delete it from the open list
            index = open_list.index(cell)
            open_list.pop(index)
            gcosts.pop(index)
            #increase gcost
            gcost += cost
            #check cell neighbors
            neighbors = []
            for move in delta:
                possible_neighbor = [cell[0] - move[0], cell[1] - move[1] ]
                #Check if it is inside the grid
                if (possible_neighbor[0] >= 0 and possible_neighbor[0] < len(grid)) and (possible_neighbor[1] >= 0 and possible_neighbor[1] < len(grid[0])):
                    neighbors.append(possible_neighbor)
                    #Check if this cell is not occupied
                    if grid[possible_neighbor[0]][possible_neighbor[1]] == 0:
                        #Check if possble_neighbor is not in the closed_list or open_list
                        if possible_neighbor not in closed_list:
                            if possible_neighbor not in open_list:
                                #Add neighbor to the open list.
                                open_list.append(possible_neighbor)
                                gcosts.append(gcost)
            #Get item with minimum gcost item in the open_list

            if len(open_list)>0:
                gcost = min(gcosts)
                cell = open_list[gcosts.index(gcost)]
            else:
                print 'fail'
                return 0







            



if __name__ == '__main__':
    path = search(grid, init, goal, cost)
    pass
