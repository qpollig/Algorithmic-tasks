'''import sys


def reader(number_of_applicants, number_of_clock_cycles):
    arr_of_applicants = []
    for i in range(1, number_of_applicants + 1):
        arr_of_applicants.append(i)
    print('arr_of_applicants', arr_of_applicants)
    if number_of_clock_cycles > number_of_applicants:
        while len(arr_of_applicants) != 1:
            remainder = number_of_clock_cycles % len(arr_of_applicants)
            print('remainder', remainder)
            if remainder == 0:
                arr_of_applicants.pop(-1)
                print('if remainder == 0', arr_of_applicants)
            else:
                arr_of_applicants.pop(remainder-1)
                print('else', arr_of_applicants)
        return arr_of_applicants
    else:
        while len(arr_of_applicants) != 1:
            arr_of_applicants.pop(number_of_clock_cycles - 1)
            print(arr_of_applicants)


if __name__ == '__main__':
    applicants = int(sys.stdin.readline().rstrip())
    clock_cycles = int(sys.stdin.readline().rstrip())
    reader_result = reader(applicants, clock_cycles)
    print(reader_result)
'''


def casting_algorithm(N, K):
    candidates = list(range(1, N + 1))
    pointer = 0
    while len(candidates) > 1:
        pointer = (pointer + K - 1) % len(candidates)
        candidates.pop(pointer)
    return candidates[0]

N = int(input())
K = int(input())
result = casting_algorithm(N, K)
print(result)