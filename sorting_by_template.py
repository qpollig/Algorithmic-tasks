import sys


def sorting(n, arr, m, template):
    arr_duplicate = []
    arr_template = []
    for i in arr:
        if i in template:
            arr_template.append(i)
        else:
            arr_duplicate.append(i)
    arr_template = template + arr_template
    for i in range(1, len(arr_template)):
        # Сохраняем текущий элемент в переменную current.
        current = arr_template[i]
        # Сохраняем индекс предыдущего элемента
        # в переменную prev (от previous - предыдущий).
        prev = i - 1
        # Сравниваем current с предыдущим элементом
        # и двигаем предыдущий элемент на одну позицию вправо,
        # пока он больше current и не достигнуто начало массива.
        while prev >= 0 and arr_template[prev] != current:
            arr_template[prev + 1] = arr_template[prev]
            prev -= 1
        # Вставляем current в отсортированную часть массива на нужное место.
        arr_template[prev + 1] = current
    print(arr_template.reverse())
    arr_duplicate.sort()
    arr_template.extend(arr_duplicate)
    return arr_template


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    arr = [int(i) for i in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline().rstrip())
    template = [int(i) for i in sys.stdin.readline().rstrip().split()]
    print(sorting(n, arr, m, template))












'''    for i in range(1, m):
        for j in range(len(arr)):
            current = arr[j]
            prev = i - 1
            while prev >= 0 and template[prev] > current:
                template[prev + 1] = template[prev]
                prev -= 1
            template[prev + 1] = current
            print(f'Шаг {i}, отсортировано элементов: {i + 1}, {arr}')
'''