class Solution(object):
    def maxProfit(self, prices):
        pre, suf = [0]*len(prices), [0]*len(prices)
        low, high = prices[0], prices[-1]
        r = len(prices)-1

        for i in range(len(prices)):
            if(low>prices[i]):
                low = prices[i]
            if(high<prices[r]):
                high = prices[r]
            pre[i] = low
            suf[r] = high
            r-=1
        print(pre)
        print(suf)
        max = 0

        for i in range(len(prices)):
            d = suf[i]-pre[i]
            if(d>max): 
                max = d
        return max

### BETTER SOLUTION - 94% less memory
class Solution(object):
    def maxProfit(self, prices):
        low = prices[0]
        Hax = 0
        for s in prices:
            low = min(low, s)
            Hax = max(Hax, s - low)
        return Hax
        
        
