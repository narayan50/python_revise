marks=float(input("Enter your marks:"))
if marks<40 and marks >=0:
    print("Failed")
elif marks <=60 and marks >40:
    print("second class")
elif marks <=75 and marks >60:
    print("First class")
elif marks >75 and marks <=100:
    print("Distinstion")
else:
    print("Invalid Marks")

