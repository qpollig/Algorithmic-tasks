import sys


def main():
    arr_str = sys.stdin.readline().rstrip().split()
    element = int(sys.stdin.readline().rstrip())
    arr = []
    for i in arr_str:
        arr.append(int(i))
    left = 0
    right = len(arr) - 1
    result = False
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if arr[mid] == element:
            result = True
            index = mid
        # Если средний элемент меньше искомого...
        if arr[mid] < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
    if result is True:
        print(index)
    else:
        print(left)


if __name__ == '__main__':
    main()