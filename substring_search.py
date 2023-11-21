import sys


def length_of_longest_substring():
    arr_str = sys.stdin.readline().rstrip()
    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(arr_str)):
        if arr_str[right] in char_index:
            left = max(left, char_index[arr_str[right]] + 1)
        char_index[arr_str[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring())
