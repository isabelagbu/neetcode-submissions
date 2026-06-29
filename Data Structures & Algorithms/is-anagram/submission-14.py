class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are same length
        if len(s) != len(t):
            return False
      
        # create sdict
        sdict = {}

        # loop through s. curr in sdict +=. no? 1
        for i in s:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1


        # loop thorugh t. curr in sdict -=. no? false. -1. false
        for j in t:
            if j not in sdict:
                return False
            else:
                sdict[j] -= 1
                if sdict[j] < 0:
                    return False

        return True
                

        
        