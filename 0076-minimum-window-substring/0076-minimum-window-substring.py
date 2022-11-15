class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        target = len(t)
        left = 0
        start = 0
        end = 0

        for i,v in enumerate(s,1):
            if need[v] > 0:
                target -= 1
            need[v] -= 1

            if target == 0:
                while left<i and need[s[left]] <0:
                    need[s[left]] += 1
                    left += 1
                if not end or i - left <= end - start:
                    start , end = left,i
                need[s[left]] += 1
                left+=1
                target +=1
        return s[start:end]
