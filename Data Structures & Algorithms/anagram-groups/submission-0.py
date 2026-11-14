class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())        