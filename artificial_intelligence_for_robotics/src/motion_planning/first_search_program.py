'''
Created on 13/05/2015

@author: Arturo Escobedo
'''
# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0 ],    # go up
         [ 0, -1],    # go left
         [ 1, 0 ],    # go down
         [ 0, 1 ]]    # go right

delta_name = ['^', '<', 'v', '>']

def draw_grid(grid):
    print '---------------'
    for row in grid:
        print '|',
        for element in row:
            print element, '\t|',
        print
    print '---------------'

def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed_grid = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed_grid[init[0]][init[1]] = 1
    gcosts = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [['' for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]    #-1 is no defined action, 1,2,3,4 will be as defined in delta up,left,down,right
    x = init[0]
    y = init[1]
    g = 0
    step = 0    # The step at which each node is expanded
    open_list = [[g, x, y]]
    gcosts[x][y] = g

    found = False    # flag that is set when search is complete
    resign = False    # flag set if we can't find expand

    while not found and not resign:
        if len(open_list) == 0:
            resign = True
        else:
            open_list.sort()
            open_list.reverse()
            next_node = open_list.pop()
            x = next_node[1]
            y = next_node[2]
            g = next_node[0]
            expand[x][y] = step
            step += 1
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed_grid[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            gcosts[x2][y2] = g
                            closed_grid[x2][y2] = 1
                            action[x2][y2] = i    #The "i" action was taken to arrive to (x2,y2)



    if found:
        #Drawing the path with >,<,^, v symbols
        x = goal[0]
        y = goal[1]
        policy[x][y] = '*'
        while x != init[0] or y != init[1]:
            x2 = x - delta[action[x][y]][0]
            y2 = y - delta[action[x][y]][1]
            policy[x2][y2] = delta_name[action[x][y]]
            x = x2
            y = y2

        draw_grid(policy)
        return policy

if __name__ == '__main__':
    print search(grid, init, goal, cost)
    pass
