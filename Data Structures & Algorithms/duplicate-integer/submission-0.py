class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico = {}
        for elem in nums : 
            if elem in dico :
                return True 
            else : 
                dico[elem]=1
        return False
        