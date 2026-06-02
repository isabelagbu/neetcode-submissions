class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #if s and t are different lengths. false
        #if not, convert to list and sort. if same. true

        '''if len(s) == len(t):
            if sorted(list(s)) == sorted(list(t)):
                return True
        return False'''

        #if s and t are different lengths. false
        #if not, initialize dict
        #populate dict with char and count
        #check if both dicts are same

        if len(s) == len(t):
            dict_s = {}
            for i in range(len(s)):
                if s[i] not in dict_s:
                    dict_s[s[i]] = 1
                else:
                    dict_s[s[i]] += 1

            dict_t={}
            for j in range(len(s)):
                if t[j] not in dict_t:
                    dict_t[t[j]] = 1
                else:
                    dict_t[t[j]] += 1

            if dict_s == dict_t:
                return True  
        return False
        