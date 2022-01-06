class Solution(object):
    def isPalindrome(self, s):
        pal = list(filter(lambda x: x.isalnum(),s.upper()))

            
        return pal == pal[::-1]
