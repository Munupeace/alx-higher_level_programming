#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
begin = "Last digit of " + str(number)
end = " and is less than 6 and not 0"
mid = " and is 0"

if number < 0 and lastdigit > 0:
    print(begin + " is " "-" + str(lastdigit) + end)
elif number < 0 and lastdigit == 0:
    print("Last digit of " + str(number) + " is " + str(lastdigit) + mid)
elif number > 0 and lastdigit == 0:
    print("Last digit of " + str(number) + " is " + str(lastdigit) + mid)
elif number > 0 and lastdigit > 5:
    print(begin + " is " + str(lastdigit) + " and is greater than 5")
elif number > 0 and lastdigit <= 5:
    print(begin + str(number) + " is " + str(lastdigit) + end)
elif number == 0 and lastdigit == 0:
    print(begin + str(lastdigit) + " is " + str(lastdigit) + mid)
