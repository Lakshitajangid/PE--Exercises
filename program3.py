def fibonacci_series(num):
    series = [0, 1]  

    while series[-1] < num:
        next_number = series[-1] + series[-2]  
        if next_number <= n:
            series.append(next_number)

    return series


print("Welcome to the Fibonacci Series Generator!")
n = int(input("Please enter a number 'n' to generate the Fibonacci series up to that number: "))

fibonacci_series = fibonacci_series(n)

print("\nThank you for providing the number 'n'.")
print("The Fibonacci sequence up to", n, "is:", ", ".join(map(str, fibonacci_series)))
