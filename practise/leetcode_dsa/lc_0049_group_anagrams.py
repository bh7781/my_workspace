# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
from collections import defaultdict
from typing import List
from collections import Counter
from practise.utils.performance_analyzer import PerformanceAnalyzer

class Solution:
    @PerformanceAnalyzer.measure
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for index in range(len(strs)):
            for next_idx in range(index + 1, len(strs[index])):
                if Counter(strs[index]) == Counter(strs[next_idx]):
                    anagrams.append([strs[index], strs[next_idx]])
        return anagrams

if __name__ == '__main__':
    solution = Solution()
    print(solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]))