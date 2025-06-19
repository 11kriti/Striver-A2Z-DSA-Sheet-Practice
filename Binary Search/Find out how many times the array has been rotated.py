#Find out how many times the array has been rotated
#Input Format: arr = [4,5,6,7,0,1,2,3] , outut = 4

def times_arr_rotate(arr):
    size = len(arr)
    ans = float('inf')
    index = - 1
    for i in range(size):
        if arr[i] < ans :
            ans = arr[i]
            index = i
    return index
    
arr = [4,5,6,7,0,1,2,3]
result = times_arr_rotate(arr)
print(result)
        
