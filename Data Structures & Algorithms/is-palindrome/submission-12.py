class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize left and right pointers
        # while left pointer less than right 
        # make sure left is alnum. no? move forward. same with right
        # now we have valid elements. make sure its lower. false if not equal
        # increment and decrement left and right

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        return True






