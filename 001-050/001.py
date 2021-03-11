# https://leetcode-cn.com/problems/two-sum/


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    assert len(nums) >= 2

    hash_map = {}

    for idx, num in enumerate(nums):
        diff = target - num

        if diff in hash_map:
            return idx, hash_map[diff]

        hash_map[num] = idx


__name__ == '__main__' and print(two_sum([1, 2, 3, 4, 5, 6, 7], 11))
