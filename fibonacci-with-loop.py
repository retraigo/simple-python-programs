## Fibonacci as you know it

n = int(input("Enter the limit of the series -> "))

a = 0
b = 1
s = 0

series = [0, 1]
for i in range(n - 2):
    s = a + b
    series.append(s)
    (a, b) = (b, s)

print(series)
