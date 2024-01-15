from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        n1 = m - 1
        n2 = n - 1
        while n1 >= 0 and n2 >= 0:
            print(n1, n2)
            if nums1[n1] > nums2[n2]:
                nums1[i] = nums1[n1]
                n1 -= 1
            else:
                nums1[i] = nums2[n2]
                n2 -= 1
            i -= 1
        while n2 >= 0:
            nums1[i] = nums2[n2]
            n2 -= 1
            i -= 1
        while n1 >= 0:
            nums1[i] = nums1[n1]
            n1 -= 1
            i -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 4, 5]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
    print(nums2)