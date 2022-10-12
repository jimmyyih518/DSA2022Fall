# Definition for singly-linked list.
from linked_list import *
            

def deleteDuplicates(head):
    curr_node = head
    
    while curr_node:
        if not curr_node.next:
            return head
        
        if curr_node.val == curr_node.next.val:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next
    
    return head
        
        
#Testing Code
head = [1,1,2,3,3]
#output = [1,2,3]

root = create_linkedlist(head)
print_linkedlist(root)
"""
deleteDuplicates(root)
print_linkedlist(root)
"""