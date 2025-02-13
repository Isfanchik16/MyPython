# Quick Sort Implementation
# Time: O(nlogn), Time: O(n)
def quick_sort(arr):
    if len(arr)<=1:return arr
    pivot = arr.pop()
    left=[]
    right=[]
    for x in arr:
        if pivot >x:left.append(x)
        else:right.append(x)
    return quick_sort(left)+[pivot]+quick_sort(right)

res=[]
words=["Hello","dad","qwwewm"]
lst = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]
hashmap={}


for i in range(len(lst)):
    for j in lst[i]:
        hashmap[j] = i
for word in words:
    prev=0
    valid=True
    saved = word
    word = word.lower()
    for letter in word:
        if prev==0:
            prev = hashmap[letter]
        else:
            if prev !=hashmap[letter]:
                valid =False
                break 
    if valid:
        res.append(saved)
print(res)