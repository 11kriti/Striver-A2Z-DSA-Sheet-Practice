#Last occurrence in a sorted array
#Input: N = 7,,target=13, array[] = {3,4,13,13,13,20,40} , Output: 4
# through linear search
def last_occur(arr , target):
    size = len(arr)
    res = -1
    for i in range(size-1 , -1 , -1):
        if arr[i] == target:
            res = i
            break
    return res
    
arr = [3,4,13,13,13,20,40]
size = len(arr)
occurence = last_occur(arr , 13)
print(occurence)
