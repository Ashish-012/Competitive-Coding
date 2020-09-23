'''
    Even a normal searching technique would work in O(n), but we need O(logn) solution.
    Perform binary search in the array. Store middle index in a variable and check if
    the middle index we found is not first or last index of the list. If it is break.
    Otherwise check if number at that index is the greatest among its neighbours. If it is
    return the number.Else check if its neighbouring left is greater than then number. Perform
    binary search in left array otherwise in right array.
    Now if we still dont reach till such number that means it is located at the beginnning or
    end of the list. Check if it present at the beginning if yes then return it otherwise return
    the last number. 
'''

def solve(A):
    n = len(A)-1
    l = 0
    r = n
    while l <= r:
        mid = int(l+(r-l)/2)
        if mid> 0 and mid < n:
            if A[mid-1] < A[mid] >A[mid+1]:
                return A[mid]
            elif A[mid-1] > A[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            break
        
    if A[0] >A[1]:   # worse case, if the list is sorted in descending order
        return A[0]
    return A[n]