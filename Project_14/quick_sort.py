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
print(quick_sort([10,1,5,8,2,6]))