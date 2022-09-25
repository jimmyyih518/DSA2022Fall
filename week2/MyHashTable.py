#Hashtable Class Exercise
class MyHashTable:
    def __init__(self, size):
        #Define the total size of the hashtable
        self.size = size
        #Create a list of empty lists
        self.table = []
        for i in range(self.size):
            self.table.append([])
            
    def __str__(self):
        return str(self.table)
        
    def hash(self, value): #the Hash Function
        value = str(value)
        hash_value = ord(value[0]) % self.size
        return hash_value
        
    def insert(self, element): #add an element into the hashtable
        hash_location = self.hash(element)
        self.table[hash_location].append(element)
    
    def member(self, element): #return true if element exists in hashtable, else false
        hash_location = self.hash(element)
        if element in self.table[hash_location]:
            return True
        else:
            return False
    
    def delete(self, element): #removes an element from the hashtable
        hash_location = self.hash(element)
        if self.member(element):
            self.table[hash_location].remove(element)
        else:
            print("Value not Found")
            
#Testing Code
s = MyHashTable(10)
s.insert('amy')
s.insert('chase')
s.insert('chris')
print(s.member('amy'))
print(s.member('chris'))
print(s.member('alyssa'))

s.delete('chase')
print(s.member('chase'))
s.delete('alyssa')