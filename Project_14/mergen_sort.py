# Merge Sort Implementation
# Time: O(nlogn), Space: O(n)
def merge_sort(arr):
    if len(arr)<=1:return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left)
    right = merge_sort(right)


    sorted_arr = []
    i=j=0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j +=1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

arr = [5,4,3,2,1]
print(merge_sort(arr))


# Merge Sort Delevoped version 
# Time: O(nlogn), Space: O(1)
def mergen_sort_dev(arr):
    if len(arr)<=1:return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    mergen_sort_dev(left)
    mergen_sort_dev(right)

    i=j=k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] =left[i]
            i +=1
        else:
            arr[k] =right[j]
            j+=1
        k +=1
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1
array = [23,4,54,6,5676,0,79,1]
mergen_sort_dev(array)
print(array)