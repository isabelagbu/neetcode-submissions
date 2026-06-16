class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 dictionaries
        # loop through s. keep count of each char
        # do the same for t
        # check if both are the same

        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for i in s:    #O(n)
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1

        for j in t:    #O(n)
            if j in tdict:
                tdict[j] += 1
            else:
                tdict[j] = 1

        if sdict == tdict:
            return True #anagram
        else:
            return False 

        






        



        
        