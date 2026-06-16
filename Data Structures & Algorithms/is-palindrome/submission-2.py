class Solution:
    def isPalindrome(self, s: str) -> bool:

        # create cleaned_s variable
        # loop through s
            # cleaned_s += check if each is alnum 

        # reverse cleaned_s
        # check id cleaned_s == reversed

        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char
        reversed_cleaned_s = cleaned_s[::-1]
        if cleaned_s.lower() == reversed_cleaned_s.lower():
            return True
        else:
            return False