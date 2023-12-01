import sys


def find_blox(arr, zero_index, left_pointer, count):
    r = len(arr[left_pointer:zero_index + 1])
    if zero_index < 1:
        return zero_index, count
    elif r - 1 != max(*arr[left_pointer:zero_index]):
        zero_index += 1
        return find_blox(arr, zero_index, left_pointer, count)
    else:
        count += 1
        zero_index += 1
        return zero_index, count


def counter_blox(n: int, arr: list):
    count = 0
    zero_index = arr.index(0)
    left_pointer = find_blox(arr, zero_index, 0, count)[0] + 1
    while left_pointer < len(arr):
        left_pointer, count = find_blox(arr, zero_index, left_pointer, count)
    return count


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(counter_blox(n, arr))


