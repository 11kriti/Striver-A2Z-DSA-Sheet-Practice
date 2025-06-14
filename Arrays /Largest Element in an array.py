#largest element in an array 
''' Input - arr = 10,2,4,6,7
output = 10'''

#through comparing and marking MAX as 0th index at first
def largest_elem(arr , size):
    max = arr[0]
    for i in range( 0 , size):
        if arr[i] > max:
            max = arr[i]
    return max

#through sorting
def largest(arr,size):
    large = arr.sort()
    return large

