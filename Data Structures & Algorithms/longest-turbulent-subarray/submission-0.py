class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        current_length = 1       
        max_length = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                current_length = 1
            elif(
                i == 1 or
                (arr[i-2] > arr[i-1] < arr[i]) or
                (arr[i-2] < arr[i-1] > arr[i])
            ):
                current_length += 1
            else:
                current_length = 2
            max_length = max(max_length, current_length)
        return max_length
        