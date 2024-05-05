#list [item1, item2]
import random
list_1 = ["deen", "duniya","study","Knowledge","practice","repeat","master"]

list_1.append("innovate")

print(list_1)

list_1[2] = "education"

num = len(list_1)
print(num)
cho = random.randint(0, num)
print(cho)
print(list_1[cho])