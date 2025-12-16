## SOLUTION that beats 100%
class Solution(object):
    def letterCombinations(self, digits):
        ret = [""]
        map  = {"2":"abc", "3":"def", "4":"ghi","5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        for i in range(len(digits)):

            word = map[digits[i]]
            new_ret = [""]*len(word)*len(ret)
            ind = 0
            for i in ret:
                for k in word:
                    new_ret[ind] = i+k
                    ind+=1
            ret = new_ret
        
        

        return ret
                

        
