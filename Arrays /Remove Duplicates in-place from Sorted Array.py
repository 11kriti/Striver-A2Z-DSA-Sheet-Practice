#Remove Duplicates in-place from Sorted Array
#Input: arr[1,1,2,2,2,3,3] ,Output: arr[1,2,3,_,_,_,_]

def removeDuplicates (arr: list[int]) ->int:
    st = set()
    n = len(arr)
    for i in range(n):
        st.add(arr[i])
    store = len(st)
    j = 0 
    for x in st:
        arr[j] = x
        j+=1
    return store
    
arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")
    
