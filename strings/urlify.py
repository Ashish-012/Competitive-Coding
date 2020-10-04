'''
	We need to change all the spaces to %20 so in python we can just split the string and join with %20
'''

t = int(input())
for _ in range(t):
    string = input().split()
    num = int(input())
    print("%20".join(string))