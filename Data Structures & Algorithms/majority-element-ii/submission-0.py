class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = []
        n = len(nums)
        freq = Counter(nums)
        for num in freq:
            if freq[num] > n/3:
                count.append(num)
        return count
