file = open("file handling 1.txt", "r")

content = file.read()
print("Full file content:\n")
print(content)

file.close()



file = open("file handling 1.txt", "r")

first_ten = file.read(10)
print("\nFirst 10 characters:")
print(first_ten)

file.close()



file = open("file handling 1.txt", "r")

first_line = file.readline()
print("\nFirst line:")
print(first_line)

file.close()



file = open("file handling 1.txt", "r")

print("\nFirst four lines:")
for i in range(4):
    print(file.readline())

file.close()



file = open("file handling 1.txt", "r")

print("\nAll lines one by one:")
for line in file:
    print(line)


file.close()