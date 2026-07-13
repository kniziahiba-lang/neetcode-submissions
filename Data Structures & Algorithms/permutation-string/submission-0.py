class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        #ça cetait mon premier code 
        dico={}
        left = 0 
        size = len(s1)
        for i in range(size): 
            dico[s1[i]] = 0 


        for i in range(len(s2)): #ici il faut faire len(s2)-size + 1 pske 
        # le k parcourt le size 
            char_left = s2[left]
            if s2[left] in s1 : 
                dico[char_left] += 1 
                for k in range(size): 
                    dico[s2[i+k]] += 1 
        
        for i in range(size): 
            if dico[s1[i]] != 1 : 
                return False 
        return True  """

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Si s1 est plus grand que s2, c'est impossible
        if len(s1) > len(s2):
            return False

        size = len(s1)

        # Correction 1 : On fait une boucle sur s2 pour tester chaque point de départ
        # On s'arrête à (len(s2) - size + 1) pour que la sous-chaîne ne dépasse jamais de s2
        for i in range(len(s2) - size + 1):
            left = i  # Ta variable left prend la position de départ actuelle
            
            # Correction 2 : On DOIT réinitialiser le dictionnaire à CHAQUE tentative
            dico = {}
            for j in range(size): 
                dico[s1[j]] = 0 

            # Ta boucle k qui remplit le dictionnaire avec la sous-chaîne actuelle de s2
            for k in range(size): 
                char_current = s2[left + k] # left + k remplace i + k pour ne pas déborder
                if char_current in dico:     # On vérifie si la lettre est attendue dans s1
                    dico[char_current] += 1 
        
            # Correction 3 : On vérifie si TOUTES les lettres de s1 ont trouvé preneur
            # Au lieu de chercher si dico == 1, on compte combien de fois chaque lettre de s1 
            # apparaît réellement dans s1, et on compare.
            match = True
            for m in range(size): 
                # s1.count(s1[m]) donne le nombre exact de fois que la lettre doit être là
                # c'est ça ce qui nous permet de résoudre le problème des doublons 
                if dico[s1[m]] != s1.count(s1[m]): 
                    match = False
                    break # Pas la peine de continuer à tester cette sous-chaîne
            
            # Si cette sous-chaîne est parfaite, on a gagné !
            if match:
                return True

        return False
