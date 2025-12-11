#3Sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ret = []
        for i, n in enumerate(nums):
            if n > 0: break
           # if i + 1 <len(nums) and nums[i]==nums[i+1]: continue
            if i > 0 and nums[i] == nums[i-1]: continue

            l, r = i+1, len(nums)-1
            
            while l<r:
                summa = n+nums[l]+nums[r]
                
                if summa>0:
                    r-=1
                elif summa<0:
                    l+=1
                else: 
                    ret.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1
                   
                
                    while l<r and nums[l] == nums[l-1]:
                       l+=1
                    while l<r and nums[r]==nums[r+1]  :
                       r-=1
        return ret
