# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List
from practise.utils.performance_analyzer import PerformanceAnalyzer

class Solution:
    @PerformanceAnalyzer.measure
    def two_sum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        output_index = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   output_index.extend([i, j])
        return list(set(output_index))

    @PerformanceAnalyzer.measure
    def two_sum_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Optimized O(n) solution using a hash map.
        """
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    solution = Solution()

    # Example input
    nums_arr = [2, 7, 11, 15]
    target_ans = 9

    print("Input nums:", nums_arr)
    print("Target:", target_ans)

    print("\n---Brute-Force Method")
    result = solution.two_sum_bruteforce(nums_arr, target_ans)
    print("Output:", result)

    print("\n---Optimized Method")
    result = solution.two_sum_bruteforce(nums_arr, target_ans)
    print("Output:", result)
