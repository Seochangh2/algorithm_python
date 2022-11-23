class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result =[]
        for i in range(len(numbers)):
            num = numbers[i]
            find_num = target - num
            idx = bisect.bisect_left(numbers,find_num)
            if len(numbers) > idx and numbers[idx] == find_num and i != idx:
                if i<idx:
                    return [i+1,idx+1]
                else:
                    return [idx+1,i+1]