from collections import deque
from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
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

    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] = replacement # replace root color
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement # replace color
                queue.append(neighbor)
                visited[r][c] = True

    bfs((r, c))
    return image
    
#Testing Code
r = 2
c = 2
replacement = 9
arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
print(flood_fill(r, c, replacement, arr))