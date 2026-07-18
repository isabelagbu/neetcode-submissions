# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize two pointers to start. fast slow
        # while fast hasnt reached end
            # move slow by 1
            # move fast by 2
        # since end reached, return slow pointer as middle

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        return slow
        