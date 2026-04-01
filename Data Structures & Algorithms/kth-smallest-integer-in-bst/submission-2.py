# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dsf(self, root:TreeNode):
        if root is None:
            return None

        ans = self.dsf(root.left)
        if ans is not None:
            return ans
        
        self.k = self.k-1
        if self.k == 0:
            return root.val
        
        ans = self.dsf(root.right)
        if ans is not None:
            return ans

        return None
        


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k 
        return self.dsf(root)



         









