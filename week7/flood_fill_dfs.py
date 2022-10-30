def flood_fill(r, c, replacement, image):
    num_rows, num_cols = len(image), len(image[0])
    color = image[r][c]
    
    def get_neighbors(row, col):
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, 1, 0, -1]
        for i in range(len(row_delta)):
            neighbor_row = row + row_delta[i]
            neighbor_col = col + col_delta[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col
                  
    def dfs(row, col, visited):
        image[row][col] = replacement
        visited.add((row, col))
        for n_row, n_col in get_neighbors(row, col):
            if (n_row, n_col) in visited:
                continue
            dfs(n_row, n_col, visited)
        
    dfs(r, c, set())
    return image
    
    
from collections import deque

def flood_fill(r, c, replacement, image):
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    def dfs(root, visited=set()):
        row, col = root
        color = image[row][col]
        image[row][col] = replacement
        visited.add((row, col))
        for n_row, n_col in get_neighbors(root, color):
            if (n_row, n_col) in visited:
                continue
            dfs((n_row, n_col), visited)        


    dfs((r, c))
    return image
    
#Testing Code
r = 2
c = 2
replacement = 9
arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
res = flood_fill(r, c, replacement, arr)
for row in res:
    print(row, end='\n')