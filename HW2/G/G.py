def find_smallest(arr):  # функция для поиска наименьшего элемента массива
    smallest = arr[0]  # для хранения наименьшего значение
    smallest_index = 0  # для хранения индекса наиментшего значения

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def solution(a, b):
    b = [i for i in b if i not in a]
    a.extend(b)

    new_arr = []
    for i in range(len(a)):
        smallest = find_smallest(a)
        new_arr.append(a.pop(smallest))
    return new_arr


