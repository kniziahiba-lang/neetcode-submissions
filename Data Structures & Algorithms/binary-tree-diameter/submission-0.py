# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Variable globale pour tracker le max diamètre
        
        def dfs(node):
            # CAS DE BASE: nœud vide
            if node is None:
                return 0
            
            # Calculer la hauteur du sous-arbre gauche et droit
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Calculer le diamètre qui passe par ce nœud
            # (longueur du chemin le plus long à travers ce nœud)
            diameter_through_node = left_height + right_height
            
            # Mettre à jour le diamètre global si c'est plus grand
            self.diameter = max(self.diameter, diameter_through_node)
            
            # Retourner la hauteur de ce nœud pour les parents
            # +1 pour compter le nœud courant
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter