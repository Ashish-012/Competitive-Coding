'''
    Reverse the first `d` digits of the array. Then reverse the remaining didits(from d till end).
    After that reverse the entire array, it will be the required array after rotation.
'''

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def reverse(arr):
    return arr[::-1]

def rotLeft(a, d):
    start = a[:d]
    start = reverse(start)
    end = a[d:]
    end = reverse(end)
    arr = start+end
    arr = reverse(arr)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
