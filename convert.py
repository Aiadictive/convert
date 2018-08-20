class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        ret=""
        n = len(s)
        cycleLen = 2 * numRows - 2
        for i in range(numRows):
            j=0
            while (j + i < n):
                ret = ret + s[j + i]
                if (i != 0 and i != numRows - 1 and j + cycleLen - i < n) :
                    ret = ret + s[j + cycleLen - i]
                j=j+cycleLen
            i=i+1
        return ret