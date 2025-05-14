# CS50 Week 3: Algorithms
# using Python


options = [5,3,2,64,612,72,21,1,0]

# Bubble sort
def sort_arr(arr):
    array_len = len(arr)
    new_array=[]
    for i in range(array_len):
        for j in range(0,array_len-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return arr

print(f"Original values: {options}")
print(f"Sorted values: {sort_arr(options)}")

# Linear search
def linear_search(n,arr):
    for i, item in enumerate(arr):
        if item == n:
            return f"{n} is found at index {i}"
    return f"{n} is not in the list/array"

# Testing linear search
while True:
    try:
        search_item = int(input("Search here :  "))
        result = linear_search(search_item,options)
        print(result)
    except ValueError:
        print("Please enter a valid number only")

# Binary Search (later after work ...)
# 1. Sort the array
# 2. Get the total length of the array then divide it
# 3. Check which half will the item should be found
# 4. If the item is in the range of whether left or right side, repeat #2

