import sys


def sort_by_template(arr, template):
    # создаем словарь для подсчета количества чисел
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    result = []
    for num in template:
        # добавляем повторяющиеся числа в соответствии с шаблоном
        result.extend([num] * count[num])
        # удаляем числа из словаря, чтобы не учитывать их повторно
        del count[num]

    # добавляем оставшиеся числа, которые не были учтены в шаблоне
    for num, freq in sorted(count.items()):
        result.extend([num] * freq)

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    arr = [int(i) for i in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline().rstrip())
    template = [int(i) for i in sys.stdin.readline().rstrip().split()]
    result = sort_by_template(arr, template)
    print(*result)
