def find_min_slice_sum(data, elements_in_slice):
    # Считаем сумму первого окна.
    window_sum = sum(data[0:elements_in_slice])
    # Запоминаем результат подсчёта в качестве минимальной суммы.
    min_sum = window_sum
    # В цикле перебираем индексы массива от elements_in_slice до последнего.
    for index in range(elements_in_slice, len(data)):
        # К сумме предыдущего окна добавляем новый элемент: data[index]
        # и вычитаем "вышедший" элемент: data[index - elements_in_slice]
        window_sum += data[index] - data[index - elements_in_slice]
        # Находим минимальную сумму.
        min_sum = min(min_sum, window_sum)
    return min_sum


if __name__ == '__main__':
    data = [5, -3, -2, 10, 2, 7, 1, -6, 13]
    elements_in_slice = 4
    print(find_min_slice_sum(data, elements_in_slice))