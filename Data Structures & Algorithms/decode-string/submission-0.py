class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_num = 0
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_string, curr_num))
                curr_string = ""
                curr_num = 0
            elif  ch == ']':
                prev_string, num = stack.pop()
                curr_string = prev_string + curr_string * num
            else:
                curr_string += ch
        return curr_string

        