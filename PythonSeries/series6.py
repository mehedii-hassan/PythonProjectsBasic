# 1x2x3+x----+n
n = int(input("Enter a number: "))
total = 1
for x in range(1, n + 1, 1):
    total = total * x
print("Total  = ", total)
