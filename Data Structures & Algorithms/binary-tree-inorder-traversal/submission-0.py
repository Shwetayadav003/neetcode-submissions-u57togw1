# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def Tree(root):
            if not root:
                return
            Tree(root.left)
            result.append(root.val)
            
            Tree(root.right)
        Tree(root)
        return result

        