# Find factorial through recursion!

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

a = int(input("Enter the number to find factorial -> "))
print(factorial(a))
