class Solution(object):
    def isPalindrome(self, s):
        
        pal = re.sub('[^A-Z0-9]','',s.upper())
            
        return pal == pal[::-1]
