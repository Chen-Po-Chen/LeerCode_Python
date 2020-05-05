# Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = len(s)
        while True:
            for i in range(len(s)-maxlen+1):
                sub_s = s[i:i+maxlen]
                sub_s_reverse = sub_s[::-1]
                if sub_s == sub_s_reverse:
                    return sub_s
            maxlen -= 1