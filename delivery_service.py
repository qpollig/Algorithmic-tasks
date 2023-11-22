# 22 ноя 2023, 13:13:14 98455989 OK 48ms 4.23Mb
import sys


def count_platforms(arr_str: list[str], limit: int) -> int:
    """Определяет минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве."""
    arr: list[int] = [int(i) for i in arr_str]
    arr.sort()
    count: int = 0
    left: int = 0
    right: int = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
    return count


if __name__ == '__main__':
    robots_mass = sys.stdin.readline().rstrip().split()
    limit_weight = int(sys.stdin.readline().rstrip())
    print(count_platforms(robots_mass, limit_weight))
