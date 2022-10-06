# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
head = [1,1,2]
#output = [1,2]

head = [1,1,2,3,3]
#output = [1,2,3]