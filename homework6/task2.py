# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).

def find_indexes(list, min_value, max_value):
    indexes = []
    for i in range(len(list)):
        if list[i] >= min_value and list[i] <= max_value:
            indexes.append(i)
    return indexes
