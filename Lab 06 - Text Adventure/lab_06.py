# Welcome text
print("Welcome to the Dragons Den!")
print("You are an adventurer who is known for your scouting abilities and love for exploration.")
print("A wizard has contacted you and asked that you check out this unmarked cave that has seemed to appear over night.")
print("The entrance of the cave is divided into two paths by a wall of stone.")
print("Do you want to enter the left path or the right path?")

# Player input
pathChoice = input("> ")

if(pathChoice == "right path"):
    print("You enter the right path.")
    print("As you walk through the right path you find another path leading further to the right.")
    print("Do you want to continue forward on the original path, or take another right turn?")

    directionChoice = input("> ")

    if(directionChoice == "forward"):
        print("You have come to a dead end, and when you turn around you find yourself at the entrance of the cave.")
        done = True
    elif(directionChoice == "right turn"):
        print("After a few steps you fall into a hole leaving you with fatal injuries.")
        print("You are now dead.")
        done = True
    else:
        print("Invalid choice. Please enter forward or right turn.")

elif(pathChoice == "left path"):
    print("You enter the left path.")
    print("As you walk down the path you eventually come across a stair case.")
    print("Do you want to go down the stairs, or would you like leave the cave?")

    missionChoice = input("> ")

    if(missionChoice == "down"):
        print("After walking down the stairs, you find yourself in a room full of gold.")
        print("You also see an injured dragon sleeping on top of a pile of gold.")
        print("Would you like to return to your client with the information, "
              "or would you like to take some gold for yourself?")

        choiceChoice = input("> ")
        if(choiceChoice == "take gold"):
            print("As you approach the gold the dragon wakes up and skewers you with its tail.")
            print("Your are now dead")
            done = True
        elif(choiceChoice == "return"):
            print("You silently make your way out of the cave and deliver the information to the wizard"
                  " about the cave and that a dragon has made it into its den.")
            print("Mission Success!")
            done = True
        else:
            print("Invalid choice. Please enter take gold or return.")
    elif(missionChoice == "leave"):
        print("You leave the cave avoiding what may have been lurking within its depths.")
        print("Mission Failed.")
        done = True
    else:
        print("Invalid choice. Please enter down or leave.")

else:
    print("Invalid choice. Please take the left path or the right path.")