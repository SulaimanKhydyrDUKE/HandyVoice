
## This solution might be wrong, I need to reimplement it
class Solution(object):
    def threeSumClosest(self, nums, target):
        # 1) Sort it
        nums.sort()
        print("SORTED ARRAY: " + str(nums))
        # 2) Two pointers 
        ret = nums[0] + nums[1] + nums[2]
        close = abs( target - ret)
        l,m, r = 0, 1, 2
        while r<len(nums)-1 and l!=r and m!=l and r!=m:
            temp = abs(target - (nums[r+1] + nums[l] + nums[m]))
            if temp < abs(target - close):
                close = temp
                r+=1
            else:
                return close
            temp = abs(abs(target) - abs((nums[r] + nums[l] + nums[m+1])))
            if temp < abs(target - close):
                close = temp
                m+=1
            else:
                return close
            temp = abs(target - (nums[r] + nums[l+1] + nums[m]))
            if temp < abs(target - close):
                close = temp
                l+=1
            else:
                return close
        return close
            

# WORKING SOLUTION FOR O(N^2) time that beats %5 in that regards, and 24% in memory
class Solution(object):
    def threeSumClosest(self, nums, target):
        # 1) Sort it
        nums.sort()
      
        # 2) Two pointers 
        ret = [] 
        ret_sum = float('inf')
        ret_dist = float('inf')
        for i, n in enumerate(nums):    
            l, r = i+1, len(nums) -1
            neg = False
            
            if target < 0:
                neg = True
            while l<r and r<len(nums):
                
                sum = n + nums[l]+nums[r]
                if sum == target:
                    return sum
                dist = float('inf')
                if neg:
                    if sum<0:
                        
                        dist = abs(abs(target)-abs(sum))
                    else:
                        dist = abs(target) + sum
                else:
                    if sum<0:

                        dist = abs(sum) + target
           
                    else:
                        dist = abs(target-sum)
                #if distance is smaller than the previous one, then replace one with another. 
                if ret_dist>dist:
                    
                    ret_dist = dist
                    ret_sum = sum
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    return sum
        return ret_sum

                

            

