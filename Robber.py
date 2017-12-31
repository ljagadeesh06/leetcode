def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last, now = 0, 0

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    for i in nums:
        last, now = now, max(last + i, now)

    return now


nums = [1, 5, 6, 9, 10, 11, 2]
print(rob([23]))

