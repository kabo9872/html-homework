import random


fruitlist = ['apple','guava','mango','banana','kiwi']
print("Fruit sample:", fruitlist[2:4]) 



my_dict = {
    'name': 'john',
    1: [2,4,3],
    'age': 27
}

print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))    
print()


my_dict['age'] = 27
print("Updated dictionary:", my_dict)
print()


my_dict.pop('age')
print("After pop:", my_dict)
print()



print("I'm thinking of a number between 1 and 5.")
secret_number = random.randint(1, 5)


number_to_fruit = {
    1: fruitlist[0],
    2: fruitlist[1],
    3: fruitlist[2],
    4: fruitlist[3],
    5: fruitlist[4]
}

guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        print("Your winning fruit is:", number_to_fruit[guess])
