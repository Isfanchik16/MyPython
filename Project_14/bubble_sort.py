# Bubble Sort Implementation Implementation 
def bubble_sort(lst):
    for x in range(len(lst)-1):
        for i in range(len(lst)-1-x):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst
print(bubble_sort([2,4,45,6,5,1]))

# Bubble Sort Improvement 2
def bubble_sort2(lst):
    sorted = False
    while not sorted:
        sorted = True
        for x in range(len(lst)-1):
            if lst[x] > lst[x+1]:
                lst[x],lst[x+1] = lst[x+1],lst[x]
                sorted=False
    return lst
print(bubble_sort2([21,12,34,1,0]))

def bubble_sort3(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]
                swapped = True
        print(lst)
        if not swapped:break
    return lst

print(bubble_sort3([1000000,223,434,1231]))
