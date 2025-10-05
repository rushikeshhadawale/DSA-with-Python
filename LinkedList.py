class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def display(head):
    print("Linked List:", end=" ")
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")

head = None
head = insert(head, 10)
head = insert(head, 20)
head = insert(head, 30)

display(head)

# Explaination of Program

# Define a Node class with data to store the value and next to point to the next node.

# Define an insert function to add a new node at the beginning of the linked list:

# Create a new node with the given value.

# Point its next to the current head of the list.

# Update the head to the new node.

# Define a display function to print the linked list:

# Start from the head and traverse each node.

# Print the data of each node followed by an arrow ->.

# Stop when the end (NULL) is reached.

# Initialize head as None (empty list).

# Insert 10, 20, and 30 at the beginning of the list (last inserted becomes first).

# Call display to print the current linked list.

# Output :- Linked List: 30 -> 20 -> 10 -> NULL

