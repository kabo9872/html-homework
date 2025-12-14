file = open('file handling operations pt1.txt', 'w')
file.write(
    "Coding is fun.\n"
    "Python is easy to learn.\n"
    "Files are important in programming.\n"
)
file.close()



file = open('file handling operations pt1.txt', 'r')
print("Reading full file:\n")
print(file.read())
file.close()



file = open('file handling operations pt1.txt', 'r')
print("\nReading in parts:\n")
print(file.read(10))
file.close()



file = open('file handling operations pt1.txt', 'r')
print("\nReading first line:\n")
print(file.readline())
file.close()
