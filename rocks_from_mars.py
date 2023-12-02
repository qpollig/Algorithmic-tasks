import sys


def customer_counter(n, arr_wt_customer, m, arr_wt_delivered_full):
    min_wt = min(arr_wt_customer)
    count = 0
    arr_wt_delivered = []
    for i in range(m):
        if arr_wt_delivered_full[i] >= min_wt:
            arr_wt_delivered.append(arr_wt_delivered_full[i])
    # Создали массив только из подходящих масс
    if len(arr_wt_delivered) == 0:
        return 0
    while arr_wt_delivered and arr_wt_customer:
        min_wt_customer = min(arr_wt_customer)
        min_wt_delivered = min(arr_wt_delivered)
        if min_wt_delivered >= min_wt_customer:
            arr_wt_delivered.remove(min_wt_delivered)
            arr_wt_customer.remove(min_wt_customer)
            count += 1
    return count


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    arr_customer = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    arr_delivered = list(map(int, sys.stdin.readline().rstrip().split()))
    print(customer_counter(n, arr_customer, m, arr_delivered))
