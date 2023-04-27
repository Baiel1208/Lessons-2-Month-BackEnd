def binary_search(element, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 5
result = binary_search(element, lst)
if result != -1:
    print(f"Элемент {element} найден в списке по индексу {result}.")
else:
    print(f"Элемент {element} не найден!")


def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

my_list = [3, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = bubble_sort(my_list)
print(sorted_list)
