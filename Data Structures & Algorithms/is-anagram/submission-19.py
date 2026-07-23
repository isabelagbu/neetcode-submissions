class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for j in t:
            if j not in seen:
                return False
            else:
                seen[j] -= 1

        for k,v in seen.items():
            if v != 0:
                return False

        return True

        