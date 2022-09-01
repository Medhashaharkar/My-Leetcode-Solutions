# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGoodNodes(node, maxVal):
            
            if (node == None):
                return 0
            else:
                maxVal = max(maxVal, node.val)
                return (node.val >= maxVal) + countGoodNodes(node.left, maxVal) + countGoodNodes(node.right, maxVal)
                
        
        return countGoodNodes(root, root.val)
