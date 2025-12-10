class Solution(object):
    def longestCommonPrefix(self, strs):
        s_strs = sorted(strs, key = len)
        ret = s_strs[0]
        for i in range(len(s_strs)):
            if i+1<len(s_strs):
                temp = ""
                for k in range(len(s_strs[i])):
                    if s_strs[i][k] == s_strs[i+1][k]:
                        temp+=s_strs[i][k]
                    else: 
                        break 
                if len(temp)<len(ret):
                    ret = temp
        return ret
                    
#This is a very slow implementation due to sorting done for each item, but I will put a code without sorting in the bottom -->

class Solution(object):
    def longestCommonPrefix(self, strs):
        s_strs = sorted(strs, key = len)
        ret = s_strs[0]
        for i in range(len(s_strs)):
            if i+1<len(s_strs):
                temp = ""
                for k in range(len(ret)):
                    if ret[k] == s_strs[i+1][k]:
                        temp+= s_strs[i+1][k]
                    else: 
                        break 
                if len(temp)<len(ret):
                    ret = temp
        return ret
# 2% faster
# THE ONE BELOW BEATS 100% of all algorithms: 100% in runtime and 26% in memory
class Solution(object):
    def longestCommonPrefix(self, strs):
        ret = strs[0]
        for i in strs:
            if len(i)<len(ret):
                ret = i
        print("RET: " + ret)
        for i in range(len(strs)):
            # so one mistak was not reading the first one as I expected ret to be set to first
            if i<len(strs):
                temp = ""
                for k in range (min(len(ret), len(strs[i]))):
                    if ret[k] == strs[i][k]:
                        temp+=ret[k]
                    else:
                        break
                if len(temp)<len(ret):
                    ret = temp

        return ret
