# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

from typing import List
from practise.utils.performance_analyzer import PerformanceAnalyzer

class Solution:
    @PerformanceAnalyzer.measure
    def get_concatenation_bf1(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        nums_len = len(nums)
        for i in range(0, nums_len):
            ans[i] = nums[i]
            ans[i + nums_len] = nums[i]
        return ans

    # --- Feedback ---
    # - Correct solution and meets optimal O(n) time / O(n) space complexity.
    # - Code is clear and easy to read.
    # - Preallocating ans is fine, but the logic can be expressed more succinctly.
    # - Minor improvement: range(0, nums_len) → range(nums_len).
    # - Could include a short docstring to explain intent & constraints.
    # - Overall: solid and efficient, but can be more Pythonic with built-in concatenation.

    @PerformanceAnalyzer.measure
    def get_concatenation_opt(self, nums: List[int]) -> List[int]:
        return nums + nums

    # Logic:
    # - List concatenation uses underlying C-level implementation for copying.
    # - Creates final list of size 2n in a single concise expression.
    # - Same asymptotic complexity as loop, but cleaner and usually faster in practice.

    # Why best:
    # - Most Pythonic and minimal code surface.
    # - Hard to misread; intention is obvious.
    # - Lower overhead than manually assigning via loop.


if __name__ == '__main__':
    solution = Solution()
    print(solution.get_concatenation_bf1([1, 2, 3, 4, 5]))
    print(solution.get_concatenation_opt([1, 2, 3, 4, 5]))