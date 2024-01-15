from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lower = 0
        min_length = float('inf')
        cumm_sum = 0
        for i in range(len(nums)):
            cumm_sum += nums[i]
            while cumm_sum >= target:
                min_length = min(min_length, i - lower + 1)
                cumm_sum -= nums[lower]
                lower += 1
        if min_length == float('inf'):
            return 0
        else:
            return int(min_length)


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(7, nums))
