try:
    per=float(input("Please enter your percentage achieved in the class:"))
except ValueError:
    print("Invalid percentage provided.")
    exit(0)

grade="A"
if per > 100 or per < 0:
    print("Invalid percentage provided.")
    exit(0)

if per < 60:
    grade = "F"
elif per <= 63.3:
    grade = "D-"
elif 63.3 < per <= 66.67:
    grade = "D"
elif 66.67 < per <= 70:
    grade = "D+"
elif 70 < per <= 73.33:
    grade = "C-"
elif 73.33 < per <= 76.67:
    grade = "C"
elif 76.67 < per <= 80:
    grade = "C+"
elif 80 < per <= 83.33:
    grade = "B-"
elif 83.33 < per <= 86.67:
    grade = "B+"
elif 86.67 < per <= 90:
    grade = "A-"

print("You grade is %s" % grade)