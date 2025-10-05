arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted array:", arr)

#Explaination of Program 

# Create a list arr with unsorted elements.

# Loop i from 1 to the last index of the list:

# Store the element at index i in key.

# Initialize j as i - 1 to compare elements in the sorted portion of the list.

# While j is greater than or equal to 0 and arr[j] is greater than key:

# Shift arr[j] one position to the right.

# Decrement j to continue comparing with previous elements.

# Place key at the correct position in the sorted portion.

# Repeat until all elements are inserted in the correct position.

# Print the sorted list.

# Output :- Sorted array: [5, 6, 11, 12, 13]
