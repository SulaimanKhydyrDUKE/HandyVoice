class Solution(object):
    def romanToInt(self, s):
        map = {"I":1, "V":5, "X":10, "L":50,"C":100, "D":500, "M":1000}
        ret = 0
        i = 0
        while i < len(s):
            print("Reading " + s[i])
            if i+1<len(s) and map[s[i]]<map[s[i+1]]:
                print("Found a sub, adding: " + str(map[s[i+1]]-map[s[i]]))
                ret+=map[s[i+1]]-map[s[i]]
                i+=2 
            else:
                print("Normal")
                ret+=map[s[i]]
                i+=1
            print("Read index "+str(i) + " , now ret = " + str(ret))
            

        return ret

        
