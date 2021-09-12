
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list = sorted(l1 + l2)

        sorted_merged_list = []

        for index, number in enumerate(sorted_list):
            # breakpoint()
            try:
                node = ListNode(number, sorted_list[index+1])
            except IndexError:
                node = ListNode(number)

            sorted_merged_list.append(node)

        return sorted_merged_list
