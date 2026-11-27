class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s = ""
        l = len(strs)
        i = 0
        while i < len(strs[0]):
            if strs[0][i] == strs[l - 1][i]:
                s += strs[0][i]
            else:
                break
            i += 1
        return s            