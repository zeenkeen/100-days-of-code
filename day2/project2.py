#Tip calculator
print("Welcome to the Tip Calculator")
bill = input("What was the total bill? ")
cent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

tip_percentage = float(cent_tip) * float(bill) / 100

print(tip_percentage)

total_bill = tip_percentage + float(bill)

pay = total_bill/ int(split)

paid = round(pay,2)# but this does not give 2 decimal # this is a float

print(paid)
print(type(paid))

final_amount = "{:.2f}".format(pay) #this is a string

print(type(final_amount))

print(f"Each person should pay: {final_amount}")
