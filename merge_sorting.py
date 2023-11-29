def merge_sort(array):
    # Базовый случай рекурсии.
    if len(array) <= 1:
        return array

    # Рекурсивный разбор массива в левой половине:
    # передаём в merge_sort() левую половину полученного на вход массива.
    left = merge_sort(array[0: len(array) // 2])

    # Рекурсивный разбор массива в правой половине:
    # передаём в merge_sort() правую половину полученного на вход массива.
    right = merge_sort(array[len(array) // 2: len(array)])

    return merge(left, right)


# А функция сортировки и слияния у нас уже есть!
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        # Сравниваем:
        if left[left_idx] <= right[right_idx]:
            # Добавляем в result:
            result.append(left[left_idx])
            # Сдвигаем указатель:
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
print(merge_sort(test_array))
