def insertion_sort(lst):
    for x in range(1,len(lst)):
        while lst[x-1] > lst[x] and x>0:
            lst[x-1], lst[x] = lst[x],lst[x-1]
            x -=1
        print(lst)
    return lst
print(insertion_sort([12,3,245,456,5]))