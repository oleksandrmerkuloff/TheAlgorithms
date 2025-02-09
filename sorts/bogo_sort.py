import random
import time


def bogo(array):
    def is_sorted(array):
        for num in range(len(array) - 1):
            if array[num] > array[num + 1]:
                return False
        return True

    while is_sorted(array) is False:
        random.shuffle(array)
    return array


if __name__ == '__main__':
    array = random.choices(range(1, 101), k=100)
    print(array)
    started = time.time()
    print(bogo(array))
    finish = time.time()
    print("Wasted time: %s" % (finish - started))
    assert bogo(array) == sorted(array)
