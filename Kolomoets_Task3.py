# Програмування. Частина 1, Лабораторна робота №3, Коломоєць Ольга, ФБ-44
print('Програмування. Частина 1, Лабораторна робота №3')
print('Коломоєць Ольга, ФБ-44')
x = float(input('Input x: '))
b = float(input('Input b: '))
c = float(input('Input c: '))
import math
if x-b >0:
    d = math.sqrt(x-b)
    a = abs(x-c)
    n = 2*x - c
    print(n/d + a)
else:
    print('Error')