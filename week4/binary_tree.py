#Binary Tree Example

class BTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class NTreeNode:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def build_tree(nodes, node_type):
    nodes = iter(nodes)
    val = next(nodes)
    if val == 'x': 
        return None
    left = build_tree(nodes, node_type)
    right = build_tree(nodes, node_type)
    
    return node_type(val, left, right)

def PrintTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].val)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)  


if __name__ == '__main__':
    
    #Binary Tree Example    
    arr = [5,4,3,'x','x',8,'x','x',6,'x','x']
    btree = build_tree(arr, BTreeNode)
    PrintTree(btree)


    arr = [5,4,3,2,'x','x','x',8,'x','x',6,1,'x','x','x']
    btree = build_tree(arr, BTreeNode)
    PrintTree(btree)