# -*- coding: utf-8 -*-

from src.linkedlist.SingleLinkedList import SingleLinkedNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy_node = SingleLinkedNode()
        node = dummy_node

        while l1 is not None and l2 is not None:
            if l1.value < l2.value:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 is None:
            node.next = l2
        else:
            node.next = l1

        return dummy_node.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left_node = self.mergeKLists(lists[:mid])
        right_node = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left_node, right_node)