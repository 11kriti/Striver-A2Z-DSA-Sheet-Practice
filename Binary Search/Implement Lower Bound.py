#find lower bond - linear search 
def lower_bound(arr , key):
  size = len(arr)
  for i in range(size):
    if arr[i] >= key:
      return i
  return size
  
arr = [11,24,25,78,89]
size = len(arr)
lower = lower_bound(arr, 26)
print(lower)
