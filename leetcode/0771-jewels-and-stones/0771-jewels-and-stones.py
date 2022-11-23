class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jList = list(jewels)
        sList = list(stones)
        sCounter = collections.Counter()
        for s in sList :
            sCounter[s]+=1
        output = 0
        for j in jList :
            output += sCounter[j]

        return output