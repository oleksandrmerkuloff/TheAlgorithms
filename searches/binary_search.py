import random
from typing import Union


def binary_search(array: list, hidden: int) -> Union[int, str]:
    if not array:
        return 'Empty array!'
    if len(array) == 1:
        if array[0] == hidden:
            return array[0]
        else:
            return 'I can\'t find your value'
    half_of_size = len(array) // 2
    if array[half_of_size] == hidden:
        return array[half_of_size]
    elif array[half_of_size] <= hidden:
        return binary_search(array[half_of_size:], hidden)
    else:
        return binary_search(array[:half_of_size], hidden)


if __name__ == '__main__':
    random_array_of_nums = [random.randint(1, 100) for x in range(100)]
    random_array_of_nums.sort()
    print(random_array_of_nums)

    hidden = random.randint(1, 100)
    print(hidden)

    print(binary_search(random_array_of_nums, hidden))
