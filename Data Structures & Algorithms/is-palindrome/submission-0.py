class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = []
        reversed_s = []

        for char in s:
            if char.isalnum():
                new_s += char.lower()
        
        for i in range(len(new_s) - 1,-1,-1):
            reversed_s += new_s[i].lower()

        if new_s == reversed_s:
            return True
        else:
            return False
        