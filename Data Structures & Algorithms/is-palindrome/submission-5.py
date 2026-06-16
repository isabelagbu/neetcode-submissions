class Solution:
    def isPalindrome(self, s: str) -> bool:

        # create cleaned_s variable
        # loop through s
            # cleaned_s += check if each is alnum 

        # reverse cleaned_s
        # check if cleaned_s.lower() == reversed.lower()

        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char
        if cleaned_s.lower() == cleaned_s[::-1].lower():
            return True
        else:
            return False