class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if node is None:
                return True                      # empty = valid, base case
            
            if node.val <= min_val:              # must be GREATER than min
                return False
            if node.val >= max_val:              # must be LESS than max
                return False
            
            left_valid = dfs(node.left, min_val, node.val)   # go left: max shrinks
            right_valid = dfs(node.right, node.val, max_val) # go right: min shrinks
            
            return left_valid and right_valid    # BOTH sides must be valid
        
        return dfs(root, float('-inf'), float('inf'))  # start with no limits