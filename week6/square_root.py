#Estimate integer square root of a number
#Example input: 16, output: 4
#Example input: 8, output: 2, because square root of 8 is ~2.83...we only want the integer part so that is 2


def square_root(n):
    if n == 0:
          return 0
          
    left =1 
    right = n
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            result = mid
            right = mid - 1            
        else:
            left = mid + 1
    return result - 1
    
    
#Testing Code
print(square_root(16))
print(square_root(8))