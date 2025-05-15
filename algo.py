# CS50 Week 3: Algorithms
# using Python
options = [5,3,2,64,612,72,21,1,0]

# SORTING ALGORITHMS

# Bubble sort
def bubble_sort(arr):
    array_len = len(arr)
    for i in range(array_len):
        for j in range(0,array_len-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return arr


# Selection sort
def selection_sort(arr):
    n = len(arr)
    for x in range(0, n-1):
        current_min_index = x
        for y in range(x + 1, n):
            if arr[y] < arr[current_min_index]:
                current_min_index = y

                # swapping values
                temp = arr[current_min_index]
                arr[current_min_index] = arr[x]
                arr[x] = temp
    return arr


print(f"Original values: {options}")
# Testing sort algorithms
print(f"Sorted values (selection sort): {selection_sort(options)}")
print(f"Sorted values (bubble sort): {bubble_sort(options)}")

# ---------------------------------------------------------------------------------
# SEARCH ALGORITHMS

# Linear search
def linear_search(n,arr):
    for i, item in enumerate(arr):
        if item == n:
            return f"{n} is found at index {i}"
    return f"{n} is not in the list/array"

# Binary Search
def binary_search(n,arr):
    start = 0
    end = len(arr)-1
    mid = 0

    for x in range(len(arr)):
        mid = (start+end)//2

        if arr[mid] == n:
            return f"{n} is found at index {mid}"
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid-1
    return f"{n} is not found"


# Testing search algorithms
while True:
    try:
        search_item = int(input("Search here :  "))

        linear_result = linear_search(search_item,options)
        binary_result = binary_search(search_item,options)

        print(f"Linear Search Result: {linear_result}")
        print(f"Binary Search Result: {binary_result}")
    except ValueError:
        print("Please enter a valid number only")


