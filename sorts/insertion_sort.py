import random


def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    print(array)
    print(insertion_sort(array))

    assert insertion_sort(array) == sorted(array)
