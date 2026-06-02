class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        answer = False

        if len(s) == len(t):
            for i in s:
                current = i
                for j in range(len(t)):
                    if current == t[j]:
                        count += 1
                        takeoutIndex = j
                        t = t[:j] + t[j+1:]
                        break
            if count == len(s):
                answer = True

        return answer