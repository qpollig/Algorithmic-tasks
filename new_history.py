import sys
from datetime import datetime as dt


def yashers(start, end):
    start_date = dt(int(start[0]), int(start[1]), int(start[2]), int(start[3]), int(start[4]), int(start[5]))
    end_date = dt(int(end[0]), int(end[1]), int(end[2]), int(end[3]), int(end[4]), int(end[5]))
    diff_date = end_date - start_date
    day = diff_date.days
    sec = diff_date.seconds
    return day, sec


if __name__ == '__main__':
    start = [int(i) for i in sys.stdin.readline().rstrip().split()]
    end = [int(i) for i in sys.stdin.readline().rstrip().split()]
    print(*yashers(start, end))
