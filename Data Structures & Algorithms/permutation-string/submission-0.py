class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frequency = Counter(s1)
        window_frequency = Counter(s2[:len(s1)])
        if window_frequency == frequency:
            return True
        for r in range(len(s1), len(s2)):
            add_char = s2 [r]
            remove_char = s2[r -  len(s1)]
            window_frequency[add_char] += 1
            window_frequency[remove_char] -= 1
            if window_frequency[remove_char] == 0:
                del window_frequency[remove_char]
            if window_frequency == frequency:
                return True
        return False
        
        