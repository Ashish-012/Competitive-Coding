'''
    Create two dictionaries containing the frequency of each character in both arrays. Set a variable count to 0.
    Now the difference in frequencies of the the characters is the answer,to do this increment count by however
    many numbers are more in 1st dict than other do the same with other dictionary. The final count will be the 
    required answer.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    count = 0

    for key,value in d1.items():
        if d2[key] < value:
            count += value - d2[key] 

    for key,value in d2.items():
        if d1[key] < value:
            count += value - d1[key] 

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
