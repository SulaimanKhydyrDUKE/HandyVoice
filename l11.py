class Solution(object):
    def maxArea(self, height):
        mak = 0
        l, r = 0, len(height)-1
        while r != l:
            small = 0
            left = height[l]
            right = height[r]
            mak = max(mak, min(left, right)*(r-l))
            if right>left:
                l+=1
            else:
                r-=1 
        return mak
        
