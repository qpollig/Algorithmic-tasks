import sys


def query(N, M, Q):
    q = 0
    count = 0
    count_finaly = 0
    table = []
    request_arr = []
    for i in range(N+1):
        line_input = input().split()
        table.append(line_input)
    for j in range(Q):
        request = input()
        request_arr.append(request)
    for i in range(M):
        request_now = request_arr[q]
        colomn_name = request_now[0]
        operator = request_now[2]
        number = int(request_now[4])
        if operator == '<':
            for j in range(1, N+1):
                if table[0][i] == colomn_name:
                    if int(table[j][i]) < number:
                        count += 1
            if count == N:
                count_finaly += N
        else:
            for j in range(1, N+1):
                if table[0][i] == colomn_name:
                    if int(table[j][i]) > number:
                        count += 1
            if count == N:
                count_finaly += N
            else:
                count_finaly = 0

    q += 1
    return count_finaly


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    print(query(N, N, Q))




