#Implement Upper Bound
#Input Format: N = 4, arr[] = {1,2,2,3}, x = 2 , output = 3

def upper_bound(arr , x):
    size = len(arr)
    for i in range(size):
        if arr[i] > x:
            return i
    return size
    
arr = [1,2,2,3]
upper = upper_bound(arr , 2)
print(upper)




