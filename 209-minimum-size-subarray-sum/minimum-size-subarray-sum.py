class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        start = 0
        end = 0
        curr = 0
        min_len = sys.maxsize
        while end<len(arr):
            curr += arr[end]
            end += 1
            while(curr >= target):
                min_len = min(min_len, end-start)
                curr -= arr[start]
                start += 1
        if min_len == sys.maxsize:
            return 0
        else:
            return min_len
