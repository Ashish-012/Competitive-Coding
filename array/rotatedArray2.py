'''
	We can perform a modified binary search. Go to the middle element and check if it is the
	required value. 
	If not check if the first element is smaller than the middle. If it is then left side is sorted.
	 Now check if the required element is greater than left and smaller than mid. If it is then it is
	 located in left side, update right by mid-1. Otherwise it is present in right side so update left by mid+1.
	Else the right list is sorted. Check if the required value lies between mid and right. If it is then perform
	 binary search in right side otherwise the required value is present in left side, so update right by mid-1.
	If no key is found return -1.
'''

def search(A, B):
    n = len(A)-1
    l = 0
    r = n
    
    while l<=r:
        mid = int(l+(r-l)/2)
        if A[mid] == B:
            return mid
        if A[l] < A[mid]:
            if A[l]<= B and B <= A[mid]:
                r = mid -1
            else:
                l = mid+1
        else:
            if A[mid] <= B and B <=A[r]:
                l = mid+1
            else:
                r = mid-1
    return -1