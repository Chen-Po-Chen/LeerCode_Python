# Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        if x<(-2**31) or x>((2**31)-1):
            return 0
        else:
            str_x = str(x)
            if str_x[0] == '-':
                reverse_x = str_x[::-1]
                if 0 - int(reverse_x[:-1])<(-2**31):
                    return 0
                else:
                    return 0 - int(reverse_x[:-1])
            else:
                if int(str_x[::-1])>((2**31)-1):
                    return 0
                else:
                    return int(str_x[::-1])