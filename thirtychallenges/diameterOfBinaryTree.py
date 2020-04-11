from .maxProfit import printResult

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @printResult
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(   self.localDiameter(root)
                    , self.diameterOfBinaryTree(root.left)
                    , self.diameterOfBinaryTree(root.right))

    def deepest(self, treeNode: TreeNode) -> int:
        if not treeNode:
            return 0
        return max(Solution().deepest(treeNode.left),
                 + Solution().deepest(treeNode.right)) + 1

    def localDiameter(self, treeNode: TreeNode) -> int:
        if not treeNode:
            return 0

        return self.deepest(treeNode.left) + self.deepest(treeNode.right)

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.left.left.left = TreeNode(6)
    tree.left.right.right = TreeNode(7)
    tree.left.left.left.left = TreeNode(8)
    tree.left.right.right.right = TreeNode(9)
    scanner = Solution()
    scanner.diameterOfBinaryTree(tree)

