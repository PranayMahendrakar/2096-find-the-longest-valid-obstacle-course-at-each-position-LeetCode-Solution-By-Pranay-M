class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        result = []
        tails = []
        
        for i in range(n):
            h = obstacles[i]
            # Find position to insert (rightmost position where tails[pos] <= h)
            pos = bisect_right(tails, h)
            
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
            
            result.append(pos + 1)
        
        return result