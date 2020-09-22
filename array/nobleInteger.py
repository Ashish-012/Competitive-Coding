'''
	Just sort the array. If the numbers are repeating go to the last index of that number. 
	Check if the quantity of the numbers greater than that number is equal to the number(mindfuck lol).
	If no such number found return -1.

'''
def solve(self, A):
    A.sort()
    n = len(A)
    for i in range(n-1):
        if A[i] == A[i+1]:
            continue
        elif A[i] == n-i-1:
            return 1
    if A[n-1] == 0:       # Edge case to check if last number is 0 (0 numbers are greater than 0 so return 1)
        return 1
    return -1