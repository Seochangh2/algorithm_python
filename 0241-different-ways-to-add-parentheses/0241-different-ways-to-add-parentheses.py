class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def calcul(left,right,v):
            re=[]
            for l in left:
                for r in right:
                    re.append( eval((str(l)+v+str(r))) )
            return re
        if expression.isdigit():
            return [int(expression)]
        result = []
        for i , v in enumerate(expression):
            if v in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                result.extend(calcul(left,right,v))
        
        return result