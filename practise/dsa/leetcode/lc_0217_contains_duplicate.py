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

    # Algorithm:
    # - Convert entire list to set (removes duplicates)
    # - Compare lengths: if different, duplicates existed

    # Time Complexity: O(n) - must process entire array
    # Space Complexity: O(n) - creates set with all unique elements

    # Drawbacks:
    # - NO EARLY EXIT: Always processes entire array even if duplicate is found at index 0 and 1
    # - Creates complete set in memory regardless of when duplicate occurs
    # - For large arrays with early duplicates, wastes computation
    # Use case: Best for small arrays or when you need the set anyway

    @PerformanceAnalyzer.measure
    def contains_duplicate_optimized(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Algorithm:
    # - Iterate through array once
    # - For each element, check if already seen
    # - If yes, return True immediately (early exit)
    # - If no, add to seen set and continue

    # Time Complexity: O(n) worst case, O(1) best case
    # Space Complexity: O(n) worst case, O(1) best case

    # Advantages:
    # - EARLY EXIT: Returns immediately when duplicate found
    # - Memory efficient: Only stores elements until duplicate found
    # - Best case O(1): [1, 1] returns after checking 2 elements
    # - Worst case O(n): [1, 2, 3, 4, 5] checks all elements

    # Why this is better:
    # 1. Performance: Can be significantly faster for arrays with early duplicates
    # 2. Memory: Uses less memory when duplicates found early
    # 3. Real-world: Most duplicate detection benefits from early termination

if __name__ == '__main__':
    solution = Solution()
    print(solution.contains_duplicate_bruteforce([1,1,1,3,3,4,3,2,4,2]))
    print('-------')
    print(solution.contains_duplicate_optimized([1,1,1,3,3,4,3,2,4,2]))