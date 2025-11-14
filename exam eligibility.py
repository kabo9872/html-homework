total_days = int(input("enter total number of working days : "))
absent_days = int(input("enter total number of days absent : "))

attended_days = total_days - absent_days

percentage = (attended_days / total_days) * 100

print("your attendance percentage is :", percentage , "%")

if attended_days>75:

    print("You may enter the exam")

else:

    print("you may not enter the exam")