class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverselist(head):
    while head is not None:
        print(head.data, end=" ")
        if head.next is not None:
            print("-> ", end="")
        head = head.next


head = Node(5)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(40)
#
# while head is not None:
#     print(head.data, end=" ")
#
#     if head.next is not None:
#         print("-> ", end="")
#     head = head.next

traverselist(head)
