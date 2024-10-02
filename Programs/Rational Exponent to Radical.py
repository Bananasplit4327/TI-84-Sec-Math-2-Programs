import cmath
import math
number = int(input("What is the number being multiplied? "))
numerator = int(input("What is the numerator of the power? "))
denominator = int(input("What is the denominator of the power? "))
print("The answer is the", denominator, "root of", number, "all raised to the power of", numerator)
explain = input("Would you like to see the steps? Y or N ")
if explain == "Y":
    print("First you take the number and take it's root from the denominator, which is the", denominator, "root of", number)
    print("Then you take the denominator and raise everything to it's power, in this case being", numerator, "and giving you the final answer of the", denominator, "root of", number, "all raised to the power of", numerator)