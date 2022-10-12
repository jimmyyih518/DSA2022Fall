# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Create a linked list from an array
def create_linkedlist(arr):

    curr_node = ListNode(arr[0])
    root = curr_node
    i=1
    
    while i < len(arr):
        next_node = ListNode(arr[i])
        curr_node.next = next_node
        curr_node = next_node
        i += 1
        
    return root
    
#Print linked list from node(root)    
def print_linkedlist(root):
    while root:
        print(root.val, '->', end = ' ')
        root = root.next
    
    print('\n')
            

if __name__ == '__main__':
        
    #testing code
    head = [1,1,2,3,3]

    root = create_linkedlist(head)
    print_linkedlist(root)