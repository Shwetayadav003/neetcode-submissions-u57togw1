class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = set()
        for i in range(n):
            for j in range(i+1, n):
                s1 = nums[i] + nums[j]
                s2 = target - s1
                left = j+1
                right = n - 1
                while left < right:
                    if nums[left] + nums [right] < s2:
                        left += 1
                    elif nums[left] + nums[right] > s2:
                        right -= 1
                    else:
                        answer.add((nums[i] , nums[j], nums[left] , nums[right]))
                        left += 1
                        right -= 1
        return [list(x) for x in answer]

        


        