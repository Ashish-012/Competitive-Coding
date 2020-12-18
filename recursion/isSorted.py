def isSorted(arr):
	if len(arr) == 1:
		return True
		
	if arr[0] < arr[1] and isSorted(arr[1:]):
		return True
	else:
		return False

print(isSorted([1, 2, 3, 4, 5, 6, 7, 8]))