'''
Given an m x n 2D binary grid grid which represents a 
map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

'''

def num_islands(grid):
	#Observe for the "graph" relationship here
    #What constitutes a vertex (node), what is an edge?
    #How to find the neighbors of each vertex?
    
    #first we define the boundaries of our graph (matrix)
    max_row = len(grid)
    max_col = len(grid[0])
    
    #The matrix is our "graph"
    #each cell on the matrix is a node
    #their "graph neighbors" are represented as the cells adjacent (up, down, left, right)
    def get_neighbors(row, col):
        
        # steps to take in each of four directions
        dir_up = (-1, 0) #ie one row up, same column
        dir_down = (1, 0)
        dir_left = (0, -1)
        dir_right = (0, 1)
        # get neighbors in each direction
        for delta_row, delta_col in (dir_up, dir_down, dir_left, dir_right):
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            # does this neighbor cell exist in grid?
            if (
                neighbor_row < max_row and 
                neighbor_col < max_col and
                neighbor_row >= 0 and
                neighbor_col >= 0
                ):
                # if it does, return this neighbor to output
                # "yield" is more efficient than "return" when you have a large sequence
                yield (neighbor_row, neighbor_col)
            
    
    #Define a graph traversal technique (dfs floodfill from last session)
    #This is what we'll use to find one island (connected 1s)
    #In addition, we'll convert all cells of island from 1 to 0
    #this ensures we don't find the same island(cell with 1) again
    #assume we are starting from a cell with value 1
    def dfs_floodfill(row, col, visited=set()):
        visited.add((row, col))
        grid[row][col] = 0 # fill the cell with 0
        for n_row, n_col in get_neighbors(row, col):
            if (
                (n_row, n_col) not in visited and 
                grid[n_row][n_col] == 1
                ):
                dfs_floodfill(n_row, n_col, visited)
                
    
    #Walk through all grid cells (0s and 1s)
    #Perform traversal and count number of islands
    count = 0
    for grid_row in range(max_row):
        for grid_col in range(max_col):
            if grid[grid_row][grid_col] == 1: #found one part of an island
                count += 1
                #"remove" this island using floodfill
                dfs_floodfill(grid_row, grid_row)
    
    return count
    
    
#Testing Code
grid = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
]
print(num_islands(grid)) # expect 1

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1],
]
print(num_islands(grid)) # expect 3
