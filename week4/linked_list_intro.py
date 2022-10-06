#Basic Linked List Implementation

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
        

#Initialize a few nodes
node1 = Node(1) # this will be the HEAD
node2 = Node(2)
node3 = Node(3)
node4 = Node(4) # this will be the TAIL

#Connect the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

#Iterate through the list
def print_linkedlist(node):
    while node:
        print(str(node.value)+' -> ', end='')
        node = node.next
        
    print('\n')
    
print_linkedlist(node1)

'''
#Insertion into linked list
def linkedlist_append(node, value):
    #traverse to TAIL node
    while node.next:
        node = node.next
        
    new_node = Node(value)
    node.next = new_node
    
linkedlist_append(node1, 5)
print_linkedlist(node1)

'''
'''
#"pop" aka delete the last element from linked list
def linkedlist_pop(node):
    #Two Pointer aka Fast Slow Pointer traversal
    curr_node = node
    next_node = node.next
    
    while next_node.next:
        curr_node = curr_node.next
        next_node = next_node.next
        
    curr_node.next = None
    
linkedlist_pop(node1)
print_linkedlist(node1)
'''    