# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True  # Variable globale
        
        def dfs(node):
            # CAS DE BASE
            if node is None:
                return 0
            
            # Calculer les hauteurs
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Vérifier si CE NŒUD est équilibré
            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            # Retourner la hauteur pour le parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.balanced
        