#Count Occurrences in Sorted Array
#Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}  Output: 4
#linear search
def count_occur(arr , X):
    size = len(arr)
    count = 0
    for i in range(size):
        if arr[i] == X:
            count +=1
    return count

arr = [2,2,3,3,3,3,4]
occur = count_occur(arr , 3)
print(occur)
