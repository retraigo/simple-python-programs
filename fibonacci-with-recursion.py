# Iunno what possessed me while I wrote this
def fibo(n, prev = [0, 1]):
    if n == 1:
        return prev
    else:
        prev.append(prev[len(prev) - 1] + prev[len(prev) - 2])
        return fibo(n - 1, prev)

a = int(input("Enter the limit of the series -> "))
print(fibo(a))
