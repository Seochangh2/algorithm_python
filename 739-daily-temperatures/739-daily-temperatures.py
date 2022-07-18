class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer =[0] * len(temperatures)
        stack_idx= []
    
        for i , temp in enumerate(temperatures):
            while stack_idx and temperatures[stack_idx[-1]] < temp:
                per = stack_idx.pop()
                answer[per] = i - per
            
            stack_idx.append(i)
            
        return answer