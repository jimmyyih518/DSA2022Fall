# basic backtracking template

def is_solution(current_index):
    #this is the logic to determine if we've found a possible solution
    #this means we've reached a leaf node on the state space tree
    return

def check_solution(path):
    #is the current solution an optimal one?
    #if it is, return and we're done
    return
    
def get_neighbours(current_index):
    #think about graph and trees
    #at the current index, what are the next steps(children)
    return

def dfs_backtrack(start_index, path=[]): #path could be a list, set, etc...
  if is_solution(start_index):
    #we found a leaf node (possible solution), but is it the optimal one?
    check_solution(path)
    return
  for neighbor in get_neighbours(start_index):
    if is_valid(neighbor): #prune the state space tree if we know this neighbor isn't valid
        #add this neighbor to our path
        path.append(neighbor)
        #recurse down this path (go all the way to the bottom)
        dfs_backtrack(start_index + 1, path)
        #if it didn't work, pop it and try a different path
        path.pop()
    
