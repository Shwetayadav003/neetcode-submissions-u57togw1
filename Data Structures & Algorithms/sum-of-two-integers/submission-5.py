class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            carry = ((a & b) << 1)  & mask
            a = (a ^ b )& mask
            b = carry
        if a > 0x7fffffff:
            return ~(a ^ mask)    
        return a
        