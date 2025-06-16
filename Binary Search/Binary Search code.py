
#binary search
def binary_search(arr, key):
    size = len(arr)
    start = 0
    end = size - 1
    
    
    while start <= end:
        mid = (start+end) // 2
        if arr[mid ]== key:
            return mid
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid -1 
    return -1
    
   

a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
size = len(a)
ind = binary_search(a, target)
if ind == -1:
    print("The target is not present.")
else:
    print("The target is at index:", ind)
