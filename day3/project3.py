print("Welcome to the treasure island.")


print('''  _______\\__
   (_. _ ._  _/
    '-' \__. /
         /  /
        /  /    .--.  .--.
       (  (    / '' \/ '' \   "
        \  \_.'            \   )
        ||               _  './
         |\   \     ___.'\  /
           '-./   .'    \ |/
              \| /       )|\
               |/       // \\
               |\    __//   \\__
              //\\  /__/  mrf\__|
          .--_/  \_--.
         /__/      \__\
''')

print("Your mission is to find the treasure.")

path = input("Which path you want to choose, left or right? ").lower()

if path == "left":
    #game continues
    choice1 = input("swim or wait ").lower()
    if choice1 == "wait":
        #game continues
        choice2 = input("which door? red, blue or yellow").lower()
        if choice2 == "yellow":
            #game continue
            print("you won")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")