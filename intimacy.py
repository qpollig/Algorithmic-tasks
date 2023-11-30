import sys


def prefix_count():
    N = int(sys.stdin.readline().rstrip())
    arr_mass = []
    arr_len = []
    count = 0
    max_count = -1
    for i in range(N):
        L = int(sys.stdin.readline().rstrip())
        arr = [int(i) for i in sys.stdin.readline().rstrip().split()]
        arr_mass.append(arr)
        arr_len.append(L)
    for mass_indx in range(N - 1):
        L = arr_len[mass_indx]
        mass = arr_mass[mass_indx]
        mass_next = arr_mass[mass_indx + 1]
        for i in range(1, L):
            count = 0
            if mass[:i] == mass_next[:i]:
                count = len(mass[:i])
                if max_count < count:
                    max_count = count




