"""
Creating an Example Linked List of Size 3 to Understand Working
1. Create the first node

2.
Allocate memory for the first node and Store data in it.
Mark this node as head.
Create the second node

3.
Allocate memory for the second node and Store data in it.
Link the first node’s next to this new node.
Create the third node

4.
Allocate memory for the third node and Store data in it.
Link the second node’s next to this node.
Set its next to NULL to ensure that the next of the last is NULL.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # initially there is no data, so there is no next node


# Create the 1st node
head = Node(5)

# 2nd node
head.next = Node(20)

# 3rd node
head.next.next = Node(40)

# 4th node
head.next.next.next = Node(50)

while head is not None:
    print(head.data, end=" ")
    head = head.next
