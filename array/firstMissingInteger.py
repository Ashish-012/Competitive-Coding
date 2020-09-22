'''
    Easy solution would be to remove negative elements from the list and then sort the list to check
    if the first positive number is present in the list. If it is present just check the first succeeding
    element that is missing from the list. But it has time complexity of 0(nlogn).
    
    Remove all the negative numbers from the list and update the list. If all are negative numbers return 1.
    Then traverse the list store that value in a variable `index`. Then go to `index -1` location in the
    array (if it exists) and update the value found at that index by negative of the value. If it is out 
    of bounds then do nothing.([3,2,1,6] here the list will change to [-3,-2,-1,6,7]). Now traverse the list,
    the first positive index + 1 will be the smallest positive number that is not present in the array.([-3,-2,-1,6,7]
    in this case 3rd index so the smallest positive integer is 4 ). Return number of elements in list + 1 in case if 
    the list contains all the numbers in sequence.
    This solution has the time complexity of O(n)
'''

def firstMissingPositive(self, A):
    a = list(A)
    j = 0
    for i in range(len(a)):
        if a[i]<0 :
            a[i],a[j] = a[j],a[i]
            j += 1
    if j ==len(a): return 1
    a = a[j:]
    n = len(a)
    for i in range(n):
        index = abs(a[i])
        if index-1 < n:
            a[index-1] *= -1
    for i in range(n):
        if a[i]>0:
            return i+1
    return n+1