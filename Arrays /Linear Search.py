#Linear Search 
#Input: arr = 2,4,1,5,7 , key = 1 , output = index of the number = 2

def linear_search(arr , size , key):
    
    size = len(arr)
    for i in range(size):
        if key == arr[i]:
            return i
    return -1
    
arr = [2,4,1,5,7]
key = 8
size = len(arr)
print("Linear Search -" , linear_search(arr,size, key))

