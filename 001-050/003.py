# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        start = 0
        hash_map = {}

        for end, i in enumerate(s):
            finder = hash_map.get(i)
            if finder is not None and finder >= start:
                finder += 1
                start = finder
            longest = max((end + 1 - start), longest)
            hash_map[i] = end
        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abccba'))
