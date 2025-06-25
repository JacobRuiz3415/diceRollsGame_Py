from Dice import Dice
print("***Rounds Scores***")
Dice1 = Dice()
score = 0
round = 1
point = 0

#the game given 100 rounds
while round <= 100:

    point = Dice.roll()
    if round % 10 == 0:
        print()
    else:
        print(point, end= " ")
        score += point
    
    round += 1
#loop end

print(f"Final Score: {score}")