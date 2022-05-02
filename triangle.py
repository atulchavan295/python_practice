side1 = float(input("Enter length of side 1:"))
side2 = float(input("Enter length of side 2:"))
side3 = float(input("Enter length of side 3:"))
if side1 == side2 and side2 == side3:
    print("Triangle is equilateral")
elif (side1 == side2 and side2 !=side3) or (side2 == side3 and side3 !=side1) or (side3 == side1 and side1 !=side2):
    print("Triangle is isosceles")
elif (side1 > side2 + side3) or (side2 > side3 + side1) or (side3 > side1 + side2):
    print("Triangle is scalene")
else:
    print("Entered length cannot form triangle")
