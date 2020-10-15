'''
    Here we used regex findall method to find all the occurances of the sub word. It returns a list so then we counted the
    number of elements in the list and that is the required answer 
'''
import re

num_ = int(input())
sentences = []
for i in range(num_):
    x = input()
    sentences.append(x)

queries = int(input())

def isSubword(q):
    count = 0
    for i in sentences:
        x=re.findall(f"[a-zA-Z0-9_]{q}[a-zA-Z0-9_]",i)
        count += len(x)
    return count

c = 0
for i in range(queries):
    que_ = input()
    c = isSubword(que_)
    print(c) 