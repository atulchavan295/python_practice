a = float(input("Enter any number:"))
if a/100>=1 and a/100<=9.99:
    print("Entered number is 3 Digit")
elif a/100<1:
	print("Entered number is less than 3 digit.")
else:
	print("Entered number is more than 3 digit.")