class Solution:
    def isPalindrome(self, s: str) -> bool:
       cleaned = "".join(char.lower() for char in s if char.isalnum())
       reversed_cleaned = cleaned[::-1]
       return cleaned == reversed_cleaned    