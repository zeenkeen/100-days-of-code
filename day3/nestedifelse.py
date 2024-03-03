#nested if / else statement

print("Welcome to the zeen dental hospital")

pt_name = input("What's your name? ")
print(f"Hello! {pt_name}")
pt_age = int(input("What's your age? "))

if pt_age>16:
    print("Welcome! How can I help you")
    if pt_age>16 and pt_age<50:
        print("don't worry, I am here to help you")
    else:
        print("sorry to say this but I don't specialize in treating older patient")
elif pt_age>10 and pt_age <16:
    print("sorry to say but i can only diagnose you")
else:
    print("you should visit a pedodontist")