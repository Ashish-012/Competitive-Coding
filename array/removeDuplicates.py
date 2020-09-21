'''
	This problem was simple if we use a hashmap. But the problem says don't take extra space
	so I used different approach.
	Initialize two variables which point at first index of the array `i` and `j`. If the value
	at index i is not same as in i-1, overwrite the `j`th element with i and increment j. So 
	basically j will always point to the index where there is a duplicate number and we can 
	overwrite it when i point to a new number. In the end we return j which will be the number
	of unique elements in the array.   
'''

n = int(input())
arr = list(map(int, input().split()))
if n==0 or n==1:
    print(n)
else:
    j = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1    
    print(j)       