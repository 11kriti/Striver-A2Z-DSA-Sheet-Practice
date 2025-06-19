Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

def insert_position(arr , key):
  size = len(arr)
  start = 0 
  end = size -1 
  result = size
  
  while start <= end :
    mid = (start +end) // 2
    if arr[mid] >= key:
      result = mid
   
      end = mid -1
    else:
      start = mid+1
  return result
  
  
arr = [11,24,25,78,89]
size = len(arr)
search = insert_position(arr, 26)
print(search)
