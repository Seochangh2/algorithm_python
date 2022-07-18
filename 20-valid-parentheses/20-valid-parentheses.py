class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mate = {
            '(':')',
            '{':'}',
            '[':']',
        }
        if len(s)%2 == 1:
            return False
        
        stack = []
        store = []
        for i in range(len(s)):
            stack.append(s[i])

        while stack :
            tmp = stack.pop()
            if tmp not in mate :
                store.append(tmp)
            else :
                if not store or mate[tmp] != store.pop() :
                    return False
                
        if store :
            return False
        return True