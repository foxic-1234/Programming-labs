# Програмування. Частина 3, Лабораторна робота №4.3, Коломоєць Ольга, ФБ-44, 9
print('Програмування. Частина 3, Лабораторна робота №4.3')
print('Коломоєць Ольга, ФБ-44, 9')
import math

def heron_sqrt(a, epsilon=1e-4):
    x_n = a / 2.0
    
    while True:
    
        x_next = 0.5 * (x_n + a / x_n)
        
        if abs(x_next - x_n) < epsilon:
            break
        
        x_n = x_next
    
    return x_n

a = float(input("Введіть число, квадратний корінь якого хочете обчислити: "))
result = heron_sqrt(a)
print(f"Квадратний корінь числа {a} за методом Герона: {result:.4f}")