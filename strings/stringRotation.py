'''
	Just concatinate the same string again to its end. Now check if the required string is in the main string.
	PS- not passing the sample case but passing all the main cases due to some error in input
'''

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    
    s2 = s2*2
    if s1 in s2:
        print('YES')
    else:
        print('NO')