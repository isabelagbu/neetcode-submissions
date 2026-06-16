class Solution:
    def isValid(self, s: str) -> bool:
        # create dict of brackets. closed : open
        # initialize empty array 
        # Loop through s 
            # if bracket is ({[. push to array
            # else. )}]. 
                # if dict[current] == array.pop
                # yes? keep going
                # no? return false
        # return true

        brackets = {')':'(','}':'{',']':'['}
        mystack = []
        for i in range(len(s)):
            if s[i] in '({[':
                mystack.append(s[i])
            else:
                if len(mystack) == 0 or brackets[s[i]] != mystack.pop():
                    return False
        return len(mystack) == 0