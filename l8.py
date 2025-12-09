class Solution(object):
    def myAtoi(self, s):
        numbers = {"1","2","3","4","5","6","7","8","9","0"}
        my_word = ""
        i = 0
        if s== "":
            return 0
        #1
        while i<len(s) and s[i] == " ":
            i+=1
            print("SKIPPING SPACE")
        #2
        sign_ind = -1
        if i<len(s) and (s[i] =="-" or s[i] == "+"):
            sign_ind = i
            i+=1
            print("GOT THE SIGN")
        #3
        if i<len(s) and s[i] not in numbers:
            return 0
        else:
            #skipping zeros
            while i<len(s) and s[i] == "0":
                i+=1
                print("Skipping Zeros")
            #reading the actual digits
            print("I at " + str(i))
            while i<len(s) and s[i] in numbers:
                print("Reading actuall numbers" + s[i])
                my_word += s[i]
                i+=1
        #4
        if my_word == "":
            return 0
        ret = int(my_word)

        if sign_ind != -1 and my_word != "":
            if s[sign_ind] == "-":
                if ret*(-1)<(-2)**31:
                    return (-2)**31
                return ret*(-1) 
        if ret>2**31-1:
            return 2**31-1
        return ret



        
