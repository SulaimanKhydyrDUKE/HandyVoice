class Solution(object):
    def longestPalindrome(self, s):
        rP, lP = 0, 0
        for i in range(len(s)):
            l, r = i, i
            print("REading " + str(i) + "'th character " + s[i])
            print("Left " + str(l)+ " Right " + str(r))
            while l>=0 and r<len(s) and s[l]==s[r] :
                lens = r-l+1
                if rP - lP +1 < lens:
                    print("Updating the range from " + str(lP) + " " + str(rP) + " to " + str(l) + " " + str(r))
                    rP = r
                    lP = l
                l-=1
                r+=1
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r] :
                lens = r-l+1
                if rP - lP +1 < lens:
                    print("Updating the range from " + str(lP) + " " + str(rP) + " to " + str(l) + " " + str(r))
                    rP = r
                    lP = l
                l-=1
                r+=1
                
        return s[lP:rP+1]
