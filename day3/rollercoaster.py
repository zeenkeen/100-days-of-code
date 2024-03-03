print("Welcome to the rollercoaster!")
bill = 0
# multiple if conditions gets executed at every conditions but if elif else condition gets executed with only the satisfied value
height = int(input("What is your height? "))

if height >120:
    print("You can ride")
    age = int(input("Write you age here: "))
    if age <12:
        bill = bill + 5
        print(f"pay {bill} dollars")
    elif age <18:
        bill += 7
        print(f"pay {bill} dollars")
    else:
        bill += 12
        print(f"pay {bill} dollars")
    photo = input("do you want to take photos, Y for yes and N for no:- ")
    if photo == "Y": #this gets executed with whatever above condition has been satisfied, it will always gets executed
        bill += 3
    print(f"Your total is {bill} including camera fee. ")
else:
    print("You can't ride")