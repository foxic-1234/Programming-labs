# Програмування. Частина 1, Лабораторна робота №7.1
print('Лабораторна робота №7.1, Коломоєць Ольга')

x=int(input("Введіть значення x "))
b=int(input("Введіть значення b "))
c=int(input("Введіть значення с "))

if x<=b:
    print('Виникла помилка')

else:
    def calculate_y(x, b, c):
        sqrt = (x-b)**0.5
        abs = x-c if x-c>=0 else -(x-c)

        y = ((2 * x - c) / sqrt) + abs
        return y

    result = calculate_y(x, b, c)
    print('Результат: ', result)