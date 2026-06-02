class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #if s and t are different lengths. false
        #if not, convert to list and sort. if same. true
        
        if len(s) == len(t):
            if sorted(list(s)) == sorted(list(t)):
                return True
        return False
        