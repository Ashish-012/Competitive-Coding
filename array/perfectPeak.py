'''
	Maintain 2 arrays left and right. Add the first element of the array in `left` 
	then check next element, if it is greater than the previously added element then 
	add the next element of the array else add the first element again (basically keep adding
	the greater value between the previously added element in `left` and the value in actual array).
	Now add the last element of the array to `right`. Again traverse the list but in reverse 
	order and keep comparing between the previously added value in `right` and the `n-1`th value
	in the array. Whoever is smaller, add to the `right` so the resulting array will be in ascending
	order. In the end check if any element in array lies between `i-1` th value of `left` and `i+1`th
	value of `right`. If any such element exists add it to some list.
'''

arr = list(map(int, input().split()))
n = len(arr)
left= []
right =  [0]*len(arr)
left.append(arr[0])
answer = []
for  i in range(1,n):
	if arr[i] > left[i-1]:
		left.append(arr[i])
	else:
		left.append(left[i-1])

right[n-1] = arr[n-1]
for i in range(n-2,0,-1):
	if arr[i] < right[i+1]:
		right[i] = arr[i]
	else:
		right[i] = right[i+1]

for i in range(1,n-1):
	if left[i-1] < arr[i] < right[i+1]:
		answer.append(arr[i])
# if arr[0] <right[1]:    			# For edge cases (Passed all interview bit tests cases without this)
# 	answer.append(arr[0])
# if arr[n-1] > left[n-2]:
# 	answer.append(arr[n-1])

print(answer)

