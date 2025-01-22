import numpy as np

import random


def bucket(array):
    n = len(array)

    bucket_cells = [[] for _ in range(n)]

    for num in array:
        num_index = int(num * n)
        bucket_cells[num_index].append(num)

    bucket_cells = [sorted(cell) for cell in bucket_cells]

    return [num for bucket in bucket_cells for num in bucket]


if __name__ == "__main__":
    array = random.choices(np.arange(0, 1, 0.1), k=5)

    assert bucket(array) == sorted(array)
