arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element found at index {i}")
        found = True
        break

if not found:
    print("Element not found")

# Explaination of Program

# Create a list arr with 5 elements.

# Ask the user to enter the element to search and store it in key.

# Initialize a boolean flag found as False to track whether the element is found.

# Loop through each element of the list:

# If the current element equals key:

# Print the index where it is found.

# Set found to True and exit the loop.

# After the loop, if found is still False, print “Element not found”.

# Output:- Enter element to search: 30
#          Element found at index 2
