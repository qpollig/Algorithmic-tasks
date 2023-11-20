import sys


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


def is_correct_bracket_seq() -> bool:
    arr_str = sys.stdin.readline().rstrip()
    stack = Stack()
    opening_brackets = ['[', '(', '{']  # открывающие скобки
    closing_brackets = [']', ')', '}']  # закрывающие скобки
    for char in arr_str:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.size() == 0:
                return False
            top = stack.peek()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # открывающая и закрывающая скобки не совпадают
            else:
                stack.pop()
    if stack.size() == 0:
        return True  # стек не пуст, есть открывающие скобки без закрывающих
    return False  # все скобки были согласованы


if __name__ == '__main__':
    print(is_correct_bracket_seq())
