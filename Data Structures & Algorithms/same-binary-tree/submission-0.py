# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            # 1️⃣ CAS DE BASE: vérifie l'état des deux nœuds
            if node1 is None and node2 is None:
                return True  # ← Deux feuilles identiques
            
            if node1 is None or node2 is None:
                return False  # ← Structure différente
            
            # 2️⃣ Vérifier les valeurs
            if node1.val != node2.val:
                return False
            
            # 3️⃣ Vérifier récursivement les enfants
            left_same = dfs(node1.left, node2.left)
            right_same = dfs(node1.right, node2.right)
            
            # 4️⃣ Retourner le résultat combiné
            return left_same and right_same
        
        return dfs(p, q)
    
        