"""
Find the length of the longest substring 
of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: longest substrings are abc, cab, both of length 3

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, length 2
"""


def longest_substring(s):
    window = set() # we can check if an element exists in o(1), unique elements only
    
    slow = 0
    longest = 0
    fast = 0
    while fast < len(s):
        if s[fast] not in window:
            window.add(s[fast])
            print(window)
            longest = max(longest, len(window))
            fast += 1
        else:
            window.remove(s[slow])
            print(window)
            slow += 1
    
    return longest

#Testing Code
s = 'abccabcabcc'
print(longest_substring(s))