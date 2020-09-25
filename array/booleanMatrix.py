'''
	Make two temp arrays row and column of length row and col of original arary and initialize them to 0.
	Traverse the array and if there is any 1 in any row or column, update that row and column of temp arrays
	to 1. Then again traverse the 2d array and if temp array's row or column is 1. Make that index element 1.
	So basically we are first updating the values in temp array then using that temp array we are updating the
	values of our main array.
'''


t = int(input())							 # number of test cases
for i in range(t):   
    m,n = map(int, input().split())          # number of row and column
    arr = []
    for i in range(m):
        a = list(map(int, input().split()))   
        arr.append(a)						  # reading the array

    r = [0]*m
    c = [0]*n
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                r[i] == 1
                c[j] == 1
    for i in range(m):
        for j in range(n):
            if r[i] == 1 or c[j] == 1:
                arr[i][j] ==1
    print(t+1)
    for i in arr:
        x = " ".join(i)
        print(x)