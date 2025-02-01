def calculate_gpa(grade):
    gpa = 0.0
    for x in grade:
        if x == 'A+':gpa +=4.5
        elif x.upper() == 'A0': gpa +=4.0
        elif x.upper() == 'B+': gpa +=3.5
        elif x.upper() == 'B0': gpa +=3.0
        elif x.upper() == 'C+': gpa +=2.5
        elif x.upper() == 'C0': gpa +=2.0
        elif x.upper() == 'D+': gpa +=1.5
        elif x.upper() == 'D0': gpa +=1.0
        elif x.upper() == 'F':  gpa +=0.0
    return round(gpa/len(grade),2)

your_grade=[]
num_sub = int(input("How many subjects did you have in Uni? "))
for x in range(num_sub):
    your_grade +=[input(f"Your {x+1} grade: ")]
print(f"Overall Your GPA is {calculate_gpa(your_grade)}")
        