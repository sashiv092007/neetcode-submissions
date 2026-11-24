class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        l = 0
        for n in nums:
            if (n - 1) not in hashset:
                le = 1
                while (n + le) in hashset:
                    le += 1
                l = max(l, le)
        return l            

