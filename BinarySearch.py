arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"Element found at index {mid}")
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")

# Explaination of Program 

# Create a sorted list arr with elements.

# Ask the user to enter the element to search and store it in key.

# Initialize low as the first index (0) and high as the last index of the list.

# Set a flag found to False to track whether the element is found.

# Repeat the following as long as low ≤ high:

# Find the middle index mid of the current search range.

# If the middle element equals key, print its index, set found to True, and stop the search.

# If key is greater than the middle element, search in the right half by setting low = mid + 1.

# If key is smaller than the middle element, search in the left half by setting high = mid - 1.

# After the loop, if found is still False, print “Element not found.”

# Output :- Enter element to search: 30
#           Element found at index 2
