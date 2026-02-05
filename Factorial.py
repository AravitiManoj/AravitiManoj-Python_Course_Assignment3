factinput = int(input("Enter a number: "))
finalvalue = 1
for i in range(1, factinput+1):
    finalvalue*= i
print(f"Factorial of {factinput} is: {finalvalue}")
