class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2" : "abc", "3" : "def", "4" : "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9": "wxyz"}
        result = []
        def backtrack(start, path):
            if len(path) == len(digits):
                result.append(path)
                return
            letters = mapping[digits[start]]
            for ch in letters:
                backtrack(start + 1, path + ch)
        backtrack(0,"")
        return result

        
        