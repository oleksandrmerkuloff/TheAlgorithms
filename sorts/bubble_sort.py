import random


def bubble(array: list) -> list:
    for i in reversed(range(len(array))):
        is_swapped = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j + 1], array[j]
                is_swapped = True
        if not is_swapped:
            return array


def recursive_bubble(array):
    is_swapped = False
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i + 1], array[i]
            is_swapped = True
    if is_swapped:
        return recursive_bubble(array)
    else:
        return array


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    print(recursive_bubble(array))
    assert recursive_bubble(array) == sorted(array)
