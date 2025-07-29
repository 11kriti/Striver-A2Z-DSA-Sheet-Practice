#square root of an integer  - x = 10
#by linear search 
def sqrt(x):
    if x == 0 or x ==1 :
        return x
    i  = 1 
    while i * i <= x: #1*1 = 1 <= 10
        i +=1 # i = 2 till i * i < =x
    return i - 1 
    
#binary search 
def sqrt_bin(x):
    if x ==0 or x ==1 :
        return x
    left = 0
    right = x
    ans = -1 # to store result 
    
    while left <= right:
        mid = (left+right)//2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            left = mid +1
        else:
            right =  mid - 1
    return ans
    
x = int(input("Enter a number to find square root: "))

result = sqrt_i(x)
print(f"The floor square root of {x} is: {result}")
    
