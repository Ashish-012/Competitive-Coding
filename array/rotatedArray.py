'''
	Perform a modified binary search. If the middle element is smaller than 1st element. That 
	means the required number is in left side of the array. Check if mid is smaller than mid-1
	if it is then mid is the required element. If it is not then update right by mid-1.
	If mid element is not smaller than left element that means required element is in the right
	side of the list. Check if mid+1 is smaller than mid, if it is return mid+1
'''

def findMin(A):
    n = len(A)-1
    l = 0
    r =n
    
    if len(A) == 1:      # if list contains only one element return it
        return A[0]
    if A[0]< A[n]:		 # if the list is already sorted return first elemenet
        return A[0]
        
    while l<=r:
        mid = l+ (r-l)/2
        if A[mid] < A[0]:
            if A[mid-1] > A[mid]:
                return A[mid]
            r = mid-1
        else:
            if A[mid+1] < A[mid]:
                return A[mid+1]
            l = mid+1 
    return -1