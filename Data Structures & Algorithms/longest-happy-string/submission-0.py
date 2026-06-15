class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        def can_add(ch):
            return not(
            len(ans) >= 2 and 
            ans[-1] == ch and 
            ans[-2] == ch)

        while a > 0 or  b > 0 or  c > 0:
            candidates = [
                (a, "a"),
                (b, "b"),
                (c, "c")
            ]
            candidates.sort(reverse = True)
            added = False
            for count, ch in candidates:
                if count == 0:
                    continue
                if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                    continue
                ans.append(ch)
                if ch == "a":
                    a -= 1
                elif ch == "b":
                    b -= 1
                else:
                    c -= 1
                added = True
                break
            if not added:
                break
        return "".join(ans)
        