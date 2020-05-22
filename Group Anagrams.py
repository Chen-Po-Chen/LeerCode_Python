# Group Anagrams

# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = []
        ans = []
        num_pattern = 0
        for i in range(len(strs)):
            if sorted(strs[i]) not in pattern:
                num_pattern += 1
                pattern.append(sorted(strs[i]))
                ans.append([strs[i]])
            else:
                index = pattern.index(sorted(strs[i]))
                ans[index].append(strs[i])
        return ans