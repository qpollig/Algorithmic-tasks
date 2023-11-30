import sys


def prefix_similarity(a, b):
    """Функция для вычисления близости префиксов двух массивов.
    a: список целых чисел - первый массив
    b: список целых чисел - второй массив
    Возвращает длину наибольшего совпадающего префикса."""
    prefix_len = min(len(a), len(b))
    for i in range(prefix_len):
        if a[i] != b[i]:
            return i
    return prefix_len


def total_similarity(arrays):
    """Функция для вычисления суммарной попарной близости массивов
       arrays: список массивов
       Возвращает сумму попарной близости массивов. """
    n = len(arrays)
    similarity_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            prefix = prefix_similarity(arrays[i], arrays[j])
            similarity_sum += prefix
    return similarity_sum


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    arrays = []
    for _ in range(n):
        _ = int(sys.stdin.readline().rstrip())
        array = list(map(int, sys.stdin.readline().rstrip().split()))
        arrays.append(array)

    result = total_similarity(arrays)
    print(result)
