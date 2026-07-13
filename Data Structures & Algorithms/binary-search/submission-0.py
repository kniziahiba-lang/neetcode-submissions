class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2   # recalculé à chaque tour

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1           # chercher à droite
            else:
                right = mid - 1          # chercher à gauche

        return -1