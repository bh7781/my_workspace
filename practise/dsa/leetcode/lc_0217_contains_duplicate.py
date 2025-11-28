# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: All elements are distinct.
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List
from practise.utils.performance_analyzer import PerformanceAnalyzer

class Solution:
    @PerformanceAnalyzer.measure
    def contains_duplicate_bruteforce(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    @PerformanceAnalyzer.measure
    def contains_duplicate_optimized(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.contains_duplicate_bruteforce([1,1,1,3,3,4,3,2,4,2]))
    print('-------')
    print(solution.contains_duplicate_optimized([1,1,1,3,3,4,3,2,4,2]))