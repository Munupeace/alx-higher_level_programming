#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

if number < 0 and lastdigit > 0:
   print("Last digit of " + str(number) + " is " "-"+ str(lastdigit) + " and is less than 6 and not 0")
elif number  <  0 and lastdigit == 0:
    print("Last digit of "+ str(number) + " is 0 and is 0")
elif number > 0 and lastdigit == 0:
    print("Last digit of "+ str(number) + " is 0 and is 0")
elif  number > 0 and lastdigit > 5:
    print("Last digit of " + str(number) + " is " + str(lastdigit) + " and is greater than 5")
elif number > 0 and lastdigit <= 5:
    print("Last digit of " + str(number) + " is " + str(lastdigit) + " and is less than 6 and not 0")
    
