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


# MERGE SORT
unsorted_array = [51,23,7,14,1,6,3,0]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2

        # separate halves to each array
        left_half = merge_sort(arr[:middle])
        right_half = merge_sort(arr[middle:])

        temp = []
        i = j = 0

        # check if each part has only one element
        while i < len(left_half) and j < len(right_half):

            # compare the values of each part then append to a new list
            if left_half[i] < right_half[j]:
                temp.append(left_half[i])
                i += 1
            else:
                temp.append(right_half[j])
                j += 1

        # uses extend function instead of append
        # if append is used, it will return a nested list
        temp.extend(left_half[i:])
        temp.extend(right_half[j:])

        return temp


print(f"This is the unsorted array: {unsorted_array}")
print(f"Merge sort result: {merge_sort(unsorted_array)}")
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


    # ------- RECURSION --------
    # Without using recursion

    def pyramid(height):
        # Outer Loop: number of layers
        for i in range(height):
            spaces = " " * (height - i - 1)
            stars = "*" * (i*2 + 1)
            print(spaces + stars + spaces)

        print("\n")
    print("Pyramid without recursive call")
    pyramid(5)

    # with recursion
    def recursive_pyramid(height, counter=0):
        if height <=0:
            print("Height must be a positive value")
            return

        if counter == height:
             return # means it will stop the recursion
        spaces = " " * (height - counter - 1)
        stars = "*" * (counter * 2 + 1)

        print(spaces + stars + spaces)

        # calling the function itself
        recursive_pyramid(height, counter+1)


    print("Recursive pyramid\n")
    recursive_pyramid(3)

