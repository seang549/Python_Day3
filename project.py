print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You started on your journey and arrive at your first split path!")
first_decision = input("Would you like to go left or right?\n").lower()
if first_decision == "left":
    print("You survived the wrath of the snakes. Congratulations!")
    print("You continue on your journey and see a river.")
    second_decision = input("You have two options: wait or swim.\n").lower()
    if second_decision == "wait":
        print("The crocs went away. You survived the wrath of the crocs. Who are you Steve Irwin....maybe too soon? ")
        print("Anyways congrats you made it to the final obstacle!")
        print("You now face the decision between three doors.")
        third_decision = input("Which one shall you pick: red, yellow, or blue?\n")
        if third_decision == "red":
            print("You entered into the door and a lot of lava comes out. Some will say it is quite spicy. YOU ARE DEAD. GAME OVER")
        elif third_decision == "blue":
            print("You entered into the door and out comes a huge amount of water. So much that you can't breathe and drown. YOU ARE DEAD. GAME OVER")
        elif third_decision == "yellow":
            print("Wow you actually found it. Wasn't quite sure this was real. Congratulations you got a penny.")
        else:
            print("Wow, you are special huh?\nYour options are RED, BLUE, or YELLOW!")
    else:
        print("Oh no you woke up the crocs.\nSwim faster.....faster.....FASTER!!!\nDang. YOU ARE DEAD. GAME OVER")
else:
    print("You fell into a pit of snakes!\nYOU ARE DEAD. GAME OVER")