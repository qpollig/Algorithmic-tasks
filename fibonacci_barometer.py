def amount_of_change(generations):
    if generations == 0:
        return 1
    elif generations == 1:
        return 1
    elif generations == 2:
        return 2
    else:
        summ = amount_of_change(generations - 1) + amount_of_change(generations - 2)
    return summ


if __name__ == '__main__':
    num = int(input())
    print(amount_of_change(num))