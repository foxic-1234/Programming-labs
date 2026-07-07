#Програмування. Частина 1. Лабораторна робота №5. Коломоєць Ольга
print("Лабораторна робота №5. Коломоєць Ольга")

c=int(input("Введіть значення с "))
d=int(input("Введіть значення d "))

x_values = []
y_values = []
x = c
step = 0.001

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x, terms=10):
    sin_sum = 0
    for k in range(terms):
        sign = (-1) ** k
        numerator = x ** (2 * k + 1)
        denominator = factorial(2 * k + 1)
        sin_sum += sign * numerator / denominator
    return sin_sum

def cos(x, terms=10):
    cos_sum = 0
    for k in range(terms):
        sign = (-1) ** k
        numerator = x ** (2 * k)
        denominator = factorial(2 * k)
        cos_sum += sign * numerator / denominator
    return cos_sum
while x <= d:
    y = sin(x**2)*x + cos(x)
    x_values.append(x)
    y_values.append(y)
    x += step

ymax = max(y_values)
print("Максимальне значення функції:", ymax)
print(factorial(5), sin(0), cos(0))