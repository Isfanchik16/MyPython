# # def merge_sort(arr):
# #     if len(arr)<=1:
# #         return arr
# #     left = arr[:len(arr)//2]
# #     right = arr[len(arr)//2:]

# #     left = merge_sort(left)
# #     right = merge_sort(right)
# #     return merge(left,right)
# # def merge(left,right):
# #     sorted_arr =[] 
# #     i=j=0
# #     while i< len(left) and j < len(right):
# #         if left[i]<right[j]:
# #             sorted_arr.append(left[i])
# #             i+=1
# #         else:
# #             sorted_arr.append(right[j])
# #             j+=1
# #     while i<len(left):
# #         sorted_arr.append(left[i])
# #         i+=1
# #     while j<len(right):
# #         sorted_arr.append(right[j])
# #         j+=1
# #     return sorted_arr

# # print(merge_sort([42, 7, 19, 3, 25, 11, 56, 1, 90, 34]))



# def merge_sort2(arr):
#     if len(arr)<=1:
#         return 
#     left = arr[:len(arr)//2]
#     right = arr[len(arr)//2:]

#     merge_sort2(left)
#     merge_sort2(right)
    
#     merge2(left,right,arr)
# def merge2(left,right,arr):
#     i=j=k=0
#     while i < len(left) and j < len(right):
#         if left[i]<right[j]:
#             arr[k] = left[i]
#             i+=1
#         else:
#             arr[k] = right[j]
#             j+=1
#         k+=1
#     while i<len(left):
#         arr[k] = left[i]
#         i+=1
#         k+=1
#     while j<len(right):
#         arr[k] = right[j]
#         j+=1
#         k+=1
# arr = [42, 7, 19, 3, 25, 11, 56, 1, 90, 34]
# merge_sort2(arr)
# print(arr)

# def majorityElement( nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res,count = nums[0],0
#         for n in nums:
#             if n==res: count+=1
#             else:
#                 count -=1
#                 if count == 0:
#                     res = n
#                     count +=1
#         return res
# print(majorityElement([6,5,5]))



# def quick_sort(lst):
#     if len(lst) <=1:return lst
#     else:pivot = lst.pop()
#     less=[]
#     more=[]
#     for x in lst:
#         if x >pivot:more +=[x]
#         else: less +=[x]
#     return quick_sort(less) + [pivot] + quick_sort(more)
# print(quick_sort([0,9,3,8,2,7,5]))



# def bubble(lst):
#     for x in range(len(lst)-1):
#         swapped = False
#         for  i in range(len(lst)-1-x):
#             if lst[i]>lst[i+1]:
#                 lst[i],lst[i+1] = lst[i+1],lst[i]
#                 swapped = True
#         if not swapped:break    
#         print(lst)
#     return lst
# print(bubble([0,9,3,8,2,7,5]))


def insertion_sort(arr):
    for x in range(1,len(arr)):
        while arr[x-1] > arr[x] and x>0:
            arr[x-1],arr[x] = arr[x],arr[x-1]
            x-=1
    return arr
print(insertion_sort([0,9,3,8,2,7,5]))
