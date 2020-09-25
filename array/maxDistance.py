'''
	Create two additional arrays left min and right max and initialize them with same size as the original.
	Store the first value of the main array in leftmin, then traverse the main array and keep adding the 
	minimum value between prev value added in leftmin and current value of array.
	Now store the last value of the array at rightmax and traverse the list backwards and keep adding the
	maximum value between the last added value and current value of array.
	Now initialize two pointers pointing at starting index of the two arrays we created. And initialize answer
	to 0. Iterate the arrays till any of them ends. Check if the right array value is greater than left array,
	if yes then update ans while checking if ans is greater or the difference between j and i. Now increment j 
	till the value of right max is greater, if it is smaller than left min increment i    
'''


def maximumGap(A):
    n = len(A)-1
    left_min = [0]*(n+1)
    right_max = [0]*(n+1)
    
    left_min[0] = A[0]
    for i in range(1,n+1):
        left_min[i] = min(left_min[i-1],A[i])
        
    right_max[n] = A[n]
    for i in range(n-1,-1,-1):
        right_max[i] = max(right_max[i+1],A[i])
        
    i = 0
    j = 0
    ans = 0
    while i <= n and j<=n :
        if right_max[j] >= left_min[i]:
            ans = max(ans,j-i)
            j += 1
        else:
            i += 1
    return ans