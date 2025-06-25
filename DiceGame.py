from Dice import Dice
print("***Rounds Scores***")
# Dice created
Dice1 = Dice()
# Dice score
score = 0
round = 1
point = 0

# control variable
choice = "y"

#the game given 100 rounds
while (choice == "y"):
    while round <= 100:

        point = Dice.roll()
        if round % 10 == 0:
            print()
        else:
            print(point, end= " ")
            score += point
        
        round += 1
    #end loop 
    print(f"Average Score: {score / 100}")
    print(f"Final Score: {score}")
    #
    print("would you like to start again?")
    print("Y or N", end = " ")

    #restarting the loop
    choice = input()
    score = 0
    round = 1
    point = 0

