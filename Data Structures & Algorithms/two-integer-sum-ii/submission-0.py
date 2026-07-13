class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #[1,5,8,9,11]
        #target = 10 
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i]+ numbers[j] >  target :
                j-= 1
            elif numbers[i]+ numbers[j] <  target :
                i+= 1
            else : 
                return [i+1,j+1]
        