line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# Write your code below this row 👇
if position == "A1":
  line1[0] = "X"
elif position == "B1":
  line1[1] = "X"
elif position == "C1":
  line1[2] = "X"
# Add more conditions here for other positions

# Write your code above this row 👆

print(f"{line1}\n{line2}\n{line3}")
