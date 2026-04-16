class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boat = 0
        left = 0
        right = n - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boat += 1
            else:
                right -= 1
                boat += 1
        return boat
        