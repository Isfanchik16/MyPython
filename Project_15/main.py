def findWords(words):
    hashmap={}
    alpha = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    res=[]

    for index in range(len(alpha)):
        for el in alpha[index]:
            hashmap[el] = index
    for word in words:
        pre=0
        word = word.lower()
        valid = True

        for letter in word:
            if pre ==0:
                pre = hashmap[letter]
            else:
                if pre != hashmap[letter]:
                    valid = False
                    break
                    
        if valid:res.append(word)
    return res

def findqW(words):
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    res=[]
    for word in words:
        wor= word.lower()
        if len(set(row1+wor))==len(row1) or len(set(row2+wor))==len(row2) or len(set(row3+wor)) == len(row3):
            res.append(word)
    return res
print(findqW(["qwert","poiu","qsc","zxcv","qwertyum"]))


    


def setfun(str1):
    hashlst = []
    for x in str1:
        if x not in hashlst:
            hashlst.append(x)
    return "".join(x for x in hashlst)
print(setfun("Abcda"))

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        nums.clear()
        for x in s:
            nums.append(x)
        print(nums)
        return len(nums)
        
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



    