class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        dp = []
        ss = []
        count = 0
        max_length = 0

        for i in range(len(str)):
            if str[i] == '(':
                ss.append(i)
            elif ss:
                ss.pop()
                    count += 2
                    max_length = max(max_length, count)
            else:
                # reset counter

