# Програмування. Частина 1, Лабораторна робота №4.2, Коломоєць Ольга, ФБ-44, 9
print('Програмування. Частина 1, Лабораторна робота №4.2')
print('Коломоєць Ольга, ФБ-44, 9')
x = int(input('Input x: '))
x = abs(x)
number_of_digits = 0
if x == 0:
    number_of_digits = 1
else:
    while x > 0:
        x //= 10   
        number_of_digits = number_of_digits + 1

print('Кількість цифр у числі: ', number_of_digits)