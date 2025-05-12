# A positive integer is considered uniform if all of its digits are equal. For example, 222 is uniform, while 223 is not.
# Given two positive integers A and B, determine the number of uniform integers between A and B, inclusive.
# Please take care to write a solution which runs within the time limit.

# Constraints:
# 1 ≤ A ≤ B ≤ 10^12

def get_uniform_integer_count_in_interval(A: int, B: int) -> int:
    def get_digits(integer: int):
        return len(str(integer))
    
    def get_uniformed_nums(digits: int):
        return [int(str(i) * digits) for i in range(1, 10)]

    count = 0
    for digits in range(get_digits(A), get_digits(B) + 1):
        for uniformed_num in get_uniformed_nums(digits=digits):
            if A <= uniformed_num <= B:
                count += 1
    
    return count
