def list_superset(list_set_1, list_set_2):
# Не меняйте названия функции и параметров. Напишите решение здесь.
    return_bool = True
    if len(list_set_1) < len(list_set_2):
        for element in list_set_1:
            if (element in list_set_1) and return_bool == True:
                return_bool = True
            else:
                return 'Супермножество не обнаружено.'
        if return_bool is True:
            return f'Набор {list_set_2} - супермножество.'
    elif len(list_set_1) == len(list_set_2):
        for element in list_set_1:
            if (element in list_set_2) and return_bool == True:
                return_bool = True
            else:
                return 'Супермножество не обнаружено.'
        if return_bool is True:
            return 'Наборы равны.'
    else:
        for element in list_set_2:
            if (element in list_set_1) and return_bool == True:
                return_bool = True
            else:
                return 'Супермножество не обнаружено.'
        if return_bool is True:
            return f'Набор {list_set_1} - супермножество.'




# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))