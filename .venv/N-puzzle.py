import math
import heapq
import numpy as np
import copy
n = int(input())
# Destination
dest = [[i for i in range(j, j+n)] for j in range(0,n**2,n)]
dict = {}
# A dictionary for destination
mp = {dest[i][j]: [i,j] for i in range(0,n) for j in range(0,n)}
# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < n) and (col >= 0) and (col < n)

# Check if a cell is the destination
def is_destination(grid):
    return grid == dest
# Mahattan distance
def calculate_h_value(grid):
    sum = 0
    for i in range(n):
        for j in range(n):
            if (grid[i][j]) :
                sum += abs(i - mp[grid[i][j]][0]) + abs(j - mp[grid[i][j]][1])
    return sum

# Implement the A* search algorithm
def a_star_search(src, dest):
    # Initialize the closed list (visited cells)
    closed_list = set()
    # Initialize the details of each cell

    # Initialize the start cell details
    dict[tuple(tuple(sublist) for sublist in src)] = [0, 0, None]

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0, src))
    count = 0
    # Main loop of A* search algorithm
    while len(open_list) > 0:
        count += 1
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        currrent_grid = copy.deepcopy(p[1])
        closed_list.add(tuple(tuple(sublist) for sublist in p[1]))

        np_array = np.array(p[1])
        pos = np.argwhere(np_array == 0)
        i, j = pos[0][0], pos[0][1]
        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) :
                new_grid = copy.deepcopy(currrent_grid)
                new_grid[i][j] = new_grid[new_i][new_j]
                new_grid[new_i][new_j] = 0
                if tuple(tuple(sublist) for sublist in new_grid) not in closed_list:
                    if is_destination(new_grid):
                    # Set the parent of the destination cell
                        g_new = dict[tuple(tuple(sublist) for sublist in currrent_grid)][0] + 1
                        h_new = calculate_h_value(new_grid)
                        f_new = g_new + h_new
                        dict[tuple(tuple(sublist) for sublist in new_grid)] = [g_new, f_new, currrent_grid]
                    # Trace and print the path from source to destination
                        return g_new, count
                    else:
                        # Calculate the new f, g, and h values
                        g_new = dict[tuple(tuple(sublist) for sublist in p[1])][0] + 1
                        h_new = calculate_h_value(new_grid)
                        f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                        if tuple(tuple(sublist) for sublist in new_grid) in dict.keys():
                            if dict[tuple(tuple(sublist) for sublist in new_grid)][1] > f_new:
                            # Add the cell to the open list
                                heapq.heappush(open_list, (f_new, new_grid))
                            # Update the cell details
                                dict[tuple(tuple(sublist) for sublist in new_grid)] = [g_new, f_new, currrent_grid]
                        else:
                            heapq.heappush(open_list, (f_new, new_grid))
                            dict[tuple(tuple(sublist) for sublist in new_grid)] = [g_new, f_new, currrent_grid]
src = [list(map(int, input().split()))for i in range(n)]
print(a_star_search(src, dest))