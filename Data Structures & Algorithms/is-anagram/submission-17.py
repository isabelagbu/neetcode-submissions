class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # populate seen hashmap using s, k:v, v = num of occurences
        # loop t using s hashmap as reference

        if len(s) != len(t):
            return False

        seen = {}

        # populate seen using s
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in seen:
                return False
            else:
                seen[t[j]] -= 1
                if seen[t[j]] < 0:
                    return False

        for k,v in seen.items():
            if v != 0:
                return False
        
        return True

        