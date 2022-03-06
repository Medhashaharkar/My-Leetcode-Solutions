class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [0] * n
        result = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                mem[i] = mem[i-1] + 1
            result += mem[i]
        return result
                        
        