# Програмування. Частина 1, Лабораторна робота №8.3
print('Лабораторна робота №8.3, Коломоєць Ольга')

def merge_and_sort_selection(list1, list2):
    merged_list = list1 + list2

    n = len(merged_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if merged_list[j] < merged_list[min_index]:
                min_index = j
        merged_list[i], merged_list[min_index] = merged_list[min_index], merged_list[i]

    return merged_list

list1 = list(map(int, input("Введіть елементи першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть елементи другого списку через пробіл: ").split()))

result = merge_and_sort_selection(list1, list2)
print("Відсортований список:", result)
