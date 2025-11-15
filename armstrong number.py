num = int(input("Enter a number: "))

n = len(str(num))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** n
    temp //= 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
