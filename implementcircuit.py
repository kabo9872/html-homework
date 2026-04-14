# program to solve the circuit using bitwise operators

A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))

# using AND operator
print("A & B :", A & B)
print("B & C :", B & C)

# using OR operator
Q = (A & B) | (B & C)

print("\nFinal Output Q =", Q)