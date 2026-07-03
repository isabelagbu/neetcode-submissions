class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers. left. right
        # while loop
        # check if alnum. no? proceed until alnum
        # check equality. no? return False

        leftindex = 0
        rightindex = len(s) - 1

        while leftindex < rightindex:
            while s[leftindex].isalnum() == False and leftindex < rightindex:
                leftindex += 1
            while s[rightindex].isalnum() == False and leftindex < rightindex:
                rightindex -= 1

            if s[leftindex].lower() != s[rightindex].lower():
                return False

            leftindex += 1
            rightindex -= 1

        return True


        