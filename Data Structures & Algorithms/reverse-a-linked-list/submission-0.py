# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
    
        while current:
            nxt = current.next      # 1. Sauvegarder le suivant
            current.next = prev     # 2. Retourner la flèche
            prev = current          # 3. Avancer prev
            current = nxt           # 4. Avancer current
        return prev 
    
        
        





    

    
    
        