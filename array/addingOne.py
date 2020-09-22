'''
	Increment the last number by 1. Store the number at its ten's position in carry and store the one's 
	place in the array. Traverse the array backwards from 2nd last element, if the carry is 1 then add
	it to the element and store its ten's position in carry and one's position in array.
	In the end if we still have carry that means the number was like [9,9,9] so just add a 1 at the
	beginning of the required list.
 '''


def plusOne(self, A):
    n = len(A)-1
    A[n] += 1
    carry = A[n]/10
    A[n] = A[n]%10
    
    for i in range(n-1,-1,-1):
        if carry ==1 :
            A[i] += carry
            carry = A[i]/10
            A[i] = int(A[i]%10)
        
    if carry == 1:
        A.insert(0,1)
        return A
    while A[0] == 0:  # For interviewbit testcase [0,1,2,3,4] or [0,0,0,1,2], etc
        del A[0]
        
    return A