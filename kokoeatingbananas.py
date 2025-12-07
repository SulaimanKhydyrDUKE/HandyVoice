class Solution(object):
    def minEatingSpeed(self, piles, h):
        # Binary search
        l = 1 
        r = 0
        ret = 1
        for i in piles:
            r = max(r, i)
        while r>=l:
                hours = 0
                mid = (r + l)/2 
                for i in piles:
                    if(i%mid):
                        hours += i/mid + 1
                    else:
                        hours += i/mid
                print("MID " + str(mid))
                print("Hours" + str(hours))
                
                if(hours<=h):
                    r = mid-1
                    ret = mid
                else:
                    l = mid + 1
                print("ret "+str(ret))
        return ret
