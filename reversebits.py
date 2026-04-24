
num = int(input("Enter your original number: "))

binary = bin(num)[2:]

reversed_binary = binary[::-1]

reversed_num = int(reversed_binary, 2)

print(f"Reversed Number: {reversed_num} ({reversed_binary})")