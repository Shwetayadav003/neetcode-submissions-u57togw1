class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ""
        min_len = min(len(word) for word in strs)
        for i in range(min_len):
            char = strs[0][i]
            if any(word[i] != char for word in strs):
                return strs[0][:i]
        return strs[0][:min_len]
        