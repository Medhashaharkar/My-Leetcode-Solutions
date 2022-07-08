class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp = []
        dp.append([nums[0]])
        
        for i in range(1, len(nums)):
            for j in range(i+1):
                if (nums[i]>dp[j][-1][-1]):
        '''            
                    
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        print(dp)
        return max(dp)