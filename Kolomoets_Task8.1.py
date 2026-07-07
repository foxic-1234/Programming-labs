# Програмування. Частина 1, Лабораторна робота №8.1
print('Лабораторна робота №8.1, Коломоєць Ольга')
def merge_and_sort_bubble(list1, list2):
    merged_list = list1 + list2

    n = len(merged_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list

list1 = list(map(int, input("Введіть елементи першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть елементи другого списку через пробіл: ").split()))

result = merge_and_sort_bubble(list1, list2)
print("Відсортований список:", result)