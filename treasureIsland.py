#Treasure Island Code

print("Welcome to Treasure Island. \nYour mission is to find the treasure")

road = input("You're at a cross road. where do you want to go? Type 'left' or 'right'?")

road = road.lower()

if road == "right":
    print("Game Over.")
elif road == "left":
    lake = input("You come to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
                 "Type 'swim' to swim across?")

    lake = lake.lower()

    if lake == "swim":
        print("Game Over")
    elif lake == "wait":
         door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                      "blue. Which color do you choose?")
         
         door = door.lower()

         if door == "red":
             print("Game Over")
         elif door == "blue":
             print("Game Over")
         elif door == "yellow":
             print("You win!!")

