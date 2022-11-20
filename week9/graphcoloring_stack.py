# Finds ALL ways to place n nonattacking queens on a n x n board
# NOTE: State[i] is the row for the queen on Column i
# NOTE: There are solutions for n>3
# Stack ADT with list implementation from Lab 5

class MyStack(object):
    
    def __init__ (self, type): # Creates an empty list
        self.elemType = type 
        self.state = [] # Empty list
    
    def __str__ (self): # for print
        return str(self.state) 
    
    def empty(self):
        return len(self.state) == 0
    
    def push(self, elem): # Adds an element to the top of a stack 
        assert type(elem) == self.elemType 
        self.state.append(elem)
        
    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack") 
        else:
            return self.state.pop()
        
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack") 
        else:
            return self.state[-1]


def nQueens(n):
    
    # Each state will include only the queens that have been placed so far
    
    initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    
    # While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentCol = len(currentState)
        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
        # Produce the state's children (if they are feasible)
        # Note children are produced backward so they come off the
        # stack later left to right
            for currentRow in range(n,0,-1):
            # Check horizontal and both diagonals of previous queens
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False 
                        break
                if feasible:
                    # Create child by making a copy and appending new col 
                    childState = currentState.copy() 
                    childState.append(currentRow)
                    s.push(childState) # Push child onto data structure

#nQueens(4)
# Testing code (check 4,5,6,7)
#for n in range(4,8):
#    nQueens(n)


def check_result(node, color, graph, result):
    curr_adj = graph[node]
    for i in range(len(curr_adj)):
        if curr_adj[i] and result[i] == color:
            return False
    return True

def graphColoring(graph, colors):
    
    color_table = dict(zip(range(0,len(colors)), colors))
    color_index = list(color_table.keys())
    
    n = len(graph)
    n_colors = len(color_index)
    result = [-1] * n
    curr_node = 0
    result[curr_node] = 0
    
    s = MyStack(list)
    s.push(result.copy())
    curr_node +=1
    tried_colors = [[] for _ in range(n)]
    
    while not s.empty():
        if all(x > -1 for x in result):
            break
        
        curr_state = s.pop()
        #print(curr_node)
        #print(curr_state)
        
        #list(range(curr_node,n))
        #child_node+=1
        for child_node in range(curr_node, n):
            curr_node_feasible = False
            for color in color_index:
                if check_result(child_node, color, graph, result) and color not in tried_colors[child_node]:
                    result
                    result[child_node] = color
                    #print(result)
                    s.push(result.copy())
                    curr_node_feasible = True
                    
                    break
                    
            if not curr_node_feasible:
                #s.push(curr_state.copy())  
                #s.pop()
                tried_colors[child_node-1].append(result[child_node-1])
                curr_node = child_node-1
                result = s.pop()
                break
        #time.sleep(1)            
    
    result_colors = [color_table[i] for i in result]
    return result_colors
    #return result
    
    
colors = ['r', 'g', 'b'] 

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
graph = [[False, True, False, False, False, True ], 
         [True, False, True, False, False, True ],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True ], 
         [True, True, False, False, True, False]]


print(graphColoring(graph, colors))

#Don's Example graph 2
graph = [[False, True, True, False, False, True],
        [True, False, True, False, False, True],
        [True, True, False, True, True, False],
        [False, False, True, False, True, True],
        [False, False, True, True, False, True],
        [True, True, False, True, True, False]]
print(graphColoring(graph, colors))

#Don's Example graph 3
graph = [[False, False, False, False, True, False],
        [False, False, True, False, False, True],
        [False, True, False, True, True, False],
        [False, False, True, False, True, True],
        [True, False, True, True, False, True],
        [False, True, False, True, True, False]]
print(graphColoring(graph, colors))

