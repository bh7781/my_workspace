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

from typing import List
from collections import defaultdict
from collections import Counter
from practise.utils.performance_analyzer import PerformanceAnalyzer

class Solution:
    @PerformanceAnalyzer.measure
    def group_anagrams_bf1(self, strs: List[str]) -> List[List[str]]:
        output = []

        for index in range(len(strs)):
            anagrams = [strs[index]]
            for next_idx in range(index + 1, len(strs[index])):
                if Counter(strs[index]) == Counter(strs[next_idx]):
                    anagrams.append(strs[next_idx])
            output.append(anagrams)
        return output

    @PerformanceAnalyzer.measure
    def group_anagrams_opt(self, strs: List[str]) -> List[List[str]]:
        # key: 26-length tuple of character counts
        # value: list of strings that share this "signature"
        groups = defaultdict(list)

        for s in strs:
            # Count frequency of each character
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            # Use the tuple of counts as a dictionary key
            key = tuple(count)
            groups[key].append(s)

        # Return the grouped anagrams
        return list(groups.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.group_anagrams_bf1(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.group_anagrams_opt(["eat", "tea", "tan", "ate", "nat", "bat"]))
