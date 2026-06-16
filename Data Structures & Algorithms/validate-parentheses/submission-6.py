class Solution:
    def isValid(self, s: str) -> bool:
        # create dict of brackets. {closed : open}
        # initialize empty array as stack 
        # Loop through s 
            # if current bracket is ({[. push to our stack
            # else if stack is empty it means no close brackets exist. return false
            # or if current closing bracket doesnt match popped stack opening bracket pair. returh false
        # if stack empty. return true. else return false.

        brackets = {')':'(','}':'{',']':'['}
        mystack = []
        for i in range(len(s)):
            if s[i] in '({[':
                mystack.append(s[i])
            else:
                if len(mystack) == 0 or brackets[s[i]] != mystack.pop():
                    return False
        return len(mystack) == 0