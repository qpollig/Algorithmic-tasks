import sys


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        ...

    def pop(self, item):
        ...

    def peek(self, item):
        ...

    def size(self):
        ...


def is_correct_bracket_seq() -> bool:
    arr_str = sys.stdin.readline().rstrip().split()
    pass