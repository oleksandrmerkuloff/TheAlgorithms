import random


def counting_sort(array: list[int]) -> list[int]:
    biggest = max(array)
    count_arr = [0] * (biggest + 1)

    for i in array:
        count_arr[i] += 1

    for i in range(1, biggest + 1):
        count_arr[i] = count_arr[i-1] + count_arr[i]

    answer = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        value = array[i]
        answer[count_arr[value] - 1] = value
        count_arr[value] -= 1

    return answer


if __name__ == '__main__':
    array = [random.randint(0, 101) for _ in range(10)]
    print(array)
    array = counting_sort(array)
    print(array)
