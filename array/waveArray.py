'''
	For interview bit they were asking for the lexicographic order as there could be 
	multiple solutions for the question. So the solution would be to sort all the elements 
	in the array and then swap every 2nd element with its neighbouring right element. But this 
	solution has a O(nlogn) complexity. The commented solution will execute in interviewbit
	A better solution would be traversing the list and checking left and right of every element.
	Traverse the list while stopping at every 2nd element and check if the previous element is greater
	than the current element, if it is then swap the two. Then check if the next element is greater than 
	the current, if it is then swap the two (it is due of the fact that for every element, we need the 
	previous element greater than the current, and next element smaller than the current).
'''
# def wave(self, a):                  # Solution for interviewbit 
# 	a.sort()
# 	n=len(A)
# 	for i in range(0,n-1,2):
# 		A[i],A[i+1]=A[i+1],A[i]
# 	return A

def wave(a):
    n = len(a)
    for i in range(0,n,2):
        if i>0 and a[i-1] > a[i]:
            a[i-1],a[i] = a[i],a[i-1]
        
        if i< n-1 and a[i] < a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    return a		

print(wave([ 5, 1, 3, 2, 4 ]))