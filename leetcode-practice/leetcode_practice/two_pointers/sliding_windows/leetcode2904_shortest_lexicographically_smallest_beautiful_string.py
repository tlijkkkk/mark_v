class Solution:
    def shortest_lexicographically_smallest_beautiful_string(self, s: str, k: int) -> str:
        count = 0
        shortest = float('inf')
        smallest = ""
        i = 0
        
        for j in range(len(s)):
            count += 1 if s[j] == '1' else 0

            while count > k:    
                count -= 1 if s[i] == '1' else 0
                i += 1

            if count == k:
                while s[i] == '0':
                    i += 1

                if j - i + 1 == shortest:
                    tmp = s[i : j + 1]
                    smallest = min(smallest, tmp)

                if j - i + 1 < shortest:
                    smallest = s[i : j + 1]
                    shortest = j - i + 1

        return smallest
                