import sys


def reader(number_of_applicants, number_of_clock_cycles):
    arr_of_applicants = []
    for i in range(1, number_of_applicants + 1):
        arr_of_applicants.append(i)
    remainder = number_of_clock_cycles % len(arr_of_applicants)
    print('arr_of_applicants', arr_of_applicants)
    while len(arr_of_applicants) != 1:
        if remainder == 0:
            arr_of_applicants.pop(-1)
            print('if remainder == 0', arr_of_applicants)
        else:
            arr_of_applicants.pop(remainder-1)
            print('else', arr_of_applicants)
    return arr_of_applicants


if __name__ == '__main__':
    clock_cycles = int(sys.stdin.readline().rstrip())
    applicants = int(sys.stdin.readline().rstrip())
    reader_result = reader(applicants, clock_cycles)
    print(*reader_result)
