import random


def quicksort(num_list):
    if len(num_list) < 2:
        return num_list
    else:
        pivot = num_list[0]
        lt_part = [x for x in num_list[1:] if x <= pivot]
        gt_part = [x for x in num_list[1:] if x > pivot]
        return quicksort(lt_part) + [pivot] + quicksort(gt_part)


if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(10)]
    print(nums)
    print(quicksort(nums))
