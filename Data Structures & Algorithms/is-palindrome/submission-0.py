class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(ch.lower() for ch in s if ch.isalnum())

        return palindrome == palindrome[::-1]