age = int(input("Enter your age: "))
if age < 7:
    print("Your ticket is free!")
elif age >= 7 and age < 18:
    print("Your ticket has a 50 percent discount.")
elif age >= 18 and age < 60:
    print("Your ticket is full price.")
else:
    print ("Your ticket has a 30 percent discount.")