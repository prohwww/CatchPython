#factorial
# 5!

result = 1
def factorial(i):
    global result
    if (i == 0):
        return
    result *= i
    factorial(i - 1)

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

factorial(5)
print(result)