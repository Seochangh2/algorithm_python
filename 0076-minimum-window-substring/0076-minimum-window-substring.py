class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)>len(s):
            return ""

        t_len = len(t)
        counter = collections.Counter(t)
        
        left = right = 0
        start = end = 0
        for right,v in enumerate(s,1):
            # if right == 0:
            #     continue
            if counter[v]>0:
                t_len -=1
            counter[v] -= 1

            if t_len == 0:
                while counter[s[left]]<0 and left <right :
                    counter[s[left]] +=1
                    left +=1
                if not end or end-start >= right-left:
                    end , start = right,left
                t_len +=1
                counter[s[left]] +=1
                left +=1

        return s[start:end]
