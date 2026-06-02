class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # read s into dict
        # loop t. check if not in dict. if not, false. else, true.

        my_dict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in my_dict: # not in dict so not anagram
                return False
            else:  # in dict, so decrement
                my_dict[t[j]] -= 1

        for k in my_dict.values():
            if k != 0: # if key is not zero then not anagram
                return False
        
        return True
            
        