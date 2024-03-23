# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        new_list = None #the last element of every linked list is None
        current = head # used to traverse the original list while building the reveresed list

        while current:
            next_node = current.next # points to the next node on the list
            current.next = new_list # start linking nodes to the reversed list by pointing "current.next"
            new_list = current
            current = next_node

        return new_list
        