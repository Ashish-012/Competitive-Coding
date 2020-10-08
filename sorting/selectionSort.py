def selectionSort(arr):
	n = len(arr)
	for i in range(n):
		min_ = i
		for j in range(i+1,n):
			if arr[j] < arr[min_]:
				min_ = j
		arr[min_],arr[i] = arr[i],arr[min_]     
	print(arr)

arr = [64, 25, 12, 22, 11, 32, 97, 4, 9, 1] 

selectionSort(arr)