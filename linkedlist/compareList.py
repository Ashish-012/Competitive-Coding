'''
    Make two pointers pointing to head of each of the list. Traverse the list till either of the pointer is None. If the data present at
    the first point is not equal to the second return 0. If the loop breaks check if both the list are poining to None, it they are then 
    the list are same otherwise they are not.
'''

def compare_lists(llist1, llist2):
    current1 = llist1
    current2 = llist2
    while current1 and current2:
        if current1.data != current2.data:
            return 0
        current1 = current1.next
        current2 = current2.next
    if not current1 and not current2:
        return 1
    return 0