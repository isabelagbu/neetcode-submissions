class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        #populate seen with s
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        #loop through seen with t valuse
        for j in t:
            if j in seen and seen[j] > 0:
                seen[j] -= 1
            else:
                return False
            
        #make sure all seen values are 0
        for k,v in seen.items():
            if v != 0:
                return False
        
        return True

        