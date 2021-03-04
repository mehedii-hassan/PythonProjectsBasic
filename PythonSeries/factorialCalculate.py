# calculate n!---------------------
n = int(input("Enter a number: "))
fact = 1
for x in range(1, n + 1, 1):
    fact = fact * x
print("Factorial = ", fact)
