def find_min_max(arr):
    min_val=max_val=arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val=num
        elif num > max_val:
            max_val=num
    return min_val,max_val
              
numbers=[3,2,1,56,10000,167]
min_element, max_element = find_min_max(numbers)
print("Minimum Element",min_element)
print("Maximum Element", max_element)
