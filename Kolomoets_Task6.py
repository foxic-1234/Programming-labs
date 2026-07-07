# Програмування. Частина 1, Лабораторна робота №6
print('Лабораторна робота №6, Коломоєць Ольга')
list1 = [int(x) for x in input("Введіть елементи першого списку, розділені пробілом: ").split()]
list2 = [int(x) for x in input("Введіть елементи другого списку, розділені пробілом: ").split()]

symmetric_difference = []

for item in list1:
    found = False
    for element in list2:
        if item == element:
            found = True
            break
    if not found:
        symmetric_difference.append(item)

for item in list2:
    found = False
    for element in list1:
        if item == element:
            found = True
            break
    if not found:
        symmetric_difference.append(item)
        
symmetric_difference = tuple(symmetric_difference)

print("Симетрична різниця двох списків:", symmetric_difference)