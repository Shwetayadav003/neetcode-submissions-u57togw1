class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0
        def backtrack(i , curr_xor):
            nonlocal answer
            if i == len(nums):
                answer += curr_xor
                return
            backtrack(i+1, curr_xor ^ nums[i])
            backtrack(i+1, curr_xor)
        backtrack(0,0)
        return answer
            
        