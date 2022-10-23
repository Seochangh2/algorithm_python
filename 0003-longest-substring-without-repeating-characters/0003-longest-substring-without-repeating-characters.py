
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used={}
        maxlen = 0
        start = 0
        for i in range(len(s)) :
            if s[i] in used and start <= used[s[i]] :
                start = used[s[i]]+1
                used[s[i]] = i
            else :
                maxlen = max(maxlen , i-start+1)
                used[s[i]] = i
                
                
        return maxlen
        