import random

miles_traveled = 0
thirst = 0
camel_tired = 0
natives_distance = -20
drinks = 3


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")

done = False

while not done:
    oasis = 0
    print("\nA. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead at full speed")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit")
    user_choice = input("Enter your choice: ")

    if user_choice.upper() == "Q":
        done = True
    elif user_choice.upper() == "A":
        if drinks > 0:
            drinks = drinks-1
            thirst = 0
            print("You feel refreshed.")
        else:
            print("You have nothing to drink!")

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
    elif user_choice.upper() == "D":
        camel_tired = 0
        print("Camel is happy! :")
        natives_distance += random.randrange(7, 14)
    elif user_choice.upper() == "E":
        print("Miles Traveled:", miles_traveled)
        print("Drinks in canteen:", drinks)
        print("The natives are", miles_traveled-natives_distance, "miles behind you.")

    if oasis == 12:
        thirst = 0
        drinks = 3
        camel_tired = 0
        print("You made it to an oasis!")

    if thirst > 6:
        print("You died of  dehydration.")
        done = True
    elif thirst > 4:
        print("You are thirsty!")

    if camel_tired > 8:
        print("Getaway camel is dead.")
        done = True
    elif camel_tired > 5:
        print("Your camel is getting tired.")

    distance_between = miles_traveled - natives_distance
    if distance_between <= 0:
        print("The native caught you!")
        done = True
    elif distance_between < 15:
        print("The natives are closing in.")

    if miles_traveled > 200 and not done:
        print("You Win!! Wou escaped the Mobi desert.")