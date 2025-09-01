import random


def quicksort(array: list) -> list:
    if len(array) < 2:
        return array
    pivot = array.pop(len(array) // 2)
    smaller = [x for x in array if x <= pivot]
    bigger = [x for x in array if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(bigger)


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=10)
    print(array)
    print(quicksort(array))
