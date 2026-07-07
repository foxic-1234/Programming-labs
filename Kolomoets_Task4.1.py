# Програмування. Частина 1, Лабораторна робота №4.1, Коломоєць Ольга, ФБ-44, 9
print('Програмування. Частина 1, Лабораторна робота №4.1')
print('Коломоєць Ольга, ФБ-44, 9')
import math

epsilon = 10**(-4)

sum_series = 0
n = 0
a_n = (3**n * math.factorial(n)) / math.factorial(3*n)
a_n_1 = 0

while abs(a_n - a_n_1) >= epsilon:
    a_n_1= a_n
    sum_series = sum_series + a_n  
    n = n + 1 
    a_n = (3**n * math.factorial(n)) / math.factorial(3*n)
    #a_n_1 = (3**(n-1) * math.factorial(n-1)) / math.factorial(3*(n-1)) 
print("Сума ряду:", sum_series)