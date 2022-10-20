#Traverse "Nested" data structure with recursion

def count_items(nested_list):
    count = 0

    for item in nested_list:
        if type(item) == list:
            #print('recurse in sublist')
            count += count_items(item)
        else:
            #print(f'counting item {item}')
            count += 1

    return count


#Testing code
my_nested_list = ['Adam', 
                  ['Bob', 
                        ['Chet', 'Cat'],
                        'Barb', 'Bert'], 
                  'Alex', 
                        ['Bea', 'Bill'], 
                  'Ann']

print(count_items(my_nested_list))


"""
#Stack Implementation of the recursive function

def count_items(nested_list):

    count = 0
    stack = []
    current_list = nested_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == nested_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if type(current_list[i]) == list:
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1
"""