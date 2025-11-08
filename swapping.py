x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))

if x > y:
    temp = x
    x = y
    y = temp

if x > z:
    temp = x
    x = z
    z = temp

if y > z:
    temp = y
    y = z
    z = temp

print("After ascending order swap : ")
print("x =", x)
print("y =", y)
print("z =", z)