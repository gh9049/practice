# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        list3 = ListNode()
        l3=list3

        while list1 and list2:
            if list1.val < list2.val:
                l3.next=list1
                list1=list1.next
            elif list1.val > list2.val:
                l3.next=list2
                list2=list2.next
            l3=l3.next
        if list1:
            l3.next=list1
        else:
            l3.next=list2
        return list3.next


