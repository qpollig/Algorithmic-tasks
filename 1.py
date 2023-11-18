example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    last_index = len(data) - 1
    # Напишите здесь код сортировки.
    for i in range(0, len(data) - 1):
        swapped = False
        for item_index in range(0, last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
        last_index -= 1
    return data


print(bubble_sort(example_array))