# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def attachnode(self, arr, start, end):
            
            if not arr or (end < start):
                return 
            else:
                mid = (start+end)//2
                p = TreeNode(arr[mid])
                p.left = attachnode(self, arr, start, mid-1)
                p.right = attachnode(self, arr, mid+1, end)
                
            return p
            
        root = attachnode(self,nums, 0, len(nums)-1)
        
        return root
        '''
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)
        '''