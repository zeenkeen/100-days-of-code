print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") 
name2 = input("What is their name? ") 
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lowern1= name1.lower()
lowern2 = name2.lower()
full_name = lowern1 + lowern2

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")
true = str(t+r+u+e)
l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")
love = str(l+o+v+e)

total = true + love
score = int(total)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


