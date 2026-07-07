# Програмування. Частина 1, Лабораторна робота №8.2
print('Лабораторна робота №8.2, Коломоєць Ольга')
def merge_and_sort_insertion(list1, list2):
    merged_list = list1 + list2

    for i in range(1, len(merged_list)):
        key = merged_list[i]
        j = i - 1
        while j >= 0 and merged_list[j] > key:
            merged_list[j + 1] = merged_list[j]
            j -= 1
        merged_list[j + 1] = key

    return merged_list

list1 = list(map(int, input("Введіть елементи першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть елементи другого списку через пробіл: ").split()))

result = merge_and_sort_insertion(list1, list2)
print("Відсортований список:", result)
