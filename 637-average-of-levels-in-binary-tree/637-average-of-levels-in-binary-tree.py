# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        def height(node):
            if not node:
                return 0
            else:
                lheight = height(node.left) + 1
                rheight = height(node.right) + 1
                return max(lheight, rheight)
            
        def average(node, levels_dict):
            if not node:
                return levels_dict
            else:
                h = height(node)
                if h not in levels_dict.keys():
                    levels_dict[h] = [node.val]
                else:
                    levels_dict[h].append(node.val)
                l_levels_dict = average(node.left, levels_dict)
                r_levels_dict = average(node.right, l_levels_dict)
                print(r_levels_dict)
                return r_levels_dict
                
        levels_dict = {}
        levels_dict = average(root, levels_dict)
        
        averages = []
        
        for key, values in levels_dict:
            avergaes.append(sum(values)/len(values))
            
        return averages
        '''
        
        level_sums = []
        def sum_levels(node, height = 0):
            if node:
                if len(level_sums) <= height:
                    level_sums.append([0, 0])
                level_sums[height][0] += node.val
                level_sums[height][1] += 1
                sum_levels(node.left, height + 1)
                sum_levels(node.right, height + 1)
        
        sum_levels(root)

        return [s/n for s, n in level_sums]
                    
        