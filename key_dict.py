dict = {"Delhi":"Red Fort", "Agra":"Taj Mahal","Jaipur":"Jal Mahal", "Mumbai": "Gateway of India"}
key = input("Enter key value:")
key = key.lower()
b = dict.keys()
lit = [x.lower() for x in b] #Found this Command on google
if key in lit:
    print("Key is part of the Dict")
else:
    print("Keys is not part of dict")
