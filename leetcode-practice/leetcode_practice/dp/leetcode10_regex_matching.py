class Solution:
    def regex_matching(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
    
        # dp[i][j] = True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Pre-fill dp[0][j] for patterns like a*, a*b*, etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # zero occurrence of preceding char
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # use one more of preceding char

        return dp[m][n]
