# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n, lst, i, j = len(nums1), len(nums2), [], 0, 0

        div, mod = divmod(m + n, 2)

        while i != m and j != n:
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                lst.append(nums2[j])
                j += 1
        while i != m:
            lst.append(nums1[i])
            i += 1
        while j != n:
            lst.append(nums2[j])
            j += 1

        if mod:
            return lst[div]
        return (lst[div - 1] + lst[div]) / 2


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(Solution().findMedianSortedArrays(nums1, nums2))
