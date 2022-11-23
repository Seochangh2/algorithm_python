class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s:
            return 0
            
        g.sort()
        s.sort()
        count =0
        g_i = s_i = 0
        while len(g)>g_i and len(s)>s_i:
            if g[g_i] <= s[s_i]:
                g_i +=1
            s_i += 1
            
        return g_i