def binary_search(lis,item):
    first = 0
    last = len(lis) - 1
    found = False
    while not found and first <= last:
        mid = (first+last)//2
        if lis[mid] == item:
            found = True
        else:
            if item < lis[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found

def binary_search_rec(lis,item):
    if len(lis) == 0:
        return False
    else:
        mid = len(lis)//2
        if lis[mid] == item:
            return True;
        else:
            if item < lis[mid]:
                return binary_search_rec(lis[:mid], item)
            else:
                return binary_search_rec(lis[mid+1:], item)

test_list = [0,1,2,8,13,17,19,32,42]
print(binary_search(test_list,3))
print(binary_search(test_list,32))
print(binary_search_rec(test_list,32))
