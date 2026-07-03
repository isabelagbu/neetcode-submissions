class Solution:
    def isValid(self, s: str) -> bool:
        # initialize bracketdict
        # create stack using array
        # for loop
            # if open bracket push to stack
            # if close pop stack, check if poped matches dict
        # if stack empty return true. else. false

        if len(s) < 2:
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
        