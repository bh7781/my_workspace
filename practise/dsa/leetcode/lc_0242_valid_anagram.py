# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
from practise.utils.performance_analyzer import PerformanceAnalyzer
from collections import Counter

class Solution:
    @PerformanceAnalyzer.measure
    def is_anagram_bruteforce(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        if len(slist) == len(tlist):
            for char in slist:
                if char in tlist:
                    tlist.remove(char)
            if len(tlist) == 0:
                return True
        return False

    @PerformanceAnalyzer.measure
    def is_anagram_optimized(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    # Hash Map Approach using Counter
    #
    # Algorithm:
    # - Count frequency of each character in both strings
    # - Compare frequency dictionaries
    #
    # Time Complexity: O(n) - single pass through each string
    # Space Complexity: O(1) - at most 26 characters for lowercase English
    # 				  O(k) - where k is character set size for Unicode
    #
    # Advantages:
    # - Optimal O(n) time complexity
    # - Works for Unicode (no changes needed)
    # - Early exit possible with length check
    # - Most efficient for large strings
    #
    # Why it's better than your solution:
    # - O(n) vs O(n²) - dramatically faster
    # - No list manipulation overhead
    # - Counter is optimized C implementation
    # - Handles all edge cases correctly

if __name__ == '__main__':
    solution = Solution()
    first = "msdhonifromchennai"
    second = "msdhonifromchennai"
    print(solution.is_anagram_bruteforce(first, second))
    print(solution.is_anagram_optimized(first, second))
