class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        window = {}
        need_count = len(need)
        have = 0
        left = 0
        right = 0
        res = ""
        res_len = float("inf")

        while right < len(s):
            
            ch = s[right]
            window[ch] = window.get(ch,0) + 1
            if ch in need and  window[ch] == need[ch]:
                have += 1
            
                
            while have == need_count:
                window_length = right - left + 1
                if window_length < res_len:
                    res = s[left:right + 1]
                    res_len = window_length
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
            right += 1
        return res



            
        
        