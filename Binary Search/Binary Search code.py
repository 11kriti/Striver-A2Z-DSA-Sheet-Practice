#binary search 
def binary_search(arr , key):
    size = len(arr)
    start = 0 
    end = size - 1
    
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == key:
            return mid
        elif  key > arr[mid]:
            start = mid +1 
        else :
            end = mid-1
    return -1
    
arr = [1,2,4,5,6,7,8,9]
size = len(arr)
search = binary_search(arr , 6)
print(search)
