class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dico = {}

        for c in s:
            dico[c] = dico.get(c, 0) + 1   # +1 pour chaque lettre de s

        for c in t:
            dico[c] = dico.get(c, 0) - 1   # -1 pour chaque lettre de t
            if dico[c] < 0:                 # trop de cette lettre dans t
                return False

        return True