'''
Created on 02/06/2015

@author: Arturo Escobedo
'''

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1    # the cost associated with moving from a cell to an adjacent one
delta = [[-1, 0 ],    # go up
         [ 0, -1],    # go left
         [ 1, 0 ],    # go down
         [ 0, 1 ]]    # go right
delta_name = ['^', '<', 'v', '>']

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

def compute_value(grid, goal, cost):
    """
    # compute_value returns a grid of values. The value of a cell is the minimum
    # number of moves required to get from the cell to the goal.
    #
    # If a cell is a wall or it is impossible to reach the goal from a cell,
    # assign that cell a value of 99.
    """
    values = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed_grid = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [['' for row in range(len(grid[0]))] for col in range(len(grid))]    #the grid with arrows >,<,v .... to draw the paths

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

            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and closed_grid[x2][y2] == 0:
                    if  grid[x2][y2] == 0:
                        values[x2][y2] = val
                        policy[x2][y2] = delta_name[(i + 2) % 4]    #Gets the inverse action
                        open_list.append([val, x2, y2])
                        closed_grid[x2][y2] = 1
                    else:
                        values[x2][y2] = 99

    draw_grid(values)
    draw_grid(policy)
    return values

if __name__ == '__main__':
    print compute_value(grid, goal, cost)
