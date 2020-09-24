'''
	Sort the array then use two for loops and 3 pointers i pointing to the first element, j 
	pointing to the next element and k pointing to the last. Now check if i+j+k is equal to the
	number if it us return the elements, if it is less than the number so we need to increase the
	difference so increment j. If it is greater than number then decrement k. 
'''


n = int(input())
arr = list(map(int, input().split()))
num = int(input())
arr.sort()

def triplets(a):
    for i in range(len(a)-1):
        j = i+1
        k = len(a)-1
        while j<k:
            if a[i]+a[j]+a[k] == num:
                return [a[i],a[j],a[k]]
            elif a[i]+a[j]+a[k] < num:
                j+=1
            elif a[i]+a[j]+a[k] > num:
                k-=1
    return -1
print(" ".join(map(str, triplets(arr))))
        
