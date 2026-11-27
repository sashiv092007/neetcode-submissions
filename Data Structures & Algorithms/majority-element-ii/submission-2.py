class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        res = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for num in freq:
            if freq[num] > n // 3:
                res.append(num)
        return res
             
        
        
             