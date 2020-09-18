'''
    Make another array `a` and initialise all its elements to zero. Each time A number appears in
    the actual array, increase the count of that index in our `a`. We now have a list of frequencies
    of all the elements in array `arr`. Just traverse the list and print the (element x its frequency).

'''


import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    n = len(arr)
    a = [0]*100
    l = []
    for i in range(n):
        index = arr[i]
        a[index] += 1
    
    for i in range(len(a)):
        if a[i]>=1:
            l += [i] * a[i]
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
