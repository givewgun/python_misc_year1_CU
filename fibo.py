def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + a
    return a

# Display the first 15 Fibonacci numbers.
sums = 0
for c in range(0, 100):
    print(fibonacci(c))
    sums += fibonacci(c)

print("Fib sum = " ,sums)
