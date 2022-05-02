percent = float(input("Please enter valid percentage:"))
if percent<=25:
    print("Student Grade is D")
elif percent>25 and percent<=45:
    print("Student Grade is C")
elif percent>45 and percent<=50:
    print("Student Grade is B")
elif percent>50 and percent<=60:
    print("Student Grade is B+")
elif percent>60 and percent<=80:
    print("Student Grade is A")
elif percent>80:
    print("Student Grade is A+")
else:
    print("Please provide valide Percentage")
