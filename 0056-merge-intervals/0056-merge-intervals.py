class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals,key=lambda x:x[0])
        idx = 0
        while idx+1 <= len(intervals)-1:
            if intervals[idx][1] >= intervals[idx+1][0] and intervals[idx][1] <=  intervals[idx+1][1]:
                intervals[idx][1] = intervals[idx+1][1]
                intervals.remove([intervals[idx+1][0],intervals[idx+1][1]])
            elif intervals[idx][1] >= intervals[idx+1][1]:
                intervals.remove([intervals[idx+1][0],intervals[idx+1][1]])
            else :
                idx += 1
        
        return intervals