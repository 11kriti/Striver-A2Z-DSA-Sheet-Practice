#Check if an Array is Sorted
#input : arr = 1,3,5,7,9 , size = 5 , output = true
def sorted_or_not(arr,size):
    for i in range (size):
        for j in range(i+1,size):
            if arr[i] > arr[j]:
                return False
    return True
    
arr = [1,3,5,7,9]
size = 5
print("True" if sorted_or_not(arr, size) else "False")
