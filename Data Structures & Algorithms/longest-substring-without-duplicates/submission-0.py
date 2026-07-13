class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        left = 0 
        max_length = 0 
        for right in range(len(s)):
            right_char= s[right]
            counts[right_char] = counts.get(right_char, 0) + 1
            while counts[right_char] > 1 : 
                left_char = s[left]
                counts[left_char]-=1 
                left += 1 
            current_window_size = right - left + 1 
            max_length = max(max_length, current_window_size)
        return max_length

        