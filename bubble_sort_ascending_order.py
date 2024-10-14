def bubble_sort_ascending(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = [100, 34, 25, 12, 22, 11, 90]
bubble_sort_ascending(numbers)

print(numbers)

