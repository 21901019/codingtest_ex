class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = 0
        res = []
        digits.reverse()
        for i in range(len(digits)):
            integer += digits[i]*10**i
        integer += 1
        for i in str(integer):
            res.append(int(i))
        
        return res
            