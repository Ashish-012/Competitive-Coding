'''
    Take the transpose of the matrix. Then swap the first column with the last 
    column, then 2nd column with the 2nd last, and so on.
'''

n = int(input())
arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
for i in range(n):
    for j in range(i,n):
        arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

for i in range (n):
    k = n - 1
    for j in range(n//2):
        arr[i][j], arr[i][k] = arr[i][k], arr[i][j]
        k = k - 1
    
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()