# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        anslist = []
        while list1:
            anslist.append(list1.val)
            list1 = list1.next
        while list2: 
            anslist.append(list2.val)
            list2 = list2.next
        
        if len(anslist) == 0:
            return list1
        
        anslist = sorted(anslist)
        tmp1 = ListNode()
        tmp1.val = anslist[len(anslist)-1]
        tmp1.next = None
        for i in reversed(range(len(anslist)-1)):
            tmp2 = ListNode()
            tmp2.val = anslist[i]
            tmp2.next = tmp1
            tmp1 = tmp2
        tmp1.val = anslist[0]
        return tmp1
        
            