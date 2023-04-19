import random

# Set constants.
miles_traveled = 0
thirst = 0
camel_tired = 0
natives_distance = -20
drinks = 3


# Print welcome message to game.
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")

done = False

# Create a loop that keeps going while done is false.
while not done:
    oasis = 0
    # Print options for user input.
    print("\nA. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead at full speed")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit")
    user_choice = input("Enter your choice: ")

    # Stop the loop by choosing quit
    if user_choice.upper() == "Q":
        done = True
    # Subtract from number of drinks by one and reset thirst to 0.
    # If there is no more drinks print message.
    elif user_choice.upper() == "A":
        if drinks > 0:
            drinks = drinks-1
            thirst = 0
            print("You feel refreshed.")
        else:
            print("You have nothing to drink!")

    # Make the camel move forward a random amount of miles between 6-13.
    # Add to thirst and camel fatigue.
    # Make natives chase the player.
    # Add random oasis encounter.
    elif user_choice.upper() == "B":
        traveled = random.randrange(6, 13)
        miles_traveled += traveled
        print("You have traveled", traveled, "miles.")
        thirst += 1
        camel_tired += 1
        natives_distance += random.randrange(7, 14)
        oasis = random.randrange(1, 21)
    elif user_choice.upper() == "C":
        traveled = random.randrange(10, 20)
        miles_traveled += traveled
        print("You have traveled", traveled, "miles.")
        thirst += 1
        camel_tired += random.randrange(1, 4)
        natives_distance += random.randrange(7, 14)
        oasis = random.randrange(1, 21)

    # Print message when camel is rested.
    elif user_choice.upper() == "D":
        camel_tired = 0
        print("Camel is happy! :")
        natives_distance += random.randrange(7, 14)

    # Print current stats.
    elif user_choice.upper() == "E":
        print("Miles Traveled:", miles_traveled)
        print("Drinks in canteen:", drinks)
        print("The natives are", miles_traveled-natives_distance, "miles behind you.")

    # If player encounters an oasis reset thirst drinks, and camel stamina.
    if oasis == 12:
        thirst = 0
        drinks = 3
        camel_tired = 0
        print("You made it to an oasis!")

    # If thirst is greater than 6 stop the loop and print you died.
    # If thirst is only greater than 4 give a headsup to the player that they are thirsty.
    if thirst > 6:
        print("You died of  dehydration.")
        done = True
    elif thirst > 4:
        print("You are thirsty!")

    # If camel fatigue surpasses 8 stop the loop the camel is dead.
    # If the camels' stamina is only greater than 5 notify player that the camel is thirsty.
    if camel_tired > 8:
        print("Getaway camel is dead.")
        done = True
    elif camel_tired > 5:
        print("Your camel is getting tired.")

    # Calculate distance between the player and their natives
    # If native occupy the same space as the player stop the loop, the player is dead.
    distance_between = miles_traveled - natives_distance
    if distance_between <= 0:
        print("The native caught you!")
        done = True
    elif distance_between < 15:
        print("The natives are closing in.")

    # When the player has travelled 200 miles or more they win the game.
    # You won, end the loop.
    if miles_traveled > 200 and not done:
        print("You Win!! Wou escaped the Mobi desert.")
        done = True
