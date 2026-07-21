class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 and len(s) % 2 != 0:
            return False

        brackets = {")":"(","}":"{","]":"["}
        mystack = []  

        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                mystack.append(s[i])
            else:
                if len(mystack) == 0:
                    return False
                if mystack.pop() != brackets[s[i]]:
                    return False

        if len(mystack) != 0:
            return False
        else:
            return True
        