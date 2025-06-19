#find lower bond - linear search 
def lower_bound(arr , key):
  size = len(arr)
  for i in range(size):
    if arr[i] >= key:
      return i
  return size

#through binary search

def lower_bound_BS(arr , key):
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
lower = lower_bound_BS(arr, 26)
print(lower)
