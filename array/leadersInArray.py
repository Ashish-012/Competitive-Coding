'''
Take a variable max and store the last element in it
(As the last element will always be a leader)
Traverse the list from the end and append if any element
greater than `max` appears and update the value of max to 
that element
'''
n = int(input())
arr = list(map(int, input().split()))
l = []
max_ = arr[-1]
l.append(max_)
for i in reversed(arr):
    if i > max_:
        l.append(i)
        max_ = i 
l = list(reversed(l))
for i in l:
    print(i,end=' ')