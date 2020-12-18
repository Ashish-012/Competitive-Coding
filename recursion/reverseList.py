def reverseList(arr):
	if len(arr) == 1:
		return arr 
	a = arr[0]
	return reverseList(arr[1:]) + [a]

arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(reverseList(arr))