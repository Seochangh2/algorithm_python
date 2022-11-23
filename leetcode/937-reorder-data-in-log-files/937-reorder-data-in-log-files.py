class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let , dig = [],[]
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let+dig
        