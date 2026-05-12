def longest_ones(number):

    longest = 0
    current = 0


    while number > 0:

        
        if (number & 1) == 1:
            current += 1

            
            if current > longest:
                longest = current
        else:
            current = 0

        
        number = number >> 1

    return longest



num = int(input("Enter your number: "))

print("Longest consecutive 1's length :", longest_ones(num))