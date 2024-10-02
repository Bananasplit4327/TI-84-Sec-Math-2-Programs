import cmath
A = int(input("What is the value of A? "))
B = int(input("What is the value of B? "))
C = int(input("What is the value of C? "))
X1 = str((-1*B - cmath.sqrt(B ** 2 - (4*A*C)))/(2*A))
X2 = str((-1*B + cmath.sqrt(B ** 2 - (4*A*C)))/(2*A))
if "+0j" in X1 or "+0j" in X2:
    print(f'The answer is X =' + X1.replace("+0j", "") + ',' + X2.replace("+0j", ""))
    X1 = X1.replace("+0j", "")
    X2 = X2.replace("+0j", "")
elif "1j" in X1 or "1j" in X2:
    print(f'The answer is X =' + X1.replace("1j", "i") + ',' + X2.replace("1j", "i"))
    X1 = X1.replace("1j", "i")
    X2 = X2.replace("1j", "i")
else:
    print(f'The answer is X =' + X1.replace("j", "i") + ',' + X2.replace("j", "i"))
    X1 = X1.replace("j", "i")
    X2 = X2.replace("j", "i")
print("Would you like to see the steps?")
explain = input("Y or N ")
if explain == "Y":
    sqrt1 = str(B**2 - (4*A*C))
    print("First you take the original quadratic equation which is", A, "X^2", B, "X", C)
    print("Then you take the A, B, and C values to put it in the quadratic formula, which is -", B, "+- the square root of", B, "^2 - (4*", A, "*", C, "), all divided by 2*", A)
    print("The first step is to take the square root which is", sqrt1, "creating the equation -", B, "+-", sqrt1, "all divided by 2")
    print("After that, just add/subtract the numbers to get your X values, those being", X1, "and", X2, "in this case.")
elif explain == "N":
    quit