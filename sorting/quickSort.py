def partition(arr, low, high):
	i = low-1
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1


def quickSort(arr, low , high):
	if low < high:
		p = partition(arr, low, high)   #calls for partition function and places it at its correct position
		quickSort(arr ,low ,p-1)             
		quickSort(arr, p+1, high)


arr = [10, 7, 8, 9, 1, 5, 23, 94, 42, 73, 420, 69] 
quickSort(arr ,0 , len(arr)-1)
print(arr)