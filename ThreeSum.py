class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums is None or len(nums) < 3:
            return res
        nums.sort()
        print(nums)
        for i, num in enumerate(nums[0:-2]):
            target = 0 - num
            idx = i + 1
            med = int((len(nums)-idx)/2)
            # print(idx, med, target)
            while idx < med:
                for jdx, jnum in enumerate(nums[idx:]):
                    print(jnum, nums[idx + 1])
                    if jnum + nums[idx + 1] == target:
                        print(num, jnum, nums[idx + 1])
                idx += 1
                # print(nums[i], nums[i+1], item, nums[i] + nums[i + 1] + item)
                # if nums[i] + nums[i + 1] + item == 0 and [nums[i], nums[i + 1], item] not in res:
                #     res.append([nums[i], nums[i + 1], item])
        return res


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))
# print(s.threeSum([-2, 0, 1, 1, 2]))

