class Solution(object):
    letter = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],
        ["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
    def dfs(self,mydigits,output):
            if not mydigits:
                return
            mydigit = mydigits.pop()
            if mydigits:
                output = self.dfs(mydigits,output)
                tmpoutput = []
                for j in range(len(output)):
                        for i in range(len(self.letter[int(mydigit) - 2])):
                            tmpoutput.append(output[j]+self.letter[int(mydigit) - 2][i])
                return tmpoutput
            else:
                for i in range(len(self.letter[int(mydigit) - 2])):
                    output.append(self.letter[int(mydigit) - 2][i])
                return output

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return
            
        output = self.dfs(list(digits),[])
        return output
        

