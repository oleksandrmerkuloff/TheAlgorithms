import random


def find_smallest(sequence):
    smallest_index = 0
    smallest = sequence[0]
    for index in range(1, len(sequence)):
        if sequence[index] < smallest:
            smallest_index = index
            smallest = sequence[smallest_index]
    return smallest_index


def find_biggest(sequence):
    biggest_index = 0
    biggest = sequence[0]
    for index in range(1, len(sequence)):
        if sequence[index] > biggest:
            biggest_index = index
            biggest = sequence[biggest_index]
    return biggest_index


def selection_sort(sequence):
    result_seq = []
    mode = input("From biggest or smallest(b/s)?: ")
    for i in range(len(sequence)):
        if mode == "b":
            result_seq.append(sequence.pop(find_biggest(sequence)))
        elif mode == "s":
            result_seq.append(sequence.pop(find_smallest(sequence)))
        else:
            raise ValueError("Wrong mode. Try again!")
    return result_seq


if __name__ == "__main__":
    test_seq = [random.randint(1, 100) for _ in range(10)]
    print(test_seq)

    test_seq = selection_sort(test_seq)
    print(test_seq)
