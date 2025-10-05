SIZE = 5
queue = []
front = -1
rear = -1

def enqueue(val):
    global front, rear
    if len(queue) == SIZE:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        queue.append(val)
        rear += 1

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print(f"Dequeued: {queue[front]}")
        front += 1

def display():
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print("Queue elements:", queue[front:rear+1])

enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()

# Explaination of Program
# Define a maximum size SIZE = 5 and create an empty list queue.

# Initialize front and rear pointers as -1 to indicate an empty queue.

# Define enqueue(val) to insert an element into the queue:

# If the queue size equals SIZE, print “Queue Overflow”.

# Otherwise, if the queue is empty (front == -1), set front = 0.

# Append the new element to the queue and increment rear.

# Define dequeue() to remove an element from the queue:

# If the queue is empty (front == -1 or front > rear), print “Queue Underflow”.

# Otherwise, print the element at front and increment front.

# Define display() to show current queue elements:

# If the queue is empty, print “Queue is empty”.

# Otherwise, print elements from front to rear.

# Enqueue 10, 20, and 30 into the queue.

# Display the queue.

# Dequeue one element and display the queue again.

# Output :- Queue elements: [10, 20, 30]
#           Dequeued: 10
#           Queue elements: [20, 30]
