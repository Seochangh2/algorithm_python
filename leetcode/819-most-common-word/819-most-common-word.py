class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]
        