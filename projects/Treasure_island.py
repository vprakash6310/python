print(''''
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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("The mission is to find the treasure.")
print("Answer the upcoming questions to reach to the treasure Bet of Luck!")

choice1= input('You are on the beach side and you have two option going left or right type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 =input('Now you are in the middle of forest enter direction to move "left" or "right"\n').lower()
    if choice2 == "left":
        choice3 = input('you see an island and you need to cross the river to get there '
                        'type "left" to swimming and "right" to wait for wait.\n ').lower()
        if choice3 == "right":
            print("You reached the Island, unharmed\n")

            choice4 = input('You see 3 chambers there RED, GREEN & BLUE and in any one of the chamber the treasure is hidden '
                            'choose the correct chamber to get the treasure\n').lower()
            if choice4 == "red":
                print("You found the treasure, You WIN !!!")

            elif choice4 == "green":
                print("You entered the room full of snakes, Game over!!!")
            elif choice4 == "blue":
                print("You entered room ful of fire, Game over!!!")
            else:
                print("you entered wrong chamber, try again")
        else:
            print("you drown in the river, Game over!!!")
    else:
        print("you have been attacked by Bear, Game Over!!!")
else:
    print("You fell in a hole. Game Over!!!")