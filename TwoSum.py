class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        look_for = {}
        for n, x in enumerate(nums):
            try:
                return look_for[x], n
            except KeyError:
                look_for.setdefault(target - x, n)


sol = Solution()
args = (3, 2, 4)
res = sol.twoSum(args, 6)
print(res[0])
print(res[1])






