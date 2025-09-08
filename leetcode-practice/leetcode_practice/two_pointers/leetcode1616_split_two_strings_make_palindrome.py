class Solution:
    def split_two_strings_make_palindrome(self, a: str, b: str) -> bool:
        n = len(a)
    
        def is_palindrome(s1: str, s2: str, i: int, j: int, allow_mismatch) -> bool:
            while i < j:
                if s1[i] != s2[j]:
                    if allow_mismatch:
                        return is_palindrome(a, a, i, j, False) or is_palindrome(b, b, i, j, False)
                    else:
                        return False
                i += 1
                j -= 1
            return True
        
        return is_palindrome(a, b, 0, n - 1, True) or is_palindrome(b, a, 0, n - 1, True)

        


