class Solution(object):
    def isAnagram(self, s, t):
        mapS = {}
        mapT = {}
        for i in s:
            if i in mapS:
                mapS[i] = mapS[i]+1
            else:
                mapS[i] = 1
        for i in t:
            if i in mapT:
                mapT[i] = mapT[i]+1
            else:
                mapT[i] = 1
        for key, value in mapS.items():
            if key not in mapT:
                return False
            elif value != mapT[key]:
                return False
        for key, value in mapT.items():
            if key not in mapS:
                return False
            elif value != mapS[key]:
                return False

        return True
        
