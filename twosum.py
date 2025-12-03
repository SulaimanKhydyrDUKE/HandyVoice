class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        l, r = 0, len(nums)-1
        for i in range(len(nums)-1):
            
            if target - nums[i] in map and map[target - nums[i]] != i:
                return [map[target - nums[i]], i]
            map[nums[i]] = i 
        return None
            




