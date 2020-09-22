'''
	Since we can move in 8 directions and one step at a time. The min distance we have to 
	travel is maximum value between difference in x and y coordinates of the preceding value.
	(if coordinates are (0,0) and (1,2) we need to travel atleast 2 steps). Store all such 
	distances in a sum and that is the required steps 
'''
def coverPoints(A, B):
    sum_ = 0
    for i in range(len(A)-1):
        sum_ += max(abs(A[i+1]-A[i]),abs(B[i+1]-B[i]))
    return sum_