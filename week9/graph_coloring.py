"""
Given a list of edges for a graph, and a list of colors, 
find all ways to assign colors to each node such 
that no two adjacent nodes share the same color
Using integers for vertices
colors = [‘r’, ‘g’, ‘b’]
edges = [(0,1),(0,5),(1,5),(1,2),(2,3),(2,4),(3,4),(4,5)]
result = [['r', 'g', 'r', 'b', 'g', 'b']...]


"""



def graphColoring(edges, colors):
    # first we need to clean up the data
    # get all vertices
    all_vertices = set([x for y in edges for x in y])
    num_vertices = len(all_vertices)
    #convert edges to graph adjacency list
    #each index is the vertex, and the element is a nested list of neighbors
    adjList = [[] for _ in range(num_vertices)]
    for (src, dest) in edges:
        adjList[src].append(dest)
        adjList[dest].append(src)
    print(adjList)
    #make a helper function to check if current color is valid
    #ie no neighbors share this color
    def valid_color(adjList, graph_color, vertex, vertex_color):
        # check the color of every adjacent vertex of `v`
        for neighbor in adjList[vertex]:
            if graph_color[neighbor] == vertex_color:
                return False
        return True
    
    num_colors = len(colors)
    
    result = []
    
    def dfs(adjList, graph_color, vertex=0):
        #print(vertex, graph_color)
 
        # if all colors are assigned, we're done, return solution
        # we used integer colors so we need to convert these back to actuals
        if vertex == num_vertices:
            #print([colors[graph_color[vertex]] for vertex in range(num_vertices)])
            result.append([colors[graph_color[vertex]] for vertex in range(num_vertices)])
            return
     
        # try all possible combinations of available colors
        for try_color in range(num_colors):
            # if it is safe to assign color `c` to vertex `v`
            if valid_color(adjList, graph_color, vertex, try_color):
                # assign color `c` to vertex `v`
                graph_color[vertex] = try_color
     
                # recur for the next vertex
                dfs(adjList, graph_color, vertex + 1)
     
                # backtrack
                graph_color[vertex] = None
    
    #initialize an empty result set
    color_result = [None] * num_vertices
    #depth first search with backtracking to color all vertices
    dfs(adjList, color_result)
    
    return result
    
    
# Testing Code
colors = ['r', 'g', 'b']
edges = [(0,1),(0,5),(1,5),(1,2),(2,3),(2,4),(3,4),(4,5)]
        
result = graphColoring(edges, colors)
for r in result:
    print(r, end='\n')