#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}

        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                # preDict[pathSum] -= 1

        dfs(root, target, 0, preDict)
        return self.count


root = TreeNode(5)
lChild1 = TreeNode(4)
rChild1 = TreeNode(8)
lChild11 = TreeNode(11)
rChild11 = TreeNode(13)
rChild12 = TreeNode(4)
lChild111 = TreeNode(7)
lChild112 = TreeNode(2)
rChild121 = TreeNode(5)
rChild122 = TreeNode(1)

root.left = lChild1
root.right = rChild1

lChild1.left = lChild11

rChild1.left = rChild11
rChild1.right = rChild12

lChild11.left = lChild111
lChild11.right = lChild112

rChild12.left = rChild121
rChild12.right = rChild122

s = Solution()
print(s.pathSum(root, 22))




