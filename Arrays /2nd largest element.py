#2nd kargest
def second_largest(arr ,size):
    arr.sort()
    return arr[size-2]
    
arr = [1,2,3,5,6]
largest = second_largest(arr,5)
#sorteds = is_sorted_or_not(arr,5)
#large = largest_elem(arr,5)
print(largest)

