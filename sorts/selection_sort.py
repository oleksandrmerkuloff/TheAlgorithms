import random


def selection_sort(array: list):
    for i in range(len(array) - 1):
        current = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current]:
                current = j
        if current != i:
            array[i], array[current] = array[current], array[i]
    return array


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    # print(array)
    # print(selection_sort(array))
    # print(sorted(array))
    assert selection_sort(array) == sorted(array)
