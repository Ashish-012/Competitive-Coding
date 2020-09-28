'''
	Just split the array by space and reverse it then join together to get the reversed string  
'''


num = int(input())
string = input().split(' ')[::-1]
print(" ".join(string))
