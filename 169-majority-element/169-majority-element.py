class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        max_element = [0,0]
        
        nums = sorted(nums)
        print(nums)
        
        count = 1
        
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                count = count + 1
            else:
                if (count > max_element[0]):
                    max_element[0] = count
                    max_element[1] = nums[i]
                count = 1
                
        if (count > max_element[0]):
                max_element[0] = count
                max_element[1] = nums[len(nums)-1]
        
        return max_element[1]
                    
            
        
        