class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.sub(r'[^\w]',' ',paragraph).lower().split()

        words = [ item for item in words if item not in banned ]
        counters = collections.Counter(words)
        
        return counters.most_common(1)[0][0]