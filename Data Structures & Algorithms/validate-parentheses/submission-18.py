class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        brackets = {")":"(","]":"[","}":"{"}
        mystack = []

        for bracket in s:
            if bracket in ["[","{","("]:
                mystack.append(bracket)
            else:
                if len(mystack) == 0:
                    return False
                if mystack.pop() != brackets[bracket]:
                    return False

        if len(mystack) == 0:
            return True
        else:
            return False