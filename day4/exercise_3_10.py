print("This program computes your GPA")
print("Please enter your completed courses.")
print("Terminate your entry by entering 0 credits.")

sum = 0
grade2value = { "A": 4.0 , "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0 , "D-": 0.7, "F": 0 }

while True:
    credits=int(input("Credits? "))
    if credits == 0:
        break
    grade=str(input("Grade? "))
    sum += credits * grade2value[grade]

print("You GPA is %.2f" % sum)