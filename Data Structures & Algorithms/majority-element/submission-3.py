class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        most_freq = max(dict1, key=dict1.get)
        return most_freq
        
             