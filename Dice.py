#dice rolling game
import random

score = 0
round = 0

while round < 100:
    num = random.randint(0,6)

    print(num)
    score += num
    round += 1
#loop end

print(f"final score:{score}")