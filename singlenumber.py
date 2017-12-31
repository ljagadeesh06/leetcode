class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for n in nums:
            print(a)
            a ^= n
            print(a)
        return a

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        print(a, b)
        return a if b == 0 else self.getSum(a ^ b, (a & b) << 1)



s = Solution()
print(s.getSum(-1, 1))

