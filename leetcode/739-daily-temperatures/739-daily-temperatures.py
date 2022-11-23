class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)
        stack = []
        
        for i in range(len(temperatures)) :
            while stack and temperatures[stack[-1]] < temperatures[i] :
                tmp = stack.pop()
                answer[tmp] = i - tmp
                
            stack.append(i)
            
        return answer