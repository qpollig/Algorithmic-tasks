import sys


def main():
    arr_str = sys.stdin.readline().rstrip().split()
    arr = [int(i) for i in arr_str]
    result = []
    for i in arr:
        count = 0
        for j in arr:
            if j < i:
                count += 1
        result.append(count)
    return result


if __name__ == '__main__':
    print(*main())