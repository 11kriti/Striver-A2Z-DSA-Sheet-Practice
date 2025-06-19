#Move all Zeros to the end of the array
#Input: 1,0 ,2 ,3 ,0 ,4 ,0 ,1 , Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

def zeros_to_end(arr):
    size = len(arr)
    temp_arr = []
    for i in range(size):
        if arr[i] != 0:
            temp_arr.append(arr[i])
    non_zero = len(temp_arr)
    for i in range(non_zero):
        arr[i] = temp_arr[i]
    for i in range(non_zero , size):
        arr[i] = 0
    return arr
    
arr = [0,0,0,0,0,0,0,1]
ans = zeros_to_end(arr)
print(arr)



