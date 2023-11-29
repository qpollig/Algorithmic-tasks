import sys


def sorting(n, arr, m, template):
    arr_duplicate = []
    for i in arr:
        if i in template:
            for j in range(1, len(template)):
                current = i
                prev = j - 1
                while prev >= 0 and template[prev] != current:
                    template[prev + 1] = template[prev]
                    prev -= 1
                template[prev + 1] = current
        else:
            arr_duplicate.append(i)
            arr_duplicate.sort()
    template.extend(arr_duplicate)
    return template


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