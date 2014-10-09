def bubble_sort(lst):
    """
    4 5 3 1 2 --> 4 3 5 1 2 --> 4 3 1 5 2 --> 4 3 1 2 5
    """
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def insert_sort(lst):
    """
    4 5 3 1 2 --> 3 4 5 1 2 --> 1 3 4 5 2 --> 1 2 3 4 5
    """
    for i in range(1, len(lst)):
        item = lst[i]
        j = i
        while j > 0 and item < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = item

def select_sort(lst):
    """
    4 5 3 1 2 --> 1 5 3 4 2 --> 1 2 3 4 5
    """
    for i, item in enumerate(lst):
        min_item = min(lst[i:])
        min_ind = lst.index(min_item)
        lst[min_ind] = lst[i]
        lst[i] = min_item

def merge(lst1, lst2):
    """
    firt sort them
    [1, 2, 3, 4] [2, 3, 5] --> [1, 2, 3, 4, 5]
    """
    lst1.sort()
    lst2.sort()
    ind1, ind2, res = 0, 0, []
    while ind1 < len(lst1) and ind2 < len(lst2):
        item1, item2 = lst1[ind1], lst2[ind2]
        if item1 == item2:
            res.append(item1)
            ind1 += 1
            ind2 += 1
        elif item1 < item2:
            res.append(item1)
            ind1 += 1
        else:
            res.append(item2)
            ind2 += 2

    if ind1 == ind2:
        return res
   
    if ind1 == len(lst1):
        res += lst2[ind2:]
    else:
        res += lst1[ind1:]
    return res



"""
Find intersection/union of two sets
debouce
interval - happens multiple times
timeout - only once
"""

