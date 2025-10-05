arr = [64, 34, 25, 12, 22, 11, 5]

n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)


# Explaination of Program

# Create a list arr with unsorted elements.

# Find the number of elements in the list using len(arr) and store it in n.

# Loop i from 0 to n-2 to perform multiple passes over the list.

# In each pass, loop j from 0 to n-i-2:

# Compare the element at index j with the next element j+1.

# If the current element is greater, swap them.

# After all passes, the list becomes sorted in ascending order.

# Print the sorted list.

# Output :- Sorted array: [5, 11, 12, 22, 25, 34, 64]
