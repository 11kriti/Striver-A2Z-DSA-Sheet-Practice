#Selection Sort 
'''Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.
Input: n = 5, arr[] = {64,25,12,22,11}
Output: 11,12,22,25,65 '''

#code- 
def sorting_tech(arr):
  n = len(arr)
  for i in range(n-1):
    min_index = i
    for j in range(i+1 , n):
      if arr[j] >< arr[min_index]:
        min_index = j
    arr[j] , arr[min_index] = arr[min_index] , arr[j]
