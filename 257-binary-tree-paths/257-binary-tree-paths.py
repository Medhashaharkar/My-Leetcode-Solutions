# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def track(root, path, path_list):
            
            if (root != None):
                path = path+"->"+str(root.val)
            
            if (root == None):
                return path, False
                
            if (root.left == None and root.right == None):
                path_list.append(path)
                return path_list, True
            else:
                track(root.left, path, path_list)
                track(root.right, path, path_list)
            
        path_list = []
        x = (track(root, "", path_list))
        res = []
        for i in path_list:
            temp = list(i)
            print(temp)
            del temp[0]
            del temp[0]
            print(temp)
            i = "".join(temp)
            res.append(i)
        
        return res
        
        