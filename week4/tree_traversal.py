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
                    

#in order traversal binary tree            
def inOrderTraversal(root):
    stack = []
    node = root
    result = []
    while True:
        if node:
            stack.append(node)
            node = node.left
            
        elif stack:
            node = stack.pop()
            #print(node.val)
            result.append(node.val)
            node = node.right
            
        else:
            break
            
    return result

#pre order traversal binary tree
def preOrderTraversal(root):
    if root is None:
        return
        
    stack = []
    stack.append(root)
    
    result = []
    
    while stack:
        node = stack.pop()
        #print(node.val)
        result.append(node.val)
        #append right child first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
            
#post order traversal binary tree
def postOrderTraversal(root):
    if root is None:
        return
        
    s1 = []
    s2 = []
    s1.append(root)
    
    result = []
    
    while s1:
        node = s1.pop()
        s2.append(node)
        #append left child first
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
            
    while s2:
        node = s2.pop()
        #print(node.val)
        result.append(node.val)
        
    return result



#Binary Tree Example    
arr = [5,4,3,'x','x',8,'x','x',6,'x','x']
btree = build_tree(arr, BTreeNode)
PrintTree(btree)

print('level order ',levelOrderTraversal(btree))
print('in order ', inOrderTraversal(btree))
print('pre order ', preOrderTraversal(btree))
print('post order ', postOrderTraversal(btree))
