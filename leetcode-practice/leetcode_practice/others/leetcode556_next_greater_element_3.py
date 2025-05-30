class Solution:
    def next_greater_element_iii(self, n: int) -> int:
        n_str = list(str(n))  # convert to list so we can swap

        if not n_str:
            return -1

        change_idx = -1
        for i in range(len(n_str) - 2, -1, -1):
            if n_str[i] < n_str[i + 1]:  
                change_idx = i
                break  # only need the first one from right

        if change_idx == -1:
            return -1

        min_next = change_idx + 1
        for i in range(change_idx + 1, len(n_str)):
            if n_str[i] > n_str[change_idx] and n_str[i] <= n_str[min_next]:
                min_next = i

        # Swap
        n_str[change_idx], n_str[min_next] = n_str[min_next], n_str[change_idx]

        # Sort the suffix
        suffix = sorted(n_str[change_idx + 1:])
        result_digits = n_str[:change_idx + 1] + suffix
        result = int("".join(result_digits))

        return result if result <= 2**31 - 1 else -1

        

