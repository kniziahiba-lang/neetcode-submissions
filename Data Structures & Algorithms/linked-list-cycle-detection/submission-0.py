# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next          # +1
            fast = fast.next.next     # +2
            if slow is fast:          # même nœud → cycle
                return True
        return False                  # fast a atteint None → pas de cycle