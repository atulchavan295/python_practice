a = float(input("Enter 1st Number:"))
b = float(input("Enter 2nd Number:"))
c = float(input("Enter 3rd Number:"))
if (a>b and a<c) or (a>c and a<b):
    print(a, "is 2nd Largest Number")
elif (b>a and b<c) or (b>c and b<a):
    print(b, "is 2nd Largest Number")
else:
    print(c, "is 2nd Largest Number")