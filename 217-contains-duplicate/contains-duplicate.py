class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        my_dict = {}

        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                return True
            else:
                my_dict[nums[i]] = i
        return False

        
        