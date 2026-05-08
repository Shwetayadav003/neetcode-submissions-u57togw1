class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            digits = [int(digit) for digit in str(n)]
            n = sum(digit **2 for digit in digits)
        return True
        