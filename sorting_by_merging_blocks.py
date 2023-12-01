import sys


def counted(n, arr):
    blocks = []
    curr_block = 1
    max_block = 1

    for i in range(1, n - 1):
        if (arr[i] > arr[i - 1]) and (arr[i] < arr[i + 1]):
            curr_block += 1
        else:
            if curr_block > max_block:
                max_block = curr_block
            blocks.append(curr_block)
            curr_block = 1

    if curr_block > max_block:
        max_block = curr_block
    blocks.append(curr_block)

    return max_block + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    print(counted(n, numbers))


