#Recursive Implmentations of Binary Tree Traversals

from binary_tree import *                 

#in order traversal binary tree, left->current->right
def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.val, end=' ') #visit the node and "do something" part
        inOrderTraversal(root.right)
    
"""   
#Stack Implementation         
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
"""

#pre order traversal binary tree, current->left->right
def preOrderTraversal(root):
    if root is not None:
        print(root.val, end=' ') #visit the node and "do something" part
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


"""
#Stack Implmentation
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
    
"""     

      
#post order traversal binary tree, left->right->current
def postOrderTraversal(root):
    if root is not None:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val, end=' ') #visit the node and "do something" part


"""
#Stack Implementation
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

"""

#Binary Tree Example    
arr = [5,4,3,'x','x',8,'x','x',6,'x','x']
btree = build_tree(arr, BTreeNode)
PrintTree(btree)


inOrderTraversal(btree)
print('in order \n')
preOrderTraversal(btree)
print('pre order \n')
postOrderTraversal(btree)
print('post order \n')
