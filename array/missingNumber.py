'''
	Since the numbers are natural numbers. You can calculate the sum of the first
	n natural numbers by the formula n*(n+1)/2 and store it in some variable. 
	Then take the sum of all the elements in the array in some variable. The difference
	of the two variables `required_sum - new_sum` is the missing number. 
'''

arr = []
for i in range(99):
    arr.append(input().strip('\r'))
arr = list(map(int,arr))

required_sum = sum(range(1,101))
new_sum = sum(arr)

print(required_sum - new_sum)
