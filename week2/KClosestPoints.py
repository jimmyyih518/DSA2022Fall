import heapq

def distance(a, b):
	distance = (a[0]-b[0])**2 + (a[1]-b[1])**2
	return distance

def KClosest(points, k):
    
    heap=[]
    #for ind, i in enumerate(points):
    for idx, pt in enumerate(points):
        pt_dist = distance(pt, (0,0))
        heapq.heappush(heap,(pt_dist,idx))
        
    result=[]
    for i in range(k):
        result.append(points[heapq.heappop(heap)[1]])
        
    return result
    
#Testing Code  
points = [[1,3],[-2,2]]
k = 1
print(KClosest(points, k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(KClosest(points, k))

#Visualize
#https://www.desmos.com/calculator