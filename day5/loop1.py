# UNDERSTANDING FOR LOOP

#iterating over a list
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number) #it will print each number

#iterating over a string\
word = "hello! this is zeen"
for letter in word:
    print(letter)
#iterationg over a tuple
colors= ("red", "green", "purple")
for color in colors:
    print(color)

#iterating over a dictionary
fruit_prices = {"apple":100, "banana": 40, "Orange": 40}
for fruit in fruit_prices:
    print(fruit)

for prices in fruit_prices.values():
    print(prices) #this will print the price of each fruit

#to print key-value pair with for loop

for fruit, price in fruit_prices.items():
    print(f"the price of {fruit} is {price}")

#CHECKING FOR KEYS

#Dictionary of fruits and their colors
fruit_colors = {"apple":"red", "banana":"yellow", "guava":"green"}

#list of fruit to check
list_fruits = list(fruit_colors.keys())#it is list of keys from fruit_colors

for phal in list_fruits:
    if phal in fruit_colors:
        print(f"{phal} is in the dictionary")
    else:
        print(f"{phal} is not in the dictionary")


#list of fruits to check
