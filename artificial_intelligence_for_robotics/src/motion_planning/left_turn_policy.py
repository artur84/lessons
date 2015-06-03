'''
Created on 03/06/2015

@author: CORE 7
'''
# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],    # go up
           [ 0, -1],    # go left
           [ 1, 0],    # go down
           [ 0, 1]]    # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = un-navigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]    # given in the form [row,col,direction]
                    # direction = 0: up
                    #             1: left
                    #             2: down
                    #             3: right

goal = [2, 0]    # given in the form [row,col]

cost = [2, 1, 20]    # cost has 3 values, corresponding to making
                        # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

def draw_grid(grid):
    """ Prints the grid in a nice way
    """
    print '---------------'
    for row in grid:
        print '|',
        for element in row:
            print element, '\t|',
        print
    print '---------------'

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    values = [[[99 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[99 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[99 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[99 for row in range(len(grid[0]))] for col in range(len(grid))]]
    closed_grid = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]    #the grid with arrows >,<,v .... to draw the paths

    val = 0
    x = goal[0]
    y = goal[1]

    open_list = [[val, x, y]]
    closed_grid[x][y] = 1

    values[x][y] = val
    policy[x][y] = '*'
    found = False    # flag that is set when search is complete

    while not found:
        if len(open_list) == 0:
            found = True
        else:
            open_list.sort()
            open_list.reverse()
            next_node = open_list.pop()
            y = next_node[2]
            x = next_node[1]
            val = next_node[0] + cost

            for i in range(len(forward)):
                x2 = x + forward[i][0]
                y2 = y + forward[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and closed_grid[x2][y2] == 0:
                    if  grid[x2][y2] == 0:
                        values[x2][y2] = val
                        policy[x2][y2] = forward_name[(i + 2) % 4]    #Gets the inverse action
                        open_list.append([val, x2, y2])
                        closed_grid[x2][y2] = 1
                    else:
                        values[x2][y2] = 99

    draw_grid(values)
    draw_grid(policy)
    return policy

if __name__ == '__main__':
    print optimum_policy2D(grid, init, goal, cost)

