import cmath
import math
radicand = int(input("What is the radicand? "))
index = int(input("What is the index? "))
exponent = int(input("What is the exponent? "))
print("The answer is",radicand, "^", exponent, "/", index)
explain = input("Would you like to see the steps? Y or N ")
if explain == "Y":
    print("First you take the radicand and put it to the power of the exponent, which is", radicand, "^", exponent)
    print("Then you take that number and put it to the power of 1/index, which is", radicand, "^", exponent, "/", index)
else:
    quit