
def allSubStrings(text):

    length = len(text)

    for i in range(length):
        for j in range(i + 1, length + 1):

            
            print(text[i:j])



word = input("Enter a string : ")

print("\nAll substrings are:\n")

allSubStrings(word)