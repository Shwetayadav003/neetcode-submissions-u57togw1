class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        prev = None
        max_count = 0
        ans = []
        pick = None
        for _ in range(len(s)):
            pick = None
            max_count = 0
            for char, count in freq.items():
                if count == 0:
                    continue
                if char == prev:
                    continue
                if count > max_count:
                    pick = char
                    max_count = count
            if pick is None:
                return ""
            ans.append(pick)
            freq[pick] -= 1
            prev = pick
        return "".join(ans)