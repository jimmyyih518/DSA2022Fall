#Merge Sort algorithm DAC example

#The DAC part, solving subproblems recursively
def mergeSort(L):
    if len(L) < 2: #base case
        return L[:]
    else:
        mid = len(L) // 2
        Left = mergeSort(L[:mid]) # DAC left
        Right = mergeSort(L[mid:])# DAC right
        return merge(Left, Right) # This is the Combine part
        
#The Combine part, merging solutions from DAC subproblems        
def merge(A, B):
    out = []
    i, j = 0, 0
    while i < len(A) and j < len(B): #walk through lists A and B, and append to output
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
            
        else:
            out.append(B[j])
            j += 1
    
    # Append remaining leftover elements from either list
    while i < len(A):
        out.append(A[i])
        i += 1
    
    while j < len(B):
        out.append(B[j])
        j += 1
    
    return out

#Testing Code
arr = [1,2,1]
print(mergeSort(arr))


