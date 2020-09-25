'''
	Create a hashmap of all the elements and check if the frequency of any number os greater than
	n/2 (where n is the length of array)
'''

from collections import Counter

def majorityElement(self, A):
    arr = list(A)
    n = len(arr)-1
    d = Counter(arr)
    for key, value in d.items():
        if value > n//2:
            return key
        