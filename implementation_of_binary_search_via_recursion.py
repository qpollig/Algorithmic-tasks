wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
my_ticket = 9314543


def binary_search(arr, x, left, right):
    if right < left:  # Если правая граница оказалась левее левой.
        return None

    mid = (left + right) // 2  # Получаем индекс среднего элемента.
    if arr[mid] == x:  # Если искомый элемент найден:
        return mid
    if x < arr[mid]:  # Если искомое значение меньше среднего...
        # ...следует продолжить поиск в левой половине массива:
        return binary_search(arr, x, left, mid - 1)
    else:  # В ином случае продолжим поиск в правой половине массива:
        return binary_search(arr, x, mid + 1, right)


# На старте запускаем бинарный поиск по всей длине массива.
index = binary_search(wins, my_ticket, left=0, right=(len(wins) - 1))
print(index)