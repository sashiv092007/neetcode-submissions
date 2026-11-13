class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxx = 0
        hashmap = {}
        for right in range(len(s)):
            curr = s[right]
            if curr in hashmap and hashmap[curr] >= left:
                left = hashmap[curr] + 1
            hashmap[curr] = right
            curr_len = right - left + 1
            maxx = max(maxx, curr_len)
        return maxx        
        