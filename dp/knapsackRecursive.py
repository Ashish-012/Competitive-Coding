'''
	This is memoization approach of knapsack problem. First initialize a 2-d matrix of size W+1 and size of val array+1 with all the elemens as 0.
	Now we have option either to pick the element or not to pick.If the weght is less than the weight of the bag then only we can pick it.
	If we pick the element we subtract its weight from the weight of the back and we add its value. We can only pick the item only if its
	weight is smaller than the weight of the bag 

	Our answer will be the bottom right value in the matrix. 
'''


val = [11, 14, 10, 45, 30]
wt = [2, 5, 1, 3, 4]
W = 7
n = 5

t = [[0 for i in range(W+1)] for j in range(n+1)]

def knapsack(wt, val, W, n):
	if n == 0 or W == 0:
		return 0

	if t[n][W] != 0:
		return t[n][W]

	if wt[n-1] <= W :
		t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
		return t[n][W]

	elif wt[n-1] > W:
		t[n][W] = knapsack(wt, val, W, n-1)
		return t[n][W]

print(knapsack(wt, val, W, n))