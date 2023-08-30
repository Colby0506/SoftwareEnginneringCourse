print("Enter a grade from 0 to 100: ")
grade = int(input())
gradeAnswer = "F"
if grade >=90:
    gradeAnswer ="A"
elif grade >=80:
    gradeAnswer= "B"
elif grade>=70:
    gradeAnswer = "C"
elif grade>=60:
    gradeAnswer="D"
print("Your grade is "+gradeAnswer)