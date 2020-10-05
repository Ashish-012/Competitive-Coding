'''
	Just make a dictionary containing frequencies of all the values of both the strings. Now check if the 
	lengths of both the strings are different then they are not anagrams of each other. Othervise check if
	the frequency of all the elements are equal, if they are equal then the strings are anagrams.
'''


from collections import Counter

s1,s2 = input().split()

d1 = Counter(s1)
d2 = Counter(s2)
flag = 1

if len(s1) != len(s2):
    print('Not Anagram')
    flag = 0
    exit()

else:
    for key,value in d1.items():
        if d2[key] != value:
            print('Not Anagram')
            flag = 0
            break
if flag == 1:
    print('Anagram')