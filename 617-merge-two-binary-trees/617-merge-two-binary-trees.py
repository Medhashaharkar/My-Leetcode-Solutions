# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
         '''
         def merge(root1, root2):
                if(root1 == None and root2 == None):
                    return None
                elif (root1 == None and root2 != None):
                    return None
                elif(root1 != None and root2 == None):
                    return root1.val
                else:
                    root2.val = root2.val + root1.val
                    l = merge(root1.left, root2.left)
                    r = merge(root1.right, root2.right)
                    
                    if (l):
                        node = TreeNode(l)
                        root2.left = node
                    if (r):
                        node = TreeNode(r)
                        root2.right = node
                        
         if (root1 != None and root2 == None):
            return root1
         merge(root1, root2)
         return root2
         '''
    
         def mergeTrees(self, t1, t2):
            if not t1 and not t2: return None
            ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
            ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
            return ans
        
         return mergeTrees(self, root1, root2)
                    