class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            prev = result[-1]
            cur = intervals[i]

            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                result.append(cur)
        
        return result
