def bubble_sort(arr):
  for i in xrange(len(arr)):
    for j in xrange(i+1, len(arr)):
      if arr[j] < arr[i]:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp 
  print arr

arr = [5,3,2,1,6,7]
bubble_sort(arr)
