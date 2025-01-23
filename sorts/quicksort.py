import random


def quick(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    pivot = array.pop(middle)
    lower, higher = [], []
    for num in range(len(array)):
        if array[num] >= pivot:
            higher.append(array[num])
        else:
            lower.append(array[num])
    return quick(lower) + [pivot] + quick(higher)


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    print(array)
    print(quick(array))
