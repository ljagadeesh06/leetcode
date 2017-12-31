# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def lToNums(self, l1):
        print(l1)
        if not l1:
            return 0
        return (10 ** (len(l1) - 1) * l1.pop()) + self.lToNums(l1)

    def numToL(self, numStr, l1):
        if len(numStr) <= 0:
            return l1
        l1.insert(len(l1), int(numStr[len(numStr) - 1]))
        return self.numToL(numStr[0:len(numStr) - 1], l1)

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


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line);
            line = lines.next()
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()