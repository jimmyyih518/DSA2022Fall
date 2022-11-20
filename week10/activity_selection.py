'''
Activity Selection
You are given n activities with their start and finish times. 
Select the maximum number of activities that can be performed 
by a single person, assuming that a person can only work on 
a single activity at a time. 

Input: activities = [(10,20), (15,25), (20,30)]
Output: [(10,20) ,(20,30)]

Greedy doesn't work if there's another variable involved:
ie each activity has a "weight" associated with it, and
we want to maximize the value of total "weight"

'''

def select_activity(activities):
    num_activities = len(activities)
    
    result = []
    
    # sort by end times
    activities.sort(key=lambda x: x[1])
    
    # Turn this into a list of start and a list of end times
    start_times, end_times = zip(*activities)
 
    # Greedy: The first activity is always selected
    i = 0
    result.append(activities[i])
 
 
    # Consider rest of the activities
    for j in range(1, num_activities):
 
        # Greedy: If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if start_times[j] >= end_times[i]:
            result.append(activities[j])
            i = j
            
    return result
    
#Testing Code
activities = [(10,20), (15,25), (20,30)]
print(select_activity(activities))