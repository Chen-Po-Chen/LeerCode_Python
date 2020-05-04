# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for start in range(len(s)):
            ans = 1
            temp = []
            temp.append(s[start])
            for index in range(start+1, len(s)):
                if s[index] not in temp:
                    temp.append(s[index])
                    ans += 1
                else:
                    break
            if ans > max_len:
                max_len = ans
        return max_len