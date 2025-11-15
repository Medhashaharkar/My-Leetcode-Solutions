class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs_memo(i, j, t1, t2, dp):
            if (i == len(t1) or j == len(t2)):
                return 0 
            if (dp[i][j] != -1):
                return dp[i][j]
            if (t1[i] == t2[j]):
                dp[i][j] = lcs_memo(i+1, j+1, t1, t2, dp)+1
                return dp[i][j]
            else:
                ans1 = lcs_memo(i, j+1, t1, t2, dp)
                ans2 = lcs_memo(i+1, j, t1, t2, dp)
                dp[i][j] = max(ans1, ans2)
                return dp[i][j]
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return lcs_memo(0, 0, text1, text2, dp)
        