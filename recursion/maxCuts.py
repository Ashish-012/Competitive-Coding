'''
	Recursively call the function subtracting a,b,c from n and store the maximum among them in result. Stop calling
	the function recursively if n < 0  (cannot cut any further) or n == 0 (we got our goal). Now at the end if the
	result is -1 that means the cut cannot be made otherwise return result+1.
'''

def maxCuts(n,a,b,c):
	if n < 0:
		return -1
	if n == 0:
		return 0

	result =  max(maxCuts(n-a,a,b,c),maxCuts(n-b,a,b,c),maxCuts(n-c,a,b,c))
	if result == -1:
		return -1
	return result + 1

a = 9
b = 11
c = 3
n = 17
print(maxCuts(n,a,b,c))