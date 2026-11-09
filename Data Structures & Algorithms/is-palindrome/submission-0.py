class Solution:
    def isPalindrome(self, s: str) -> bool:
       lst = []
       for word in s:
        if word.isalnum():
            lst.append(word.lower())
       rev_s = "".join(lst)
       return rev_s == rev_s[::-1]     