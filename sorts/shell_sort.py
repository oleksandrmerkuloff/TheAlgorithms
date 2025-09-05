import random


def shell_sort(array: list[int]) -> list[int]:
    length = len(array)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            key = array[i]
            j = i

            while j >= gap and key < array[j - gap]:
                array[j] = array[j - gap]
                j -= gap

            array[j] = key
        gap //= 2
    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    print(array)
    print(shell_sort(array))
