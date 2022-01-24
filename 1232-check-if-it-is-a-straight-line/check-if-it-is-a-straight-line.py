class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        # Cross multiplication
        
        (x0, y0), (x1, y1) = coordinates[:2]
        dy = (y1 - y0)
        dx = (x1 - x0)
        
        for c in coordinates:
            if dy * (c[0] - x1) != (c[1] - y1) * dx:
                return False
        return True
