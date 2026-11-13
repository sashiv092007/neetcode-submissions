class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_num1 = {}
        for i in s:
            freq_num1[i] = freq_num1.get(i, 0) + 1
        for i in t:
            freq_num1[i] = freq_num1.get(i, 0) - 1
            if freq_num1[i] < 0:
                return False
        return True
               


        