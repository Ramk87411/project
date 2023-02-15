# head and tails using random number program

import random

value = input("Please press enter to get head or tail ! ")
random_value = random.randint(0, 9)
# print(random_value)
if random_value % 2 == 0:
    print("Head")
else:
    print("Tail")
