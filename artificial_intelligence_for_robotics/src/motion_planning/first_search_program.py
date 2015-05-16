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
        print row
    print '---------------'

def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed_grid = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed_grid[init[0]][init[1]] = 1
    gcosts = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    path_drawing = [['' for row in range(len(grid[0]))] for col in range(len(grid))]
    actions_grid = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]    #-1 is no defined action, 1,2,3,4 will be as defined in delta up,left,down,right
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
    draw_grid(expand)
    draw_grid(closed_grid)
    draw_grid(gcosts)
    draw_grid(path_drawing)

if __name__ == '__main__':
    print search(grid, init, goal, cost)
    pass
