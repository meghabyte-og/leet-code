class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x <= 2:
            return 1
        
        for i in xrange(x):
            if i*i > x:
                return i-1
        
         
        