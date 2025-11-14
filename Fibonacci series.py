def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

num = int(input("Enter how many Fibonacci terms you want: "))

if num <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(recur_fibo(i))
