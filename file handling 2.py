import os

intro = "Hi, my name is Kabo. I am learning Python programming and file handling."


with open("file handling 2.txt", "w") as file:
    file.write(intro)


with open("file handling 2.txt", "r") as file:
    content = file.read()
    words = content.split()

print("Words in the file:")
for word in words:
    print(word)


if os.path.exists("my_file.txt"):
    print("my_file.txt exists")
else:
    print("my_file.txt does not exist")


with open("my_file.txt", "a") as file:
    file.write("\n" + intro)

print("Text added to my_file.txt")


if os.path.exists("sample_doc.txt"):
    os.remove("sample_doc.txt")
    print("sample_doc.txt deleted")
else:
    print("sample_doc.txt does not exist")