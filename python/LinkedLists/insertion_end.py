class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printlist(head):
    while head is not None:
        print(head.data, end=" ")
        if head.next is not None:
            print("-> ", end="")
        head = head.next


def insert_end(head, new_node):
    while head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head


# Create initial list
head = Node(20)
head.next = Node(100)
head.next.next = Node(300)

# Create and insert new node
new_node = Node(500)
head = insert_end(head, new_node)

printlist(head)
