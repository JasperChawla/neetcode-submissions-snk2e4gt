# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def splitArray(self, preorder: List[int], inorder: List[int]):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_inx = inorder.index(root.val)

        left_inorder = inorder[:root_inx]
        right_inorder = inorder[root_inx + 1:]

        a = len(left_inorder)
        left_preorder = preorder[1:1 + a]
        right_preorder = preorder[1 + a:]

        root.left = self.splitArray(left_preorder, left_inorder)
        root.right = self.splitArray(right_preorder, right_inorder)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.splitArray(preorder, inorder)