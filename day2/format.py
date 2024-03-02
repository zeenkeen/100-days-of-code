# f-strings
score = 4
#print("this is your score" + score) #it gives a type error
print("this is your score" + str(score)) #it works

# now lets see what f strings can do
# but first lets add some more different data types
height = 1.3
isWinning = True

print(f"you score is{score} which is awesome looking at your {height} meters of height and of course you are {isWinning}")