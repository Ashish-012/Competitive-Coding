'''
	Simple recursion function. If the number is single digit, return the number otherwise take the last digit
	apart and recursively call the function, also add the last digit that we just seperated to the recursive call. 
'''

def sumOfNum(n):
	if n < 10:
		return n

	return  n%10 + sumOfNum(int(n/10)) 

print(sumOfNum(15834))