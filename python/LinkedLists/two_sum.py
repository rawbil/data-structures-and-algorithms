# 'https://leetcode.com/problems/add-two-numbers/description/'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head1 = Node(2)
        head1.next = Node(4)
        head1.next.next = Node(3)

        head2 = Node(5)
        head2.next = Node(6)
        head2.next.next = Node(4)

        while head1 is not None:
            l1.append(head1.data)
            head1 = head1.next

        while head2 is not None:
            l2.append(head2.data)
            head2 = head2.next

        joinl1 = ""
        for i in range(len(l1)):
            joinl1 += str(l1[i])

        joinl2 = ""
        for i in range(len(l2)):
            joinl2 += str(l2[i])

        index1 = len(l1) - 1
        reversedl1 = ""

        while index1 >= 0:
            reversedl1 += joinl1[index1]
            index1 -= 1

        index2 = len(l2) - 1
        reversedl2 = ""

        while index2 >= 0:
            reversedl2 += joinl2[index2]
            index2 -= 1

        sum = str(int(reversedl1) + int(reversedl2))

        reversed_sum = ""
        sum_index = len((sum)) - 1
        while sum_index >= 0:
            reversed_sum += sum[sum_index]
            sum_index -= 1

        current_head = Node(int(reversed_sum[0]))
        # current_head.next = Node(reversed_sum[1])
        # current_head.next.next = Node(reversed_sum[2])
        # current_head.next.next.next(Node(reversed_sum[3]))

        head = current_head
        for i in range(1, len(reversed_sum)):
            current_head.next = Node(int(reversed_sum[i]))
            current_head = current_head.next
            # print(current_head.data)

        final_list = []

        while head is not None:
            final_list.append(head.data)
            head = head.next

        print(final_list)


sol = Solution()
sol.addTwoNumbers([], [])
