class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = {}

        # populate hashmap
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1
        print(seen)
        
        # loop t and lookup seen
        for j in range(len(t)):
            if t[j] in seen:
                seen[t[j]] -= 1
            else:
                return False
        print(seen)

        for k in seen.values():
            if k != 0:
                return False
        
        return True