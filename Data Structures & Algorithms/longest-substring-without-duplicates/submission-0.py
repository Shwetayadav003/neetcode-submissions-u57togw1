class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        left = 0
        right = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length