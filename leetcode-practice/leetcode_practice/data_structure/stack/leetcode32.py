class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        stack = []
        leftover = []
        count = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                leftover.append(i)
            elif leftover:
                leftover.pop()
        
        j = 0
        for i in range(len(s)):
            if s[i] == '(':
                if j < len(leftover) and i == leftover[j]:
                    count = 0
                    j += 1
                else:
                    stack.append()
            elif stack:
                stack.pop()
                count += 2
                max_length = max(max_length, count)
            else:
                count = 0

        return max_length   



