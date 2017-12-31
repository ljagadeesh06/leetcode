class Solution:
    def lToNums(self, l1):
        if len(l1) <= 0:
            return 0
        return (10**(len(l1) - 1) * l1.pop()) + self.lToNums(l1)

    def numToL(self, numStr, l1):
        if len(numStr) <= 0:
            return l1
        l1.insert(len(l1), int(numStr[len(numStr)-1]))
        return self.numToL(numStr[0:len(numStr)-1], l1)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.lToNums(l1)
        num2 = self.lToNums(l2)
        l3 = []
        return self.numToL(str(num1 + num2), l3)


l1 = (4, 7, 2)
l2 = (3, 4, 6)
sol = Solution()

print(sol.addTwoNumbers(list(l1), list(l2)))
