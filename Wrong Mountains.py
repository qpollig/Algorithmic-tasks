import sys


def main():
    arr_str = sys.stdin.readline().rstrip().split()
    arr = []
    return_bool = True
    max_apex = max(arr_str)
    left = arr.index(max_apex)
    right = len(arr)
    for i in arr_str:
        arr.append(int(i))
    for index_height in range(0, left):
        if (arr[index_height] < arr[index_height + 1]) and return_bool is True:
            return_bool = True
        elif arr[index_height] == arr[index_height + 1]:
            return False
        else:
            return False
    for index_height in range(left, right):
        if (arr[index_height] > arr[index_height + 1]) and return_bool is True:
            return_bool = True
        elif arr[index_height] == arr[index_height + 1]:
            return False
    if return_bool is True:
        return True


if __name__ == '__main__':
    main()
