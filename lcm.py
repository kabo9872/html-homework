#Program to find the LCM of two numbers

#function to calculate LCM
def find_LCM(a, b):
    #Find the greater number
    if a > b:
        greater = a
    else:
        greater = b

    #Loop until LCM is found    

    while True:
        if (greater % a == 0) and (greater % b == 0):
            LCM = greater
            break
        greater += 1

    return LCM

#Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Calling function

result = find_LCM(num1, num2)

#displaying the result
print("The LCM of", num1, "and", num2, "is:", result)
