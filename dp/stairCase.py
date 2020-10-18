'''
	We pass a list qb to store the paths we already found with which we can reach our goal. We check if a path exists in our list to 
	reach the goal we don't calculate it again we just return its value. So this decreases the complexity from O(2^n) to O(n) as we
	dont need to calculate all the paths we already calculated in previous iterations.
'''

def countStair(n, qb):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if qb[n]:
		return qb[n]

	path = countStair(n-1, qb) + countStair(n-2 ,qb) + countStair(n-3, qb)
	qb[n] = path

	return path

n = 10
qb = [None]*100
print(countStair(n, qb))
