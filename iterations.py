def multiply_once(n,m):
    return n * m

def multiply_n_times(n,m):
    result = 0
    for i in range(n):
        result+=m
    return result

n = int(input("Enter value of n: "))
m = int(input("Enter value of m: "))

result1 = multiply_once(n,m)
result2 = multiply_n_times(n,m)

print("Using 1 iteration(direct):", result1)
print("Using n iterations(loop):", result2)