#Data Types
#1. String

print("zeen"[3]) #this is called subscripting

#2. Integer
 # to write something like 123,23 we can use dash as it is ignored by the interpreter but becomes easy for us to read.
print(1_60_540) # it prints one lakh sixty thousand and five hundred forty

#Float
3.135

#boolean
True
False

#len function only with strings
#print(len(546)) #its a type error but 
x = "zeen"
num_char = len(x)
print(num_char)
print(type(num_char)) #it gives a class int, it means that len is itself an integer but takes string

# Type Casting - changing one particular type of data into other type
# for example the num_char can be converted in string 
new_num_char = str(num_char)

#print("my name contain"+ num_char + "letters") #it gives type error beause only string can be concatenated with other string

print("my name contains "+ new_num_char+ " letters") # this works because new_num_char is a string now after typecasting
x = input("write any thing here")
print(type(x))

