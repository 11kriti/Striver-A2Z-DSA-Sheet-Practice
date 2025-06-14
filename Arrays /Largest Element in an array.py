#largest element in an array 
''' Input - arr = 10,2,4,6,7
output = 10'''

#through sorting
def largest_elem(arr , size):
    max = arr[0]
    for i in range( 0 , size):
        if arr[i] > max:
            max = arr[i]
    return max
