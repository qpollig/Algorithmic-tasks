import sys


def yashers(start_date, end_date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_year, start_month, start_day, start_hour, start_minute, start_second = map(int, start_date)
    end_year, end_month, end_day, end_hour, end_minute, end_second = map(int, end_date)
    days_end = end_year * sum(days_in_month) + sum(days_in_month[0:end_month - 1]) + end_day
    days_start = start_year * sum(days_in_month) + sum(days_in_month[0:start_month - 1]) + start_day
    total_days = days_end - days_start
    end_sec = end_hour * 60 * 60 + end_minute * 60 + end_second
    start_sec = start_hour * 60 * 60 + start_minute * 60 + start_second
    total_seconds = end_sec - start_sec
    if total_seconds < 0:
        total_days -= 1
        total_seconds = end_sec + 24 * 60 * 60 - start_sec
    return total_days, total_seconds


if __name__ == '__main__':
    start = [int(i) for i in sys.stdin.readline().rstrip().split()]
    end = [int(i) for i in sys.stdin.readline().rstrip().split()]
    print(*yashers(start, end))
