def elem_list(lenght):
    res=[]
    i=0
    while i<lenght:
        string = "Enter elements "+"#"+str(i+1)+": "
        res.append(input(string))
        i+=1
    return res
lenght=int(input("Enter lenght of the list : "))
print(elem_list(lenght))