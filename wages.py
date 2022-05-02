sex = input("Enter Sex of the employee(M/F):")
age = int(input("Enter age of the Employee:"))
if age>=18 and age<30:
    if sex == "M":
        print("wages of the day:700")
    elif sex == "F":
        print("wages of the day:750")
    else:
        print("Wrong Input")
elif age>=30 and age<=40:
    if sex == "M":
        print("wages of the day:800")
    elif sex == "F":
        print("wages of the day:850")
    else:
        print("Wrong Input")
else:
    print("Enter appropriate age")
