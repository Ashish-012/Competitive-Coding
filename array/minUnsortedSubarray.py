'''
    Take two variables pointing to first and last index of the list. Traverse the list and search for a number
    which is smaller than the previous numbers, and make `i` point to it. If no such number exists it means that 
    the list is already sorted so return `-1`. Then traverse the list from the end and look for the first number which
    is smaller than its predecessor ([1, 3, 2, 4, 5] here 2 is a number which is smaller than its predecessor 3) and j
    will point to that number.
    Then traverse the list from `i` to `j` and find the `max` and `min` number in the subarray. Then check if there
    exist a number greater than `min` in our sorted list from the beginning, if it does then update `i` with index 
    of that element. Then check if there exist a number smaller than `max` in our sorted end list, if it does update 
    `j` with its index. `i` and `j` are beginning and ending index of our required unsorted list.  
'''
def subUnsort(A):
    ans = []
    i = 0
    while i<len(A)-1:
        if A[i] > A[i+1]:
            break
        i += 1
    if i == len(A)-1:
        return [-1]

    j = len(A)-1
    while j>0:
        if A[j] < A[j-1]:
            break
        j -= 1
        
    max_ = A[i]
    min_ = A[j]

    for x in range(i+1,j+1):
        if A[x] < min_:
            min_ = A[x]
        if A[x] > max_:
            max_ = A[x]
        
    for x in range(0,i):
        if A[x] > min_:
            i = x
            break
    for x in range(len(A)-1,j,-1):
        if A[x] < max_:
            j = x
            break
    ans.append(i)
    ans.append(j)
    return ans