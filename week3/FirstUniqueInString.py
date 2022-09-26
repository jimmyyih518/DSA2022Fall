#Find first unique element in string 
#using a Queue data structure with a hashtable

from collections import deque

def firstUniqChar(s):

    hashtable = {}
    queue = deque() #using double-ended queue here
    
    for idx, char in enumerate(s):
        hashtable[char] = hashtable.get(char, 0) + 1
        
        if hashtable[char] == 1:
            queue.append((char, idx))
            
        while len(queue) > 0 and hashtable[queue[0][0]] > 1:
            queue.popleft()
            
    if len(queue) == 0:
        return -1
    else:
        return queue[0][1]
    
       
#Testing Code
print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))
print(firstUniqChar('abba'))