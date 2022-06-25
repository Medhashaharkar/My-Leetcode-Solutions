# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left, right):
            
            if (left == None and right == None):
                return True
            if (left == None or right == None):
                return False
            if (left.val == right.val):
                outerPair = isMirror(left.left, right.right)
                innerPair = isMirror(left.right, right.left)
                return outerPair and innerPair
            else:
                return False
            
        if (root == None):
            return None
        else:
            return isMirror(root.left, root.right)
        