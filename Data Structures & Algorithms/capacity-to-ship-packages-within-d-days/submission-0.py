class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            needed_days = 1
            current = 0
            for w in weights:
                if current + w > mid:
                    needed_days += 1
                    current = w
                else:
                    current += w
            if needed_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
        