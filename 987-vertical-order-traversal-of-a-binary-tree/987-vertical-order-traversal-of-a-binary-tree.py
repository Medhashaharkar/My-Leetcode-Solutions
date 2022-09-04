# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def sort_levelwise(vertical_level,horizontal_level, root, levelwise):
            if(not root):
                return
            levelwise[vertical_level].append((horizontal_level, root.val))
            sort_levelwise(vertical_level-1, horizontal_level+1, root.left, levelwise)
            sort_levelwise(vertical_level+1, horizontal_level+1, root.right, levelwise)

        levelwise = defaultdict(list)
        sort_levelwise(0,0, root, levelwise)
        result = []
        for i in sorted(levelwise.keys()):
            temp = []
            for j in sorted(levelwise[i]):
                temp.append(j[1])
            result.append(temp)
        return result
