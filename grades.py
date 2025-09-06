
marks=float(input("Enter the Grade of the student: "))
if(marks>=90):
    grade="A"
elif(marks<90 and marks>80):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>60 and marks<70):
    grade="D"
elif(marks>50 and marks<60):
    grade="E"
elif(marks>40 and marks<50):
    grade="NI"
else:
    grade="Fail"

print("The grade of the student is: ", grade)
