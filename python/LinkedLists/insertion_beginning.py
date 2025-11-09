"""
- Create the first node and assign memory
- Create the second node, and link it to the first node
- To insert node at beginning, create the node
- Link the node to the second node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beginning(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


head = Node(10)
head.next = Node(30)
head.next.next = Node(50)

new_node = Node(100)
new_node.next = head
head = new_node

insert_at_beginning(head)
