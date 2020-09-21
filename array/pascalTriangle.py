'''
	This solution has both space and time complexity O(n^2) as we are storing the entire triangle.
	Initialize list of n x n elements with 0's. Make two nested loops and traverse the outer(i) one
	till `n` and inner(j) one till the outer(i) . If index of j is 0 or i, that means we are at the
	beginning or ending point of a row so we have to store 1 at index i j and print 1. Otherwise we
	need to store the values at i j that are sum of values just above and left of above.  

'''

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            arr[i][j] = 1
            print(arr[i][j],end =' ')
        else:
            arr[i][j] = arr[i-1][j-1]+ arr[i-1][j]
            print(arr[i][j],end =' ')
    print()