class Solution:
    
    def fib(self, n: int) -> int:

        def fibo(n):
            if (n == 0):
                return 0
            if (n == 1):
                return 1
            if dp[n] != -1 :
                return dp[n]
            dp[n] = fibo(n-1) + fibo(n-2)
            
            print(dp)
            return dp[n]
        
        dp = [-1]*(n+1)
        return fibo(n)

            


        