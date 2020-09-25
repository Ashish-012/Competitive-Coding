'''
	Set two pointers i and j to the end of the list. Traverse the list backwards. If we dont find a 0 decrement i
	if we find a zero then swap values at i and j. 
'''


def moveZeroes(arr, n): 
	j = n-1
	i = n-1
	while i >= 0 and j >= 0:
		if arr[i] == 0:
			arr[j],arr[i] = arr[i],arr[j]
			j-=1
			i-=1
		else:
			i-=1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
n = len(arr) 
moveZeroes(arr, n) 
 
print(arr) 