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


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    assert bubble(array) == sorted(array)
