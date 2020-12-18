def arraysum(arr):
	if len(arr) == 0:
		return 0
	num = arr[0]
	return num + arraysum(arr[1:])

arr = [15, 12, 13, 10]
print(arraysum(arr))