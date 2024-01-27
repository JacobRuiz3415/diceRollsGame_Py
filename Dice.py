#dice rolling game
import random

score = 0
round = 0

while round < 20:
    num = random.randint(0,2)

    print(num)
    score += num
    round += 1
#loop end

print(f"final score:{score}")