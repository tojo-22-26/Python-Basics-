
marks=float(input("Enter the Grade of the student: "))
if(marks>=90):
    grade="A"
elif(marks>=80):
    grade="B"
elif(marks>=70):
    grade="C"
elif(marks>=60):
    grade="D"
elif(marks>=50):
    grade="E"
elif(marks>=40):
    grade="NI (Needs Improvement)"
else:
    grade="Fail"

print("The grade of the student is: ", grade)
