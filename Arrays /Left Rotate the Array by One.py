#Left Rotate the Array by One
#input : arr = [1, 2, 3, 4, 5] , Output : 2 3 4 5 1
def rotate_arr_by_one(arr, size):
    temp_arr = [0]*size
    for i in range(1,size):
        temp_arr[i-1] = arr[i]
    temp_arr[size-1] = arr[0]
    for i in range(size):
        print(temp_arr[i], end=" ")
    print()
arr = [1,2,3,4,5]
size = 5
(rotate_arr_by_one(arr,size))
