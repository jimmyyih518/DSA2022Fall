from binary_tree import *

#level order traversal binary tree
def levelOrderTraversal(root):
    from collections import deque
    queue = deque()
    queue.append(root)
    
    levels = 0
    result = []
    while queue:
        n = len(queue)
        curr_level = []
        for i in range(n):
            curr = queue.popleft()
            if curr:
                curr_level.append(curr.val)
            for child in [curr.left, curr.right]:
                if child:
                    queue.append(child)
        
        levels += 1
        for val in curr_level:
            result.append(val)
        
    return result
                    


#Binary Tree Example    
arr = [5,4,3,'x','x',8,'x','x',6,'x','x']
btree = build_tree(arr, BTreeNode)
PrintTree(btree)

print('level order ',levelOrderTraversal(btree))



#level order traversal binary tree
def Value_in_tree(root, target):
    from collections import deque
    queue = deque()
    queue.append(root)
    
    levels = 0
    result = []
    while queue:
        n = len(queue)
        curr_level = []
        for i in range(n):
            curr = queue.popleft()
            if curr.val == target: #check the value is in tree
                return True
            if curr:
                curr_level.append(curr.val)
            for child in [curr.left, curr.right]:
                if child:
                    queue.append(child)
        
        levels += 1
        for val in curr_level:
            result.append(val)
        
    return False #return false if value not found

#Testing Code    
Value_in_tree(btree, 8)
Value_in_tree(btree, 7)