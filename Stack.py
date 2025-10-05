SIZE = 5
stack = []
top = -1

def push(val):
    global top
    if top == SIZE - 1:
        print("Stack Overflow")
    else:
        top += 1
        if len(stack) > top:
            stack[top] = val
        else:
            stack.append(val)

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print(f"Popped: {stack[top]}")
        top -= 1

def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:", end=" ")
        for i in range(top, -1, -1):
            print(stack[i], end=" ")
        print()

push(10)
push(20)
push(30)
display()
pop()
display()


# Explaination of Program 

# Define a maximum size SIZE = 5 and create an empty list stack.

# Initialize top = -1 to indicate that the stack is empty.

# Define push(val) to add an element to the stack:

# If top equals SIZE - 1, print “Stack Overflow”.

# Otherwise, increment top and insert the new element at stack[top].

# Define pop() to remove the top element from the stack:

# If top == -1, print “Stack Underflow”.

# Otherwise, print the element at stack[top] and decrement top.

# Define display() to print the stack elements from top to bottom:

# If top == -1, print “Stack is empty”.

# Otherwise, loop from top to 0 and print each element.

# Push 10, 20, and 30 onto the stack.

# Display the stack.

# Pop the top element and display the stack again.

# Output:- Stack elements: 30 20 10
#          Popped: 30
#          Stack elements: 20 10
