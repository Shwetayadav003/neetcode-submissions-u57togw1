class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        for i in range(len(s)):
            new_str = s[:i] + s[i +1:]
            if  new_str == new_str[::-1]:
                return True
        return s == s[::-1]