'''
    Sorting an array recursively
'''

def insert(arr, last):
    if len(arr) == 0 or arr[-1] <= last:
        arr.append(last)
        return
    end = arr[-1]
    arr.pop()
    insert(arr,last)
    arr.append(end)
    
def sort_arr(arr):
    if len(arr) == 1:
        return 
    last = arr[-1]
    arr.pop()
    sort_arr(arr)
    insert(arr,last)
    return arr

arr = [1,3,5,2,0,6,12,9]

sort_arr(arr)
print(arr)