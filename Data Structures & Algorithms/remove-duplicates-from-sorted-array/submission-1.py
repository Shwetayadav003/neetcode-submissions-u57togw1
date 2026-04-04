class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(i +1, len(nums)):

                if nums[i] == nums[i +1]:
                    nums.pop(i + 1)
        k = len(nums)

        return k
        