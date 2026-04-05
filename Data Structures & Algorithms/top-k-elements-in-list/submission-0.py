class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []
        freq = Counter(nums)
        arr = list(freq.items())
        arr.sort(key = lambda x:x[1], reverse = True)
        for i in range(k):
        
            count.append(arr[i][0])
        return count
        
        