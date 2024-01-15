from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        l = len(nums)
        for i in range(1, l):
            if nums[i - 1] != nums[i]:
                nums[start] = nums[i]
                start += 1
        return start


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 5, 6]
    idx = Solution().removeDuplicates(nums)
    print(", ".join(map(str, nums[:idx])))